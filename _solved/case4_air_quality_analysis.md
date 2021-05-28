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

<p><font size="6"><b> Case study: air quality data of European monitoring stations (AirBase)</b></font></p><br>

__AirBase (The European Air quality dataBase): hourly measurements of all air quality monitoring stations from Europe.__

> *DS Data manipulation, analysis and visualisation in Python*  
> *December, 2019*

> *© 2016, Joris Van den Bossche and Stijn Van Hoey  (<mailto:jorisvandenbossche@gmail.com>, <mailto:stijnvanhoey@gmail.com>). Licensed under [CC BY 4.0 Creative Commons](http://creativecommons.org/licenses/by/4.0/)*

---

```{code-cell} ipython3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotnine as pn

pd.options.display.max_rows = 8
```

In the previous notebook, we processed some raw data files of the AirBase air quality data. As a reminder, the data contains hourly concentrations of nitrogen dioxide (NO2) for 4 different measurement stations:

- FR04037 (PARIS 13eme): urban background site at Square de Choisy
- FR04012 (Paris, Place Victor Basch): urban traffic site at Rue d'Alesia
- BETR802: urban traffic site in Antwerp, Belgium
- BETN029: rural background site in Houtem, Belgium

See http://www.eea.europa.eu/themes/air/interactive/no2

+++

# Importing and quick exploration

+++

We processed the individual data files in the previous notebook, and saved it to a csv file `../data/airbase_data_processed.csv`. Let's import the file here (if you didn't finish the previous notebook, a version of the dataset is also available in `../data/airbase_data.csv`):

```{code-cell} ipython3
alldata = pd.read_csv('../data/airbase_data.csv', index_col=0, parse_dates=True)
```

We only use the data from 1999 onwards:

```{code-cell} ipython3
data = alldata['1999':].copy()
```

Some first exploration with the *typical* functions:

```{code-cell} ipython3
data.head() # tail()
```

```{code-cell} ipython3
data.info()
```

```{code-cell} ipython3
data.describe(percentiles=[0.1, 0.5, 0.9])
```

```{code-cell} ipython3
data.plot(figsize=(12,6))
```

<div class="alert alert-warning">
<b>ATTENTION!</b>: <br><br>

When just using `.plot()` without further notice (selection, aggregation,...)
 <ul>
  <li>Risk of running into troubles by overloading your computer processing (certainly with looooong time series)</li>
  <li>Not always the most informative/interpretable visualisation</li>
</ul>
</div>

+++

**Plot only a subset**

+++

Why not just using the `head`/`tail` possibilities?

```{code-cell} ipython3
data.tail(500).plot(figsize=(12,6))
```

**Summary figures**

+++

Use summary statistics...

```{code-cell} ipython3
data.plot(kind='box', ylim=[0,250])
```

Also with seaborn plots function, just start with some subsets as first impression...

As we already have seen previously, the plotting library [seaborn](http://seaborn.pydata.org/generated/seaborn.heatmap.html) provides some high-level plotting functions on top of matplotlib (check the [docs](http://seaborn.pydata.org/examples/index.html)!). One of those functions is `pairplot`, which we can use here to quickly visualize the concentrations at the different stations and their relation:

```{code-cell} ipython3
import seaborn as sns
```

```{code-cell} ipython3
sns.pairplot(data.tail(5000).dropna())
```

# Is this a tidy dataset ?

```{code-cell} ipython3
data.head()
```

In principle this is not a tidy dataset. The variable that was measured is the NO2 concentration, and is divided in 4 columns. Of course those measurements were made at different stations, so one could interpet it as separate variables. But in any case, such format typically does not work well with `plotnine` which expects a pure tidy format.


Reason to not use a tidy dataset here: 

* bigger memory use
* timeseries functionality like resample works better
* pandas plotting already does what we want when having different columns for *some* types of plots (eg line plots of the timeseries)

+++

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>Create a tidy version of this dataset <code>data_tidy</code>, ensuring the result has new columns 'station' and 'no2'.</li>
  <li>Check how many missing values are contained in the 'no2' column.</li>
  <li>Drop the rows with missing values in that column.</li>
</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

data_tidy = data.reset_index().melt(id_vars=["datetime"], var_name='station', value_name='no2')
data_tidy.head()
```

```{code-cell} ipython3
:clear_cell: true

data_tidy['no2'].isnull().sum()
```

```{code-cell} ipython3
:clear_cell: true

data_tidy = data_tidy.dropna()
```

In the following exercises we will mostly do our analysis on `data`and often use pandas (or seaborn) plotting, but once we produced some kind of summary dataframe as the result of an analysis, then it becomes more interesting to convert that result to a tidy format to be able to use the more advanced plotting functionality of `plotnine`.

+++

# Exercises

+++

<div class="alert alert-warning">

<b>REMINDER</b>: <br><br>

Take a look at the [Timeseries notebook](pandas_04_time_series_data.ipynb) when you require more info about:

 <ul>
  <li><code>resample</code></li>
  <li>string indexing of DateTimeIndex</li>
</ul><br>

Take a look at the [matplotlib](visualization_01_matplotlib.ipynb) and [plotnine](visualization_02_plotnine.ipynb) notebooks when you require more info about the plot requirements.

</div>

+++

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>Plot the monthly mean and median concentration of the 'FR04037' station for the years 2009 - 2013 in a single figure/ax</li>
</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

fig, ax = plt.subplots()
data.loc['2009':, 'FR04037'].resample('M').mean().plot(ax=ax, label='mean')
data.loc['2009':, 'FR04037'].resample('M').median().plot(ax=ax, label='median')
ax.legend(ncol=2)
ax.set_title("FR04037");
```

```{code-cell} ipython3
:clear_cell: true

data.loc['2009':, 'FR04037'].resample('M').agg(['mean', 'median']).plot()
```

<div class="alert alert-success">

<b>EXERCISE</b>

 <ul>
  <li>Make a violin plot for January 2011 until August 2011 (check out the documentation to improve the plotting settings)</li>
  <li>Change the y-label to 'NO$_2$ concentration (µg/m³)'</li>
</ul><br>

NOTE: 

When having the data not in a long format but when having different columns for which you want to make violin plots, you can use [seaborn](http://seaborn.pydata.org/examples/index.html).
When using the tidy data, we can use `plotnine`.
</div>

```{code-cell} ipython3
:clear_cell: true

# with seaborn
fig, ax = plt.subplots()
sns.violinplot(data=data['2011-01': '2011-08'], palette="GnBu_d", ax=ax)
ax.set_ylabel("NO$_2$ concentration (µg/m³)")
```

```{code-cell} ipython3
:clear_cell: true

# with plotnine
data_tidy_subset = data_tidy[(data_tidy['datetime'] >= "2011-01") & (data_tidy['datetime'] < "2011-09")]

(pn.ggplot(data_tidy_subset, pn.aes(x='station', y='no2'))
    + pn.geom_violin()
    + pn.ylab("NO$_2$ concentration (µg/m³)"))
```

<div class="alert alert-success">

<b>EXERCISE</b>

 <ul>
  <li>Make a bar plot with pandas of the mean of each of the stations in the year 2012 (check the documentation of Pandas plot to adapt the rotation of the labels) and make sure all bars have the same color.</li>
  <li>Using the matplotlib objects, change the y-label to 'NO$_2$ concentration (µg/m³)</li>
  <li>Add a 'darkorange' horizontal line on the ax for the y-value 40 µg/m³ (command for horizontal line from matplotlib: <code>axhline</code>).</li>
  <li><a href="visualization_01_matplotlib.ipynb">Place the text</a> 'Yearly limit is 40 µg/m³' just above the 'darkorange' line.</li>
</ul><br>

</div>

```{code-cell} ipython3
:clear_cell: true

fig, ax = plt.subplots()
data['2012'].mean().plot(kind='bar', ax=ax, rot=0, color='C0')
ax.set_ylabel("NO$_2$ concentration (µg/m³)")
ax.axhline(y=40., color='darkorange')
ax.text(0.01, 0.48, 'Yearly limit is 40 µg/m³',
        horizontalalignment='left', fontsize=13, 
        transform=ax.transAxes, color='darkorange');
```

<div class="alert alert-success">

<b>EXERCISE:</b> Did the air quality improve over time?

 <ul>
  <li>For the data from 1999 till the end, plot the yearly averages</li>
  <li>For the same period, add the overall mean (all stations together) as an additional line to the graph, use a thicker black line (<code>linewidth=4</code> and <code>linestyle='--'</code>)</li>
  <li>[OPTIONAL] Add a legend above the ax for all lines</li>
  

</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

fig, ax = plt.subplots()

data['1999':].resample('A').mean().plot(ax=ax)
data['1999':].mean(axis=1).resample('A').mean().plot(color='k', 
                                            linestyle='--', 
                                            linewidth=4, 
                                            ax=ax, 
                                            label='Overall mean')
ax.legend(loc='center', ncol=3, 
          bbox_to_anchor=(0.5, 1.06))
ax.set_ylabel("NO$_2$ concentration (µg/m³)");
```

<div class="alert alert-info">

<b>REMEMBER</b>: <br><br>

`resample` is a special version of a`groupby` operation. For example, taking annual means with `data.resample('A').mean()` is equivalent to `data.groupby(data.index.year).mean()` (but the result of `resample` still has a DatetimeIndex).<br><br>

Checking the index of the resulting DataFrame when using **groupby** instead of resample: You'll notice that the Index lost the DateTime capabilities:

<code>
> data.groupby(data.index.year).mean().index
</code>

Results in:

<code>
Int64Index([1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000,
            2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011,
            2012],
           dtype='int64')$
</code>

<br>

When using **resample**, we keep the DateTime capabilities:

<code>
> data.resample('A').mean().index
</code>

Results in:

<code>
DatetimeIndex(['1999-12-31', '2000-12-31', '2001-12-31', '2002-12-31',
               '2003-12-31', '2004-12-31', '2005-12-31', '2006-12-31',
               '2007-12-31', '2008-12-31', '2009-12-31', '2010-12-31',
               '2011-12-31', '2012-12-31'],
              dtype='datetime64[ns]', freq='A-DEC')
</code>
<br>

But, `groupby` is more flexible and can also do resamples that do not result in a new continuous time series, e.g. by grouping by the hour of the day to get the diurnal cycle.
</div>

+++

<div class="alert alert-success">

<b>EXERCISE</b>

 <ul>
    <li>How does the <i>typical yearly profile</i> (typical averages for the different months over the years) look like for the different stations? (add a 'month' column as a first step)</li>

</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

# add a column to the dataframe that indicates the month (integer value of 1 to 12):
data['month'] = data.index.month

# now, we can calculate the mean of each month over the different years:
data.groupby('month').mean()

# plot the typical monthly profile of the different stations:
data.groupby('month').mean().plot()
```

```{code-cell} ipython3
data = data.drop("month", axis=1)
```

Note: Technically, we could reshape the result of the groupby operation to a tidy format (we no longer have a real time series), but since we already have the things we want to plot as lines in different columns, doing `.plot` already does what we want.

+++

<div class="alert alert-success">

<b>EXERCISE</b>

 <ul>
  <li>Plot the weekly 95% percentiles of the concentration in 'BETR801' and 'BETN029' for 2011</li>

</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

# Groupby wise
df2011 = data['2011']
df2011.groupby(df2011.index.week)[['BETN029', 'BETR801']].quantile(0.95).plot()
```

```{code-cell} ipython3
:clear_cell: true

# Resample wise (not possible to use quantile directly on a resample, so you need a lambda function)
# Note the different x-axis labels
df2011[['BETN029', 'BETR801']].resample('W').agg(lambda x: x.quantile(0.75)).plot()
```

<div class="alert alert-success">

<b>EXERCISE</b>

 <ul>
  <li>Plot the typical diurnal profile (typical hourly averages) for the different stations taking into account the whole time period.</li>

</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

data.groupby(data.index.hour).mean().plot()
```

<div class="alert alert-success">

<b>EXERCISE</b> <br><br>

What is the difference in the typical diurnal profile between week and weekend days? (and visualise it)<br><br>

Start with only visualizing the different in diurnal profile for the BETR801 station. In a next step, make the same plot for each station.<br><br>

**Hints:**

 <ul>
  <li>Add a column 'weekend' defining if a value of the index is in the weekend (i.e. weekdays 5 and 6) or not</li>
  <li>Add a column 'hour' with the hour of the day for each row.</li>
  <li>You can groupby on multiple items at the same time.</li>

</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

data['weekend'] = data.index.weekday.isin([5, 6])
data['weekend'] = data['weekend'].replace({True: 'weekend', False: 'weekday'})
data['hour'] = data.index.hour
```

```{code-cell} ipython3
:clear_cell: true

data_weekend = data.groupby(['weekend', 'hour']).mean()
data_weekend.head()
```

```{code-cell} ipython3
:clear_cell: true

# using unstack and pandas plotting
data_weekend_BETR801 = data_weekend['BETR801'].unstack(level=0)
data_weekend_BETR801.plot()
```

```{code-cell} ipython3
:clear_cell: true

# using a tidy dataset and plotnine
data_weekend_BETR801_tidy = data_weekend['BETR801'].reset_index()

(pn.ggplot(data_weekend_BETR801_tidy,
           pn.aes(x='hour', y='BETR801', color='weekend'))
    + pn.geom_line())
```

```{code-cell} ipython3
:clear_cell: true

# tidy dataset that still includes all stations

data_weekend_tidy = pd.melt(data_weekend.reset_index(), id_vars=['weekend', 'hour'],
                            var_name='station', value_name='no2')
data_weekend_tidy.head()
```

```{code-cell} ipython3
:clear_cell: true

# when still having multiple factors, it becomes useful to convert to tidy dataset and use plotnine
(pn.ggplot(data_weekend_tidy,
           pn.aes(x='hour', y='no2', color='weekend'))
    + pn.geom_line()
    + pn.facet_wrap('station'))
```

```{code-cell} ipython3
data = data.drop(['hour', 'weekend'], axis=1)
```

<div class="alert alert-success">

<b>EXERCISE</b>:<br><br>

 <ul>
  <li>Calculate the correlation between the different stations (check in the documentation, google "pandas correlation" or use the magic function <code>%psearch</code>)</li>

</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

data[['BETR801', 'BETN029', 'FR04037', 'FR04012']].corr()
```

<div class="alert alert-success">

<b>EXERCISE</b>:<br><br>

Count the number of exceedances of hourly values above the European limit 200 µg/m3 for each year and station after 2005. Make a barplot of the counts. Add an horizontal line indicating the maximum number of exceedances (which is 18) allowed per year?<br><br>

**Hints:**

 <ul>
  <li>Create a new DataFrame, called <code>exceedances</code>, (with boolean values) indicating if the threshold is exceeded or not</li>
  <li>Remember that the sum of True values can be used to count elements</li>
  <li>Adding a horizontal line can be done with the matplotlib function <code>ax.axhline</code></li>


</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

exceedances = data > 200
```

```{code-cell} ipython3
:clear_cell: true

# group by year and count exceedances (sum of boolean)
exceedances = exceedances.groupby(exceedances.index.year).sum()
```

```{code-cell} ipython3
:clear_cell: true

# Make a barplot of the yearly number of exceedances
ax = exceedances.loc[2005:].plot(kind='bar')
ax.axhline(18, color='k', linestyle='--')
```

# More advanced exercises...

```{code-cell} ipython3
data = alldata['1999':].copy()
```

<div class="alert alert-success">

<b>EXERCISE</b>: Perform the following actions for the station `'FR04012'` only:

 <ul>
  <li>Remove the rows containing <code>NaN</code> or zero values</li>
  <li>Sort the values  of the rows according to the air quality values (low to high values)</li>
  <li>Rescale the values to the range [0-1] and store result as <code>FR_scaled</code> (Hint: check <a href="https://en.wikipedia.org/wiki/Feature_scaling#Rescaling">wikipedia</a>)</li>
  <li>Use pandas to plot these values sorted, not taking into account the dates</li>
  <li>Add the station name 'FR04012' as y-label</li>
  <li>[OPTIONAL] Add a vertical line to the plot where the line (hence, the values of variable FR_scaled) reach the value <code>0.3</code>. You will need the documentation of <code>np.searchsorted</code> and matplotlib's <code>axvline</code></li>
</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

FR_station = data['FR04012'] # select the specific data series
FR_station = FR_station[(FR_station.notnull()) & (FR_station != 0.0)]  # exclude the Nan and zero values
```

```{code-cell} ipython3
:clear_cell: true

FR_sorted = FR_station.sort_values(ascending=True)
FR_scaled = (FR_sorted - FR_sorted.min())/(FR_sorted.max() - FR_sorted.min())
```

```{code-cell} ipython3
:clear_cell: true

fig, axfr = plt.subplots()
FR_scaled.plot(use_index=False, ax = axfr)  #alternative version: FR_scaled.reset_index(drop=True).plot(use_index=False)  
axfr.set_ylabel('FR04012')
# optional addition, just in case you need this
axfr.axvline(x=FR_scaled.searchsorted(0.3), color='0.6', linestyle='--', linewidth=3)
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>Create a Figure with two subplots (axes), for which both ax<b>i</b>s are shared</li>
  <li>In the left subplot, plot the histogram (30 bins) of station 'BETN029', only for the year 2009</li>
  <li>In the right subplot, plot the histogram (30 bins) of station 'BETR801', only for the year 2009</li>
  <li>Add the title representing the station name on each of the subplots, you do not want to have a legend</li>
</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

# Mixing an matching matplotlib and Pandas
fig, (ax1, ax2) = plt.subplots(1, 2, 
                               sharex=True, 
                               sharey=True)

data.loc['2009', ['BETN029', 'BETR801']].plot(kind='hist', subplots=True, 
                                              bins=30, legend=False, 
                                              ax=(ax1, ax2))
ax1.set_title('BETN029')
ax2.set_title('BETR801')
# Remark: the width of the bins is calculated over the x data range for both plots together
```

```{code-cell} ipython3
:clear_cell: true

# A more step by step approach (equally valid)
fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True, sharex=True)
data.loc['2009', 'BETN029'].plot(kind='hist', bins=30, ax=ax1)
ax1.set_title('BETN029')
data.loc['2009', 'BETR801'].plot(kind='hist', bins=30, ax=ax2)
ax2.set_title('BETR801')
# Remark: the width of the bins is calculated over the x data range for each plot individually
```

<div class="alert alert-success">

<b>EXERCISE</b>

 <ul>
  <li>Make a selection of the original dataset of the data in January 2009, call the resulting variable <code>subset</code></li>
  <li>Add a new column, called 'weekday', to the variable <code>subset</code> which defines for each data point the day of the week</li>
  <li>From the <code>subset</code> DataFrame, select only Monday (= day 0) and Sunday (=day 6) and remove the others (so, keep this as variable <code>subset</code>)</li>
  <li>Change the values of the weekday column in <code>subset</code> according to the following mapping: <code>{0:"Monday", 6:"Sunday"}</code></li>
  <li>With plotnine, make a scatter plot of the measurements at 'BETN029' vs 'FR04037', with the color variation based on the weekday. Add a linear regression to this plot.</li>
</ul><br>

**Note**: If you run into the **SettingWithCopyWarning** and do not know what to do, recheck [pandas_03b_indexing](pandas_03b_indexing.ipynb)

</div>

```{code-cell} ipython3
:clear_cell: true

subset = data['2009-01'].copy()
subset["weekday"] = subset.index.weekday
subset = subset[subset['weekday'].isin([0, 6])]
```

```{code-cell} ipython3
:clear_cell: true

subset["weekday"] = subset["weekday"].replace(to_replace={0:"Monday", 6:"Sunday"})
```

```{code-cell} ipython3
:clear_cell: true

(pn.ggplot(subset,
           pn.aes(x="BETN029", y="FR04037", color="weekday"))
    + pn.geom_point()
    + pn.stat_smooth(method='lm'))
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>The maximum daily, 8 hour mean, should be below 100 µg/m³. What is the number of exceedances of this limit for each year/station?</li><br><br>
  </ul>
 
  
**Tip:**<br>

Have a look at the `rolling` method to perform moving window operations.<br><br>

**Note:**<br>
This is not an actual limit for NO$_2$, but a nice exercise to introduce the `rolling` method. Other pollutans, such as 0$_3$ have actually such kind of limit values based on 8-hour means.

</div>

```{code-cell} ipython3
:clear_cell: true

exceedances = data.rolling(8).mean().resample('D').max() > 100
```

```{code-cell} ipython3
:clear_cell: true

exceedances = exceedances.groupby(exceedances.index.year).sum()
ax = exceedances.plot(kind='bar')
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>Visualize the typical week profile for station 'BETR801' as boxplots (where the values in one boxplot are the <i>daily means</i> for the different <i>weeks</i> for a certain weekday).</li><br><br>
  </ul>
 
  
**Tip:**<br>

The boxplot method of a DataFrame expects the data for the different boxes in different columns. For this, you can either use `pivot_table` or a combination of `groupby` and `unstack`


</div>

+++

Calculating daily means and add weekday information:

```{code-cell} ipython3
:clear_cell: true

data_daily = data.resample('D').mean()
```

```{code-cell} ipython3
:clear_cell: true

# add a weekday column
data_daily['weekday'] = data_daily.index.weekday
data_daily.head()
```

Plotting with plotnine:

```{code-cell} ipython3
:clear_cell: true

# plotnine
(pn.ggplot(data_daily["2012"],
           pn.aes(x='factor(weekday)', y='BETR801'))
    + pn.geom_boxplot())
```

Reshaping and plotting with pandas:

```{code-cell} ipython3
:clear_cell: true

# when using pandas to plot, the different boxplots should be different columns
# therefore, pivot table so that the weekdays are the different columns
data_daily['week'] = data_daily.index.week
data_pivoted = data_daily['2012'].pivot_table(columns='weekday', index='week', values='BETR801')
data_pivoted.head()
data_pivoted.boxplot();
```

```{code-cell} ipython3
:clear_cell: true

# An alternative method using `groupby` and `unstack`
data_daily['2012'].groupby(['weekday', 'week'])['BETR801'].mean().unstack(level=0).boxplot();
```
