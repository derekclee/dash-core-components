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


class Graph(DashComponent):
    """
    
    """
    _namespace = 'dash_core_components'
    _typename = 'Graph'
    available_wildcard_properties = [

    ]
    id = ComponentProp('id', UNDEFINED, False)
    clickData = ComponentProp('clickData', "null", False)
    clickAnnotationData = ComponentProp('clickAnnotationData', "null", False)
    hoverData = ComponentProp('hoverData', "null", False)
    clear_on_unhover = ComponentProp('clear_on_unhover', False, False)
    selectedData = ComponentProp('selectedData', "null", False)
    relayoutData = ComponentProp('relayoutData', "null", False)
    restyleData = ComponentProp('restyleData', "null", False)
    figure = ComponentProp('figure', "{data: [], layout: {}}", False)
    style = ComponentProp('style', UNDEFINED, False)
    className = ComponentProp('className', UNDEFINED, False)
    animate = ComponentProp('animate', False, False)
    animation_options = ComponentProp('animation_options', "{\n    frame: {\n        redraw: false,\n    },\n    transition: {\n        duration: 750,\n        ease: 'cubic-in-out',\n    },\n}", False)
    config = ComponentProp('config', "{\n    staticPlot: false,\n    editable: false,\n    edits: {\n        annotationPosition: false,\n        annotationTail: false,\n        annotationText: false,\n        axisTitleText: false,\n        colorbarPosition: false,\n        colorbarTitleText: false,\n        legendPosition: false,\n        legendText: false,\n        shapePosition: false,\n        titleText: false,\n    },\n    autosizable: false,\n    queueLength: 0,\n    fillFrame: false,\n    frameMargins: 0,\n    scrollZoom: false,\n    doubleClick: 'reset+autosize',\n    showTips: true,\n    showAxisDragHandles: true,\n    showAxisRangeEntryBoxes: true,\n    showLink: false,\n    sendData: true,\n    linkText: 'Edit chart',\n    showSources: false,\n    displayModeBar: 'hover',\n    modeBarButtonsToRemove: [],\n    modeBarButtonsToAdd: [],\n    modeBarButtons: false,\n    displaylogo: true,\n    plotGlPixelRatio: 2,\n    topojsonURL: 'https://cdn.plot.ly/',\n    mapboxAccessToken: null,\n}", False)
    loading_state = ComponentProp('loading_state', UNDEFINED, False)

    def __init__(
        self,
        id=UNDEFINED,
        clickData="null",
        clickAnnotationData="null",
        hoverData="null",
        clear_on_unhover=False,
        selectedData="null",
        relayoutData="null",
        restyleData="null",
        figure="{data: [], layout: {}}",
        style=UNDEFINED,
        className=UNDEFINED,
        animate=False,
        animation_options="{\n    frame: {\n        redraw: false,\n    },\n    transition: {\n        duration: 750,\n        ease: 'cubic-in-out',\n    },\n}",
        config="{\n    staticPlot: false,\n    editable: false,\n    edits: {\n        annotationPosition: false,\n        annotationTail: false,\n        annotationText: false,\n        axisTitleText: false,\n        colorbarPosition: false,\n        colorbarTitleText: false,\n        legendPosition: false,\n        legendText: false,\n        shapePosition: false,\n        titleText: false,\n    },\n    autosizable: false,\n    queueLength: 0,\n    fillFrame: false,\n    frameMargins: 0,\n    scrollZoom: false,\n    doubleClick: 'reset+autosize',\n    showTips: true,\n    showAxisDragHandles: true,\n    showAxisRangeEntryBoxes: true,\n    showLink: false,\n    sendData: true,\n    linkText: 'Edit chart',\n    showSources: false,\n    displayModeBar: 'hover',\n    modeBarButtonsToRemove: [],\n    modeBarButtonsToAdd: [],\n    modeBarButtons: false,\n    displaylogo: true,\n    plotGlPixelRatio: 2,\n    topojsonURL: 'https://cdn.plot.ly/',\n    mapboxAccessToken: null,\n}",
        loading_state=UNDEFINED,
        **kwargs
    ):
        # type: (typing.Union[str, Undefined], typing.Union[typing.Dict, Undefined], typing.Union[typing.Dict, Undefined], typing.Union[typing.Dict, Undefined], typing.Union[bool, Undefined], typing.Union[typing.Dict, Undefined], typing.Union[typing.Dict, Undefined], typing.Union[typing.List, Undefined], typing.Union[typing.Dict, Undefined], typing.Union[typing.Dict, Undefined], typing.Union[str, Undefined], typing.Union[bool, Undefined], typing.Union[typing.Dict, Undefined], typing.Union[typing.Dict[str, typing.Union[bool, typing.Dict[str, typing.Union[bool]], typing.Union[float, int], typing.Any, str, typing.List]], Undefined], typing.Union[typing.Dict[str, typing.Union[bool, str]], Undefined], typing.Any) -> None # noqa: E501
        """
        :param id: The ID of this component, used to identify dash
            components in callbacks. The ID needs to be unique
            across all of the components in an app.
        :param clickData: Data from latest click event. Read-only.
        :param clickAnnotationData: Data from latest click annotation
            event. Read-only.
        :param hoverData: Data from latest hover event. Read-only.
        :param clear_on_unhover: If True, `clear_on_unhover` will clear the
            `hoverData` property when the user
            "unhovers" from a point. If False, then
            the `hoverData` property will be equal to
            the data from the last point that was
            hovered over.
        :param selectedData: Data from latest select event. Read-only.
        :param relayoutData: Data from latest relayout event which occurs
            when the user zooms or pans on the plot or
            other layout-level edits. Has the form `{<attr
            string>: <value>}` describing the changes
            made. Read-only.
        :param restyleData: Data from latest restyle event which occurs
            when the user toggles a legend item, changes
            parcoords selections, or other trace-level
            edits. Has the form `[edits, indices]`, where
            `edits` is an object `{<attr string>: <value>}`
            describing the changes made, and `indices` is
            an array of trace indices that were edited.
            Read-only.
        :param figure: Plotly `figure` object. See schema:
            https://plot.ly/javascript/reference Only supports
            `data` array and `layout` object. `config` is set
            separately by the `config` property, and `frames` is
            not supported.
        :param style: Generic style overrides on the plot div
        :param className: className of the parent div
        :param animate: Beta: If true, animate between updates using
            plotly.js's `animate` function
        :param animation_options: Beta: Object containing animation
            settings. Only applies if `animate` is
            `true`
        :param config: Plotly.js config options. See
            https://plot.ly/javascript/configuration-options/
            for more info.
        :param loading_state: Object that holds the loading state object
            coming from dash-renderer
        """
        kws = {
            k: v for k, v in locals().items() if k not in ('self', 'kwargs')
        }
        kws.update(kwargs)
        DashComponent.__init__(self, **kws)
