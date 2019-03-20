"""
Autogenerated file
DO NOT EDIT.
CONTENT WILL BE OVERWRITTEN!

WARNING: Do not import this file directly!
"""
import typing

from dash_component_system import (
    DashComponent, UNDEFINED, Undefined, ComponentProp
)


class Checklist(DashComponent):
    """
    Checklist is a component that encapsulates several checkboxes. The values
    and labels of the checklist is specified in the `options` property and the
    checked items are specified with the `values` property. Each checkbox is
    rendered as an input with a surrounding label.
    """
    _namespace = 'dash_core_components'
    _typename = 'Checklist'
    available_wildcard_properties = [

    ]
    id = ComponentProp('id', UNDEFINED, False)
    options = ComponentProp('options', "[]", False)
    values = ComponentProp('values', UNDEFINED, False)
    className = ComponentProp('className', UNDEFINED, False)
    style = ComponentProp('style', UNDEFINED, False)
    inputStyle = ComponentProp('inputStyle', "{}", False)
    inputClassName = ComponentProp('inputClassName', '', False)
    labelStyle = ComponentProp('labelStyle', "{}", False)
    labelClassName = ComponentProp('labelClassName', '', False)
    loading_state = ComponentProp('loading_state', UNDEFINED, False)

    def __init__(
        self,
        id=UNDEFINED,
        options="[]",
        values=UNDEFINED,
        className=UNDEFINED,
        style=UNDEFINED,
        inputStyle="{}",
        inputClassName='',
        labelStyle="{}",
        labelClassName='',
        loading_state=UNDEFINED,
        **kwargs
    ):
        # type: (typing.Union[str, Undefined], typing.Union[typing.List[typing.Dict[str, typing.Union[str, bool]]], Undefined], typing.Union[typing.List[str], Undefined], typing.Union[str, Undefined], typing.Union[typing.Dict, Undefined], typing.Union[typing.Dict, Undefined], typing.Union[str, Undefined], typing.Union[typing.Dict, Undefined], typing.Union[str, Undefined], typing.Union[typing.Dict[str, typing.Union[bool, str]], Undefined], typing.Any) -> None # noqa: E501
        """
        :param id:
        :param options: An array of options
        :param values: The currently selected value
        :param className: The class of the container (div)
        :param style: The style of the container (div)
        :param inputStyle: The style of the <input> checkbox element
        :param inputClassName: The class of the <input> checkbox element
        :param labelStyle: The style of the <label> that wraps the checkbox
            input  and the option's label
        :param labelClassName: The class of the <label> that wraps the
            checkbox input  and the option's label
        :param loading_state: Object that holds the loading state object
            coming from dash-renderer
        """
        kws = {
            k: v for k, v in locals().items() if k not in ('self', 'kwargs')
        }
        kws.update(kwargs)
        DashComponent.__init__(self, **kws)
