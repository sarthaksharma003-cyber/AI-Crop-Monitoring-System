import folium

def create_base_map(latitude, longitude, tile_url=None):

    m = folium.Map(
        location=[latitude, longitude],
        zoom_start=14,
        control_scale=True
    )

    # Add marker
    folium.Marker(
        [latitude, longitude],
        tooltip="Selected Field"
    ).add_to(m)

    # Add NDVI overlay
    if tile_url:
        folium.TileLayer(
            tiles=tile_url,
            attr="Google Earth Engine",
            overlay=True,
            name="NDVI",
            opacity=0.7
        ).add_to(m)

    # Layer selector
    folium.LayerControl().add_to(m)

    return m