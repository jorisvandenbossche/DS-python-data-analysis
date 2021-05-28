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

<p><font size="6"><b>04 - Pandas: Working with time series data</b></font></p>

> *DS Data manipulation, analysis and visualisation in Python*  
> *December, 2019*

> *© 2016-2019, Joris Van den Bossche and Stijn Van Hoey  (<mailto:jorisvandenbossche@gmail.com>, <mailto:stijnvanhoey@gmail.com>). Licensed under [CC BY 4.0 Creative Commons](http://creativecommons.org/licenses/by/4.0/)*

---

```{code-cell} ipython3
# %matplotlib notebook
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')
```

# Introduction: `datetime` module

+++

Standard Python contains the `datetime` module to handle date and time data:

```{code-cell} ipython3
import datetime
```

```{code-cell} ipython3
dt = datetime.datetime(year=2016, month=12, day=19, hour=13, minute=30)
dt
```

```{code-cell} ipython3
print(dt) # .day,...
```

```{code-cell} ipython3
print(dt.strftime("%d %B %Y"))
```

# Dates and times in pandas

+++

## The ``Timestamp`` object

+++

Pandas has its own date and time objects, which are compatible with the standard `datetime` objects, but provide some more functionality to work with.  

The `Timestamp` object can also be constructed from a string:

```{code-cell} ipython3
ts = pd.Timestamp('2016-12-19')
ts
```

Like with `datetime.datetime` objects, there are several useful attributes available on the `Timestamp`. For example, we can get the month (experiment with tab completion!):

```{code-cell} ipython3
ts.month
```

There is also a `Timedelta` type, which can e.g. be used to add intervals of time:

```{code-cell} ipython3
ts + pd.Timedelta('5 days')
```

## Parsing datetime strings 

+++

![](http://imgs.xkcd.com/comics/iso_8601.png)

+++

Unfortunately, when working with real world data, you encounter many different `datetime` formats. Most of the time when you have to deal with them, they come in text format, e.g. from a `CSV` file. To work with those data in Pandas, we first have to *parse* the strings to actual `Timestamp` objects.

+++

<div class="alert alert-info">
<b>REMEMBER</b>: <br><br>

To convert string formatted dates to Timestamp objects: use the `pandas.to_datetime` function

</div>

```{code-cell} ipython3
pd.to_datetime("2016-12-09")
```

```{code-cell} ipython3
pd.to_datetime("09/12/2016")
```

```{code-cell} ipython3
pd.to_datetime("09/12/2016", dayfirst=True)
```

```{code-cell} ipython3
pd.to_datetime("09/12/2016", format="%d/%m/%Y")
```

A detailed overview of how to specify the `format` string, see the table in the python documentation: https://docs.python.org/3.5/library/datetime.html#strftime-and-strptime-behavior

+++

## `Timestamp` data in a Series or DataFrame column

```{code-cell} ipython3
s = pd.Series(['2016-12-09 10:00:00', '2016-12-09 11:00:00', '2016-12-09 12:00:00'])
```

```{code-cell} ipython3
s
```

The `to_datetime` function can also be used to convert a full series of strings:

```{code-cell} ipython3
ts = pd.to_datetime(s)
```

```{code-cell} ipython3
ts
```

Notice the data type of this series has changed: the `datetime64[ns]` dtype. This indicates that we have a series of actual datetime values.

+++

The same attributes as on single `Timestamp`s are also available on a Series with datetime data, using the **`.dt`** accessor:

```{code-cell} ipython3
ts.dt.hour
```

```{code-cell} ipython3
ts.dt.weekday
```

To quickly construct some regular time series data, the [``pd.date_range``](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.date_range.html) function comes in handy:

```{code-cell} ipython3
pd.Series(pd.date_range(start="2016-01-01", periods=10, freq='3H'))
```

# Time series data: `Timestamp` in the index

+++

## River discharge example data

+++

For the following demonstration of the time series functionality, we use a sample of discharge data of the Maarkebeek (Flanders) with 3 hour averaged values, derived from the [Waterinfo website](https://www.waterinfo.be/).

```{code-cell} ipython3
data = pd.read_csv("../data/vmm_flowdata.csv")
```

```{code-cell} ipython3
data.head()
```

We already know how to parse a date column with Pandas:

```{code-cell} ipython3
data['Time'] = pd.to_datetime(data['Time'])
```

With `set_index('datetime')`, we set the column with datetime values as the index, which can be done by both `Series` and `DataFrame`.

```{code-cell} ipython3
data = data.set_index("Time")
```

```{code-cell} ipython3
data
```

The steps above are provided as built-in functionality of `read_csv`:

```{code-cell} ipython3
data = pd.read_csv("../data/vmm_flowdata.csv", index_col=0, parse_dates=True)
```

<div class="alert alert-info">
<b>REMEMBER</b>: <br><br>

`pd.read_csv` provides a lot of built-in functionality to support this kind of transactions when reading in a file! Check the help of the read_csv function...

</div>

+++

## The DatetimeIndex

+++

When we ensure the DataFrame has a `DatetimeIndex`, time-series related functionality becomes available:

```{code-cell} ipython3
data.index
```

Similar to a Series with datetime data, there are some attributes of the timestamp values available:

```{code-cell} ipython3
data.index.day
```

```{code-cell} ipython3
data.index.dayofyear
```

```{code-cell} ipython3
data.index.year
```

The `plot` method will also adapt its labels (when you zoom in, you can see the different levels of detail of the datetime labels):

```{code-cell} ipython3
# %matplotlib notebook
```

```{code-cell} ipython3
data.plot()
```

We have too much data to sensibly plot on one figure. Let's see how we can easily select part of the data or aggregate the data to other time resolutions in the next sections.

+++

## Selecting data from a time series

+++

We can use label based indexing on a timeseries as expected:

```{code-cell} ipython3
data[pd.Timestamp("2012-01-01 09:00"):pd.Timestamp("2012-01-01 19:00")]
```

But, for convenience, indexing a time series also works with strings:

```{code-cell} ipython3
data["2012-01-01 09:00":"2012-01-01 19:00"]
```

A nice feature is **"partial string" indexing**, where we can do implicit slicing by providing a partial datetime string.

E.g. all data of 2013:

```{code-cell} ipython3
data['2013']
```

Normally you would expect this to access a column named '2013', but as for a DatetimeIndex, pandas also tries to interprete it as a datetime slice.

+++

Or all data of January up to March 2012:

```{code-cell} ipython3
data['2012-01':'2012-03']
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>select all data starting from 2012</li>
</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

data['2012':]
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>select all data in January for all different years</li>
</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

data[data.index.month == 1]
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>select all data in April, May and June for all different years</li>
</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

data[data.index.month.isin([4, 5, 6])]
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>select all 'daytime' data (between 8h and 20h) for all days</li>
</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

data[(data.index.hour > 8) & (data.index.hour < 20)]
```

## The power of pandas: `resample`

+++

A very powerfull method is **`resample`: converting the frequency of the time series** (e.g. from hourly to daily data).

The time series has a frequency of 1 hour. I want to change this to daily:

```{code-cell} ipython3
data.resample('D').mean().head()
```

Other mathematical methods can also be specified:

```{code-cell} ipython3
data.resample('D').max().head()
```

<div class="alert alert-info">
<b>REMEMBER</b>: <br><br>

The string to specify the new time frequency: http://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offset-aliases <br><br>

These strings can also be combined with numbers, eg `'10D'`...

</div>


```{code-cell} ipython3
data.resample('M').mean().plot() # 10D
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>plot the monthly standard deviation of the columns</li>
</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

data.resample('M').std().plot() # 'A'
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>plot the monthly mean and median values for the years 2011-2012 for 'L06_347'<br><br></li>
</ul>
    
**Note** remember the `agg` when using `groupby` to derive multiple statistics at the same time?
    
</div>

```{code-cell} ipython3
:clear_cell: true

subset = data['2011':'2012']['L06_347']
subset.resample('M').agg(['mean', 'median']).plot()
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>plot the monthly mininum and maximum daily average value of the 'LS06_348' column</li>
</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

daily = data['LS06_348'].resample('D').mean() # daily averages calculated
```

```{code-cell} ipython3
:clear_cell: true

daily.resample('M').agg(['min', 'max']).plot() # monthly minimum and maximum values of these daily averages
```

<div class="alert alert-success">
<b>EXERCISE</b>:

 <ul>
  <li>Make a bar plot of the mean of the stations in year of 2013</li>
</ul>

</div>

```{code-cell} ipython3
:clear_cell: true

data['2013'].mean().plot(kind='barh')
```
