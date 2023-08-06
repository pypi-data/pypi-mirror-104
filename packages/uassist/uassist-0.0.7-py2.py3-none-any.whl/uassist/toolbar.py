"""Toolbar Module for controls in map interface
    """
    
import os
import ipywidgets as widgets
from ipyleaflet import WidgetControl, TileLayer, WMSLayer, basemap_to_tiles
from ipyfilechooser import FileChooser
import ipyleaflet.basemaps as ipybasemaps
from IPython.display import display


ua_basemaps = {
    "HYBRID": TileLayer(
        url="https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}",
        attribution="Google",
        name="Google Satellite Hybrid",
    ),
    "ROADMAP": TileLayer(
        url="https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}",
        attribution="Google",
        name="Google Maps",
    ),
    "SATELLITE": TileLayer(
        url="https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}",
        attribution="Google",
        name="Google Satellite",
    ),
    "TERRAIN": TileLayer(
        url="https://mt1.google.com/vt/lyrs=p&x={x}&y={y}&z={z}",
        attribution="Google",
        name="Google Terrain",
    ),
    "Esri Satellite": TileLayer(
        url="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
        attribution="Esri",
        name="Esri Satellite",
    ),
    "Esri Streetmap": TileLayer(
        url="https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}",
        attribution="Esri",
        name="Esri Streetmap",
    ),
    "Esri Terrain": TileLayer(
        url="https://server.arcgisonline.com/ArcGIS/rest/services/World_Terrain_Base/MapServer/tile/{z}/{y}/{x}",
        attribution="Esri",
        name="Esri Terrain",
    ),
    "Esri Transportation": TileLayer(
        url="https://server.arcgisonline.com/ArcGIS/rest/services/Reference/World_Transportation/MapServer/tile/{z}/{y}/{x}",
        attribution="Esri",
        name="Esri Transportation",
    ),
    "Esri Topo World": TileLayer(
        url="https://services.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}",
        attribution="Esri",
        name="Esri Topo World",
    ),
    "FWS NWI Wetlands": WMSLayer(
        url="https://www.fws.gov/wetlands/arcgis/services/Wetlands/MapServer/WMSServer?",
        layers="1",
        name="FWS NWI Wetlands",
        attribution="FWS",
        format="image/png",
        transparent=True,
    ),
    "FWS NWI Wetlands Raster": WMSLayer(
        url="https://www.fws.gov/wetlands/arcgis/services/Wetlands_Raster/ImageServer/WMSServer?",
        layers="0",
        name="FWS NWI Wetlands Raster",
        attribution="FWS",
        format="image/png",
        transparent=True,
    ),
    "OpenStreetMap": TileLayer(
        url="https://c.tile.openstreetmap.org/${z}/${x}/${y}.png",
        attribution="OSM",
        name="OpenStreetMap",
    ),
    "NLCD 2016 CONUS Land Cover": WMSLayer(
        url="https://www.mrlc.gov/geoserver/mrlc_display/NLCD_2016_Land_Cover_L48/wms?",
        layers="NLCD_2016_Land_Cover_L48",
        name="NLCD 2016 CONUS Land Cover",
        attribution="MRLC",
        format="image/png",
        transparent=True,
    ),
    "USGS NAIP Imagery": WMSLayer(
        url="https://services.nationalmap.gov/arcgis/services/USGSNAIPImagery/ImageServer/WMSServer?",
        layers="0",
        name="USGS NAIP Imagery",
        attribution="USGS",
        format="image/png",
        transparent=True,
    ),
    "USGS Hydrography": WMSLayer(
        url="https://basemap.nationalmap.gov/arcgis/services/USGSHydroCached/MapServer/WMSServer?",
        layers="0",
        name="USGS Hydrography",
        attribution="USGS",
        format="image/png",
        transparent=True,
    ),
    "USGS 3DEP Elevation": WMSLayer(
        url="https://elevation.nationalmap.gov/arcgis/services/3DEPElevation/ImageServer/WMSServer?",
        layers="3DEPElevation:None",
        name="USGS 3DEP Elevation",
        attribution="USGS",
        format="image/png",
        transparent=True,
    ),
}


def main_toolbar(m):

    padding = "0px 0px 0px 5px"  # upper, right, bottom, left

    toolbar_button = widgets.ToggleButton(
        value=False,
        tooltip="Toolbar",
        icon="wrench",
        layout=widgets.Layout(width="28px", height="28px", padding=padding),
    )

    close_button = widgets.ToggleButton(
        value=False,
        tooltip="Close the tool",
        icon="times",
        button_style="primary",
        layout=widgets.Layout(height="28px", width="28px", padding=padding),
    )    

    toolbar = widgets.HBox([toolbar_button])

    def close_click(change):
        if change["new"]:
            toolbar_button.close()
            close_button.close()
            toolbar.close()
            
    close_button.observe(close_click, "value")

    rows = 2
    cols = 2
    grid = widgets.GridspecLayout(rows, cols, grid_gap="0px", layout=widgets.Layout(width="62px"))

    icons = ["folder-open", "map", "gears", "question"]

    for i in range(rows):
        for j in range(cols):
            grid[i, j] = widgets.Button(description="", button_style="primary", icon=icons[i*rows+j], 
                                        layout=widgets.Layout(width="28px", padding="0px"))

    toolbar = widgets.VBox([toolbar_button])

    def toolbar_click(change):
        if change["new"]:
            toolbar.children = [widgets.HBox([close_button, toolbar_button]), grid]
        else:
            toolbar.children = [toolbar_button]
        
    toolbar_button.observe(toolbar_click, "value")

    toolbar_ctrl = WidgetControl(widget=toolbar, position="topright")

    m.add_control(toolbar_ctrl)

    output = widgets.Output()
    output_ctrl = WidgetControl(widget=output, position="topright")

    buttons = widgets.ToggleButtons(
        value=None,
        options=["Apply", "Reset", "Close"],
        tooltips=["Apply", "Reset", "Close"],
        button_style="primary",
    )
    buttons.style.button_width = "80px"

    data_dir = os.path.abspath('./data')

    fc = FileChooser(data_dir)
    fc.use_dir_icons = True
    fc.filter_pattern = ['*.shp', '*.geojson']

    filechooser_widget = widgets.VBox([fc, buttons])

    def button_click(change):
        if change["new"] == "Apply" and fc.selected is not None:
            if fc.selected.endswith(".shp"):
                m.add_shapefile(fc.selected, layer_name="Shapefile")
            elif fc.selected.endswith(".geojson"):
                m.add_geojson(fc.selected, layer_name="GeoJSON")
        elif change["new"] == "Reset":
            fc.reset()
        elif change["new"] == "Close":
            fc.reset()
            m.remove_control(output_ctrl)
    buttons.observe(button_click, "value")  


    # Basemap Widget
    dropdown_basemap = widgets.Dropdown(
        options=list(ua_basemaps.keys()),
        value="HYBRID",
        layout=widgets.Layout(width="160px"),
        #description="Basemaps",
    )

    close_button_basemap = widgets.Button(
        icon="times",
        tooltip="Close the basemap widget",
        button_style="primary",
        layout=widgets.Layout(width="32px"),
    )

    basemap_widget = widgets.HBox([dropdown_basemap, close_button_basemap])

    def on_click(change):
        basemap_name = change["new"]

        if len(m.layers) == 1:
            old_basemap = m.layers[0]
        else:
            old_basemap = m.layers[1]
        m.substitute_layer(old_basemap, ua_basemaps[basemap_name])

    dropdown_basemap.observe(on_click, "value")

    def close_click(change):
        if m.basemap_ctrl is not None and m.basemap_ctrl in m.controls:
            m.remove_control(m.basemap_ctrl)
        basemap_widget.close()

    close_button_basemap.on_click(close_click)

    basemap_control = WidgetControl(widget=basemap_widget, position="topright")
    m.basemap_ctrl = basemap_control  


    def tool_click(b):    
        with output:
            output.clear_output()
            if b.icon == "folder-open":
                display(filechooser_widget)
                m.add_control(output_ctrl)
            
            elif b.icon =="map":
                display(basemap_widget)
                m.add_control(basemap_control)

            elif b.icon == "gears":
                import whiteboxgui.whiteboxgui as wbt

                if hasattr(m, "whitebox") and m.whitebox is not None:
                    if m.whitebox in m.controls:
                        m.remove_control(m.whitebox)

                tools_dict = wbt.get_wbt_dict()
                wbt_toolbox = wbt.build_toolbox(
                    tools_dict, max_width="800px", max_height="500px"
                )

                wbt_control = WidgetControl(
                    widget=wbt_toolbox, position="bottomright"
                )                

                m.whitebox = wbt_control
                m.add_control(wbt_control)

    for i in range(rows):
        for j in range(cols):
            tool = grid[i, j]
            tool.on_click(tool_click)