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

<p><font size="6"><b>Plotnine: Introduction </b></font></p>


> *DS Data manipulation, analysis and visualisation in Python*  
> *December, 2019*

> *© 2016, Joris Van den Bossche and Stijn Van Hoey  (<mailto:jorisvandenbossche@gmail.com>, <mailto:stijnvanhoey@gmail.com>). Licensed under [CC BY 4.0 Creative Commons](http://creativecommons.org/licenses/by/4.0/)*

---

```{code-cell} ipython3
import pandas as pd
```

# Plotnine

http://plotnine.readthedocs.io/en/stable/

+++

* Built on top of Matplotlib, but providing
    1. High level functions
    2. Implementation of the [Grammar of Graphics](https://www.amazon.com/Grammar-Graphics-Statistics-Computing/dp/0387245448), which became famous due to the `ggplot2` R package 
    3. The syntax is highly similar to the `ggplot2` R package
* Works well with Pandas

```{code-cell} ipython3
import plotnine as p9
```

## Introduction

+++

We will use the Titanic example data set:

```{code-cell} ipython3
titanic = pd.read_csv('../data/titanic.csv')
```

```{code-cell} ipython3
titanic.head()
```

Let's consider following question:
>*For each class at the Titanic, how many people survived and how many died?*

+++

Hence, we should define the *size* of respectively the zeros (died) and ones (survived) groups of column `Survived`, also grouped by the `Pclass`. In Pandas terminology:

```{code-cell} ipython3
survived_stat = titanic.groupby(["Pclass", "Survived"]).size().rename('count').reset_index()
survived_stat
# Remark: the `rename` syntax is to provide the count column a column name 
```

Providing this data in a bar chart with pure Pandas is still partly supported:

```{code-cell} ipython3
survived_stat.plot(x='Survived', y='count', kind='bar')
## A possible other way of plotting this could be using groupby again:   
#survived_stat.groupby('Pclass').plot(x='Survived', y='count', kind='bar') # (try yourself by uncommenting)
```

but with mixed results...

+++

Plotting libraries focussing on the **grammar of graphics** are really targeting these *grouped* plots. For example, the plotting of the resulting counts can be expressed in the grammar of graphics:

```{code-cell} ipython3
(p9.ggplot(survived_stat, 
           p9.aes(x='Survived', y='count', fill='factor(Survived)'))
    + p9.geom_bar(stat='identity', position='dodge')
    + p9.facet_wrap(facets='Pclass'))
```

Moreover, these `count` operations are embedded in the typical Grammar of Graphics packages and we can do these operations directly on the original `titanic` data set in a single coding step:

```{code-cell} ipython3
(p9.ggplot(titanic,
           p9.aes(x='Survived', fill='factor(Survived)'))
    + p9.geom_bar(stat='count', position='dodge')
    + p9.facet_wrap(facets='Pclass'))
```

<div class="alert alert-info">

 <b>Remember</b>: 

 <ul>
    <li>The <b>Grammar of Graphics</b> is especially suitbale for these so-called <a href="http://vita.had.co.nz/papers/tidy-data.pdf">tidy</a> dataframe representations (check <a href="#this_is_tidy">here</a> for more about `tidy` data)</li>
  <li>plotnine is a library that supports the <a href="https://www.springer.com/gp/book/9780387245447">Grammar of graphics</a></li>
</ul>
<br>

</div>

+++

## Building a plotnine graph

+++

Building plots with plotnine is typically an iterative process. As illustrated in the introduction, a graph is setup by layering different elements on top of each other using the `+` operator. putting everything together in brackets `()` provides Python-compatible syntax.

+++

#### data

+++

* Bind the plot to a specific data frame using the data argument:

```{code-cell} ipython3
(p9.ggplot(data=titanic))
```

We haven 't defined anything else, so just an empty *figure* is available.

+++

#### aesthestics

+++

 
* Define aesthetics (**aes**), by **selecting variables** used in the plot and linking them to presentation such as plotting size, shape color, etc. You can interpret this as: **how** the variable will influence the plotted objects/geometries:

+++

The most important `aes` are: `x`, `y`, `alpha`, `color`, `colour`, `fill`, `linetype`, `shape`, `size` and `stroke`

```{code-cell} ipython3
(p9.ggplot(titanic,
           p9.aes(x='factor(Pclass)', y='Fare')))
```

#### geometry

+++

* Still nothing plotted yet, as we have to define what kind of [**geometry**](http://plotnine.readthedocs.io/en/stable/api.html#geoms) will be used for the plot. The easiest is probably using points:

```{code-cell} ipython3
(p9.ggplot(titanic,
           p9.aes(x='factor(Pclass)', y='Fare'))
     + p9.geom_point()
) 
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>Starting from the code of the last figure, adapt the code in such a way that the <code>Sex</code> variable defines the <b>color</b> of the points in the graph. </li>
  <li>As both sex categories overlap, use an alternative geometry, so called <code>geom_jitter</code> </li>
</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

(p9.ggplot(titanic,
           p9.aes(x='factor(Pclass)', y='Fare', color='Sex'))
     + p9.geom_jitter()
) 
```

These are the basic elements to have a graph, but other elements can be added to the graph:

+++

#### labels

+++

* Change the [**labels**](http://plotnine.readthedocs.io/en/stable/api.html#Labels):

```{code-cell} ipython3
(p9.ggplot(titanic,
           p9.aes(x='factor(Pclass)', y='Fare'))
     + p9.geom_point()
     + p9.xlab("Cabin class")
) 
```

#### facets

+++

* Use the power of `groupby` and define [**facets**](http://plotnine.readthedocs.io/en/stable/api.html#facets) to group the plot by a grouping variable:

```{code-cell} ipython3
(p9.ggplot(titanic,
           p9.aes(x='factor(Pclass)', y='Fare'))
     + p9.geom_point()
     + p9.xlab("Cabin class")
     + p9.facet_wrap('Sex')#, dir='v')
) 
```

#### scales

+++

* Defining [**scale**](http://plotnine.readthedocs.io/en/stable/api.html#scales) for colors, axes,...

For example, a log-version of the y-axis could support the interpretation of the lower numbers:

```{code-cell} ipython3
(p9.ggplot(titanic,
           p9.aes(x='factor(Pclass)', y='Fare'))
     + p9.geom_point() 
     + p9.xlab("Cabin class")
     + p9.facet_wrap('Sex')
     + p9.scale_y_log10()
) 
```

#### theme

+++

* Changing [**theme** ](http://plotnine.readthedocs.io/en/stable/api.html#themes):

```{code-cell} ipython3
(p9.ggplot(titanic,
           p9.aes(x='factor(Pclass)', y='Fare'))
     + p9.geom_point() 
     + p9.xlab("Cabin class")
     + p9.facet_wrap('Sex')
     + p9.scale_y_log10()
     + p9.theme_bw()
) 
```

or changing specific [theming elements](http://plotnine.readthedocs.io/en/stable/api.html#Themeables), e.g. text size:

```{code-cell} ipython3
(p9.ggplot(titanic,
           p9.aes(x='factor(Pclass)', y='Fare'))
     + p9.geom_point() 
     + p9.xlab("Cabin class")
     + p9.facet_wrap('Sex')
     + p9.scale_y_log10()
     + p9.theme_bw()
     + p9.theme(text=p9.element_text(size=14))
) 
```

#### more...

+++

* adding [**statistical derivatives**](http://plotnine.readthedocs.io/en/stable/api.html#stats)
* changing the [**plot coordinate**](http://plotnine.readthedocs.io/en/stable/api.html#coordinates) system

+++

<div class="alert alert-info">

 <b>Remember</b>: 

 <ul>
  <li>Start with defining your <code>data</code>, <code>aes</code> variables and a <code>geometry</code></li>
  <li>Further extend your plot with <code>scale_*</code>, <code>theme_*</code>, <code>xlab/ylab</code>, <code>facet_*</code></li>
</ul>
<br>

</div>

+++

## plotnine is built on top of Matplotlib

+++

As plotnine is built on top of Matplotlib, we can still retrieve the matplotlib `figure` object from plotnine for eventual customization:

```{code-cell} ipython3
myplot = (p9.ggplot(titanic, 
                    p9.aes(x='factor(Pclass)', y='Fare'))
     + p9.geom_point()
) 
```

The trick is to use the `draw()` function in plotnine:

```{code-cell} ipython3
my_plt_version = myplot.draw()
```

```{code-cell} ipython3
my_plt_version.axes[0].set_title("Titanic fare price per cabin class")
ax2 = my_plt_version.add_axes([0.5, 0.5, 0.3, 0.3], label="ax2")
my_plt_version
```

<div class="alert alert-info" style="font-size:18px">

 <b>Remember</b>: 

Similar to Pandas handling above, we can set up a matplotlib `Figure` with plotnine. Use `draw()` and the Matplotlib `Figure` is returned.

</div>

+++

## (OPTIONAL SECTION) Some more plotnine functionalities to remember...

+++

**Histogram**: Getting the univariaite distribution of the `Age`

```{code-cell} ipython3
(p9.ggplot(titanic.dropna(subset=['Age']), p9.aes(x='Age'))
     + p9.geom_histogram(bins=30))
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>Make a histogram of the age, grouped by the <code>Sex</code> of the passengers</li>
  <li>Make sure both graphs are underneath each other instead of next to each other to enhance comparison</li>

</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

(p9.ggplot(titanic.dropna(subset=['Age']), p9.aes(x='Age'))
     + p9.geom_histogram(bins=30)
     + p9.facet_wrap('Sex', nrow=2)
)
```

**boxplot/violin plot**: Getting the univariaite distribution of `Age` per `Sex`

```{code-cell} ipython3
(p9.ggplot(titanic.dropna(subset=['Age']), p9.aes(x='Sex', y='Age'))
     + p9.geom_boxplot())
```

Actually, a *violinplot* provides more inside to the distribution:

```{code-cell} ipython3
(p9.ggplot(titanic.dropna(subset=['Age']), p9.aes(x='Sex', y='Age'))
     + p9.geom_violin()
)
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>Make a violin plot of the Age for each `Sex`</li>
  <li>Add `jitter` to the plot to see the actual data points</li>
  <li>Adjust the transparency of the jitter dots to improve readability</li>

</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

(p9.ggplot(titanic.dropna(subset=['Age']), p9.aes(x='Sex', y='Age'))
     + p9.geom_violin()
     + p9.geom_jitter(alpha=0.2)
)
```

**regressions**

+++

plotnine supports a number of statistical functions with the [`geom_smooth` function]:(http://plotnine.readthedocs.io/en/stable/generated/plotnine.stats.stat_smooth.html#plotnine.stats.stat_smooth)

The available methods are:
```
* 'auto'       # Use loess if (n<1000), glm otherwise
* 'lm', 'ols'  # Linear Model
* 'wls'        # Weighted Linear Model
* 'rlm'        # Robust Linear Model
* 'glm'        # Generalized linear Model
* 'gls'        # Generalized Least Squares
* 'lowess'     # Locally Weighted Regression (simple)
* 'loess'      # Locally Weighted Regression
* 'mavg'       # Moving Average
* 'gpr'        # Gaussian Process Regressor
```

each of these functions are provided by existing Python libraries and integrated in plotnine, so make sure to have these dependencies installed (read the error message!)

```{code-cell} ipython3
(p9.ggplot(titanic.dropna(subset=['Age', 'Sex', 'Fare']), 
           p9.aes(x='Fare', y='Age', color="Sex"))
     + p9.geom_point()
     + p9.geom_rug(alpha=0.2)
     + p9.geom_smooth(method='lm')
)
```

```{code-cell} ipython3
(p9.ggplot(titanic.dropna(subset=['Age', 'Sex', 'Fare']), 
           p9.aes(x='Fare', y='Age', color="Sex"))
     + p9.geom_point()
     + p9.geom_rug(alpha=0.2)
     + p9.geom_smooth(method='lm')
     + p9.facet_wrap("Survived")
     + p9.scale_color_brewer(type="qual")
)
```

# Need more plotnine inspiration? 

+++

<div class="alert alert-info" style="font-size:18px">

 <b>Remember</b>

[plotnine gallery](http://plotnine.readthedocs.io/en/stable/gallery.html) and [great documentation](http://plotnine.readthedocs.io/en/stable/api.html)</li>
<br><br>
Important resources to start from!

</div>

+++

<a id='this_is_tidy'></a>

+++

# What is `tidy`?

+++

If you're wondering what *tidy* data representations are, you can read the scientific paper by Hadley Wickham, http://vita.had.co.nz/papers/tidy-data.pdf. 

Here, we just introduce the main principle very briefly:

+++

Compare:

#### un-tidy
        
| WWTP | Treatment A | Treatment B |
|:------|-------------|-------------|
| Destelbergen | 8.  | 6.3 |
| Landegem | 7.5  | 5.2 |
| Dendermonde | 8.3  | 6.2 |
| Eeklo | 6.5  | 7.2 |

*versus*

#### tidy

| WWTP | Treatment | pH |
|:------|:-------------:|:-------------:|
| Destelbergen | A  | 8. |
| Landegem | A  | 7.5 |
| Dendermonde | A  | 8.3 |
| Eeklo | A  | 6.5 |
| Destelbergen | B  | 6.3 |
| Landegem | B  | 5.2 |
| Dendermonde | B  | 6.2 |
| Eeklo | B  | 7.2 |

+++

This is sometimes also referred as *short* versus *long* format for a specific variable... Plotnine (and other grammar of graphics libraries) work better on `tidy` data, as it better supports `groupby`-like transactions!

+++

<div class="alert alert-info" style="font-size:16px">

 <b>Remember:</b>
 
 <br><br>
 
 A tidy data set is setup as follows:
 
<ul>
  <li>Each <code>variable</code> forms a <b>column</b> and contains <code>values</code></li>
  <li>Each <code>observation</code> forms a <b>row</b></li>
    <li>Each type of <code>observational unit</code> forms a <b>table</b>.</li>
</ul>
</div>
