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

<p><font size="6"><b> CASE - Biodiversity data - analysis</b></font></p>


> *DS Data manipulation, analysis and visualisation in Python*  
> *December, 2019*

> *© 2016, Joris Van den Bossche and Stijn Van Hoey  (<mailto:jorisvandenbossche@gmail.com>, <mailto:stijnvanhoey@gmail.com>). Licensed under [CC BY 4.0 Creative Commons](http://creativecommons.org/licenses/by/4.0/)*

---

```{code-cell} ipython3
%matplotlib inline

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn-whitegrid')
```

## Reading in the enriched survey data set

+++

<div class="alert alert-success">
    <b>EXERCISE</b>:

<ul>
  <li>Read in the 'survey_data_completed.csv' file and save the resulting DataFrame as variable <code>survey_data_processed</code> (if you did not complete the previous notebook, a version of the csv file is available in the `../data` folder).</li>
  <li>Interpret the 'eventDate' column directly as python datetime object and make sure the 'occurrenceID' column is used as the index of the resulting DataFrame (both can be done at once when reading the csv file using parameters of the `read_csv` function)</li>
  <li>Inspect the resulting frame (remember `.head()` and `.info()`) and check that the 'eventDate' indeed has a datetime data type.</li>
</ul> 
    
</div>

```{code-cell} ipython3
:clear_cell: true

survey_data_processed = pd.read_csv("../data/survey_data_completed.csv", 
                                    parse_dates=['eventDate'], index_col="occurrenceID")
```

```{code-cell} ipython3
:clear_cell: true

survey_data_processed.head()
```

```{code-cell} ipython3
:clear_cell: true

survey_data_processed.info()
```

## Tackle missing values (NaN) and duplicate values

+++

<div class="alert alert-success">
    <b>EXERCISE</b>: How many records are in the data set without information on the 'species' name?
</div>

```{code-cell} ipython3
:clear_cell: true

survey_data_processed['species'].isnull().sum()
```

<div class="alert alert-success">
    <b>EXERCISE</b>: How many duplicate records are present in the dataset?

_Tip_: Pandas has a function to find `duplicated` values... 
</div>

```{code-cell} ipython3
:clear_cell: true

survey_data_processed.duplicated().sum()
```

<div class="alert alert-success">
    <b>EXERCISE</b>: Extract a list of all duplicates, sort on the columns `eventDate` and `verbatimLocality` and show the first 10 records
    
_Tip_: Check documentation of `duplicated`
</div>

```{code-cell} ipython3
:clear_cell: true

survey_data_processed[survey_data_processed.duplicated(keep=False)].sort_values(["eventDate", "verbatimLocality"]).head(10)
```

<div class="alert alert-success">
    
<b>EXERCISE</b>: Exclude the duplicate values from the survey data set and save the result as <code>survey_data_unique</code>
    
__Tip__: Next to finding `duplicated` values, Pandas has a function to `drop duplicates`...
    
</div>

```{code-cell} ipython3
:clear_cell: true

survey_data_unique = survey_data_processed.drop_duplicates()
```

```{code-cell} ipython3
len(survey_data_unique)
```

<div class="alert alert-success">

<b>EXERCISE</b>: For how many records (rows) we have all the information available (i.e. no NaN values in any of the columns)?

__Tip__: Just counting the nan (null) values won't work, maybe `dropna` can help you?
    
</div>

```{code-cell} ipython3
:clear_cell: true

len(survey_data_unique.dropna())
```

<div class="alert alert-success">
    
<b>EXERCISE</b>: Select the subset of records without a species name, while having information on the sex and store the result as variable <code>not_identified</code>
    
__Tip__: next to `isnull`, also `notnull` exists...

</div>

```{code-cell} ipython3
:clear_cell: true

mask = survey_data_unique['species'].isnull() & survey_data_unique['sex'].notnull()
not_identified = survey_data_unique[mask]
```

```{code-cell} ipython3
not_identified.head()
```

<div class="alert alert-success">
    <b>EXERCISE</b>: Select only those records that do have species information and save them as the variable <code>survey_data</code>. Make sure <code>survey_data</code> is a copy of the original DataFrame. This is the DataFrame we will use in the further analyses.
</div>

```{code-cell} ipython3
:clear_cell: true

survey_data = survey_data_unique.dropna(subset=['species']).copy()
```

<div class="alert alert-danger">
    <b>NOTE</b>: For biodiversity studies, absence values (knowing that someting is not present) are useful as well to normalize the observations, but this is out of scope for these exercises.
</div>

+++

## Observations over time

+++

<div class="alert alert-success">
    
<b>EXERCISE</b>: Make a plot visualizing the evolution of the number of observations for each of the individual years (i.e. annual counts).

__Tip__: In the `pandas_04_time_series_data.ipynb` notebook, a powerful command to resample a time series
    
</div>

```{code-cell} ipython3
:clear_cell: true

survey_data.resample('A', on='eventDate').size().plot()
```

To evaluate the intensity or number of occurrences during different time spans, a heatmap is an interesting representation. We can actually use the plotnine library as well to make heatmaps, as it provides the [`geom_tile`](http://plotnine.readthedocs.io/en/stable/generated/plotnine.geoms.geom_tile.html) geometry. Loading the library:

```{code-cell} ipython3
import plotnine as pn
```

<div class="alert alert-success">
    
<b>EXERCISE</b>: Create a table, called <code>heatmap_prep_plotnine</code>, based on the <code>survey_data</code> DataFrame with a column for the years, a column for the months a column with the counts (called `count`).

__Tip__: You have to count for each year/month combination. Also `reset_index` could be useful.
    
</div>

```{code-cell} ipython3
:clear_cell: true

heatmap_prep_plotnine = survey_data.groupby([survey_data['eventDate'].dt.year, 
                                             survey_data['eventDate'].dt.month]).size()
heatmap_prep_plotnine.index.names = ["year", "month"]
heatmap_prep_plotnine = heatmap_prep_plotnine.reset_index(name='count')
```

```{code-cell} ipython3
:clear_cell: true

heatmap_prep_plotnine.head()
```

<div class="alert alert-success">
    
<b>EXERCISE</b>: Based on <code>heatmap_prep_plotnine</code>, make a heatmap using the plotnine package. 


__Tip__: When in trouble, check [this section of the documentation](http://plotnine.readthedocs.io/en/stable/generated/plotnine.geoms.geom_tile.html#Annotated-Heatmap)
    
</div>

```{code-cell} ipython3
:clear_cell: true

(pn.ggplot(heatmap_prep_plotnine, pn.aes(x="factor(month)", y="year", fill="count"))
    + pn.geom_tile()
    + pn.scale_fill_cmap("Reds")
    + pn.scale_y_reverse()
    + pn.theme( 
     axis_ticks=pn.element_blank(),
     panel_background=pn.element_rect(fill='white'))
)  
```

Remark that we started from a `tidy` data format (also called *long* format). 

The heatmap functionality is also provided by the plotting library [seaborn](http://seaborn.pydata.org/generated/seaborn.heatmap.html) (check the docs!). Based on the documentation, seaborn uses the *short* format with in the row index the years, in the column the months and the counts for each of these year/month combinations as values.

Let's reformat the `heatmap_prep_plotnine` data to be useable for the seaborn heatmap function:

+++

<div class="alert alert-success">
    
<b>EXERCISE</b>: Create a table, called <code>heatmap_prep_sns</code>, based on the <code>heatmap_prep_plotnine</code> DataFrame with in the row index the years, in the column the months and as values of the table, the counts for each of these year/month combinations.
    
__Tip__: The `pandas_07_reshaping_data.ipynb` notebook provides all you need to know
    
</div>

```{code-cell} ipython3
:clear_cell: true

heatmap_prep_sns = heatmap_prep_plotnine.pivot_table(index='year', columns='month', values='count')
```

<div class="alert alert-success">
    <b>EXERCISE</b>: Using the seaborn <a href="http://seaborn.pydata.org/generated/seaborn.heatmap.html">documentation</a> make a heatmap starting from the <code>heatmap_prep_sns</code> variable.
</div>

```{code-cell} ipython3
:clear_cell: true

fig, ax = plt.subplots(figsize=(10, 8))
ax = sns.heatmap(heatmap_prep_sns, cmap='Reds')
```

<div class="alert alert-success">
    
<b>EXERCISE</b>: Based on the <code>heatmap_prep_sns</code> DataFrame, return to the <i>long</i> format of the table with the columns `year`, `month` and `count` and call the resulting variable <code>heatmap_tidy</code>.
    
__Tip__: The `pandas_07_reshaping_data.ipynb` notebook provides all you need to know, but a `reset_index` could be useful as well
    
</div>

```{code-cell} ipython3
:clear_cell: true

heatmap_tidy = heatmap_prep_sns.reset_index().melt(id_vars=["year"], value_name="count")
heatmap_tidy.head()
```

## Species abundance for each of the plots

+++

The name of the observed species consists of two parts: the 'genus' and 'species' columns. For the further analyses, we want the combined name. This is already available as the 'name' column if you completed the previous notebook, otherwise you can add this again in the following exercise.

+++

<div class="alert alert-success">
    
<b>EXERCISE</b>: Make a new column 'name' that combines the 'Genus' and 'species' columns (with a space in between).
    
__Tip__: You are aware you can count with strings in Python 'a' + 'b' = 'ab'?   
    
</div>

```{code-cell} ipython3
:clear_cell: true

survey_data['name'] = survey_data['genus'] + ' ' + survey_data['species']
```

<div class="alert alert-success">

<b>EXERCISE</b>: Which 8 species have been observed most of all?
    
__Tip__: Pandas provide a function to combine sorting and showing the first n records, see [here](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.nlargest.html)...
    
</div>

```{code-cell} ipython3
:clear_cell: true

survey_data.groupby("name").size().nlargest(8)
```

```{code-cell} ipython3
:clear_cell: true

survey_data['name'].value_counts()[:8]
```

<div class="alert alert-success">
    <b>EXERCISE</b>: How many records are available of each of the species in each of the plots (called `verbatimLocality`)? How would you visualize this information with seaborn?
</div>

```{code-cell} ipython3
:clear_cell: true

species_per_plot = survey_data.reset_index().pivot_table(index="name", 
                                                         columns="verbatimLocality", 
                                                         values="occurrenceID", 
                                                         aggfunc='count')

# alternative ways to calculate this
#species_per_plot =  survey_data.groupby(['name', 'plot_id']).size().unstack(level=-1)
#species_per_plot = pd.crosstab(survey_data['name'], survey_data['plot_id'])
```

```{code-cell} ipython3
:clear_cell: true

fig, ax = plt.subplots(figsize=(8,8))
sns.heatmap(species_per_plot, ax=ax, cmap='Reds')
```

<div class="alert alert-success">
    
<b>EXERCISE</b>: What is the number of different species in each of the plots? Make a bar chart, using Pandas `plot` function, providing for each plot the diversity of species, by defining a matplotlib figure and ax to make the plot. Change the y-label to 'plot number'

__Tip__: next to `unique`, Pandas also provides a function `nunique`...
    
</div>

```{code-cell} ipython3
:clear_cell: true

n_species_per_plot = survey_data.groupby(["verbatimLocality"])["name"].nunique()

fig, ax = plt.subplots(figsize=(6, 6))
n_species_per_plot.plot(kind="barh", ax=ax, color="lightblue")
ax.set_ylabel("plot number")

# Alternative option:
# inspired on the pivot table we already had:
# species_per_plot = survey_data.reset_index().pivot_table(
#     index="name", columns="verbatimLocality", values="occurrenceID", aggfunc='count')
# n_species_per_plot = species_per_plot.count()
```

<div class="alert alert-success">

<b>EXERCISE</b>: What is the number of plots each species have been observed? Make an horizontal bar chart using Pandas `plot` function providing for each species the spread amongst the plots for which the species names are sorted to the number of plots

</div>

```{code-cell} ipython3
:clear_cell: true

n_plots_per_species = survey_data.groupby(["name"])["verbatimLocality"].nunique().sort_values()

fig, ax = plt.subplots(figsize=(8, 8))
n_plots_per_species.plot(kind="barh", ax=ax, color='0.4')

# Alternatives
# species_per_plot2 = survey_data.reset_index().pivot_table(index="verbatimLocality",
#                                                           columns="name",
#                                                           values="occurrenceID",
#                                                           aggfunc='count')
# nplots_per_species = species_per_plot2.count().sort_values(ascending=False)
# or
# species_per_plot.count(axis=1).sort_values(ascending=False).plot(kind='bar')
```

<div class="alert alert-success">

<b>EXERCISE</b>: First, exclude the NaN-values from the `sex` column and save the result as a new variable called `subselection_sex`. Based on this variable `subselection_sex`, calculate the amount of males and females present in each of the plots. Save the result (with the verbatimLocality as index and sex as column names) as a variable <code>n_plot_sex</code>.
    
__Tip__: Release the power of `unstack`...  
    
</div>

```{code-cell} ipython3
:clear_cell: true

subselection_sex = survey_data.dropna(subset=["sex"])
#subselection_sex = survey_data[survey_data["sex"].notnull()]
```

```{code-cell} ipython3
:clear_cell: true

n_plot_sex = subselection_sex.groupby(["sex", "verbatimLocality"]).size().unstack(level=0)
n_plot_sex.head()
```

As such, we can use the variable `n_plot_sex` to plot the result:

```{code-cell} ipython3
:clear_cell: false

n_plot_sex.plot(kind='bar', figsize=(12, 6), rot=0)
```

<div class="alert alert-success">

<b>EXERCISE</b>: Create the previous plot with the plotnine library, directly from the variable <code>subselection_sex</code>. 
    
__Tip__: When in trouble, check these [docs](http://plotnine.readthedocs.io/en/stable/generated/plotnine.geoms.geom_col.html#Two-Variable-Bar-Plot).

</div>

```{code-cell} ipython3
:clear_cell: true

(pn.ggplot(subselection_sex, pn.aes(x="verbatimLocality", fill="sex"))
     + pn.geom_bar(position='dodge')
     + pn.scale_x_discrete(breaks=np.arange(1, 25, 1), limits=np.arange(1, 25, 1))
)
```

## Select subsets according to taxa of species

```{code-cell} ipython3
survey_data["taxa"].unique()
```

```{code-cell} ipython3
survey_data['taxa'].value_counts()
#survey_data.groupby('taxa').size()
```

<div class="alert alert-success">

<b>EXERCISE</b>: Select the records for which the `taxa` is equal to 'Rabbit', 'Bird' or 'Reptile'. Call the resulting variable `non_rodent_species`.
    
__Tip__: You do not have to combine three different conditions, as Pandas has a function to check if something is in a certain list of values    
    
</div>

```{code-cell} ipython3
:clear_cell: true

non_rodent_species = survey_data[survey_data['taxa'].isin(['Rabbit', 'Bird', 'Reptile'])]
```

```{code-cell} ipython3
len(non_rodent_species)
```

<div class="alert alert-success">

<b>EXERCISE</b>: Select the records for which the `taxa` starts with an 'ro' (make sure it does not matter if a capital character is used in the 'taxa' name). Call the resulting variable <code>r_species</code>.

__Tip__: Remember the `.str.` construction to provide all kind of string functionalities?

</div>

```{code-cell} ipython3
:clear_cell: true

r_species = survey_data[survey_data['taxa'].str.lower().str.startswith('ro')]
```

```{code-cell} ipython3
len(r_species)
```

<div class="alert alert-success">
    <b>EXERCISE</b>: Select the records that are not Birds. Call the resulting variable <code>non_bird_species</code>.
</div>

```{code-cell} ipython3
:clear_cell: true

non_bird_species = survey_data[survey_data['taxa'] != 'Bird']
```

```{code-cell} ipython3
len(non_bird_species)
```

## (OPTIONAL SECTION) Evolution of species during monitoring period

+++

*In this section, all plots can be made with the embedded Pandas plot function, unless specificly asked*

+++

<div class="alert alert-success">
    <b>EXERCISE</b>: Plot using Pandas `plot` function the number of records for `Dipodomys merriami` on yearly basis during time
</div>

```{code-cell} ipython3
:clear_cell: true

merriami = survey_data[survey_data["name"] == "Dipodomys merriami"]
```

```{code-cell} ipython3
:clear_cell: true

fig, ax = plt.subplots()
merriami.groupby(merriami['eventDate'].dt.year).size().plot(ax=ax)
ax.set_xlabel("")
ax.set_ylabel("number of occurrences")
```

<div class="alert alert-danger">
    <b>NOTE</b>: Check the difference between the following two graphs? What is different? Which one would you use?
</div>

```{code-cell} ipython3
merriami = survey_data[survey_data["species"] == "merriami"]
fig, ax = plt.subplots(2, 1, figsize=(14, 8))
merriami.groupby(merriami['eventDate']).size().plot(ax=ax[0], style="-") # top graph
merriami.resample("D", on="eventDate").size().plot(ax=ax[1], style="-") # lower graph
```

<div class="alert alert-success">

<b>EXERCISE</b>: Plot, for the species 'Dipodomys merriami', 'Dipodomys ordii', 'Reithrodontomys megalotis' and 'Chaetodipus baileyi', the monthly number of records as a function of time for the whole monitoring period. Plot each of the individual species in a separate subplot and provide them all with the same y-axis scale
    
__Tip__: have a look at the documentation of the pandas plot function.
    
</div>

```{code-cell} ipython3
:clear_cell: true

subsetspecies = survey_data[survey_data["name"].isin(['Dipodomys merriami', 'Dipodomys ordii',
                                                      'Reithrodontomys megalotis', 'Chaetodipus baileyi'])]
```

```{code-cell} ipython3
:clear_cell: true

month_evolution = subsetspecies.groupby("name").resample('M', on='eventDate').size()
```

```{code-cell} ipython3
:clear_cell: true

species_evolution = month_evolution.unstack(level=0)
axs = species_evolution.plot(subplots=True, figsize=(14, 8), sharey=True)
```

<div class="alert alert-success">
    <b>EXERCISE</b>: Reproduce the previous plot using the plotnine package.
</div>

```{code-cell} ipython3
:clear_cell: true

subsetspecies = survey_data[survey_data["name"].isin(['Dipodomys merriami', 'Dipodomys ordii',
                                                      'Reithrodontomys megalotis', 'Chaetodipus baileyi'])]
month_evolution = subsetspecies.groupby("name").resample('M', on='eventDate').size()
```

```{code-cell} ipython3
:clear_cell: true

(pn.ggplot(month_evolution.reset_index(name='count'), 
           pn.aes(x='eventDate', y='count', color='name'))
    + pn.geom_line()
    + pn.facet_wrap('name', nrow=4)
    + pn.theme_light()
)
```

<div class="alert alert-success">
    <b>EXERCISE</b>: Evaluate the yearly amount of occurrences for each of the 'taxa' as a function of time.
</div>

```{code-cell} ipython3
:clear_cell: true

year_evolution = survey_data.groupby("taxa").resample('A', on='eventDate').size()
species_evolution = year_evolution.unstack(level=0)
axs = species_evolution.plot(subplots=True, figsize=(16, 8), sharey=False)
```

<div class="alert alert-success">
    <b>EXERCISE</b>: Calculate the number of occurrences for each weekday, grouped by each year of the monitoring campaign, without using the `pivot` functionality. Call the variable <code>count_weekday_years</code>
</div>

```{code-cell} ipython3
:clear_cell: true

count_weekday_years = survey_data.groupby([survey_data["eventDate"].dt.year, survey_data["eventDate"].dt.dayofweek]).size().unstack()
```

```{code-cell} ipython3
:clear_cell: true

# Alternative
#years = survey_data["eventDate"].dt.year.rename('year')
#dayofweaks = survey_data["eventDate"].dt.dayofweek.rename('dayofweak')
#count_weekday_years = pd.crosstab(index=years, columns=dayofweaks)
```

```{code-cell} ipython3
count_weekday_years.head()
```

```{code-cell} ipython3
count_weekday_years.plot()
```

<div class="alert alert-success">
    <b>EXERCISE</b>: Based on the variable `count_weekday_years`, calculate for each weekday the median amount of records based on the yearly count values. Modify the labels of the plot to indicate the actual days of the week (instead of numbers)
</div>

```{code-cell} ipython3
:clear_cell: true

fig, ax = plt.subplots()
count_weekday_years.median(axis=0).plot(kind='barh', ax=ax, color='#66b266')
xticks = ax.set_yticklabels(['Monday', 'Tuesday', 'Wednesday', "Thursday", "Friday", "Saturday", "Sunday"])
```

Nice work!
