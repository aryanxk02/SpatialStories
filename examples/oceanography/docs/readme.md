# Global Coral Reef Inspector

This example demonstrates how to combine **GeoPandas**, **Lonboard**, and **ipywidgets** to build an interactive, high-performance web map for oceanographic data exploration. 

The application loads vector geometries from Natural Earth, performs a spatial join to enrich raw line features with regional marine names, attaches curated educational metadata, and leverages Lonboard's WebGL rendering engine alongside `ipywidgets` event listeners for real-time hover and click inspection.

---

## Overview

Natural Earth provides a high-resolution 10m vector dataset representing global coral reefs (`ne_10m_reefs.geojson`). While geometric coverage is comprehensive, the raw shapefile attributes lack human-readable reef system names and ecological context.

In this example, we:
* **Fetch Data:** Download coral reef geometries alongside regional marine boundaries (`ne_10m_geography_marine_polys.geojson`) and land outlines (`ne_10m_land.geojson`).
* **Spatial Join:** Perform a nearest-neighbor spatial join (`gpd.sjoin_nearest`) to dynamically map each coral geometry to its surrounding marine region (e.g., *Great Barrier Reef*, *Coral Sea*).
* **Metadata Enrichment:** Enrich the resulting GeoDataFrame with curated, beginner-friendly educational facts (location, key marine species, ecosystem highlights, and environmental threats).
* **GPU Rendering:** Render high-contrast, GPU-accelerated vector layers on top of a dark MapLibre basemap without textual occlusion.
* **Interactive UI:** Bind Lonboard layer interaction traits (`selected_index`) to a dynamic HTML widget card that updates instantly as users hover or click on reef features.