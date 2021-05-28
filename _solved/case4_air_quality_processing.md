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

+++

AirBase is the European air quality database maintained by the European Environment Agency (EEA). It contains air quality monitoring data and information submitted by participating countries throughout Europe. The [air quality database](https://www.eea.europa.eu/data-and-maps/data/aqereporting-8/air-quality-zone-geometries) consists of a multi-annual time series of air quality measurement data and statistics for a number of air pollutants.

+++

Some of the data files that are available from AirBase were included in the data folder: the hourly **concentrations of nitrogen dioxide (NO2)** for 4 different measurement stations:

- FR04037 (PARIS 13eme): urban background site at Square de Choisy
- FR04012 (Paris, Place Victor Basch): urban traffic site at Rue d'Alesia
- BETR802: urban traffic site in Antwerp, Belgium
- BETN029: rural background site in Houtem, Belgium

See http://www.eea.europa.eu/themes/air/interactive/no2

```{code-cell} ipython3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.options.display.max_rows = 8
plt.style.use("seaborn-whitegrid")
```

# Processing a single file

We will start with processing one of the downloaded files (`BETR8010000800100hour.1-1-1990.31-12-2012`). Looking at the data, you will see it does not look like a nice csv file:

```{code-cell} ipython3
with open("../data/BETR8010000800100hour.1-1-1990.31-12-2012") as f:
    print(f.readline())
```

So we will need to do some manual processing.

+++

Just reading the tab-delimited data:

```{code-cell} ipython3
data = pd.read_csv("../data/BETR8010000800100hour.1-1-1990.31-12-2012", sep='\t')#, header=None)
```

```{code-cell} ipython3
data.head()
```

The above data is clearly not ready to be used! Each row contains the 24 measurements for each hour of the day, and also contains a flag (0/1) indicating the quality of the data. Furthermore, there is no header row with column names.

+++

<div class="alert alert-success">

<b>EXERCISE</b>: <br><br> Clean up this dataframe by using more options of `read_csv` (see its [docstring](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html))

 <ul>
  <li>specify the correct delimiter</li>
  <li>specify that the values of -999 and -9999 should be regarded as NaN</li>
  <li>specify are own column names (for how the column names are made up, see See <a href="http://stackoverflow.com/questions/6356041/python-intertwining-two-lists">http://stackoverflow.com/questions/6356041/python-intertwining-two-lists</a>)
</ul>
</div>

```{code-cell} ipython3
# Column names: list consisting of 'date' and then intertwined the hour of the day and 'flag'
hours = ["{:02d}".format(i) for i in range(24)]
column_names = ['date'] + [item for pair in zip(hours, ['flag' + str(i) for i in range(24)]) for item in pair]
```

```{code-cell} ipython3
:clear_cell: true

data = pd.read_csv("../data/BETR8010000800100hour.1-1-1990.31-12-2012",
                   sep='\t', header=None, names=column_names, na_values=[-999, -9999])
```

```{code-cell} ipython3
:clear_cell: true

data.head()
```

For the sake of this tutorial, we will disregard the 'flag' columns (indicating the quality of the data). 

+++

<div class="alert alert-success">

<b>EXERCISE</b>:
<br><br>
Drop all 'flag' columns ('flag1', 'flag2', ...) 

```{code-cell} ipython3
flag_columns = [col for col in data.columns if 'flag' in col]
# we can now use this list to drop these columns
```

```{code-cell} ipython3
:clear_cell: true

data = data.drop(flag_columns, axis=1)
```

```{code-cell} ipython3
data.head()
```

Now, we want to reshape it: our goal is to have the different hours as row indices, merged with the date into a datetime-index. Here we have a wide and long dataframe, and want to make this a long, narrow timeseries.

+++

<div class="alert alert-info">

<b>REMEMBER</b>: 


Recap: reshaping your data with [`stack` / `melt` and `unstack` / `pivot`](./pandas_07_reshaping_data.ipynb)</li>



<img src="../img/schema-stack.svg" width=70%>

</div>

+++

<div class="alert alert-success">

<b>EXERCISE</b>:

<br><br>

Reshape the dataframe to a timeseries. 
The end result should look like:<br><br>


<div class='center'>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>BETR801</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1990-01-02 09:00:00</th>
      <td>48.0</td>
    </tr>
    <tr>
      <th>1990-01-02 12:00:00</th>
      <td>48.0</td>
    </tr>
    <tr>
      <th>1990-01-02 13:00:00</th>
      <td>50.0</td>
    </tr>
    <tr>
      <th>1990-01-02 14:00:00</th>
      <td>55.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>2012-12-31 20:00:00</th>
      <td>16.5</td>
    </tr>
    <tr>
      <th>2012-12-31 21:00:00</th>
      <td>14.5</td>
    </tr>
    <tr>
      <th>2012-12-31 22:00:00</th>
      <td>16.5</td>
    </tr>
    <tr>
      <th>2012-12-31 23:00:00</th>
      <td>15.0</td>
    </tr>
  </tbody>
</table>
<p style="text-align:center">170794 rows × 1 columns</p>
</div>

 <ul>
  <li>Reshape the dataframe so that each row consists of one observation for one date + hour combination</li>
  <li>When you have the date and hour values as two columns, combine these columns into a datetime (tip: string columns can be summed to concatenate the strings) and remove the original columns</li>
  <li>Set the new datetime values as the index, and remove the original columns with date and hour values</li>

</ul>


**NOTE**: This is an advanced exercise. Do not spend too much time on it and don't hesitate to look at the solutions. 

</div>


+++

Reshaping using `melt`:

```{code-cell} ipython3
:clear_cell: true

data_stacked = pd.melt(data, id_vars=['date'], var_name='hour')
data_stacked.head()
```

Reshaping using `stack`:

```{code-cell} ipython3
:clear_cell: true

# we use stack to reshape the data to move the hours (the column labels) into a column.
# But we don't want to move the 'date' column label, therefore we first set this as the index.
# You can check the difference with "data.stack()"
data_stacked = data.set_index('date').stack()
data_stacked.head()
```

```{code-cell} ipython3
:clear_cell: true

# We reset the index to have the date and hours available as columns
data_stacked = data_stacked.reset_index()
data_stacked = data_stacked.rename(columns={'level_1': 'hour'})
data_stacked.head()
```

Combine date and hour:

```{code-cell} ipython3
:clear_cell: true

# Now we combine the dates and the hours into a datetime, and set this as the index
data_stacked.index = pd.to_datetime(data_stacked['date'] + data_stacked['hour'], format="%Y-%m-%d%H")
```

```{code-cell} ipython3
:clear_cell: true

# Drop the origal date and hour columns
data_stacked = data_stacked.drop(['date', 'hour'], axis=1)
data_stacked.head()
```

```{code-cell} ipython3
:clear_cell: true

# rename the remaining column to the name of the measurement station
# (this is 0 or 'value' depending on which method was used)
data_stacked = data_stacked.rename(columns={0: 'BETR801'})
```

```{code-cell} ipython3
data_stacked.head()
```

Our final data is now a time series. In pandas, this means that the index is a `DatetimeIndex`:

```{code-cell} ipython3
data_stacked.index
```

```{code-cell} ipython3
data_stacked.plot()
```

# Processing a collection of files

+++

We now have seen the code steps to process one of the files. We have however multiple files for the different stations with the same structure. Therefore, to not have to repeat the actual code, let's make a function from the steps we have seen above.

+++

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
    <li>Write a function <code>read_airbase_file(filename, station)</code>, using the above steps the read in and process the data, and that returns a processed timeseries.</li>
</ul>
</div>

```{code-cell} ipython3
def read_airbase_file(filename, station):
    """
    Read hourly AirBase data files.
    
    Parameters
    ----------
    filename : string
        Path to the data file.
    station : string
        Name of the station.
       
    Returns
    -------
    DataFrame
        Processed dataframe.
    """
    
    ...
    
    return ...
```

```{code-cell} ipython3
:clear_cell: true

def read_airbase_file(filename, station):
    """
    Read hourly AirBase data files.
    
    Parameters
    ----------
    filename : string
        Path to the data file.
    station : string
        Name of the station.
       
    Returns
    -------
    DataFrame
        Processed dataframe.
    """
    
    # construct the column names    
    hours = ["{:02d}".format(i) for i in range(24)]
    flags = ['flag' + str(i) for i in range(24)]
    colnames = ['date'] + [item for pair in zip(hours, flags) for item in pair]
    
    # read the actual data
    data = pd.read_csv(filename, sep='\t', header=None, na_values=[-999, -9999], names=colnames)
    
    # drop the 'flag' columns
    data = data.drop([col for col in data.columns if 'flag' in col], axis=1)

    # reshape
    data = data.set_index('date')
    data_stacked = data.stack()
    data_stacked = data_stacked.reset_index()
    
    # parse to datetime and remove redundant columns 
    data_stacked.index = pd.to_datetime(data_stacked['date'] + data_stacked['level_1'], format="%Y-%m-%d%H")
    data_stacked = data_stacked.drop(['date', 'level_1'], axis=1)
    data_stacked = data_stacked.rename(columns={0: station})
    
    return data_stacked
```

Test the function on the data file from above:

```{code-cell} ipython3
import os
```

```{code-cell} ipython3
filename = "../data/BETR8010000800100hour.1-1-1990.31-12-2012"
station = os.path.split(filename)[-1][:7]
```

```{code-cell} ipython3
station
```

```{code-cell} ipython3
:clear_cell: false

test = read_airbase_file(filename, station)
test.head()
```

We now want to use this function to read in all the different data files from AirBase, and combine them into one Dataframe. 

+++

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>Use the <code>glob.glob</code> function to list all 4 AirBase data files that are included in the 'data' directory, and call the result <code>data_files</code>.</li>
</ul>
</div>

```{code-cell} ipython3
:clear_cell: false

import glob
```

```{code-cell} ipython3
:clear_cell: true

data_files = glob.glob("../data/*0008001*")
data_files
```

<div class="alert alert-success">

<b>EXERCISE</b>:

 <ul>
  <li>Loop over the data files, read and process the file using our defined function, and append the dataframe to a list.</li>
  <li>Combine the the different DataFrames in the list into a single DataFrame where the different columns are the different stations. Call the result <code>combined_data</code>.</li>

</ul>
</div>

```{code-cell} ipython3
:clear_cell: true

dfs = []

for filename in data_files:
    station = filename.split("/")[-1][:7]
    df = read_airbase_file(filename, station)
    dfs.append(df)
```

```{code-cell} ipython3
:clear_cell: true

combined_data = pd.concat(dfs, axis=1)
```

```{code-cell} ipython3
combined_data.head()
```

Finally, we don't want to have to repeat this each time we use the data. Therefore, let's save the processed data to a csv file.

```{code-cell} ipython3
# let's first give the index a descriptive name
combined_data.index.name = 'datetime'
```

```{code-cell} ipython3
combined_data.to_csv("../data/airbase_data_processed.csv")
```
