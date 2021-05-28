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


> *DS Data manipulation, analysis and visualisation in Python*  
> *December, 2019*

> *© 2016, Joris Van den Bossche and Stijn Van Hoey  (<mailto:jorisvandenbossche@gmail.com>, <mailto:stijnvanhoey@gmail.com>). Licensed under [CC BY 4.0 Creative Commons](http://creativecommons.org/licenses/by/4.0/)*

---

+++

<img src="https://nbocdn.akamaized.net/Assets/Images_Upload/2016/11/24/GEFV45415.jpg?maxheight=460&maxwidth=638">

+++

In this case study, we will make use of the freely available bike count data of the city of Ghent. At the Coupure Links, next to the Faculty of Bioscience Engineering, a counter keeps track of the number of passing cyclists in both directions.  

Those data are available on the open data portal of the city: https://data.stad.gent/data/236

```{code-cell} ipython3
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')

%matplotlib notebook
```

## Reading and processing the data

+++

### Read csv data from URL

+++

The data are avaible in CSV, JSON and XML format. We will make use of the CSV data. The link to download the data can be found on the webpage. For the first dataset, this is:

    link = "https://datatank.stad.gent/4/mobiliteit/fietstellingencoupure.csv"
    
A limit defines the size of the requested data set, by adding a limit parameter `limit` to the URL :

    link = "https://datatank.stad.gent/4/mobiliteit/fietstellingencoupure.csv?limit=100000"

Those datasets contain the historical data of the bike counters, and consist of the following columns:

- The first column `datum` is the date, in `dd/mm/yy` format
- The second column `tijd` is the time of the day, in `hh:mm` format
- The third and fourth column `ri Centrum` and `ri Mariakerke` are the counts at that point in time (counts between this timestamp and the previous)

```{code-cell} ipython3
limit = 200000
link = "https://datatank.stad.gent/4/mobiliteit/fietstellingencoupure.csv?limit={}".format(limit)
```

<div class="alert alert-success">
 <b>EXERCISE</b>:
 <ul>
  <li>Read the csv file from the url into a DataFrame `df`, the delimiter of the data is `;`</li>
  <li>Inspect the first and last 5 rows, and check the number of observations</li>
  <li>Inspect the data types of the different columns</li>

</ul> 

</div>

```{code-cell} ipython3
:clear_cell: true

df = pd.read_csv(link, sep=';')
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

<div class="alert alert-warning">

 <b>Remark</b>: If the download is very slow, consider to reset the limit variable to a lower value as most execises will just work with the first 100000 records as well.

</div>

+++

### Data processing

+++

As explained above, the first and second column (respectively `datum` and `tijd`) indicate the date and hour of the day. To obtain a time series, we have to combine those two columns into one series of actual datetime values. 

+++

<div class="alert alert-success">

 <b>EXERCISE</b>: Preprocess the data

 <ul>
  <li>Combine the 'datum' and 'tijd' columns into one Series of string datetime values (Hint: concatenating strings can be done with the addition operation)</li>
  <li>Parse the string datetime values (Hint: specifying the format will make this a lot faster)</li>
  <li>Set the resulting dates as the index</li>
  <li>Remove the original 'tijd' and 'tijd' columns (Hint: check the <code>drop</code> method)</li>
  <li>Rename the 'ri Centrum', 'ri Mariakerke' to 'direction_centre', 'direction_mariakerke' (Hint: check the <code>rename</code> function)</li>
</ul> 

</div>

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

df = df.drop(columns=['datum', 'tijd'])
```

```{code-cell} ipython3
:clear_cell: true

df = df.rename(columns={'ri Centrum': 'direction_centre', 'ri Mariakerke':'direction_mariakerke'})
```

```{code-cell} ipython3
df.head()
```

Having the data available with an interpreted datetime, provides us the possibility of having time aware plotting:

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
%timeit -n 1 -r 1 pd.to_datetime(combined, dayfirst=True)
```

However, when we already know the format of the dates (and if this is consistent throughout the full dataset), we can use this information to interpret the dates:

```{code-cell} ipython3
%timeit pd.to_datetime(combined, format="%d/%m/%Y %H:%M")
```

<div class="alert alert-info">

 <b>Remember</b>: Whenever possible, specify the date format to interpret the dates to datetime values!

</div>

+++

### Write the data set cleaning as a function

In order to make it easier to reuse the code for the preprocessing we have now implemented, let's convert the code to a Python function

+++

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>Write a function <code>process_bike_count_data(df)</code> that performs the processing steps as done above for an input DataFrame and return the updated DataFrame</li>
</ul> 

</div>

```{code-cell} ipython3
:clear_cell: true

def process_bike_count_data(df):
    """
    Process the provided dataframe: parse datetimes and rename columns.
    
    """
    df.index = pd.to_datetime(df['datum'] + ' ' + df['tijd'], format="%d/%m/%Y %H:%M")
    df = df.drop(columns=['datum', 'tijd'])
    df = df.rename(columns={'ri Centrum': 'direction_centre', 'ri Mariakerke':'direction_mariakerke'})
    return df
```

```{code-cell} ipython3
df_raw = pd.read_csv(link, sep=';')
df_preprocessed = process_bike_count_data(df_raw)
```

### Store our collected dataset as an interim data product

+++

As we finished our data-collection step, we want to save this result as a interim data output of our small investigation. As such, we do not have to re-download all the files each time something went wrong, but can restart from our interim step.

```{code-cell} ipython3
df_preprocessed.to_csv("bike_count_interim.csv")
```

## Data exploration and analysis

+++

We now have a cleaned-up dataset of the bike counts at Coupure Links. Next, we want to get an impression of the characteristics and properties of the data

+++

### Load the interim data

+++

Reading the file in from the interim file (when you want to rerun the whole analysis on the updated online data, you would comment out this cell...)

```{code-cell} ipython3
df = pd.read_csv("bike_count_interim.csv", index_col=0, parse_dates=True)
```

### Count interval verification

+++

The number of bikers are counted for intervals of approximately 15 minutes. But let's check if this is indeed the case.  
For this, we want to calculate the difference between each of the consecutive values of the index. We can use the `Series.diff()` method:

```{code-cell} ipython3
pd.Series(df.index).diff()
```

Again, the count of the possible intervals is of interest:

```{code-cell} ipython3
pd.Series(df.index).diff().value_counts()
```

There are a few records that is not exactly 15min. But given it are only a few ones, we will ignore this for the current case study and just keep them as such for this explorative study.  

Bonus question: do you know where the values of `-1 days +23:15:01` and `01:15:00` are coming from?

```{code-cell} ipython3
df.describe()
```

### Quiet periods

+++

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>Create a new Series, <code>df_both</code> which contains the sum of the counts of both directions</li>
</ul> 

<br>

_Tip:_ check the purpose of the `axis` argument of the `sum` function

</div>

```{code-cell} ipython3
:clear_cell: true

df_both = df.sum(axis=1)
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>Using the <code>df_both</code> from the previous exercise, create a new Series <code>df_quiet</code> which contains only those intervals for which less than 5 cyclists passed in both directions combined</li>
</ul> 

</div>

```{code-cell} ipython3
:clear_cell: true

df_quiet = df_both[df_both < 5]
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>Using the original data, select only the intervals for which less than 3 cyclists passed in one or the other direction. Hence, less than 3 cyclists towards the centre or less than 3 cyclists towards Mariakerke.</li>
</ul> 

</div>

```{code-cell} ipython3
:clear_cell: true

df[(df['direction_centre'] < 3) | (df['direction_mariakerke'] < 3)]
```

### Count statistics

+++

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>What is the average number of bikers passing each 15 min?</li>
</ul> 

</div>

```{code-cell} ipython3
:clear_cell: true

df.mean()
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>What is the average number of bikers passing each hour?</li>
</ul> 

_Tip:_ you can use `resample` to first calculate the number of bikers passing each hour.

</div>

```{code-cell} ipython3
:clear_cell: true

df.resample('H').sum().mean()
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>What are the 10 highest peak values observed during any of the intervals for the direction towards the centre of Ghent?</li>
</ul> 

</div>

```{code-cell} ipython3
:clear_cell: true

df['direction_centre'].nlargest(10)
# alternative:
# df['direction_centre'].sort_values(ascending=False).head(10)
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>What is the maximum number of cyclist that passed on a single day calculated on both directions combined?</li>
</ul> 

</div>

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
df_daily.nlargest(10)
```

2013-06-05 was the first time more than 10,000 bikers passed on one day. Apparanlty, this was not just by coincidence... http://www.nieuwsblad.be/cnt/dmf20130605_022

+++

### Trends as function of time

+++

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>How does the long-term trend look like? Calculate monthly sums and plot the result.</li>
</ul> 

</div>

```{code-cell} ipython3
:clear_cell: true

df_monthly = df.resample('M').sum()
df_monthly.plot()
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>Let's have a look at some short term patterns. For the data of the first 3 weeks of January 2014, calculate the hourly counts and visualize them.</li>
</ul> 

</div>

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

<b>EXERCISE</b>:

 <ul>
  <li>Select a subset of the data set from 2013-12-31 12:00:00 untill 2014-01-01 12:00:00, store as variable <code>newyear</code> and plot this subset</li>
  <li>Use a <code>rolling</code> function (check documentation of the function!) to smooth the data of this period and make a plot of the smoothed version</li>
</ul> 

</div>

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

A more advanced usage of matplotlib to create a combined plot:

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

Such patterns can easily be calculated and visualized in pandas using the DatetimeIndex attributes `weekday` combined with `groupby` functionality. Below a taste of the possibilities, and we will learn about this in the proceeding notebooks:

+++

**Weekly pattern**:

```{code-cell} ipython3
df_daily = df.resample('D').sum()
```

```{code-cell} ipython3
df_daily.groupby(df_daily.index.weekday).mean().plot(kind='bar')
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
