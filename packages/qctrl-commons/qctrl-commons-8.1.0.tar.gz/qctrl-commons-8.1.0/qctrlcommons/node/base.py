# Copyright 2020 Q-CTRL Pty Ltd & Q-CTRL Inc. All rights reserved.
#
# Licensed under the Q-CTRL Terms of service (the "License"). Unauthorized
# copying or use of this file, via any medium, is strictly prohibited.
# Proprietary and confidential. You may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
#     https://q-ctrl.com/terms
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS. See the
# License for the specific language.
"""Module for Node."""
from typing import (
    Any,
    Dict,
    Optional,
)

import forge

from qctrlcommons.node.wrapper import (
    NodeData,
    Operation,
)


class Node:
    """
    Custom structure.

    Parameters
    ----------
    node_id: str
        Graph node identity (user-specified name of the node).
    input_kwargs: Dict
        Dictionary of inputs passed to the graph node.

    Attributes
    ----------
    node_id: str
        Graph node identity (user-specified name of the node).
    input_kwargs: Dict:
        Dictionary of inputs passed to the graph node.
    name: str
        Name of node class (corresponding to the name of the generated function).
    args: List
        List of supported arguments for building the function signature.
    kwargs: Dict
        Dictionary of keyword-only arguments for building the function signature.
    rtype: TypeVar
        Return type for the generated function signature.
    """

    name = None
    args = []
    kwargs = {"name": forge.kwarg("name", type=Optional[str], default=None)}
    rtype = Any
    optimizable_variable = False

    def __init__(self, node_id, input_kwargs):
        self.node_id = node_id
        self.input_kwargs = input_kwargs

    @classmethod
    def create_node_data(cls, _operation, **kwargs):  # pylint:disable=unused-argument
        """
        Creates the `NodeData` (or sub-class thereof, as determined by the `rtype`) to be returned
        as the node value.

        Can optionally perform validation of the inputs (which themselves will be `NodeData`
        objects, if they come from other graph function calls).
        """
        return NodeData(_operation)

    @classmethod
    def create_pf(cls):
        """Creates the corresponding pythonflow function."""

        def func(name=None, **kwargs):
            operation = Operation(cls.name, name=name, **kwargs)
            return cls.create_node_data(_operation=operation, name=name, **kwargs)

        func.__doc__ = cls.__doc__
        func.__name__ = cls.name  # pylint:disable=non-str-assignment-to-dunder-name
        sig = forge.sign(*cls.args, **cls.kwargs)
        func = sig(func)
        func = forge.returns(cls.rtype)(func)

        return func

    def _evaluate_inputs(self, execution_context: "ExecutionContext") -> Dict:
        """Evaluates the args and kwargs. Called before evaluating the node
        itself.

        Parameters
        ----------
        execution_context : ExecutionContext
            helper class for evaluating the node value.

        Returns
        -------
        Dict
            the kwargs
        """

        def _recursive_evaluate(arg):
            if isinstance(arg, Node):
                return arg.evaluate(execution_context)
            if isinstance(arg, list):
                return [_recursive_evaluate(element) for element in arg]
            if isinstance(arg, dict):
                return {key: _recursive_evaluate(arg[key]) for key in arg}
            return arg

        kwargs = _recursive_evaluate(self.input_kwargs)

        return kwargs

    def evaluate(self, execution_context: "ExecutionContext") -> Any:
        """Get the value from the Node itself.

        Parameters
        ----------
        execution_context : ExecutionContext
            helper class for evaluating the value of node.

        Returns
        -------
        Any
            the value of the node.
        """
        # check if it is evaluated
        if execution_context.is_recorded(self):
            return execution_context.get_recorded_value(self)

        kwargs = self._evaluate_inputs(execution_context)

        node_function = getattr(execution_context.nodes, self.name, None)
        value = node_function(**kwargs)

        execution_context.record(self, value)
        return value
