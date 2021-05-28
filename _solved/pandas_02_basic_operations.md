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

<p><font size="6"><b> 02 - Pandas: Basic operations on Series and DataFrames</b></font></p>


> *DS Data manipulation, analysis and visualisation in Python*  
> *December, 2019*

> *© 2016-2019, Joris Van den Bossche and Stijn Van Hoey  (<mailto:jorisvandenbossche@gmail.com>, <mailto:stijnvanhoey@gmail.com>). Licensed under [CC BY 4.0 Creative Commons](http://creativecommons.org/licenses/by/4.0/)*

---

```{code-cell} ipython3
import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
```

As you play around with DataFrames, you'll notice that many operations which work on NumPy arrays will also work on dataframes.

```{code-cell} ipython3
# redefining the example objects

population = pd.Series({'Germany': 81.3, 'Belgium': 11.3, 'France': 64.3, 
                        'United Kingdom': 64.9, 'Netherlands': 16.9})

countries = pd.DataFrame({'country': ['Belgium', 'France', 'Germany', 'Netherlands', 'United Kingdom'],
        'population': [11.3, 64.3, 81.3, 16.9, 64.9],
        'area': [30510, 671308, 357050, 41526, 244820],
        'capital': ['Brussels', 'Paris', 'Berlin', 'Amsterdam', 'London']})
```

```{code-cell} ipython3
countries.head()
```

# The 'new' concepts

+++

## Elementwise-operations 

+++

Just like with numpy arrays, many operations are element-wise:

```{code-cell} ipython3
population / 100
```

```{code-cell} ipython3
countries['population'] / countries['area']
```

```{code-cell} ipython3
np.log(countries['population'])
```

which can be added as a new column, as follows:

```{code-cell} ipython3
countries["log_population"] = np.log(countries['population'])
```

```{code-cell} ipython3
countries.columns
```

```{code-cell} ipython3
countries['population'] > 40
```

<div class="alert alert-info">

<b>REMEMBER</b>:

* When you have an operation which does NOT work element-wise or you have no idea how to do it directly in Pandas, use the **apply()** function
* A typical use case is with a custom written or a **lambda** function

</div>

```{code-cell} ipython3
countries["capital"].apply(lambda x: len(x)) # in case you forgot the functionality: countries["capital"].str.len()
```

```{code-cell} ipython3
def population_annotater(population):
    """annotate as large or small"""
    if population > 50:
        return 'large'
    else:
        return 'small'
```

```{code-cell} ipython3
countries["population"].apply(population_annotater) # a custom user function
```

## Aggregations (reductions)

+++

Pandas provides a large set of **summary** functions that operate on different kinds of pandas objects (DataFrames, Series, Index) and produce single value. When applied to a DataFrame, the result is returned as a pandas Series (one value for each column). 

+++

The average population number:

```{code-cell} ipython3
population.mean()
```

The minimum area:

```{code-cell} ipython3
countries['area'].min()
```

For dataframes, often only the numeric columns are included in the result:

```{code-cell} ipython3
countries.median()
```

# Application on a real dataset

+++

Reading in the titanic data set...

```{code-cell} ipython3
df = pd.read_csv("../data/titanic.csv")
```

Quick exploration first...

```{code-cell} ipython3
df.head()
```

```{code-cell} ipython3
len(df)
```

The available metadata of the titanic data set provides the following information:

VARIABLE   |  DESCRIPTION
------ | --------
Survived       | Survival (0 = No; 1 = Yes)
Pclass         | Passenger Class (1 = 1st; 2 = 2nd; 3 = 3rd)
Name           | Name
Sex            | Sex
Age            | Age
SibSp          | Number of Siblings/Spouses Aboard
Parch          | Number of Parents/Children Aboard
Ticket         | Ticket Number
Fare           | Passenger Fare
Cabin          | Cabin
Embarked       | Port of Embarkation (C = Cherbourg; Q = Queenstown; S = Southampton)

+++

<div class="alert alert-success">
<b>EXERCISE</b>:

 <ul>
  <li>What is the average age of the passengers?</li>
</ul>

</div>

```{code-cell} ipython3
:clear_cell: true

df['Age'].mean()
```

<div class="alert alert-success">
<b>EXERCISE</b>:

 <ul>
  <li>Plot the age distribution of the titanic passengers</li>
</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

df['Age'].hist() #bins=30, log=True
```

<div class="alert alert-success">
<b>EXERCISE</b>:

 <ul>
  <li>What is the survival rate? (the relative number of people that survived)</li>
</ul>
<br>

Note: the 'Survived' column indicates whether someone survived (1) or not (0).
</div>

```{code-cell} ipython3
:clear_cell: true

df['Survived'].sum() / len(df['Survived'])
```

```{code-cell} ipython3
:clear_cell: true

df['Survived'].mean()
```

<div class="alert alert-success">
<b>EXERCISE</b>:

 <ul>
  <li>What is the maximum Fare? And the median?</li>
</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

df['Fare'].max()
```

```{code-cell} ipython3
:clear_cell: true

df['Fare'].median()
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>Calculate the 75th percentile (`quantile`) of the Fare price (Tip: look in the docstring how to specify the percentile)</li>
</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

df['Fare'].quantile(0.75)
```

<div class="alert alert-success">
<b>EXERCISE</b>:

 <ul>
  <li>Calculate the normalized Fares (normalized relative to its mean)</li>
</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

df['Fare'] / df['Fare'].mean()
```

<div class="alert alert-success">
<b>EXERCISE</b>:

 <ul>
  <li>Calculate the log of the Fares, and add this as a new column ('Fare_log') to the DataFrame.</li>
</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

np.log(df['Fare'])
```

```{code-cell} ipython3
:clear_cell: true

df['Fare_log'] = np.log(df['Fare'])
df.head()
```

# Acknowledgement


> This notebook is partly based on material of Jake Vanderplas (https://github.com/jakevdp/OsloWorkshop2014).

---
