# datascientists

Quick Data Science tools, providing data processing and visualization in Hypotheses Testing, Regression, and etc.

---

## Best Practices

Best Practices for `datascientists` visualization require `nodejs` and `jupyter`.

---

## Best Practices for Python venv

If you need to isolate the Python environment, visit [venv — Creation of virtual environments](https://docs.python.org/3/library/venv.html)

---

### Best Practices for nodejs

[Install nvm (Node Version Manager) from github](https://github.com/nvm-sh/nvm)

Check your nvm version:

```sh CLI
nvm -v
```

Once you installed nvm, using `nvm` to install node:

```sh CLI
nvm install node
```

To list all local nodes:

```sh CLI
nvm list
```

To choose your node version:
For example, using v`16.0.0`

```sh CLI
nvm use node v16.0.0
```

You can list available versions using `ls-remote`:

```sh CLI
nvm ls-remote
```

---

### Best Practices for Jupyterlab

Install jupyterlab

```sh CLI
pip install jupyterlab
```

Set jupyterlab and install extensions for plotly:

```sh CLI
# (OS X/Linux)
export NODE_OPTIONS=--max-old-space-size=4096

# Jupyter widgets extension
jupyter labextension install @jupyter-widgets/jupyterlab-manager --no-build

# jupyterlab renderer support
jupyter labextension install jupyterlab-plotly --no-build

# FigureWidget support
jupyter labextension install plotlywidget --no-build

# Build jupyterlab (must be done to activate extensions since --no-build is used above)
jupyter lab build

# Unset NODE_OPTIONS environment variable
# (OS X/Linux)
unset NODE_OPTIONS
```

See if you have installed the three extensions correctly:

```sh CLI
jupyter labextension list
```

You should see:
- ` @jupyter-widgets/jupyterlab-manager`
- `jupyterlab-plotly`
- `plotlywidget`

![](https://raw.githubusercontent.com/ZacksAmber/PicGo/master/img/20210503130838.png)