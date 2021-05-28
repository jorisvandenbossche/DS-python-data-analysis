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

<p><font size="6"><b>06 - Pandas: "Group by" operations</b></font></p>

> *DS Data manipulation, analysis and visualisation in Python*  
> *December, 2019*

> *© 2016-2019, Joris Van den Bossche and Stijn Van Hoey  (<mailto:jorisvandenbossche@gmail.com>, <mailto:stijnvanhoey@gmail.com>). Licensed under [CC BY 4.0 Creative Commons](http://creativecommons.org/licenses/by/4.0/)*

---

```{code-cell} ipython3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
```

# Some 'theory': the groupby operation (split-apply-combine)

```{code-cell} ipython3
df = pd.DataFrame({'key':['A','B','C','A','B','C','A','B','C'],
                   'data': [0, 5, 10, 5, 10, 15, 10, 15, 20]})
df
```

### Recap: aggregating functions

+++

When analyzing data, you often calculate summary statistics (aggregations like the mean, max, ...). As we have seen before, we can easily calculate such a statistic for a Series or column using one of the many available methods. For example:

```{code-cell} ipython3
df['data'].sum()
```

However, in many cases your data has certain groups in it, and in that case, you may want to calculate this statistic for each of the groups.

For example, in the above dataframe `df`, there is a column 'key' which has three possible values: 'A', 'B' and 'C'. When we want to calculate the sum for each of those groups, we could do the following:

```{code-cell} ipython3
for key in ['A', 'B', 'C']:
    print(key, df[df['key'] == key]['data'].sum())
```

This becomes very verbose when having multiple groups. You could make the above a bit easier by looping over the different values, but still, it is not very convenient to work with.

What we did above, applying a function on different groups, is a "groupby operation", and pandas provides some convenient functionality for this.

+++

### Groupby: applying functions per group

+++

The "group by" concept: we want to **apply the same function on subsets of your dataframe, based on some key to split the dataframe in subsets**

This operation is also referred to as the "split-apply-combine" operation, involving the following steps:

* **Splitting** the data into groups based on some criteria
* **Applying** a function to each group independently
* **Combining** the results into a data structure

<img src="../img/splitApplyCombine.png">

Similar to SQL `GROUP BY`

+++

Instead of doing the manual filtering as above


    df[df['key'] == "A"].sum()
    df[df['key'] == "B"].sum()
    ...

pandas provides the `groupby` method to do exactly this:

```{code-cell} ipython3
df.groupby('key').sum()
```

```{code-cell} ipython3
df.groupby('key').aggregate(np.sum)  # 'sum'
```

And many more methods are available. 

```{code-cell} ipython3
df.groupby('key')['data'].sum()
```

# Application of the groupby concept on the titanic data

+++

We go back to the titanic passengers survival data:

```{code-cell} ipython3
df = pd.read_csv("../data/titanic.csv")
```

```{code-cell} ipython3
df.head()
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>Using groupby(), calculate the average age for each sex.</li>
</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

df.groupby('Sex')['Age'].mean()
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>Calculate the average survival ratio for all passengers.</li>
</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

# df['Survived'].sum() / len(df['Survived'])
df['Survived'].mean()
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>Calculate this survival ratio for all passengers younger than 25 (remember: filtering/boolean indexing).</li>
</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

df25 = df[df['Age'] < 25]
df25['Survived'].sum() / len(df25['Survived'])
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>What is the difference in the survival ratio between the sexes?</li>
</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

df.groupby('Sex')['Survived'].mean()
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>Make a bar plot of the survival ratio for the different classes ('Pclass' column).</li>
</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

df.groupby('Pclass')['Survived'].mean().plot(kind='bar') #and what if you would compare the total number of survivors?
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>Make a bar plot to visualize the average Fare payed by people depending on their age. The age column is divided in separate classes using the `pd.cut` function as provided below.</li>
</ul>
</div>

```{code-cell} ipython3
:clear_cell: false

df['AgeClass'] = pd.cut(df['Age'], bins=np.arange(0,90,10))
```

```{code-cell} ipython3
:clear_cell: true

df.groupby('AgeClass')['Fare'].mean().plot(kind='bar', rot=0)
```

If you are ready, more groupby exercises can be found below.

+++

# Some more theory

+++

## Specifying the grouper

+++

In the previous example and exercises, we always grouped by a single column by passing its name. But, a column name is not the only value you can pass as the grouper in `df.groupby(grouper)`. Other possibilities for `grouper` are:

- a list of strings (to group by multiple columns)
- a Series (similar to a string indicating a column in df) or array
- function (to be applied on the index)
- levels=[], names of levels in a MultiIndex

```{code-cell} ipython3
df.groupby(df['Age'] < 18)['Survived'].mean()
```

```{code-cell} ipython3
df.groupby(['Pclass', 'Sex'])['Survived'].mean()
```

## The size of groups - value counts

+++

Often you want to know how many elements there are in a certain group (or in other words: the number of occurences of the different values from a column).

To get the size of the groups, we can use `size`:

```{code-cell} ipython3
df.groupby('Pclass').size()
```

```{code-cell} ipython3
df.groupby('Embarked').size()
```

Another way to obtain such counts, is to use the Series `value_counts` method:

```{code-cell} ipython3
df['Embarked'].value_counts()
```

# [OPTIONAL] Additional exercises using the movie data

+++

These exercises are based on the [PyCon tutorial of Brandon Rhodes](https://github.com/brandon-rhodes/pycon-pandas-tutorial/) (so credit to him!) and the datasets he prepared for that. You can download these data from here: [`titles.csv`](https://drive.google.com/open?id=0B3G70MlBnCgKajNMa1pfSzN6Q3M) and [`cast.csv`](https://drive.google.com/open?id=0B3G70MlBnCgKal9UYTJSR2ZhSW8) and put them in the `/data` folder.

+++

`cast` dataset: different roles played by actors/actresses in films

- title: title of the movie
- year: year it was released
- name: name of the actor/actress
- type: actor/actress
- n: the order of the role (n=1: leading role)

```{code-cell} ipython3
cast = pd.read_csv('data/cast.csv')
cast.head()
```

`titles` dataset:

* title: title of the movie
* year: year of release

```{code-cell} ipython3
titles = pd.read_csv('data/titles.csv')
titles.head()
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>Using `groupby()`, plot the number of films that have been released each decade in the history of cinema.</li>
</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

titles['decade'] = titles['year'] // 10 * 10
```

```{code-cell} ipython3
:clear_cell: true

titles.groupby('decade').size().plot(kind='bar', color='green')
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>Use `groupby()` to plot the number of 'Hamlet' movies made each decade.</li>
</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

titles['decade'] = titles['year'] // 10 * 10
hamlet = titles[titles['title'] == 'Hamlet']
hamlet.groupby('decade').size().plot(kind='bar', color="orange")
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>For each decade, plot all movies of which the title contains "Hamlet".</li>
</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

titles['decade'] = titles['year'] // 10 * 10
hamlet = titles[titles['title'].str.contains('Hamlet')]
hamlet.groupby('decade').size().plot(kind='bar', color="lightblue")
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>List the 10 actors/actresses that have the most leading roles (n=1) since the 1990's.</li>
</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

cast1990 = cast[cast['year'] >= 1990]
cast1990 = cast1990[cast1990['n'] == 1]
cast1990.groupby('name').size().nlargest(10)
```

```{code-cell} ipython3
:clear_cell: true

cast1990['name'].value_counts().head(10)
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>In a previous exercise, the number of 'Hamlet' films released each decade was checked. Not all titles are exactly called 'Hamlet'. Give an overview of the titles that contain 'Hamlet' and an overview of the titles that start with 'Hamlet',  each time providing the amount of occurrences in the data set for each of the movies</li>
</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

hamlets = titles[titles['title'].str.contains('Hamlet')]
hamlets['title'].value_counts()
```

```{code-cell} ipython3
:clear_cell: true

hamlets = titles[titles['title'].str.startswith('Hamlet')]
hamlets['title'].value_counts()
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>List the 10 movie titles with the longest name.</li>
</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

title_longest = titles['title'].str.len().nlargest(10)
title_longest
```

```{code-cell} ipython3
:clear_cell: true

pd.options.display.max_colwidth = 210
titles.loc[title_longest.index]
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>How many leading (n=1) roles were available to actors, and how many to actresses, in each year of the 1950s?</li>
</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

cast1950 = cast[cast['year'] // 10 == 195]
cast1950 = cast1950[cast1950['n'] == 1]
cast1950.groupby(['year', 'type']).size()
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>What are the 11 most common character names in movie history?</li>
</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

cast.character.value_counts().head(11)
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>Plot how many roles Brad Pitt has played in each year of his career.</li>
</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

cast[cast.name == 'Brad Pitt'].year.value_counts().sort_index().plot()
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>What are the 10 most occurring movie titles that start with the words 'The Life'?</li>
</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

titles[titles['title'].str.startswith('The Life')]['title'].value_counts().head(10)
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>Which actors or actresses were most active in the year 2010 (i.e. appeared in the most movies)?</li>
</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

cast[cast.year == 2010].name.value_counts().head(10)
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>Determine how many roles are listed for each of 'The Pink Panther' movies.</li>
</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

pink = cast[cast['title'] == 'The Pink Panther']
pink.groupby(['year'])[['n']].max()
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li> List, in order by year, each of the movies in which 'Frank Oz' has played more than 1 role.</li>
</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

oz = cast[cast['name'] == 'Frank Oz']
oz_roles = oz.groupby(['year', 'title']).size()
oz_roles[oz_roles > 1]
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li> List each of the characters that Frank Oz has portrayed at least twice.</li>
</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

oz = cast[cast['name'] == 'Frank Oz']
oz_roles = oz.groupby(['character']).size()
oz_roles[oz_roles > 1].sort_values()
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li> Add a new column to the `cast` DataFrame that indicates the number of roles for each movie. [Hint](http://pandas.pydata.org/pandas-docs/stable/groupby.html#transformation)</li>
</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

cast['n_total'] = cast.groupby(['title', 'year'])['n'].transform('max') # transform will return an element for each row, so the max value is given to the whole group
cast.head()
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li> Calculate the ratio of leading actor and actress roles to the total number of leading roles per decade. </li>
</ul><br>

**Tip**: you can do a groupby twice in two steps, first calculating the numbers, and secondly, the ratios.
</div>

```{code-cell} ipython3
:clear_cell: true

leading = cast[cast['n'] == 1]
sums_decade = leading.groupby([cast['year'] // 10 * 10, 'type']).size()
sums_decade
```

```{code-cell} ipython3
:clear_cell: true

#sums_decade.groupby(level='year').transform(lambda x: x / x.sum())
ratios_decade = sums_decade / sums_decade.groupby(level='year').transform('sum')
ratios_decade
```

```{code-cell} ipython3
:clear_cell: true

ratios_decade[:, 'actor'].plot()
ratios_decade[:, 'actress'].plot()
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li> In which years the most films were released?</li>
</ul><br>
</div>

```{code-cell} ipython3
:clear_cell: true

t = titles
t.year.value_counts().head(3)
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>How many leading (n=1) roles were available to actors, and how many to actresses, in the 1950s? And in 2000s?</li>
</ul><br>
</div>

```{code-cell} ipython3
:clear_cell: true

cast1950 = cast[cast['year'] // 10 == 195]
cast1950 = cast1950[cast1950['n'] == 1]
cast1950['type'].value_counts()
```

```{code-cell} ipython3
:clear_cell: true

cast2000 = cast[cast['year'] // 10 == 200]
cast2000 = cast2000[cast2000['n'] == 1]
cast2000['type'].value_counts()
```

```{code-cell} ipython3

```
