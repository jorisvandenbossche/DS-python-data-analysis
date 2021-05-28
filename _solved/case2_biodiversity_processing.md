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

<p><font size="6"><b> CASE - Biodiversity data - data cleaning and enrichment</b></font></p>


> *DS Data manipulation, analysis and visualisation in Python*  
> *December, 2019*

> *© 2016, Joris Van den Bossche and Stijn Van Hoey  (<mailto:jorisvandenbossche@gmail.com>, <mailto:stijnvanhoey@gmail.com>). Licensed under [CC BY 4.0 Creative Commons](http://creativecommons.org/licenses/by/4.0/)*

---

```{code-cell} ipython3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')
```

**Scenario**:<br> You are interested in occurrence data for a number of species in Flanders. Unfortunately, the sources for this type of data are still scattered among different institutes. After a mailing campaign, you receive a number of files from different formats, in various data formats and styles... 

You decide to be brave and script the interpretation and transformation, in order to provide reproducibility of your work. Moreover, similar analysis will be needed in the future with new data requests. You *hope* that future data requests will result in similar data formats from the individual partners. So, having a script will enhance the efficiency at that moment.

+++

Besides from the technical differences in the data formats (`csv`, `excel`, `shapefile`, `sqlite`...), there are also differences in the naming of the content. For example, the coordinates, can be named `x`/`y`, `decimalLatitude`/`decimalLongitude`, `lat`/`long`... Luckely, you know of an international **open data standard** to describe occurrence data, i.e. [Darwin Core (DwC)](http://rs.tdwg.org/dwc/terms/#sex). Instead of inventing your own data model, you decide to comply to this international standard. The latter will enhance communication and will also make your data compliant to other data services working with this kind of data.

+++

In short, the DwC describes a flat table (cfr. CSV) with an agreed name convention on the header names and conventions on how certain data types need to be represented. Whereas the standard definitions are out of scope, an in depth description is given [here](https://www.tdwg.org/standards/dwc/). For this tutorial, we will focus on a few of the existing terms to learn some elements about data cleaning:
* `eventDate`: ISO 6801 format of dates
* `scientificName`: the accepted scientific name of the species
* `decimalLatitude`/`decimalLongitude`: coordinates of the occurrence in WGS84 format
* `sex`: either `male` or `female` to characterise the sex of the occurrence
* `occurrenceID`: a identifier within the dataset to identify the individual records
* `datasetName`: a static string defining the source of the data

Futhermore, additional information concering the taxonomy will be added using an external API service

+++

**Dataset to work on:**

+++

For this dataset, the data is provided in the following main data files:
* `surveys.csv` the data with the surveys observed in the individual plots
* `species.csv` the overview list of the species shortnames
* `plot_location.xlsx` the overview of coordinates of the individual locations

The data originates from a [study](http://esapubs.org/archive/ecol/E090/118/metadata.htm) of a Chihuahuan desert ecosystem near Portal, Arizona

![](../img/plot_overview.png)

+++

## Survey-data

+++

Reading in the data of the individual surveys:

```{code-cell} ipython3
survey_data = pd.read_csv("../data/surveys.csv")
```

```{code-cell} ipython3
survey_data.head()
```

<div class="alert alert-success">
    
<b>EXERCISE</b>: How many individual records (occurrences) does the survey data set contain?

</div>

```{code-cell} ipython3
:clear_cell: true

len(survey_data)
```

### Adding the data source information as static column

+++

For convenience when this dataset will be combined with other datasets, we first add a column of static values, defining the `datasetName` of this particular data:

```{code-cell} ipython3
datasetname = "Ecological Archives E090-118-D1."
```

Adding this static value as a new column `datasetName`:

+++

<div class="alert alert-success">
    
<b>EXERCISE</b>: Add a new column, 'datasetName', to the survey data set with <code>datasetname</code> as value for all of the records (static value for the entire data set)

</div>

```{code-cell} ipython3
:clear_cell: true

survey_data["datasetName"] = datasetname
```

### Cleaning the sex_char column into a DwC called [sex](http://rs.tdwg.org/dwc/terms/#sex) column

+++

<div class="alert alert-success">

<b>EXERCISE</b>: Get a list of the unique values for the column <code>sex_char</code>.
    
__Tip__, to find the unique values, look for a function called `unique`...

</div>

```{code-cell} ipython3
:clear_cell: true

survey_data["sex_char"].unique().tolist()
```

So, apparently, more information is provided in this column, whereas according to the [metadata](http://esapubs.org/archive/ecol/E090/118/Portal_rodent_metadata.htm) information, the sex information should be either `M` (male) or `F` (female). We will create a column, named `sex` and convert the symbols to the corresponding sex, taking into account the following mapping of the values (see [metadata](http://esapubs.org/archive/ecol/E090/118/Portal_rodent_metadata.htm) for more details):
* `M` -> `male`
* `F` -> `female`
* `R` -> `male`
* `P` -> `female`
* `Z` -> nan

At the same time, we will save the original information of the `sex_char` in a separate column, called `verbatimSex`, as a reference.

+++

In summary, we have to:
* create a new column `verbatimSex`, which is a copy of the current `sex_char` column
* create a new column with the name `sex`
* map the original values of the `sex_char` to the values `male` and `female` according to the listing above

+++

Converting the name of the column header `sex_char` to `verbatimSex` with the `rename` function:

```{code-cell} ipython3
survey_data = survey_data.rename(columns={'sex_char': 'verbatimSex'})
```

<div class="alert alert-success">

<b>EXERCISE</b>: Express the mapping of the the values (e.g. M -> male) into a dictionary object called sex_dict 
    
__Tip__: (1) a NaN-value can be defined as `np.nan`, (2) a dictionary is a Python data structure, https://docs.python.org/3/tutorial/datastructures.html#dictionaries

</div>

```{code-cell} ipython3
:clear_cell: true

sex_dict = {"M": "male",
            "F": "female",
            "R": "male",
            "P": "female",
            "Z": np.nan}
```

<div class="alert alert-success">

<b>EXERCISE</b>: Use the dictionary to replace the values in the `verbatimSex` column to the new values according to the `sex_dict` mapping dictionary and save the mapped values in a new column 'sex'.
    
__Tip__: to replace values using a mapping dictionary, look for a function called `replace`...

</div>

```{code-cell} ipython3
:clear_cell: true

survey_data['sex'] = survey_data['verbatimSex'].replace(sex_dict)
```

Checking the current frequency of values (this should result in the values `male`, `female` and `nan`):

```{code-cell} ipython3
survey_data["sex"].unique()
```

To check what the frequency of occurrences is for male/female of the categories, a bar chart is an possible representation:

+++

<div class="alert alert-success">

<b>EXERCISE</b>: Make a horizontal bar chart comparing the number of male, female and unknown (NaN) records in the dataset
    
__Tip__: check in the help of the Pandas plot function for the `kind` parameter

</div>

```{code-cell} ipython3
:clear_cell: true

survey_data["sex"].value_counts(dropna=False).plot(kind="barh", color="#00007f")
```

<div class="alert alert-warning">

<b>NOTE</b>: The usage of `groupby` combined with a `count` of each group would be an option as well. However, the latter does not support to count the `NaN` values as well. The `value_counts` method does support this with the `dropna=False` argument.

</div>

+++

### Solving double entry field by decoupling

+++

When checking the species unique information:

```{code-cell} ipython3
survey_data["species"].unique()
```

```{code-cell} ipython3
survey_data.head(10)
```

There apparently exists a double entry: `'DM and SH'`, which basically defines two records and should be decoupled to two individual records (i.e. rows). Hence, we should be able to create a additional row based on this split. To do so, Pandas provides a dedicated function since version 0.25, called `explode`. Starting from a small subset example:

```{code-cell} ipython3
example = survey_data.loc[7:10, "species"]
example
```

Using the `split` method on strings, we can split the string using a given character, in this case the word `and`:

```{code-cell} ipython3
example.str.split("and")
```

The `explode` method will create a row for each element in the list:

```{code-cell} ipython3
example_split = example.str.split("and").explode()
example_split
```

Hence, the `DM` and `SH` are now enlisted in separate rows. Other rows remain unchanged. The only remaining issue is the spaces around the characters:

```{code-cell} ipython3
example_split.iloc[1], example_split.iloc[2]
```

Which we can solve again using the string method `strip`, removing the spaces before and after the characters:

```{code-cell} ipython3
example_split.str.strip()
```

To make this reusable, let's create a dedicated function to combine these steps, called `solve_double_field_entry`:

```{code-cell} ipython3
def solve_double_field_entry(df, keyword="and", column="verbatimEventDate"):
    """split on keyword in column for an enumeration and create extra record
    
    Parameters
    ----------
    df: pd.DataFrame
        DataFrame with a double field entry in one or more values
    keyword: str
        word/character to split the double records on
    column: str
        column name to use for the decoupling of the records
    """
    df[column] = df[column].str.split(keyword)
    df = df.explode(column)
    df[column] = df[column].str.strip()  # remove white space around the words
    return df
```

The function takes a DataFrame as input, splits the record into separate rows and returns the updated DataFrame. We can use this function to get an update of the dataFrame, with the an additional row (occurrence) added by decoupling the specific field:

+++

<div class="alert alert-success">
<b>EXERCISE</b>: Use the function <code>solve_double_field_entry</code> to create a dataFrame with an additional row, by decoupling the double entries. Save the result as a variable <code>survey_data_decoupled</code>.
</div>

```{code-cell} ipython3
:clear_cell: true

survey_data_decoupled = solve_double_field_entry(survey_data.copy(), 
                                                 "and", 
                                                 column="species") # get help of the function by SHIFT + TAB
# REMARK: the copy() statement here (!) see pandas_03b_indexing.ipynb notebook `chained indexing section`
```

```{code-cell} ipython3
survey_data_decoupled["species"].unique()
```

```{code-cell} ipython3
survey_data_decoupled.head(11)
```

### Create new occurrence identifier

+++

The `record_id` is no longer a unique identifier after the decoupling of this dataset. We will make a new dataset-specific identifier, by adding a column called `occurrenceID` that takes a new counter as identifier. As a simply and straightforward approach, we will use a new counter for the whole dataset, starting with 1:

```{code-cell} ipython3
np.arange(1, len(survey_data_decoupled) + 1, 1)
```

Create a new column with header <code>occurrenceID</code> with the values 1 -> 35550 as field values:

```{code-cell} ipython3
:clear_cell: false

survey_data_decoupled["occurrenceID"] = np.arange(1, len(survey_data_decoupled) + 1, 1)
```

<div class="alert alert-warning">

 <b>Remark</b>: A reset of the index to generate this column with `reset_index(drop=False)` would be technically perfectly valid. Still, we want the indices to start at 1 instead of 0 (and Python starts counting at 0!)
    
</div>

+++

To overcome the confusion on having both a `record_id` and `occurrenceID` field, we will remove the `record_id` term:

```{code-cell} ipython3
survey_data_decoupled = survey_data_decoupled.drop(columns="record_id")
```

Hence, columns can be `drop`-ped out of a DataFrame

```{code-cell} ipython3
survey_data_decoupled.head(10)
```

### Converting the date values

+++

In the survey-dataset we received, the `month`, `day`, and `year` columns are containing the information about the date, i.e. `eventDate` in DarwinCore terms. We want this data in a ISO format `YYYY-MM-DD`. A convenvient Pandas function is the usage of `to_datatime`, which provides multiple options to interpret dates. One of thes options is the automatic interpretation of some 'typical' columns, like `year`, `month` and `day`, when passing a DataFrame.

```{code-cell} ipython3
# pd.to_datetime(survey_data_decoupled[["year", "month", "day"]])  # uncomment the line and test this statement
```

This is not working, not all dates can be interpreted... We should get some more information on the reason of the errors. By using the option `coerce`, the problem makers will be labeled as a missing value `NaT`. We can count the number of dates that can not be interpreted:

```{code-cell} ipython3
sum(pd.to_datetime(survey_data_decoupled[["year", "month", "day"]], errors='coerce').isnull())
```

<div class="alert alert-success">

<b>EXERCISE</b>: Make a subselection of <code>survey_data_decoupled</code> containing those records that can not correctly be interpreted as date values and save the resulting dataframe as variable <code>trouble_makers</code>

</div>

```{code-cell} ipython3
:clear_cell: true

mask = pd.to_datetime(survey_data_decoupled[["year", "month", "day"]], errors='coerce').isnull()
trouble_makers = survey_data_decoupled[mask]
```

Checking some charactersitics of the trouble_makers:

```{code-cell} ipython3
trouble_makers.head()
```

```{code-cell} ipython3
trouble_makers["day"].unique()
```

```{code-cell} ipython3
trouble_makers["month"].unique()
```

```{code-cell} ipython3
trouble_makers["year"].unique()
```

So, basically the problem is the presence of day `31` during the months April and September of the year 2000. At this moment, we would have to recheck the original data in order to know how the issue could be solved. Apparently, - for this specific case - there has been a data-entry problem in 2000, making the `31` days during this period should actually be `30`. It would be optimal to correct this in the source dataset, but for the further exercise, it will be corrected here.

+++

<div class="alert alert-success">
    <b>EXERCISE</b>: Replace in the dataFrame <code>survey_data_decoupled</code> all of the troublemakers <code>day</code> values into the value 30
</div>

```{code-cell} ipython3
:clear_cell: true

mask = pd.to_datetime(survey_data_decoupled[["year", "month", "day"]], errors='coerce').isnull()
survey_data_decoupled.loc[mask, "day"] = 30
```

Now, we do the parsing again to create a proper `eventDate` field, containing the dates:

```{code-cell} ipython3
survey_data_decoupled["eventDate"] = \
    pd.to_datetime(survey_data_decoupled[["year", "month", "day"]])
```

Just let's do a check the amount of data for each year:

+++

<div class="alert alert-success">
    <b>EXERCISE</b>: Create a horizontal bar chart with the number of records for each year
</div>

```{code-cell} ipython3
:clear_cell: true

survey_data_decoupled.groupby("year").size().plot(kind='barh', color="#00007f", figsize=(10, 10))
```

```{code-cell} ipython3
survey_data_decoupled.head()
```

Currently, the dates are stored in a python specific date format:

```{code-cell} ipython3
survey_data_decoupled["eventDate"].dtype
```

This is great, because it allows for many functionalities:

```{code-cell} ipython3
survey_data_decoupled.eventDate.dt #add a dot and press TAB to explore the date options it provides 
```

<div class="alert alert-success">

<b>EXERCISE</b>: Create a horizontal bar chart with the number of records for each year (cfr. supra), but without using the column `year`

</div>

```{code-cell} ipython3
:clear_cell: true

survey_data_decoupled.groupby(survey_data_decoupled["eventDate"].dt.year).size().plot(kind='barh', color="#00007f", figsize=(10, 10))
```

So, we actually do not need the `day`, `month`, `year` columns anymore and have other options available as well

+++

<div class="alert alert-success">
    <b>EXERCISE</b>: Create a bar chart with the number of records for each weekday
</div>

```{code-cell} ipython3
:clear_cell: true

nrecords_by_weekday = survey_data_decoupled.groupby(survey_data_decoupled["eventDate"].dt.weekday).size()
ax = nrecords_by_weekday.plot(kind="barh", color="#00007f", figsize=(6, 6))
# I you want to represent the ticklabels as proper names, uncomment the following line:
#ticklabels = ax.set_yticklabels(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
```

When saving the information to a file (e.g. CSV-file), this data type will be automatically converted to a string representation. However, we could also decide to explicitly provide the string format the dates are stored (losing the date type functionalities), in order to have full control on the way these dates are formatted:

```{code-cell} ipython3
survey_data_decoupled["eventDate"] = survey_data_decoupled["eventDate"].dt.strftime('%Y-%m-%d')
```

```{code-cell} ipython3
survey_data_decoupled["eventDate"].head()
```

As we do not need the `day`, `month`, `year` columns anymore, we can drop them from the DataFrame:

+++

<div class="alert alert-success">

<b>EXERCISE</b>: Remove the columns day, month and year from the `survey_data_decoupled` DataFrame:
    
__Tip__: Remember the `drop` method?

</div>

```{code-cell} ipython3
:clear_cell: true

survey_data_decoupled = survey_data_decoupled.drop(columns=["day", "month", "year"])
```

## Add coordinates from the plot locations

+++

### Loading the coordinate data

+++

The individual plots are only identified by a `plot` identification number. In order to provide sufficient information to external users, additional information about the coordinates should be added. The coordinates of the individual plots are saved in another file: `plot_location.xlsx`. We will use this information to further enrich our dataset and add the Darwin Core Terms `decimalLongitude` and `decimalLatitude`.

+++

<div class="alert alert-success">
    
<b>EXERCISE</b>: Read in the excel file 'plot_location.xlsx' and store the data as the variable `plot_data`, with 3 columns: plot, xutm, yutm.

</div>

```{code-cell} ipython3
:clear_cell: true

plot_data = pd.read_excel("../data/plot_location.xlsx", skiprows=3, index_col=0)
```

```{code-cell} ipython3
plot_data.head()
```

### Transforming to other coordinate reference system

+++

These coordinates are in meters, more specifically in [UTM 12 N](https://en.wikipedia.org/wiki/Universal_Transverse_Mercator_coordinate_system) coordinate system. However, the agreed coordinate system for Darwin Core is the [World Geodetic System 1984 (WGS84)](http://spatialreference.org/ref/epsg/wgs-84/). 

As this is not a GIS course, we will shortcut the discussion about different projection systems, but provide an example on how such a conversion from UTM12N to WGS84 can be performed with the projection toolkit `pyproj` and by relying on the existing EPSG codes (a registry originally setup by the association of oil & gas producers).

+++

First, we define out two projection systems, using their corresponding EPSG codes:

```{code-cell} ipython3
import pyproj
```

```{code-cell} ipython3
utm12n = pyproj.Proj("+init=EPSG:32612")
wgs84 = pyproj.Proj("+init=EPSG:4326")
```

The reprojection can be done by the function `transform` of the projection toolkit, providing the coordinate systems and a set of x, y coordinates. For example, for a single coordinate, this can be applied as follows:

```{code-cell} ipython3
pyproj.transform(utm12n, wgs84, 681222.131658, 3.535262e+06)
```

Instead of writing a `for` loop to do this for each of the coordinates in the list, we can <code>apply</code> this function to each of them:

+++

<div class="alert alert-success">
    <b>EXERCISE</b>: Apply the pyproj function <code>transform</code> to plot_data, using the columns <code>xutm</code> and <code>yutm</code> and save the resulting output in 2 new columns, called <code>decimalLongitude</code> and <code>decimalLatitude</code>:
    
<ul>
  <li>Create a function <code>transform_utm_to_wgs</code> that takes a row of a DataFrame and returns a Series of two elements with the longitude and latitude.</li>
  <li>Test this function on the first row of <code>plot_data</code> </li>
  <li>Now <b>apply</b> this function on all rows (remember the <code>axis</code> parameter)</li>
  <li>Assign the result of the previous step to <code>decimalLongitude</code> and <code>decimalLatitude</code> columns</li>
</ul> 
    
</div>

```{code-cell} ipython3
:clear_cell: true

def transform_utm_to_wgs(row):
    """
    Converts the x and y coordinates of this row into a Series of the
    longitude and latitude.
    
    """
    utm12n = pyproj.Proj("+init=EPSG:32612")
    wgs84 = pyproj.Proj("+init=EPSG:4326")
    
    return pd.Series(pyproj.transform(utm12n, wgs84, row['xutm'], row['yutm']))
```

```{code-cell} ipython3
:clear_cell: true

transform_utm_to_wgs(plot_data.loc[0])
```

```{code-cell} ipython3
:clear_cell: true

plot_data.apply(transform_utm_to_wgs, axis=1)
```

```{code-cell} ipython3
:clear_cell: true

plot_data[["decimalLongitude" ,"decimalLatitude"]] = plot_data.apply(transform_utm_to_wgs, axis=1)
```

```{code-cell} ipython3
plot_data.head()
```

The above function `transform_utm_to_wgs` you have created is a very specific function that knows the structure of the DataFrame you will apply it to (it assumes the 'xutm' and 'yutm' column names). We could also make a more generic function that just takes a X and Y coordinate and returns the Series of converted coordinates (`transform_utm_to_wgs2(X, Y)`).  

To apply such a more generic function to the `plot_data` DataFrame, we can make use of the `lambda` construct, which lets you specify a function on one line as an argument:
    
    plot_data.apply(lambda row : transform_utm_to_wgs2(row['xutm'], row['yutm']), axis=1)

If you have time, try to implement this function and test it as well.

+++

### (intermezzo) Checking the coordinates on a map 

+++

To check the transformation, let's put these on an interactive map. [Leaflet](http://leafletjs.com/) is a famous service for this and in many programming languages wrappers do exist to simplify the usage. [Folium](https://github.com/python-visualization/folium) is an extensive library providing multiple options. As we just want to do a quick checkup of the coordinates, we will rely on the package [mplleaflet](https://github.com/jwass/mplleaflet), which just converts a matplotlib image to a leaflet map:

```{code-cell} ipython3
import mplleaflet  # https://github.com/jwass/mplleaflet
```

```{code-cell} ipython3
fig, ax = plt.subplots(figsize=(5, 8))
plt.plot(plot_data['decimalLongitude'], plot_data['decimalLatitude'], 'rs')

mplleaflet.display(fig=fig) # zoom out to see where the measurement plot is located
```

### Join the coordinate information to the survey data set

+++

All points are inside the desert region as we expected, so we can extend our survey dataset with this coordinate information. Making the combination of two data sets based on a common identifier is completely similar to the usage of `JOIN` operations in databases. In Pandas, this functionality is provided by [`pd.merge`](http://pandas.pydata.org/pandas-docs/stable/merging.html#database-style-DataFrame-joining-merging). 

In practice, we have to add the columns `decimalLongitude`/`decimalLatitude` to the current dataset `survey_data_decoupled`, by using the plot identification number as key to join. 

+++

<div class="alert alert-success">
    <b>EXERCISE</b>: Extract only the columns to join to our survey dataset: the plot identifiers, decimalLatitude and decimalLongitude into a new variable named <code>plot_data_selection</code>
</div>

```{code-cell} ipython3
:clear_cell: true

plot_data_selection = plot_data[["plot", "decimalLongitude", "decimalLatitude"]]
```

<div class="alert alert-success">
    
<b>EXERCISE</b>: Based on the documentation of Pandas <code>merge</code>, add the coordinate information (plot_data_selection) to the survey data set and save the resulting DataFrame as <code>survey_data_plots</code>.
    
__Tip__: documentation of [merge](http://pandas.pydata.org/pandas-docs/stable/merging.html#database-style-DataFrame-joining-merging)...

</div>

```{code-cell} ipython3
:clear_cell: true

survey_data_plots = pd.merge(survey_data_decoupled, plot_data_selection, 
                             how="left", on="plot")
```

```{code-cell} ipython3
survey_data_plots.head()
```

The plot locations need to be stored with the variable name `verbatimLocality` indicating th identifier as integer value of the plot:

```{code-cell} ipython3
survey_data_plots = survey_data_plots.rename(columns={'plot': 'verbatimLocality'})
```

## Add species names to dataset

+++

The column `species` only provides a short identifier in the survey overview. The name information is stored in a separate file `species.csv`. As we want our dataset to include this information, we will read in this data and add it to our survey dataset:

+++

<div class="alert alert-success">

<b>EXERCISE</b>: Read in the 'species.csv' file and save the resulting DataFrame as variable <code>species_data</code>

__Tip__: check the delimiter (`sep`) to define
    
</div>

```{code-cell} ipython3
:clear_cell: true

species_data = pd.read_csv("../data/species.csv", sep=";")
```

```{code-cell} ipython3
species_data.head()
```

### Fix a wrong acronym naming

+++

When reviewing the metadata, you see that in the data-file the acronym `NE` is used to describe `Neotoma albigula`, whereas in the [metadata description](http://esapubs.org/archive/ecol/E090/118/Portal_rodent_metadata.htm), the acronym `NA` is used. 

+++

<div class="alert alert-success">
    <b>EXERCISE</b>: Convert the value of 'NE' to 'NA' by using boolean indexing for the `species_id` column
</div>

```{code-cell} ipython3
:clear_cell: true

species_data.loc[species_data["species_id"] == "NE", "species_id"] = "NA"
```

(At the same time, you decide to cure this problem at the source and alert the data provider about this issue.)

+++

### Merging surveys and species

+++

As we now prepared the two series, we can combine the data, using the `merge` operation. Take into account that our key-column is different for `species_data` and `survey_data_plots`, respectively `species_id` and `species`:

+++

We want to add the data of the species to the survey data, in order to see the full species names:

+++

<div class="alert alert-success">

<b>EXERCISE</b>: Merge the `survey_data_plots` data set with the `species_data` information in order to pass the species information to the survey data:

</div>

```{code-cell} ipython3
:clear_cell: true

survey_data_species = pd.merge(survey_data_plots, species_data, how="left",  # LEFT OR INNER?
                                left_on="species", right_on="species_id")
```

```{code-cell} ipython3
len(survey_data_species)
```

The join is ok, but we are left with some redundant columns and wrong naming:

```{code-cell} ipython3
 survey_data_species.head()
```

We do not need the columns `species_x` and `species_id` column anymore, as we will use the scientific names from now on:

```{code-cell} ipython3
survey_data_species = survey_data_species.drop(["species_x", "species_id"], axis=1)
```

The column `species_y` could just be named `species`:

```{code-cell} ipython3
survey_data_species = survey_data_species.rename(columns={"species_y": "species"})
```

```{code-cell} ipython3
survey_data_species.head()
```

```{code-cell} ipython3
len(survey_data_species)
```

Let's now save our cleaned-up to a csv file, so we can further analyze the data in a following notebook:

```{code-cell} ipython3
survey_data_species.to_csv("interim_survey_data_species.csv", index=False)
```

## (OPTIONAL SECTION) Using a API service to match the scientific names

+++

As the current species names are rather short and could eventually lead to confusion when shared with other users, retrieving additional information about the different species in our dataset would be useful to integrate our work with other research. An option is to match our names with an external service to request additional information about the different species.

One of these services is [GBIF API](http://www.gbif.org/developer/species). The service can most easily be illustrated with a small example:<br><br>
In a new tabblad of the browser, go to the URL [http://www.gbif.org/species/2475532](http://www.gbif.org/species/2475532), which corresponds to the page of `Alcedo atthis` (*ijsvogel* in dutch). One could for each of the species in the list we have do a search on the website of GBIF to find the corresponding page of the different species, from which more information can be extracted manually. However, this would take a lot of time...

Therefore, GBIF (and many other organisations!) provides a service to extract the same information on a machine-readable way, in order to automate these searches. As an example, let's search for the information of `Alcedo atthis`, using the GBIF API: Go to the URL: [http://api.gbif.org/v1/species/match?name=Alcedo atthis](http://api.gbif.org/v1/species/match?name=%22Alcedo%20atthis%22) and check the output. What we did is a machine-based search on the GBIF website for information about `Alcedo atthis`.

The same can be done using Python. The main library we need to this kind of automated searches is the [`requests` package](http://docs.python-requests.org/en/master/), which can be used to do request to any kind of API out there.

```{code-cell} ipython3
import requests
```

### Example matching with Alcedo Atthis

+++

For the example of `Alcedo atthis`:

```{code-cell} ipython3
species_name = 'Alcedo atthis'
```

```{code-cell} ipython3
base_string = 'http://api.gbif.org/v1/species/match?'
request_parameters = {'verbose': False, 'strict': True, 'name': species_name}
message = requests.get(base_string, params=request_parameters).json()
message
```

From which we get a dictionary containing more information about the taxonomy of the `Alcedo atthis`.

+++

In the species data set available, the name to match is provided in the combination of two columns, so we have to combine those to in order to execute the name matching:

```{code-cell} ipython3
genus_name = "Callipepla"
species_name = "squamata"
name_to_match = '{} {}'.format(genus_name, species_name)
base_string = 'http://api.gbif.org/v1/species/match?'
request_parameters = {'strict': True, 'name': name_to_match} # use strict matching(!)
message = requests.get(base_string, params=request_parameters).json()
message
```

To apply this on our species data set, we will have to do this request for each of the individual species/genus combination. As, this is a returning functionality, we will write a small function to do this:

+++

### Writing a custom matching function

+++

<div class="alert alert-success">
    
<b>EXERCISE</b>: Write a function, called `name_match` that takes the `genus`, the `species` and the option to perform a strict matching or not as inputs, performs a matching with the GBIF name matching API and return the received message as a dictionary.

</div>

```{code-cell} ipython3
:clear_cell: true

def name_match(genus_name, species_name, strict=True):
    """
    Perform a GBIF name matching using the species and genus names
    
    Parameters
    ----------
    genus_name: str
        name of the genus of the species
    species_name: str
        name of the species to request more information
    strict: boolean
        define if the mathing need to be performed with the strict 
        option (True) or not (False)
    
    Returns
    -------
    message: dict
        dictionary with the information returned by the GBIF matching service
    """
    name = '{} {}'.format(genus_name, species_name)
    base_string = 'http://api.gbif.org/v1/species/match?'
    request_parameters = {'strict': strict, 'name': name} # use strict matching(!)
    message = requests.get(base_string, params=request_parameters).json()
    return message
```

<div class="alert alert-danger">
    
<b>NOTE</b>: For many of these API request handling, dedicated packages do exist, e.g. <a href="https://github.com/sckott/pygbif">pygbif</a> provides different functions to do requests to the GBIF API, basically wrapping the request possibilities. For any kind of service, just ask yourself: is the dedicated library providing sufficient additional advantage, or can I easily setup the request myself. (or sometimes: for which the documentation is the best...)<br><br>Many services do exist for a wide range of applications, e.g. scientific name matching, matching of addresses, downloading of data,...
    
</div>

+++

Testing our custom matching function:

```{code-cell} ipython3
genus_name = "Callipepla"
species_name = "squamata"
name_match(genus_name, species_name, strict=True)
```

However, the matching won't provide an answer for every search:

```{code-cell} ipython3
genus_name = "Lizard"
species_name = "sp."
name_match(genus_name, species_name, strict=True)
```

### Match each of the species names of the survey data set

+++

Hence, in order to add this information to our survey DataFrame, we need to perform the following steps:
1. extract the unique genus/species combinations in our dataset and combine them in single column
2. match each of these names to the GBIF API service
3. process the returned message:
    * if a match is found, add the information of the columns 'class', 'kingdom', 'order', 'phylum', 'scientificName', 'status' and 'usageKey'
    * if no match was found: nan-values
4. Join the DataFrame of unique genus/species information with the enriched GBIF info to the `survey_data_species` data set

+++

<div class="alert alert-success">
    <b>EXERCISE</b>: Extract the unique combinations of genus and species in the `survey_data_species` using the function <code>drop_duplicates()</code>. Save the result as the variable <code>unique_species</code>
</div>

```{code-cell} ipython3
:clear_cell: true

#%%timeit
unique_species = survey_data_species[["genus", "species"]].drop_duplicates().dropna()
```

```{code-cell} ipython3
len(unique_species)
```

<div class="alert alert-success">
    
<b>EXERCISE</b>: Extract the unique combinations of genus and species in the `survey_data_species` using <code>groupby</code>. Save the result as the variable <code>unique_species</code>

</div>

```{code-cell} ipython3
:clear_cell: true

#%%timeit
unique_species = \
    survey_data_species.groupby(["genus", "species"]).first().reset_index()[["genus", "species"]]
```

```{code-cell} ipython3
len(unique_species)
```

<div class="alert alert-success">
    <b>EXERCISE</b>: Combine the columns genus and species to a single column with the complete name, save it in a new column named 'name'
</div>

```{code-cell} ipython3
:clear_cell: true

unique_species["name"] = unique_species["genus"] + " " + unique_species["species"] 
# an alternative approach worthwhile to know:
#unique_species["name"] = unique_species["genus"].str.cat(unique_species["species"], " ")
```

```{code-cell} ipython3
unique_species.head()
```

To perform the matching for each of the combination, different options do exist. 

Just to show the possibility of using `for` loops, the addition of the matched information will be done as such. First, we will store everything in one dictionary, where the keys of the dictionary are the index values of `unique_species` (in order to later merge them again) and the values are the entire messages (which are dictionaries aon itself). The format will look as following: 

```
species_annotated = {O: {'canonicalName': 'Squamata', 'class': 'Reptilia', 'classKey': 358, ...}, 
                     1: {'canonicalName':...},
                     2:...}
```

```{code-cell} ipython3
species_annotated = {}
for key, row in unique_species.iterrows():
    species_annotated[key] = name_match(row["genus"], row["species"], strict=True)
```

```{code-cell} ipython3
 species_annotated
```

We can now transform this to a pandas DataFrame:

+++

<div class="alert alert-success">

<b>EXERCISE</b>: Convert the dictionary <code>species_annotated</code> into a pandas DataFrame with the row index the key-values corresponding to <code>unique_species</code> and the column headers the output columns of the API response. Save the result as the variable <code>df_species_annotated</code>.
    
__Tip__: `transpose` can be used to flip rows and columns
    
</div>

```{code-cell} ipython3
:clear_cell: true

df_species_annotated = pd.DataFrame(species_annotated).transpose()
```

```{code-cell} ipython3
df_species_annotated.head()
```

### Select relevant information and add this to the survey data

+++

<div class="alert alert-success">
    
<b>EXERCISE</b>: Subselect the columns 'class', 'kingdom', 'order', 'phylum', 'scientificName', 'status' and  'usageKey' from the DataFrame `df_species_annotated`. Save it as the variable <code>df_species_annotated_subset</code>

</div>

```{code-cell} ipython3
:clear_cell: true

df_species_annotated_subset = df_species_annotated[['class', 'kingdom', 'order', 'phylum', 
                                                    'scientificName', 'status', 'usageKey']]
```

```{code-cell} ipython3
df_species_annotated_subset.head()
```

<div class="alert alert-success">
    <b>EXERCISE</b>: Join the df_species_annotated_subset information to the `unique_species` overview of species. Save the result as variable <code>unique_species_annotated</code>:
</div>

```{code-cell} ipython3
:clear_cell: true

unique_species_annotated = pd.merge(unique_species, df_species_annotated_subset, 
                                    left_index=True, right_index=True)
```

<div class="alert alert-success">
    
<b>EXERCISE</b>: Add the `unique_species_annotated` data to the `survey_data_species` data set, using both the genus and species column as keys. Save the result as the variable <code>survey_data_completed</code>.
 
</div>

```{code-cell} ipython3
:clear_cell: true

survey_data_completed = pd.merge(survey_data_species, unique_species_annotated, 
                                 how='left', on= ["genus", "species"])
```

```{code-cell} ipython3
len(survey_data_completed)
```

```{code-cell} ipython3
survey_data_completed.head()
```

Congratulations! You did a great cleaning job, save your result:

```{code-cell} ipython3
survey_data_completed.to_csv("../data/survey_data_completed.csv", index=False)
```

## Acknowledgements

+++

* `species.csv` and `survey.csv` are used from the [data carpentry workshop](https://github.com/datacarpentry/python-ecology-lesson) This data is from the paper S. K. Morgan Ernest, Thomas J. Valone, and James H.
Brown. 2009. Long-term monitoring and experimental manipulation of a Chihuahuan Desert ecosystem near Portal, Arizona, USA. Ecology 90:1708. http://esapubs.org/archive/ecol/E090/118/
* The `plot_location.xlsx` is a dummy created location file purely created for this exercise, using the plots location on google maps
* [GBIF API](http://www.gbif.org/developer/summary)
