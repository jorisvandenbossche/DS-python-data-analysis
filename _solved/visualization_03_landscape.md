---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.1
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

<p><font size="6"><b>Python's Visualization Landscape</b></font></p>


> *DS Data manipulation, analysis and visualisation in Python*  
> *December, 2019*

> *© 2016, Joris Van den Bossche and Stijn Van Hoey  (<mailto:jorisvandenbossche@gmail.com>, <mailto:stijnvanhoey@gmail.com>). Licensed under [CC BY 4.0 Creative Commons](http://creativecommons.org/licenses/by/4.0/)*

---

+++

---
**Remark:**

The packages used in this notebook are not provided by default in the conda environment of the course. In case you want to try these featutes yourself, make sure to install these packages with conda.

To make some of the more general plotting packages available:

```
conda install -c conda-forge bokeh plotly altair vega
```

an additional advice will appear about the making the vega nbextension available. This can be activated with the command:

```
jupyter nbextension enable vega --py --sys-prefix
```

and use the interaction between plotly and pandas, install `cufflinks` as well

```
pip install cufflinks --upgrade
```

To run the large data set section, additional package installations are required:

```
conda install -c bokeh datashader holoviews
```
---

+++

## What have we done so far?

+++

What we have encountered until now:

* [matplotlib](https://matplotlib.org/)
* [pandas .plot](https://pandas.pydata.org/pandas-docs/stable/visualization.html)
* [plotnine](https://github.com/has2k1/plotnine)
* a bit of [seaborn](https://seaborn.pydata.org/)

```{code-cell} ipython3
import numpy as np
import pandas as pd

import matplotlib.pylab as plt
import plotnine as p9
import seaborn as sns
```

### To 'grammar of graphics' or not to 'grammar of graphics'?

+++

#### Introduction

+++

There is `titanic` again...

```{code-cell} ipython3
titanic = pd.read_csv("../data/titanic.csv")
```

Pandas plot...

```{code-cell} ipython3
fig, ax = plt.subplots()
plt.style.use('ggplot')
survival_rate = titanic.groupby("Pclass")['Survived'].mean()
survival_rate.plot(kind='bar', color='grey', 
                   rot=0, figsize=(6, 4), ax=ax)
ylab = ax.set_ylabel("Survival rate")
xlab = ax.set_xlabel("Cabin class")
```

Plotnine plot...

```{code-cell} ipython3
(p9.ggplot(titanic, p9.aes(x="factor(Pclass)", 
                           y="Survived"))   #add color/fill
     + p9.geom_bar(stat='stat_summary', width=0.5)
     + p9.theme(figure_size=(5, 3))
     + p9.ylab("Survival rate")
     + p9.xlab("Cabin class")
)
```

An important difference is the *imperative* approach from `matplotlib` versus the *declarative* approach from `plotnine`:

+++

| imperative | declarative |
|------------|-------------|
| Specify **how** something should be done |  Specify **what** should be done            |
| **Manually specify** the individual plotting steps | Individual plotting steps based on **declaration** |
| e.g. `for ax in axes: ax.plot(...` | e.g. `+ facet_wrap('my_variable)` |

+++

<center><i>(seaborn lands somewhere in between)</i></center>

+++

Which approach to use, is also a matter of personal preference....

+++

Although, take following elements into account:
* When your data consists of only **1 factor variable**, such as

| ID | variable 1 | variable 2 | variabel ... | 
|------------|-------------| ---- | ----- |
| 1 | 0.2 | 0.8 | ... |
| 2 | 0.3 | 0.1 | ... |
| 3 | 0.9 | 0.6 | ... |
| 4 | 0.1 | 0.7 | ... |
| ...  | ... | ... | ...|

the added value of using a grammar of graphics approach is LOW. 

* When working with **timeseries data** from sensors or continuous logging, such as

| datetime | station 1 | station 2 | station ... | 
|------------|-------------| ---- | ----- |
| 2017-12-20T17:50:46Z | 0.2 | 0.8 | ... |
| 2017-12-20T17:50:52Z | 0.3 | 0.1 | ... |
| 2017-12-20T17:51:03Z | 0.9 | 0.6 | ... |
| 2017-12-20T17:51:40Z | 0.1 | 0.7 | ... |
| ...  | ... | ... | ...|

the added value of using a grammar of graphics approach is LOW.

* When working with different experiments, different conditions, (factorial) **experimental designs**, such as

| ID | substrate | addition (ml)  | measured_value | 
|----|-----------| ----- | ------ |
| 1  | Eindhoven | 0.3 | 7.2 |
| 2  | Eindhoven | 0.6 | 6.7 |
| 3  | Eindhoven | 0.9 | 5.2 |
| 4  | Destelbergen | 0.3 | 7.2 |
| 5  | Destelbergen | 0.6 | 6.8 |
| ...  | ... | ... | ...|

the added value of using a grammar of graphics approach is HIGH. Represent you're data [`tidy`](http://www.jeannicholashould.com/tidy-data-in-python.html) to achieve maximal benefit!

+++

<div class="alert alert-info">

 <b>Remember</b>: 

 <ul>
    <li>These packages will support you towards <b>static, publication quality</b> figures in a variety of <b>hardcopy</b> formats</li>
    <li>In general, start with a <i>high-level</i> function and finish with matplotlib</li>
</ul>
<br>

</div>

+++

Still...

> *I've been wasting too much time on this one stupid detail for this publication graph*

![](https://imgs.xkcd.com/comics/is_it_worth_the_time.png)

```{code-cell} ipython3
fig.savefig("my_plot_with_one_issue.pdf")
```

<div class="alert alert-warning"  style="font-size:120%">

 <b>Notice</b>: 

 <ul>
    <li>In the end... there is still <a href="https://inkscape.org/en/">Inkscape</a> to the rescue!</li>
</ul>
<br>

</div>

+++

### Seaborn

```{code-cell} ipython3
plt.style.use('seaborn-white')
```

> Seaborn is a library for making attractive and **informative statistical** graphics in Python. It is built **on top of matplotlib** and tightly integrated with the PyData stack, including **support for numpy and pandas** data structures and statistical routines from scipy and statsmodels.

+++

Seaborn provides a set of particularly interesting plot functions:

+++

#### scatterplot matrix

+++

We've already encountered the [`pairplot`](https://seaborn.pydata.org/examples/scatterplot_matrix.html), a typical quick explorative plot function

```{code-cell} ipython3
# the discharge data for a number of measurement stations as example
flow_data = pd.read_csv("../data/vmm_flowdata.csv", parse_dates=True, index_col=0)
flow_data = flow_data.dropna()
flow_data['year'] = flow_data.index.year
flow_data.head()
```

```{code-cell} ipython3
# pairplot
sns.pairplot(flow_data, vars=["L06_347", "LS06_347", "LS06_348"], 
             hue='year', palette=sns.color_palette("Blues_d"), 
             diag_kind='kde', dropna=True)
```

#### heatmap

+++

Let's just start from a Ghent data set: The city of Ghent provides data about migration in the different districts as open data, https://data.stad.gent/data/58

```{code-cell} ipython3
district_migration = pd.read_csv("https://datatank.stad.gent/4/bevolking/wijkmigratieperduizend.csv", 
                                 sep=";", index_col=0)
district_migration.index.name = "wijk"
district_migration.head()
```

```{code-cell} ipython3
# cleaning the column headers
district_migration.columns = [year[-4:] for year in district_migration.columns]
district_migration.head()
```

```{code-cell} ipython3
#adding a total column
district_migration['TOTAAL'] = district_migration.sum(axis=1)
```

```{code-cell} ipython3
fig, ax = plt.subplots(figsize=(10, 10))
sns.heatmap(district_migration, annot=True, fmt=".1f", linewidths=.5, 
            cmap="PiYG", ax=ax, vmin=-20, vmax=20)
ylab = ax.set_ylabel("")
ax.set_title("Migration of Ghent districts", size=14)
```

#### jointplot

+++

[jointplot](https://seaborn.pydata.org/generated/seaborn.jointplot.html#seaborn.jointplot) provides a very convenient function to check the combined distribution of two variables in a DataFrame (bivariate plot)

+++

Using the default options on the flow_data dataset

```{code-cell} ipython3
g = sns.jointplot(data=flow_data, 
                  x='LS06_347', y='LS06_348')
```

```{code-cell} ipython3
g = sns.jointplot(data=flow_data, 
                  x='LS06_347', y='LS06_348', 
                  kind="reg", space=0)
```

more options, applied on the migration data set:

```{code-cell} ipython3
g = sns.jointplot(data=district_migration.transpose(), 
                  x='Oud Gentbrugge', y='Nieuw Gent - UZ', 
                  kind="kde", height=7, space=0) # kde
```

<div class="alert alert-danger">

 <b>Notice!</b>: 

 <ul>
    <li>Watch out with the interpretation. The representations (`kde`, `regression`) is based on a very limited set of data points!</li>
</ul>
<br>

</div>

+++

Adding the data points itself, provides at least this info to the user:

```{code-cell} ipython3
g = (sns.jointplot(
        data=district_migration.transpose(), 
        x='Oud Gentbrugge', y='Nieuw Gent - UZ', 
        kind="scatter", height=7, space=0, stat_func=None,
        marginal_kws=dict(bins=20, rug=True)
        ).plot_joint(sns.kdeplot, zorder=0, 
                     n_levels=5, cmap='Reds'))
g.savefig("my_great_plot.pdf")
```

#### jointplot

+++

With [catplot](https://seaborn.pydata.org/generated/seaborn.catplot.html) and [relplot](https://seaborn.pydata.org/generated/seaborn.relplot.html#seaborn.relplot), Seaborn provides similarities with the Grammar of Graphics

```{code-cell} ipython3
sns.catplot(data=titanic, x="Survived",
            col="Pclass", kind="count")
```

<div class="alert alert-info">

 <b>Remember - Check the package galleries</b>: 

 <ul>
    <li><a href="https://matplotlib.org/gallery.html">Matplotlib gallery</a></li>
    <li><a href="http://seaborn.pydata.org/examples/">Seaborn gallery</a></li>
    <li><a href="http://plotnine.readthedocs.io/en/stable/gallery.html">Plotnine gallery</a> and <a href="https://www.r-graph-gallery.com/portfolio/ggplot2-package/">R ggplot2 gallery</a> </li>
    <li>An overview based on the type of graph using Python is given <a href="https://python-graph-gallery.com/">here</a>.</li>
</ul>
<br>

</div>

+++

## Interactivity and the web matter these days!

+++

### Bokeh

+++

> *[Bokeh](https://bokeh.pydata.org/en/latest/) is a Python interactive visualization library that targets modern web browsers for presentation*

```{code-cell} ipython3
from bokeh.plotting import figure, output_file, show
```

By default, Bokeh will open a new webpage to plot the figure. Still, the **integration with notebooks** is provided as well:

```{code-cell} ipython3
from bokeh.io import output_notebook
```

```{code-cell} ipython3
output_notebook()
```

```{code-cell} ipython3
p = figure()
p.line(x=[1, 2, 3], y=[4,6,2])
show(p)
```

<div class="alert alert-danger">

 <b>Notice!</b>: 

 <ul>
    <li>Bokeh does <b>not</b> support <code>eps</code>, <code>pdf</code> export of plots directly. Exporting to svg is available but still limited, see <a href="https://docs.bokeh.org/en/latest/docs/user_guide/export.html">documentation</a></li>.
</ul>

</div>

+++

To accomodate the users of **Pandas**, a `pd.DataFrame` can also be used as the input for a Bokeh plot:

```{code-cell} ipython3
from bokeh.models import ColumnDataSource
source_data = ColumnDataSource(data=flow_data)
```

```{code-cell} ipython3
flow_data.head()
```

Useful to know when you want to use the index as well:
> *If the DataFrame has a named index column, then CDS will also have a column with this name. However, if the index name (or any subname of a MultiIndex) is None, then the CDS will have a column generically named index for the index.*

```{code-cell} ipython3
p = figure(x_axis_type="datetime", plot_height=300, plot_width=900)
p.line(x='Time', y='L06_347', source=source_data)
show(p)
```

The setup of the graph, is by adding new elements to the figure object, e.g. adding annotations:

```{code-cell} ipython3
from bokeh.models import ColumnDataSource, BoxAnnotation, Label
```

```{code-cell} ipython3
p = figure(x_axis_type="datetime", plot_height=300, plot_width=900)
p.line(x='Time', y='L06_347', source=source_data)
p.circle(x='Time', y='L06_347', source=source_data, fill_alpha= 0.3, line_alpha=0.3)

alarm_box = BoxAnnotation(bottom=10, fill_alpha=0.3, 
                          fill_color='#ff6666')  # arbitrary value; this is NOT the real-case value
p.add_layout(alarm_box)

alarm_label = Label(text="Flood risk", x_units='screen', 
                    x= 10, y=10, text_color="#330000")
p.add_layout(alarm_label)

show(p)
```

Also [this `jointplot`](https://demo.bokehplots.com/apps/selection_histogram) and [this gapminder reproduction](https://demo.bokehplots.com/apps/gapminder) is based on Bokeh!

+++

<div class="alert alert-info">

 <b>More Bokeh?</b>

 <ul>
    <li>Try the <a href="http://nbviewer.jupyter.org/github/bokeh/bokeh-notebooks/blob/master/quickstart/quickstart.ipynb">quickstart notebook</a> yourself and check the <a href="http://nbviewer.jupyter.org/github/bokeh/bokeh-notebooks/blob/master/tutorial/00%20-%20Introduction%20and%20Setup.ipynb">tutorials</a></li>
    <li>Check the <a href="https://bokeh.pydata.org/en/latest/docs/gallery.html">Bokeh package gallery</a></li>
    <li><a href="https://bokeh.pydata.org/en/latest/docs/user_guide.html">Documentation</a> is very extensive...</li>
    <li>Bokeh is used by a number of other plotting libraries for interactive visualisation: <a href="http://holoviews.org/index.html">holoviews</a>, <a href="https://hvplot.holoviz.org/index.html">hvplot</a> and <a href="http://geoviews.org/">geoviews</a>.</li>
</ul>
    
</div>

+++

### Plotly

+++

> [plotly.py](https://plot.ly/python/) is an interactive, browser-based graphing library for Python

```{code-cell} ipython3
import plotly
```

In the last years, plotly has been developed a lot and provides now a lot of functionalities for interactive plotting, see https://plot.ly/python/#fundamentals. It consists of two main components: __plotly__ provides all the basic components (so called `plotly.graph_objects`) to create plots and __plotly express__ provides a more high-level wrapper around `plotly.graph_objects` for rapid data exploration and figure generation. The latter focuses on _tidy_ data representation.

As an example: create a histogram using the plotly `graph_objects`:

```{code-cell} ipython3
import plotly.graph_objects as go

fig = go.Figure(data=[go.Histogram(x=titanic['Fare'].values)])
fig.show()
```

Can be done in plotly express as well, supporting direct interaction with a Pandas DataFrame:

```{code-cell} ipython3
import plotly.express as px

fig = px.histogram(titanic, x="Fare")
fig.show()
```

<div class="alert alert-danger">

 <b>Notice!</b>: 

 <ul>
    <li>Prior versions of plotly.py contained functionality for creating figures in both "online" and "offline" modes. Version 4 of plotly is "offline"-only. Make sure you check the latest documentation and watch out with outdated stackoverflow suggestions. The previous commercial/online version is rebranded into <a href='https://plot.ly/online-chart-maker/'>chart studio</a>.
     </li>
</ul>

</div>

+++

As mentioned in the example, the interaction of plotly with Pandas is supported:

+++

.1. Indirectly, by using the `plotly` specific [dictionary](https://plot.ly/python/creating-and-updating-figures/#figures-as-dictionaries) syntax:

```{code-cell} ipython3
import plotly.graph_objects as go

df = flow_data[["L06_347", "LS06_348"]]

fig = go.Figure({
    "data": [{'x': df.index, 
              'y': df[col], 
              'name': col} for col in df.columns],  # remark, we use a list comprehension here ;-)
    "layout": {"title": {"text": "Streamflow data"}}
})
fig.show()
```

.2. or using the `plotly` object oriented approach with [graph objects](https://plot.ly/python/creating-and-updating-figures/#figures-as-graph-objects):

```{code-cell} ipython3
df = flow_data[["L06_347", "LS06_348"]]

fig = go.Figure()

for col in df.columns:
    fig.add_trace(go.Scatter(
                    x=df.index,
                    y=df[col],
                    name=col))
    
fig.layout=go.Layout(
        title=go.layout.Title(text="Streamflow data")
    )
fig.show()
```

.3. or using the `plotly express` functionalities:

```{code-cell} ipython3
df = flow_data[["L06_347", "LS06_348"]].reset_index()  # reset index, as plotly express can not use the index directly
df = df.melt(id_vars="Time")  # from wide to long format
df.head()
```

As mentioned, plotly express targets __tidy__ data (cfr. plotnine,...), so we converted the data to tidy/long format before plotting:

```{code-cell} ipython3
import plotly.express as px

fig = px.line(df, x='Time', y='value', color="variable", title="Streamflow data")
fig.show()
```

.4. or by installing an additional package, `cufflinks`, which enables Pandas plotting with `iplot` instead of `plot`:

```{code-cell} ipython3
import cufflinks as cf

df = flow_data[["L06_347", "LS06_348"]]
fig = df.iplot(kind='scatter', asFigure=True)
fig.show()
```

`cufflinks` applied on the data set of district migration:

```{code-cell} ipython3
district_migration.transpose().iplot(kind='box', asFigure=True).show()
```

<div class="alert alert-info">

 <b>Plotly</b>

 <ul>
    <li>Check the <a href="https://plot.ly/python/">package gallery</a> for plot examples.</li>
    <li>Plotly express provides high level plotting functionalities and plotly graph objects the low level components.
    <li>More information about the cufflinks connection with Pandas is available <a href="https://nbviewer.jupyter.org/gist/santosjorge/aba934a0d20023a136c2">here</a>.</li>
</ul>
<br>

</div>

+++

<div class="alert alert-warning">

 <b>For R users...</b>: 
<br><br>
Both plotly and Bokeh provide interactivity (sliders,..), but are not the full equivalent of [`Rshiny`](https://shiny.rstudio.com/).<br>A similar functionality of Rshiny is provided by [`dash`](https://plot.ly/products/dash/), created by the same company as plotly.
<br>

</div>

+++

## You like web-development and Javascript?

+++

### Altair

> *[Altair](https://altair-viz.github.io/) is a declarative statistical visualization library for Python, based on Vega-Lite.*

```{code-cell} ipython3
import altair as alt
```

Reconsider the titanic example of the start fo this notebook:

```{code-cell} ipython3
fig, ax = plt.subplots()
plt.style.use('ggplot')
survival_rate = titanic.groupby("Pclass")['Survived'].mean()
survival_rate.plot(kind='bar', color='grey', 
                   rot=0, figsize=(6, 4), ax=ax)
ylab = ax.set_ylabel("Survival rate")
xlab = ax.set_xlabel("Cabin class")
```

Translating this to `Altair` syntax:

```{code-cell} ipython3
alt.Chart(titanic).mark_bar().encode(
    x=alt.X('Pclass:O', axis=alt.Axis(title='Cabin class')),
    y=alt.Y('mean(Survived):Q', 
            axis=alt.Axis(format='%', 
                          title='survival_rate'))
)
```

Similar to `plotnine` with `aesthetic`, expressing the influence of a varibale on the plot building can be `encoded`:

```{code-cell} ipython3
alt.Chart(titanic).mark_bar().encode(
    x=alt.X('Pclass:O', axis=alt.Axis(title='Cabin class')),
    y=alt.Y('mean(Survived):Q', 
            axis=alt.Axis(format='%', 
                          title='survival_rate')),
    column="Sex"
)
```

The typical ingedrients of the **grammar of graphics** are available again:

```{code-cell} ipython3
(alt.Chart(titanic)  # Link with the data
     .mark_circle().encode(  # defining a geometry
        x="Fare:Q",   # provide aesthetics by linking variables to channels
        y="Age:Q",
        column="Pclass:O",
        color="Sex:N",
))
# scales,... can be adjusted as well
```

For information on this `...:Q`, `...:N`,`...:O`, see the [data type section](https://altair-viz.github.io/user_guide/encoding.html#encoding-data-types) of the documentation:

Data Type |	Shorthand Code |	Description
----------|-----------------|---------------
quantitative |		Q |		a continuous real-valued quantity
ordinal |		O |		a discrete ordered quantity
nominal |		N |		a discrete unordered category
temporal |		T |		a time or date value

+++

<div class="alert alert-info">

 <b>Remember</b>

 <ul>
    <li>Altair provides a pure-Python <b>Grammar of Graphics</b> implementation!</li>
    <li>Altair is built on top of the <a href="https://vega.github.io/vega-lite/">Vega-Lite</a> visualization grammar, which can be interpreted as a language to specify a graph (from data to figure).</li>
    <li>Altair easily integrates with web-technology (HTML/Javascript)</li>
</ul>
<br>

</div>

+++

## You're data sets are HUGE?

+++

When you're working with a lot of records, the visualization of the individual points does not always make sense as there are simply to many dots overlapping eachother (check [this](https://bokeh.github.io/datashader-docs/user_guide/1_Plotting_Pitfalls.html) notebook for a more detailed explanation).

+++

Consider the open data set:
> Bird tracking - GPS tracking of Lesser Black-backed Gulls and Herring Gulls breeding at the southern North Sea coast https://www.gbif.org/dataset/83e20573-f7dd-4852-9159-21566e1e691e with > 8e6 records

+++

Working with such a data set on a local machine is not straightforward anymore, as this data set will consume a lot of memory to be handled by the default plotting libraries. Moreover, visualizing every single dot is not useful anymore at coarser zoom levels. 

+++

The package [datashader](https://bokeh.github.io/datashader-docs/index.html) provides a solution for this size of data sets and works together with other packages such as `bokeh` and `holoviews`.

+++

We download just a single year (e.g. 2018) of data from [the gull data set](zenodo.org/record/3541812#.XfZYcNko-V6) and store it in the `data` folder. The 2018 data file has around 4.8 million records.

```{code-cell} ipython3
import pandas as pd, holoviews as hv
from colorcet import fire
from datashader.geo import lnglat_to_meters
from holoviews.element.tiles import EsriImagery
from holoviews.operation.datashader import rasterize, shade

df = pd.read_csv('../data/HG_OOSTENDE-gps-2018.csv', usecols=['location-long', 'location-lat'])
df.columns = ['longitude', 'latitude']
df.loc[:,'longitude'], df.loc[:,'latitude'] = lnglat_to_meters(df.longitude, df.latitude)
```

```{code-cell} ipython3
hv.extension('bokeh')

map_tiles  = EsriImagery().opts(alpha=1.0, width=800, height=800, bgcolor='black')
points     = hv.Points(df, ['longitude', 'latitude'])
rasterized = shade(rasterize(points, x_sampling=1, y_sampling=1, width=800, height=800), cmap=fire)

map_tiles * rasterized
```

<div class="alert alert-info">

 <b>When not to use datashader</b>

 <ul>
    <li>Plotting less than 1e5 or 1e6 data points</li>
    <li>When every datapoint matters; standard Bokeh will render all of them</li>
    <li>For full interactivity (hover tools) with every datapoint</li>
 </ul>
<br>

 <b>When to use datashader</b>

 <ul>
    <li>Actual big data; when Bokeh/Matplotlib have trouble</li>
    <li>When the distribution matters more than individual points</li>
    <li>When you find yourself sampling or binning to better understand the distribution</li>
 </ul>
<br>

([source](http://nbviewer.jupyter.org/github/bokeh/bokeh-notebooks/blob/master/tutorial/A2%20-%20Visualizing%20Big%20Data%20with%20Datashader.ipynb))

</div>

+++

<div class="alert alert-warning">

 <b>More alternatives for large data set visualisation that are worthwhile exploring:</b>: 

 <ul>
    <li><a href="http://vaex.astro.rug.nl/">vaex</a> which also provides on the fly binning or aggregating the data on a grid to be represented.</li>
    <li><a href="https://glumpy.github.io/">Glumpy</a> and <a href="http://vispy.org/">Vispy</a>, which both rely on <a href="https://www.opengl.org/">OpenGL</a> to achieve high performance</li>
</ul>
<br>

</div>

+++

## You want to dive deeper into Python viz?

+++

For a overview of the status of Python visualisation packages and tools, have a look at the [pyviz](https://pyviz.org) website.

```{code-cell} ipython3
from IPython.display import Image
Image('https://raw.githubusercontent.com/rougier/python-visualization-landscape/master/landscape.png')
```

or check the interactive version [here](https://rougier.github.io/python-visualization-landscape/landscape-colors.html).

+++

further reading: http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003833

+++

## Acknowledgements


https://speakerdeck.com/jakevdp/pythons-visualization-landscape-pycon-2017
