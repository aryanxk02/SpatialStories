# Spatial Stories

This is a static gallery and documentation site for the examples in this repository. The notebook cards also link to Voilà for live execution.

## Run locally

From the repository root:

```bash
python3 -m http.server 8000
```

In a second terminal, from the repository root, start Voilà:

```bash
JUPYTER_PATH="$(python3 -c 'import sys; print(sys.prefix + "/share/jupyter")')" voila --port=8866 --no-browser
```

Then open <http://localhost:8000>. The root page redirects to `docs/`, while source files and preview media remain available from `examples/`. The **Run interactively** buttons open the notebook UI served from <http://localhost:8866>.

## Publish with GitHub Pages

The site can be published at [github.com/aryanxk02/SpatialStories](https://github.com/aryanxk02/SpatialStories). For GitHub Pages, publish the repository root (or use a Pages workflow) so the `docs/` site and `examples/` source/media paths are deployed together. Voilà still needs a Python-capable host; GitHub Pages alone cannot execute notebooks.

Install the Python dependencies, including Voilà, with `python3 -m pip install -r requirements.txt`. The cards link back to the original notebooks, scripts, and preview media in `examples/`, keeping the gallery and source together in one repository.
