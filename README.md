# Spatial Stories

Interactive geospatial stories built with Python, GeoPandas, and [Lonboard](https://github.com/developmentseed/lonboard). The project turns notebook examples into a visual gallery where every story explains its data, code pattern, and interaction model.

**Website:** [Spatial Stories](http://localhost:8000) locally  ·  **Source:** [github.com/aryanxk02/SpatialStories](https://github.com/aryanxk02/SpatialStories)

## What is included

The gallery currently contains five examples:

- **Point Cloud Canopy** — a generated 3D LiDAR-style forest rendered with `PointCloudLayer`.
- **Global Coral Reef Inspector** — Natural Earth reef geometries enriched with marine regions and educational metadata.
- **Where New Yorkers Reported 311 Issues** — NYC 311 requests aggregated into neighborhood-scale geohash cells.
- **Live Seismic Activity** — USGS earthquake events styled by depth and magnitude.
- **Global Airport Network** — Natural Earth airports rendered as a pickable global scatterplot.

Each notebook includes a short explanation of the data pipeline, the Lonboard layer being used, styling choices, and the interaction available to the user.

## Run the website locally

Clone the repository and install the dependencies:

```bash
git clone https://github.com/aryanxk02/SpatialStories.git
cd SpatialStories
python3 -m pip install -r requirements.txt
```

Start the static gallery from the repository root:

```bash
python3 -m http.server 8000
```

Open [http://localhost:8000](http://localhost:8000). The root page redirects to `docs/`, while the `examples/` directory remains available for source notebooks and preview media.

## Run notebooks interactively with Voilà

The **Run** buttons on notebook cards launch the actual notebook UI through Voilà. In a second terminal, start Voilà from the repository root:

```bash
JUPYTER_PATH="$(python3 -c 'import sys; print(sys.prefix + "/share/jupyter")')" voila --port=8866 --no-browser
```

Then use the **Run** buttons in the gallery. Voilà executes the notebooks on the Python server and streams their widgets and Lonboard maps into the browser.

The notebooks fetch public data at runtime, so interactive examples require an internet connection. The NYC example uses a bounded, reproducible week of 311 data; the earthquake example uses the USGS seven-day feed.

## Project structure

```text
examples/                         Notebook and script examples
  administration/                 NYC 311 geohash map
  demo/                           3D canopy point cloud
  natural_hazards/                USGS earthquake map
  oceanography/                   Coral reef inspector
  transportation_logistics/       Global airport map
docs/                             Spatial Stories gallery
  index.html                      Gallery markup
  app.js                          Example data and filters
  styles.css                      Visual design and responsive layout
  assets/                         Gallery-only preview artwork
```

## Deployment

The gallery is static HTML, CSS, and JavaScript, so it can be published through GitHub Pages or another static host. To keep the source links and preview media working, deploy the repository root so both `docs/` and `examples/` are available.

The interactive Voilà notebooks require a Python-capable host. GitHub Pages cannot run Python kernels by itself; use a service or server that can install the dependencies and keep Voilà running, then update the `interactive` URLs in `docs/app.js` to point to that deployment.

## Resources

- [Lonboard examples](https://github.com/developmentseed/lonboard/tree/main/examples)
- [Lonboard documentation](https://developmentseed.org/lonboard/)
- [30DayMapChallenge](https://30daymapchallenge.com/)
