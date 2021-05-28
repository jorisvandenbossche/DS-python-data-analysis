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

<p><font size="6"><b>03 - Pandas: Indexing and selecting data - part II</b></font></p>


> *DS Data manipulation, analysis and visualisation in Python*  
> *December, 2019*

> *© 2016-2019, Joris Van den Bossche and Stijn Van Hoey  (<mailto:jorisvandenbossche@gmail.com>, <mailto:stijnvanhoey@gmail.com>). Licensed under [CC BY 4.0 Creative Commons](http://creativecommons.org/licenses/by/4.0/)*

---

```{code-cell} ipython3
import pandas as pd
```

```{code-cell} ipython3
# redefining the example objects

# series
population = pd.Series({'Germany': 81.3, 'Belgium': 11.3, 'France': 64.3, 
                        'United Kingdom': 64.9, 'Netherlands': 16.9})

# dataframe
data = {'country': ['Belgium', 'France', 'Germany', 'Netherlands', 'United Kingdom'],
        'population': [11.3, 64.3, 81.3, 16.9, 64.9],
        'area': [30510, 671308, 357050, 41526, 244820],
        'capital': ['Brussels', 'Paris', 'Berlin', 'Amsterdam', 'London']}
countries = pd.DataFrame(data)
countries
```

<div class="alert alert-info" style="font-size:120%">
<b>REMEMBER</b>: <br><br>

So as a summary, `[]` provides the following convenience shortcuts:

* **Series**: selecting a **label**: `s[label]`
* **DataFrame**: selecting a single or multiple **columns**:`df['col']` or `df[['col1', 'col2']]`
* **DataFrame**: slicing or filtering the **rows**: `df['row_label1':'row_label2']` or `df[mask]`

</div>

+++

# Changing the DataFrame index

+++

We have mostly worked with DataFrames with the default *0, 1, 2, ... N* row labels (except for the time series data). But, we can also set one of the columns as the index.

Setting the index to the country names:

```{code-cell} ipython3
countries = countries.set_index('country')
countries
```

Reversing this operation, is `reset_index`:

```{code-cell} ipython3
countries.reset_index('country')
```

# Selecting data based on the index

+++

<div class="alert alert-warning" style="font-size:120%">
<b>ATTENTION!</b>: <br><br>

One of pandas' basic features is the labeling of rows and columns, but this makes indexing also a bit more complex compared to numpy. <br><br> We now have to distuinguish between:

* selection by **label** (using the row and column names)
* selection by **position** (using integers)

</div>

+++

## Systematic indexing with `loc` and `iloc`

+++

When using `[]` like above, you can only select from one axis at once (rows or columns, not both). For more advanced indexing, you have some extra attributes:
    
* `loc`: selection by label
* `iloc`: selection by position

Both `loc` and `iloc` use the following pattern: `df.loc[ <selection of the rows> , <selection of the columns> ]`.

This 'selection of the rows / columns' can be: a single label, a list of labels, a slice or a boolean mask.

+++

Selecting a single element:

```{code-cell} ipython3
countries.loc['Germany', 'area']
```

But the row or column indexer can also be a list, slice, boolean array (see next section), ..

```{code-cell} ipython3
countries.loc['France':'Germany', ['area', 'population']]
```

<div class="alert alert-danger">
<b>NOTE</b>:

* Unlike slicing in numpy, the end label is **included**!

</div>

+++

---
Selecting by position with `iloc` works similar as **indexing numpy arrays**:

```{code-cell} ipython3
countries.iloc[0:2,1:3]
```

---

The different indexing methods can also be used to **assign data**:

```{code-cell} ipython3
countries2 = countries.copy()
countries2.loc['Belgium':'Germany', 'population'] = 10
```

```{code-cell} ipython3
countries2
```

<div class="alert alert-info" style="font-size:120%">
<b>REMEMBER</b>: <br><br>

Advanced indexing with **loc** and **iloc**

* **loc**: select by label: `df.loc[row_indexer, column_indexer]`
* **iloc**: select by position: `df.iloc[row_indexer, column_indexer]`

</div>

+++

<div class="alert alert-success">
<b>EXERCISE</b>:

<p>
<ul>
    <li>Add the population density as column to the DataFrame.</li>
</ul>
</p>
Note: the population column is expressed in millions.
</div>

```{code-cell} ipython3
:clear_cell: true

countries['density'] = countries['population']*1000000 / countries['area']
```

<div class="alert alert-success">
<b>EXERCISE</b>:

 <ul>
  <li>Select the capital and the population column of those countries where the density is larger than 300</li>
</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

countries.loc[countries['density'] > 300, ['capital', 'population']]
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>Add a column 'density_ratio' with the ratio of the population density to the average population density for all countries.</li>
</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

countries['density_ratio'] = countries['density'] / countries['density'].mean()
countries
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>Change the capital of the UK to Cambridge</li>
</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

countries.loc['United Kingdom', 'capital'] = 'Cambridge'
countries
```

<div class="alert alert-success">
<b>EXERCISE</b>:

 <ul>
  <li>Select all countries whose population density is between 100 and 300 people/km²</li>
</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

countries[(countries['density'] > 100) & (countries['density'] < 300)]
```

# Alignment on the index

+++

<div class="alert alert-danger">

**WARNING**: **Alignment!** (unlike numpy)

* Pay attention to **alignment**: operations between series will align on the index:

</div>

```{code-cell} ipython3
population = countries['population']
s1 = population[['Belgium', 'France']]
s2 = population[['France', 'Germany']]
```

```{code-cell} ipython3
s1
```

```{code-cell} ipython3
s2
```

```{code-cell} ipython3
s1 + s2
```

# Pitfall: chained indexing (and the 'SettingWithCopyWarning')

```{code-cell} ipython3
df = countries.copy()
```

When updating values in a DataFrame, you can run into the infamous "SettingWithCopyWarning" and issues with chained indexing.

Assume we want to cap the population and replace all values above 50 with 50. We can do this using the basic `[]` indexing operation twice ("chained indexing"):

```{code-cell} ipython3
df[df['population'] > 50]['population'] = 50
```

However, we get a warning, and we can also see that the original dataframe did not change:

```{code-cell} ipython3
df
```

The warning message explains that we should use `.loc[row_indexer,col_indexer] = value` instead. That is what we just learned in this notebook, so we can do:

```{code-cell} ipython3
df.loc[df['population'] > 50, 'population'] = 50
```

And now the dataframe actually changed:

```{code-cell} ipython3
df
```

To explain *why* the original `df[df['population'] > 50]['population'] = 50` didn't work, we can do the "chained indexing" in two explicit steps:

```{code-cell} ipython3
temp = df[df['population'] > 50]
temp['population'] = 50
```

For Python, there is no real difference between the one-liner or this two-liner. And when writing it as two lines, you can see we make a temporary, filtered dataframe (called `temp` above). So here, with `temp['population'] = 50`, we are actually updating `temp` but not the original `df`.

+++

<div class="alert alert-info" style="font-size:120%">

<b>REMEMBER!</b><br><br>

What to do when encountering the *value is trying to be set on a copy of a slice from a DataFrame* error?

* Use `loc` instead of chained indexing **if possible**!
* Or `copy` explicitly if you don't want to change the original data.

</div>

+++

# Exercises using the Titanic dataset

```{code-cell} ipython3
df = pd.read_csv("../data/titanic.csv")
```

```{code-cell} ipython3
df.head()
```

<div class="alert alert-success">

<b>EXERCISE</b>:

* Select all rows for male passengers and calculate the mean age of those passengers. Do the same for the female passengers. Do this now using `.loc`.

</div>

```{code-cell} ipython3
:clear_cell: true

df.loc[df['Sex'] == 'male', 'Age'].mean()
```

```{code-cell} ipython3
:clear_cell: true

df.loc[df['Sex'] == 'female', 'Age'].mean()
```

We will later see an easier way to calculate both averages at the same time with groupby.

```{code-cell} ipython3

```
