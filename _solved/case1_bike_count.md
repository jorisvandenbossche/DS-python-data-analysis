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

<p><font size="6"><b> CASE - Bike count data</b></font></p>


> *DS Data manipulation, analysis and visualization in Python*  
> *May/June, 2021*
>
> *© 2021, Joris Van den Bossche and Stijn Van Hoey  (<mailto:jorisvandenbossche@gmail.com>, <mailto:stijnvanhoey@gmail.com>). Licensed under [CC BY 4.0 Creative Commons](http://creativecommons.org/licenses/by/4.0/)*

---

+++

<img src="https://static.nieuwsblad.be/Assets/Images_Upload/2014/04/17/57b8f34e-5042-11e2-80ee-5d1d7b74455f_original.jpg.h380.jpg.568.jpg?maxheight=460&maxwidth=638&scale=both">

+++

In this case study, we will make use of the openly available bike count data of the city of Ghent (Belgium). At the Coupure Links, next to the Faculty of Bioscience Engineering, a counter keeps track of the number of passing cyclists in both directions.  

```{code-cell} ipython3
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
```

# Reading and processing the data

+++

## Read csv data

+++

The data were previously available on the open data portal of the city, and we downloaded them in the `CSV` format, and provided the original file as `data/fietstellingencoupure.csv`. 

This data set contains the historical data of the bike counters, and consists of the following columns:

- The first column `datum` is the date, in `dd/mm/yy` format
- The second column `tijd` is the time of the day, in `hh:mm` format
- The third and fourth column `ri Centrum` and `ri Mariakerke` are the counts at that point in time (counts between this timestamp and the previous)

+++

<div class="alert alert-success">

**EXERCISE**

- Read the csv file from the url into a DataFrame `df`, the delimiter of the data is `;`
- Inspect the first and last 5 rows, and check the number of observations
- Inspect the data types of the different columns

<details><summary>Hints</summary>

- With the cursor on a function, you can combine the SHIFT + TAB keystrokes to see the documentation of a function.
- Both the `sep` and `delimiter` argument will work to define the delimiter.
- Methods like `head`/`tail` have round brackets `()`, attributes like `dtypes` not.

</details>    
    
</div>

```{code-cell} ipython3
:clear_cell: true

df = pd.read_csv("data/fietstellingencoupure.csv", sep=';')
```

```{code-cell} ipython3
:clear_cell: true

df.head()
```

```{code-cell} ipython3
:clear_cell: true

df.tail()
```

```{code-cell} ipython3
:clear_cell: true

len(df)
```

```{code-cell} ipython3
:clear_cell: true

df.dtypes
```

## Data processing

+++

As explained above, the first and second column (respectively `datum` and `tijd`) indicate the date and hour of the day. To obtain a time series, we have to combine those two columns into one series of actual `datetime` values. 

+++

<div class="alert alert-success">

**EXERCISE**

Pre-process the data:

* Combine the 'datum' and 'tijd' columns into one Pandas Series of string `datetime` values, call this new variable `combined`.
* Parse the string `datetime` values to `datetime` objects.
* Set the resulting `datetime` column as the index of the `df` DataFrame.
* Remove the original 'datum' and 'tijd' columns using the `drop` method, and call the new dataframe `df2`.
* Rename the columns in the DataFrame 'ri Centrum', 'ri Mariakerke' to resp. 'direction_centre', 'direction_mariakerke' using the `rename` method.

<details><summary>Hints</summary>

- Concatenating strings can be done with the addition operation `+`.
- When converting strings to a `datetime` with `pd.to_datetime`, specifying the format will make the conversion a lot faster.
- `drop` can remove both rows and columns using the names of the index or column name. Make sure to define `columns=` argument to remove columns.
- `rename` can be used for both rows/columns. It needs a dictionary with the current names as keys and the new names as values. 

</details>    

```{code-cell} ipython3
:clear_cell: true

combined = df['datum'] + ' ' + df['tijd']
combined.head()
```

```{code-cell} ipython3
:clear_cell: true

df.index = pd.to_datetime(combined, format="%d/%m/%Y %H:%M")
```

```{code-cell} ipython3
:clear_cell: true

df2 = df.drop(columns=['datum', 'tijd'])
```

```{code-cell} ipython3
:clear_cell: true

df2 = df2.rename(columns={'ri Centrum': 'direction_centre', 
                          'ri Mariakerke':'direction_mariakerke'})
```

```{code-cell} ipython3
df2.head()
```

Having the data available with an interpreted `datetime`, provides us the possibility of having time aware plotting:

```{code-cell} ipython3
fig, ax = plt.subplots(figsize=(10, 6))
df.plot(colormap='coolwarm', ax=ax)
```

<div class="alert alert-warning">

 <b>Remark</b>: Interpretation of the dates with and without predefined date format.

</div>

+++

When we just want to interpret the dates, without specifying how the dates are formatted, Pandas makes an attempt as good as possible:

```{code-cell} ipython3
combined = df['datum'] + ' ' + df['tijd']
```

```{code-cell} ipython3
%timeit -n 1 -r 1 pd.to_datetime(combined, dayfirst=True)
```

However, when we already know the format of the dates (and if this is consistent throughout the full data set), we can use this information to interpret the dates:

```{code-cell} ipython3
%timeit pd.to_datetime(combined, format="%d/%m/%Y %H:%M")
```

<div class="alert alert-info">

 <b>Remember</b>: Whenever possible, specify the date format to interpret the dates to `datetime` values!

</div>

+++

### Write the data set cleaning as a function

In order to make it easier to reuse the code for the pre-processing we have implemented, let's convert the code to a Python function:

+++

<div class="alert alert-success">

**EXERCISE**

Write a function `process_bike_count_data(df)` that performs the processing steps as done above for an input Pandas DataFrame and returns the updated DataFrame.

<details><summary>Hints</summary>

- Want to know more about proper documenting your Python functions? Check out the official guide of [numpydoc](https://numpydoc.readthedocs.io/en/latest/format.html). The `Parameters` and `Returns` sections should always be explained.

</details>

```{code-cell} ipython3
:clear_cell: true

def process_bike_count_data(df):
    """Process the provided dataframe: parse datetimes and rename columns.
    
    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame as read from the raw `fietstellingen`, 
        containing the `datum`, `tijd`, `ri Centrum` 
        and `ri Mariakerke` columns.
        
    Returns
    -------
    df2 : pandas.DataFrame
        DataFrame with the datetime info as index and the 
        `direction_centre` and `direction_mariakerke` columns 
        with the counts.
    """
    df.index = pd.to_datetime(df['datum'] + ' ' + df['tijd'], 
                              format="%d/%m/%Y %H:%M")
    df2 = df.drop(columns=['datum', 'tijd'])
    df2 = df2.rename(columns={'ri Centrum': 'direction_centre', 
                              'ri Mariakerke':'direction_mariakerke'})
    return df2
```

```{code-cell} ipython3
df_raw = pd.read_csv("data/fietstellingencoupure.csv", sep=';')
df_preprocessed = process_bike_count_data(df_raw)
df_preprocessed.head()
```

### Store our collected data set as an interim data product

+++

As we finished our data-collection step, we want to save this result as an interim data output of our small investigation. As such, we do not have to re-download all the files each time something went wrong, but can restart from our interim step.

```{code-cell} ipython3
df_preprocessed.to_csv("bike_count_interim.csv")
```

## Data exploration and analysis

+++

We now have a cleaned-up data set of the bike counts at Coupure Links in Ghent (Belgium). Next, we want to get an impression of the characteristics and properties of the data

+++

### Load the interim data

+++

Reading the file in from the interim file (when you want to rerun the whole analysis on the updated online data, you would comment out this cell...)

```{code-cell} ipython3
df = pd.read_csv("bike_count_interim.csv", index_col=0, parse_dates=True)
```

### Count interval verification

+++

The number of bikers are counted for intervals of approximately 15 minutes. But let's check if this is indeed the case. Calculate the difference between each of the consecutive values of the index. We can use the `Series.diff()` method:

```{code-cell} ipython3
pd.Series(df.index).diff()
```

The count of the possible intervals is of interest:

```{code-cell} ipython3
pd.Series(df.index).diff().value_counts()
```

There are a few records that are not exactly 15min. But given it are only a few ones, we will ignore this for the current case study and just keep them for this explorative study.  

Bonus question: do you know where the values of `-1 days +23:15:01` and `01:15:00` are coming from?

```{code-cell} ipython3
df.describe()
```

### Quiet periods

+++

<div class="alert alert-success">

**EXERCISE**

Create a new Pandas Series `df_both` which contains the sum of the counts of both directions.

<details><summary>Hints</summary>

- Check the purpose of the `axis` argument of the `sum` method.

</details>   

```{code-cell} ipython3
:clear_cell: true

df_both = df.sum(axis=1)
df_both
```

<div class="alert alert-success">

**EXERCISE**

Using the `df_both` from the previous exercise, create a new Series `df_quiet` which contains only those intervals for which less than 5 cyclists passed in both directions combined

<details><summary>Hints</summary>

- Use the `[]` to select data. You can use conditions (so-called _boolean indexing_) returning True/False inside the brackets.

</details>    
   

```{code-cell} ipython3
:clear_cell: true

df_quiet = df_both[df_both < 5]
```

<div class="alert alert-success">

**EXERCISE**

Using the original data `df`, select only the intervals for which less than 3 cyclists passed in one or the other direction. Hence, less than 3 cyclists towards the center or less than 3 cyclists towards Mariakerke.

<details><summary>Hints</summary>

- To combine conditions use the `|` (or) or the `&` (and) operators.
- Make sure to use `()` around each individual condition.    

</details>    
  

```{code-cell} ipython3
:clear_cell: true

df[(df['direction_centre'] < 3) | (df['direction_mariakerke'] < 3)]
```

### Count statistics

+++

<div class="alert alert-success">

**EXERCISE**

What is the average number of bikers passing each 15 min?
    
<details><summary>Hints</summary>

- As the time series is already 15min level, this is just the same as taking the mean.

</details>    
    

```{code-cell} ipython3
:clear_cell: true

df.mean()
```

<div class="alert alert-success">

**EXERCISE**

What is the average number of bikers passing each hour?

<details><summary>Hints</summary>

- Use `resample` to first calculate the number of bikers passing each hour. 
- `resample` requires an aggregation function that defines how to combine the values within each group (in this case all values within each hour).

</details>

```{code-cell} ipython3
:clear_cell: true

df.resample('H').sum().mean()
```

<div class="alert alert-success">

**EXERCISE**

What are the 10 highest peak values observed during any of the intervals for the direction towards the center of Ghent?

<details><summary>Hints</summary>

- Pandas provides the `nsmallest` and  `nlargest` methods to derive N smallest/largest values of a column.

</details>

```{code-cell} ipython3
:clear_cell: true

df['direction_centre'].nlargest(10)
# alternative:
# df['direction_centre'].sort_values(ascending=False).head(10)
```

<div class="alert alert-success">

**EXERCISE**

What is the maximum number of cyclist that passed on a single day calculated on both directions combined?

<details><summary>Hints</summary>

- Combine both directions by taking the sum.
- Next, `resample` to daily values
- Get the maximum value or ask for the n largest to see the dates as well.    

</details>

```{code-cell} ipython3
:clear_cell: true

df_both = df.sum(axis=1)
```

```{code-cell} ipython3
:clear_cell: true

df_daily = df_both.resample('D').sum()
```

```{code-cell} ipython3
:clear_cell: true

df_daily.max()
```

```{code-cell} ipython3
:clear_cell: false

df_daily.nlargest(10)
```

The high number of bikers passing on 2013-06-05 was not by coincidence: http://www.nieuwsblad.be/cnt/dmf20130605_022 ;-)

+++

### Trends as function of time

+++

<div class="alert alert-success">

**EXERCISE**

How does the long-term trend look like? Calculate monthly sums and plot the result.

<details><summary>Hints</summary>

- The symbol for monthly resampling is `M`.
- Use the `plot` method of Pandas, which will generate a line plot of each numeric column by default.

</details>

```{code-cell} ipython3
:clear_cell: true

df_monthly = df.resample('M').sum()
df_monthly.plot()
```

<div class="alert alert-success">

**EXERCISE**

Let's have a look at some short term patterns. For the data of the first 3 weeks of January 2014, calculate the hourly counts and visualize them.

<details><summary>Hints</summary>

- Slicing is done using `[]`, you can use string representation of dates to select from a `datetime` index: e.g. `'2010-01-01':'2020-12-31'`

</details>

```{code-cell} ipython3
:clear_cell: true

df_hourly = df.resample('H').sum()
```

```{code-cell} ipython3
:clear_cell: true

df_hourly.head()
```

```{code-cell} ipython3
:clear_cell: true

df_hourly['2014-01-01':'2014-01-20'].plot()
```

**New Year's Eve 2013-2014**

+++

<div class="alert alert-success">

**EXERCISE**

- Select a subset of the data set from 2013-12-31 12:00:00 until 2014-01-01 12:00:00 and assign the result to a new variable `newyear` 
- Plot the selected data `newyear`.
- Use a `rolling` function with a window of 10 values (check documentation of the function) to smooth the data of this period and make a plot of the smoothed version.

<details><summary>Hints</summary>

- Just like `resample`, `rolling` requires an aggregate statistic (e.g. mean, median,...) to combine the values within the window.

</details>

```{code-cell} ipython3
:clear_cell: true

newyear = df["2013-12-31 12:00:00": "2014-01-01 12:00:00"]
```

```{code-cell} ipython3
:clear_cell: true

newyear.plot()
```

```{code-cell} ipython3
:clear_cell: true

newyear.rolling(10, center=True).mean().plot(linewidth=2)
```

A more advanced usage of Matplotlib to create a combined plot:

```{code-cell} ipython3
:clear_cell: true

# A more in-detail plotting version of the graph.
fig, ax = plt.subplots()
newyear.plot(ax=ax, color=['LightGreen', 'LightBlue'], legend=False, rot=0)
newyear.rolling(10, center=True).mean().plot(linewidth=2, ax=ax, color=['DarkGreen', 'DarkBlue'], rot=0)

ax.set_xlabel('')
ax.set_ylabel('Cyclists count')
```

---

## The power of `groupby`...

Looking at the data in the above exercises, there seems to be clearly a:

- daily pattern
- weekly pattern
- yearly pattern

Such patterns can easily be calculated and visualized in pandas using the `DatetimeIndex` attributes `dayofweek` combined with `groupby` functionality. Below a taste of the possibilities, and we will learn about this in the proceeding notebooks:

+++

**Weekly pattern**:

```{code-cell} ipython3
df_daily = df.resample('D').sum()
```

```{code-cell} ipython3
df_daily.groupby(df_daily.index.dayofweek).mean().plot(kind='bar')
```

**Daily pattern:**

```{code-cell} ipython3
df_hourly.groupby(df_hourly.index.hour).mean().plot()
```

So the daily pattern is clearly different for both directions. In the morning more people go north, in the evening more people go south. The morning peak is also more condensed.

+++

**Monthly pattern**

```{code-cell} ipython3
df_monthly = df.resample('M').sum()
```

```{code-cell} ipython3
from calendar import month_abbr 
```

```{code-cell} ipython3
ax = df_monthly.groupby(df_monthly.index.month).mean().plot()
ax.set_ylim(0)
xlabels = ax.set_xticklabels(list(month_abbr)[0::2]) #too lazy to write the month values yourself...
```

## Acknowledgements
Thanks to the [city of Ghent](https://data.stad.gent/) for opening their data
