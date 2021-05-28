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

<p><font size="6"><b>07 - Pandas: Reshaping data</b></font></p>

> *DS Data manipulation, analysis and visualisation in Python*  
> *December, 2019*

> *© 2016-2019, Joris Van den Bossche and Stijn Van Hoey  (<mailto:jorisvandenbossche@gmail.com>, <mailto:stijnvanhoey@gmail.com>). Licensed under [CC BY 4.0 Creative Commons](http://creativecommons.org/licenses/by/4.0/)*

---

```{code-cell} ipython3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

# Pivoting data

+++

## Cfr. excel

+++

People who know Excel, probably know the **Pivot** functionality:

+++

![](../img/pivot_excel.png)

+++

The data of the table:

```{code-cell} ipython3
excelample = pd.DataFrame({'Month': ["January", "January", "January", "January", 
                                  "February", "February", "February", "February", 
                                  "March", "March", "March", "March"],
                   'Category': ["Transportation", "Grocery", "Household", "Entertainment",
                                "Transportation", "Grocery", "Household", "Entertainment",
                                "Transportation", "Grocery", "Household", "Entertainment"],
                   'Amount': [74., 235., 175., 100., 115., 240., 225., 125., 90., 260., 200., 120.]})
```

```{code-cell} ipython3
excelample
```

```{code-cell} ipython3
excelample_pivot = excelample.pivot(index="Category", columns="Month", values="Amount")
excelample_pivot
```

Interested in *Grand totals*?

```{code-cell} ipython3
# sum columns
excelample_pivot.sum(axis=1)
```

```{code-cell} ipython3
# sum rows
excelample_pivot.sum(axis=0)
```

## Pivot is just reordering your data:

+++

Small subsample of the titanic dataset:

```{code-cell} ipython3
df = pd.DataFrame({'Fare': [7.25, 71.2833, 51.8625, 30.0708, 7.8542, 13.0],
                   'Pclass': [3, 1, 1, 2, 3, 2],
                   'Sex': ['male', 'female', 'male', 'female', 'female', 'male'],
                   'Survived': [0, 1, 0, 1, 0, 1]})
```

```{code-cell} ipython3
df
```

```{code-cell} ipython3
df.pivot(index='Pclass', columns='Sex', values='Fare')
```

```{code-cell} ipython3
df.pivot(index='Pclass', columns='Sex', values='Survived')
```

So far, so good...

+++

Let's now use the full titanic dataset:

```{code-cell} ipython3
df = pd.read_csv("../data/titanic.csv")
```

```{code-cell} ipython3
df.head()
```

And try the same pivot (*no worries about the try-except, this is here just used to catch a loooong error*):

```{code-cell} ipython3
try:
    df.pivot(index='Sex', columns='Pclass', values='Fare')
except Exception as e:
    print("Exception!", e)
```

This does not work, because we would end up with multiple values for one cell of the resulting frame, as the error says: `duplicated` values for the columns in the selection. As an example, consider the following rows of our three columns of interest:

```{code-cell} ipython3
df.loc[[1, 3], ["Sex", 'Pclass', 'Fare']]
```

Since `pivot` is just restructering data, where would both values of `Fare` for the same combination of `Sex` and `Pclass` need to go?

Well, they need to be combined, according to an `aggregation` functionality, which is supported by the function`pivot_table`

+++

<div class="alert alert-danger">

<b>NOTE</b>:

 <ul>
  <li><b>Pivot</b> is purely restructering: a single value for each index/column combination is required.</li>
</ul>

</div>

+++

# Pivot tables - aggregating while pivoting

```{code-cell} ipython3
df = pd.read_csv("../data/titanic.csv")
```

```{code-cell} ipython3
df.pivot_table(index='Sex', columns='Pclass', values='Fare')
```

<div class="alert alert-info">

<b>REMEMBER</b>:

* By default, `pivot_table` takes the **mean** of all values that would end up into one cell. However, you can also specify other aggregation functions using the `aggfunc` keyword.

</div>

```{code-cell} ipython3
df.pivot_table(index='Sex', columns='Pclass', 
               values='Fare', aggfunc='max')
```

```{code-cell} ipython3
df.pivot_table(index='Sex', columns='Pclass', 
               values='Fare', aggfunc='count')
```

<div class="alert alert-info">

<b>REMEMBER</b>:

 <ul>
  <li>There is a shortcut function for a <code>pivot_table</code> with a <code>aggfunc='count'</code> as aggregation: <code>crosstab</code></li>
</ul>
</div>

```{code-cell} ipython3
pd.crosstab(index=df['Sex'], columns=df['Pclass'])
```

+++ {"clear_cell": false}

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>Make a pivot table with the survival rates for Pclass vs Sex.</li>
</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

df.pivot_table(index='Pclass', columns='Sex', 
               values='Survived', aggfunc='mean')
```

```{code-cell} ipython3
:clear_cell: true

fig, ax1 = plt.subplots()
df.pivot_table(index='Pclass', columns='Sex', 
               values='Survived', aggfunc='mean').plot(kind='bar', 
                                                       rot=0, 
                                                       ax=ax1)
ax1.set_ylabel('Survival ratio')
```

+++ {"clear_cell": false}

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>Make a table of the median Fare payed by aged/underaged vs Sex.</li>
</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

df['Underaged'] = df['Age'] <= 18
```

```{code-cell} ipython3
:clear_cell: true

df.pivot_table(index='Underaged', columns='Sex', 
               values='Fare', aggfunc='median')
```

# Melt - from pivot table to long or tidy format

+++

The `melt` function performs the inverse operation of a `pivot`. This can be used to make your frame longer, i.e. to make a *tidy* version of your data.

```{code-cell} ipython3
pivoted = df.pivot_table(index='Sex', columns='Pclass', values='Fare').reset_index()
pivoted.columns.name = None
```

```{code-cell} ipython3
pivoted
```

Assume we have a DataFrame like the above. The observations (the average Fare people payed) are spread over different columns. In a tidy dataset, each observation is stored in one row. To obtain this, we can use the `melt` function:

```{code-cell} ipython3
pd.melt(pivoted)
```

As you can see above, the `melt` function puts all column labels in one column, and all values in a second column.

In this case, this is not fully what we want. We would like to keep the 'Sex' column separately:

```{code-cell} ipython3
pd.melt(pivoted, id_vars=['Sex']) #, var_name='Pclass', value_name='Fare')
```

# Reshaping with `stack` and `unstack`

+++

The docs say:

> Pivot a level of the (possibly hierarchical) column labels, returning a
DataFrame (or Series in the case of an object with a single level of
column labels) having a hierarchical index with a new inner-most level
of row labels.

Indeed... 
<img src="../img/schema-stack.svg" width=50%>

Before we speak about `hierarchical index`, first check it in practice on the following dummy example:

```{code-cell} ipython3
df = pd.DataFrame({'A':['one', 'one', 'two', 'two'], 
                   'B':['a', 'b', 'a', 'b'], 
                   'C':range(4)})
df
```

To use `stack`/`unstack`, we need the values we want to shift from rows to columns or the other way around as the index:

```{code-cell} ipython3
df = df.set_index(['A', 'B']) # Indeed, you can combine two indices
df
```

```{code-cell} ipython3
result = df['C'].unstack()
result
```

```{code-cell} ipython3
df = result.stack().reset_index(name='C')
df
```

<div class="alert alert-info">

<b>REMEMBER</b>:

 <ul>
  <li><b>stack</b>: make your data <i>longer</i> and <i>smaller</i> </li>
  <li><b>unstack</b>: make your data <i>shorter</i> and <i>wider</i> </li>
</ul>
</div>

+++

## Mimick pivot table 

+++

To better understand and reason about pivot tables, we can express this method as a combination of more basic steps. In short, the pivot is a convenient way of expressing the combination of a `groupby` and `stack/unstack`.

```{code-cell} ipython3
df = pd.read_csv("../data/titanic.csv")
```

```{code-cell} ipython3
df.head()
```

```{code-cell} ipython3
df.pivot_table(index='Pclass', columns='Sex', 
               values='Survived', aggfunc='mean')
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>Get the same result as above based on a combination of `groupby` and `unstack`</li>
  <li>First use `groupby` to calculate the survival ratio for all groups`unstack`</li>
  <li>Then, use `unstack` to reshape the output of the groupby operation</li>
</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

df.groupby(['Pclass', 'Sex'])['Survived'].mean().unstack()
```

# [OPTIONAL] Exercises: use the reshaping methods with the movie data

+++

These exercises are based on the [PyCon tutorial of Brandon Rhodes](https://github.com/brandon-rhodes/pycon-pandas-tutorial/) (so credit to him!) and the datasets he prepared for that. You can download these data from here: [`titles.csv`](https://drive.google.com/open?id=0B3G70MlBnCgKajNMa1pfSzN6Q3M) and [`cast.csv`](https://drive.google.com/open?id=0B3G70MlBnCgKal9UYTJSR2ZhSW8) and put them in the `/data` folder.

```{code-cell} ipython3
cast = pd.read_csv('../data/cast.csv')
cast.head()
```

```{code-cell} ipython3
titles = pd.read_csv('../data/titles.csv')
titles.head()
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>Plot the number of actor roles each year and the number of actress roles each year over the whole period of available movie data.</li>
</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

grouped = cast.groupby(['year', 'type']).size()
table = grouped.unstack('type')
table.plot()
```

```{code-cell} ipython3
:clear_cell: true

cast.pivot_table(index='year', columns='type', values="character", aggfunc='count').plot() 
# for values in using the , take a column with no Nan values in order to count effectively all values -> at this stage: aha-erlebnis about crosstab function(!)
```

```{code-cell} ipython3
:clear_cell: true

pd.crosstab(index=cast['year'], columns=cast['type']).plot()
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>Plot the number of actor roles each year and the number of actress roles each year. Use kind='area' as plot type</li>
</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

pd.crosstab(index=cast['year'], columns=cast['type']).plot(kind='area')
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>Plot the fraction of roles that have been 'actor' roles each year over the whole period of available movie data.</li>
</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

grouped = cast.groupby(['year', 'type']).size()
table = grouped.unstack('type')
(table['actor'] / (table['actor'] + table['actress'])).plot(ylim=[0,1])
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>Define a year as a "Superman year" when films of that year feature more Superman characters than Batman characters. How many years in film history have been Superman years?</li>
</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

c = cast
c = c[(c.character == 'Superman') | (c.character == 'Batman')]
c = c.groupby(['year', 'character']).size()
c = c.unstack()
c = c.fillna(0)
c.head()
```

```{code-cell} ipython3
:clear_cell: true

d = c.Superman - c.Batman
print('Superman years:')
print(len(d[d > 0.0]))
```
