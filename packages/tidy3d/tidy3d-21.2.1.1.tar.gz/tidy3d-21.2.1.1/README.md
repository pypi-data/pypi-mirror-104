# Tidy3d Python API

To compile the docs, you'll need to install `sphinx`, `sphinx-rtd-theme`, and `jupyter-sphinx`. Then:

```
cd docs
make html
browse _build/html/index.html
```

There is also a script that does some cleanup before building, and optionally copies the core code from the `tidy3d` repo. In the docs folder, call this with `bash build_docs.sh`. The core code will not be copied over by default, but you have the option to do so if you are sure you want to.

## How to update what

- Stuff in the `tidy3d/` folder here (apart from the `web/` module inside of it) is never directly updated. Instead the `tidy3d/sim/` folder in the `tidy3d` repo is copied over when the core code needs to be updated.

- Docs are only updated here. After an update, all the notebooks from `docs/examples` should be pushed to the public `tidy3d-notebooks` repo, and the build in `docs/_build/html/` should be pushed to the docs folder of the `tidy3d_static_web`. For convenience, you could use

```
bash push_notebooks.sh
bash push_docs.sh
```

- To test a new build (including pip installing a new release), do `bash -i test_notebooks.sh`. You can edit the file to select which notebooks to run. The script assumes you are running conda and will make a new conda environment, pip install the working Tidy3D version from this repo, and run and store the notebooks.
