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


class Interval(DashComponent):
    """
    A component that repeatedly increments a counter `n_intervals` with a
    fixed time delay between each increment. Interval is good for triggering a
    component on a recurring basis. The time delay is set with the property
    "interval" in milliseconds.
    """
    _namespace = 'dash_core_components'
    _typename = 'Interval'
    available_wildcard_properties = [

    ]
    id = ComponentProp('id', UNDEFINED, False)
    interval = ComponentProp('interval', 1000, False)
    disabled = ComponentProp('disabled', UNDEFINED, False)
    n_intervals = ComponentProp('n_intervals', 0, False)
    max_intervals = ComponentProp('max_intervals', -1, False)

    def __init__(
        self,
        id=UNDEFINED,
        interval=1000,
        disabled=UNDEFINED,
        n_intervals=0,
        max_intervals=-1,
        **kwargs
    ):
        # type: (typing.Union[str, Undefined], typing.Union[typing.Union[float, int], Undefined], typing.Union[bool, Undefined], typing.Union[typing.Union[float, int], Undefined], typing.Union[typing.Union[float, int], Undefined], typing.Any) -> None # noqa: E501
        """
        :param id:
        :param interval: This component will increment the counter
            `n_intervals` every `interval` milliseconds
        :param disabled: If True, the counter will no longer update
        :param n_intervals: Number of times the interval has passed
        :param max_intervals: Number of times the interval will be fired.
            If -1, then the interval has no limit (the
            default) and if 0 then the interval stops
            running.
        """
        kws = {
            k: v for k, v in locals().items() if k not in ('self', 'kwargs')
        }
        kws.update(kwargs)
        DashComponent.__init__(self, **kws)
