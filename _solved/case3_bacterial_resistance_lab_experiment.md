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

<p><font size="6"><b>CASE - Bacterial resistance experiment</b></font></p>


> *DS Data manipulation, analysis and visualization in Python*  
> *May/June, 2021*
>
> *© 2021, Joris Van den Bossche and Stijn Van Hoey  (<mailto:jorisvandenbossche@gmail.com>, <mailto:stijnvanhoey@gmail.com>). Licensed under [CC BY 4.0 Creative Commons](http://creativecommons.org/licenses/by/4.0/)*

---

+++

In this case study, we will make use of the open data, affiliated to the following [journal article](http://rsbl.royalsocietypublishing.org/content/12/5/20160064):

>Arias-Sánchez FI, Hall A (2016) Effects of antibiotic resistance alleles on bacterial evolutionary responses to viral parasites. Biology Letters 12(5): 20160064. https://doi.org/10.1098/rsbl.2016.0064


+++

<img src="../img/bacteriophage.jpeg">

+++

Check the full paper on the [web version](http://rsbl.royalsocietypublishing.org/content/12/5/20160064). The study handles:
> Antibiotic resistance has wide-ranging effects on bacterial phenotypes and evolution. However, the influence of antibiotic resistance on bacterial responses to parasitic viruses remains unclear, despite the ubiquity of such viruses in nature and current interest in therapeutic applications. We experimentally investigated this by exposing various Escherichia coli genotypes, including eight antibiotic-resistant genotypes and a mutator, to different viruses (lytic bacteriophages). Across 960 populations, we measured changes in population density and sensitivity to viruses, and tested whether variation among bacterial genotypes was explained by their relative growth in the absence of parasites, or mutation rate towards phage resistance measured by fluctuation tests for each phage

```{code-cell} ipython3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
```

## Reading and processing the data

+++

The data is available on [Dryad](http://www.datadryad.org/resource/doi:10.5061/dryad.90qb7.3), a general purpose data repository providing all kinds of data sets linked to journal papers. The downloaded data is available in this repository in the `data` folder as an excel-file called `Dryad_Arias_Hall_v3.xlsx`.

For the exercises, two sheets of the excel file will be used: 
* `Main experiment`: 


| Variable name | Description |
|---------------:|:-------------|
|**AB_r** |	Antibiotic resistance |
|**Bacterial_genotype** | Bacterial genotype |
|**Phage_t** |	Phage treatment |
|**OD_0h** |	Optical density at the start of the experiment (0h) |
|**OD_20h**	| Optical density after 20h |
|**OD_72h**	| Optical density at the end of the experiment (72h) |
|**Survival_72h** |	Population survival at 72h (1=survived, 0=extinct) |
|**PhageR_72h**	| Bacterial sensitivity to the phage they were exposed to (0=no bacterial growth, 1= colony formation in the presence of phage) |

* `Falcor`: we focus on a subset of the columns:

| Variable name | Description |
|---------------:|:-------------|
| **Phage**  | Bacteriophage used in the fluctuation test (T4, T7 and lambda) |
| **Bacterial_genotype** | Bacterial genotype. |
| **log10 Mc** |	Log 10 of corrected mutation rate |
| **log10 UBc** |	Log 10 of corrected upper bound |
| **log10 LBc** |	Log 10 of corrected lower bound |

+++

Reading the `main experiment` data set from the corresponding sheet:

```{code-cell} ipython3
main_experiment = pd.read_excel("data/Dryad_Arias_Hall_v3.xlsx", 
                                sheet_name="Main experiment")
main_experiment
```

Read the `Falcor` data and subset the columns of interest:

```{code-cell} ipython3
falcor = pd.read_excel("data/Dryad_Arias_Hall_v3.xlsx", sheet_name="Falcor", 
                       skiprows=1)
falcor = falcor[["Phage", "Bacterial_genotype", "log10 Mc", "log10 UBc", "log10 LBc"]]
falcor.head()
```

## Tidy the `main_experiment` data

+++

*(If you're wondering what `tidy` data representations are, check again the `pandas_07_reshaping_data.ipynb` notebook)*

+++

Actually, the columns `OD_0h`, `OD_20h` and `OD_72h` are representing the same variable (i.e. `optical_density`) and the column names itself represent a variable, i.e. `experiment_time_h`. Hence, it is stored in the table as *short* format and we could *tidy* these columns by converting them to 2 columns: `experiment_time_h` and `optical_density`.

+++

Before making any changes to the data, we will add an identifier column for each of the current rows to make sure we keep the connection in between the entries of a row when converting from wide to long format.

```{code-cell} ipython3
main_experiment["experiment_ID"] = ["ID_" + str(idx) for idx in range(len(main_experiment))]
main_experiment
```

<div class="alert alert-success">

<b>EXERCISE</b>:

Convert the columns `OD_0h`, `OD_20h` and `OD_72h` to a long format with the values stored in a column `optical_density` and the time in the experiment as `experiment_time_h`. Save the variable as <code>tidy_experiment</code>

<details><summary>Hints</summary>

- Have a look at `pandas_07_reshaping_data.ipynb` to find out the required function.
- Remember to check the documentation of a function using the `SHIFT` + `TAB` keystroke combination when the cursor is on the function of interest.
    
</details>
    
</div>

```{code-cell} ipython3
:clear_cell: true

tidy_experiment = main_experiment.melt(id_vars=['AB_r', 'Bacterial_genotype', 'Phage_t', 
                                                'Survival_72h', 'PhageR_72h', 'experiment_ID'], 
                                       value_vars=['OD_0h', 'OD_20h', 'OD_72h'], 
                                       var_name='experiment_time_h', 
                                       value_name='optical_density', )
tidy_experiment
```

## Visual data exploration

```{code-cell} ipython3
tidy_experiment.head()
```

<div class="alert alert-success">

<b>EXERCISE</b>:

* Make a histogram using the [Seaborn package](https://seaborn.pydata.org/index.html) to visualize the distribution of the `optical_density`
* Change the overall theme to any of the available Seaborn themes
* Change the border color of the bars to `white` and the fill color of the bars to `grey`
    
<details><summary>Hints</summary>

- See https://seaborn.pydata.org/tutorial/distributions.html#plotting-univariate-histograms.
- There are five preset seaborn themes: `darkgrid`, `whitegrid`, `dark`, `white`, and `ticks`.
- Make sure to set the theme before creating the graph.
- Seaborn relies on Matplotlib to plot the individual bars, so the available parameters (`**kwargs`) to adjust the bars that can be passed (e.g. `color` and `edgecolor`) are enlisted in the [matplotlib.axes.Axes.bar](https://matplotlib.org/3.3.2/api/_as_gen/matplotlib.axes.Axes.bar.html) documentation.
    
</details>


</div>

```{code-cell} ipython3
:clear_cell: true

sns.set_style("white")
sns.displot(tidy_experiment, x="optical_density", 
            color='grey', edgecolor='white')
```

<div class="alert alert-success">

**EXERCISE**

Use a Seaborn `violin plot` to check the distribution of the `optical_density` in each of the experiment time phases (`experiment_time_h` in the x-axis).

<details><summary>Hints</summary>

- See https://seaborn.pydata.org/tutorial/categorical.html#violinplots.
- Whereas the previous exercise focuses on the distribution of data (`distplot`), this exercise focuses on distributions _for each category of..._ and needs the categorical functions of Seaborn (`catplot`).
    
</details>

```{code-cell} ipython3
:clear_cell: true

sns.catplot(data=tidy_experiment, x="experiment_time_h", 
            y="optical_density", kind="violin")
```

<div class="alert alert-success">

**EXERCISE**

For each `Phage_t` in an individual subplot, use a `violin plot` to check the distribution of the `optical_density` in each of the experiment time phases (`experiment_time_h`)

<details><summary>Hints</summary>

- The technical term for splitting in subplots using a categorical variable is 'faceting' (or sometimes also 'small multiple'), see https://seaborn.pydata.org/tutorial/categorical.html#showing-multiple-relationships-with-facets
- You want to wrap the number of columns on 2 subplots, look for a function argument in the documentation of the `catplot` function.
    
</details>

```{code-cell} ipython3
:clear_cell: true

sns.catplot(data=tidy_experiment, x="experiment_time_h", y="optical_density", 
            col="Phage_t", col_wrap=2, kind="violin")
```

<div class="alert alert-success">

**EXERCISE**

Create a summary table of the __average__ `optical_density` with the `Bacterial_genotype` in the rows and the `experiment_time_h` in the columns

<details><summary>Hints</summary>

- No Seaborn required here, rely on Pandas `pivot_table()` function to reshape tables. 
    
</details>

```{code-cell} ipython3
:clear_cell: true

pd.pivot_table(tidy_experiment, values='optical_density', 
               index='Bacterial_genotype', 
               columns='experiment_time_h',
               aggfunc='mean')
```

```{code-cell} ipython3
:clear_cell: true

# advanced/optional solution
tidy_experiment.groupby(['Bacterial_genotype', 'experiment_time_h'])['optical_density'].mean().unstack()
```

<div class="alert alert-success">

**EXERCISE**

- Calculate for each combination of `Bacterial_genotype`, `Phage_t` and `experiment_time_h` the <i>mean</i> `optical_density` and store the result as a DataFrame called `density_mean` (tip: use `reset_index()` to convert the resulting Series to a DataFrame).
- Based on `density_mean`, make a _barplot_ of the (mean) values for each `Bacterial_genotype`, with for each `Bacterial_genotype` an individual bar and with each `Phage_t` in a different color/hue (i.e. grouped bar chart).
- Use the `experiment_time_h` to split into subplots. As we mainly want to compare the values within each subplot, make sure the scales in each of the subplots are adapted to its own data range, and put the subplots on different rows.
- Adjust the size and aspect ratio of the Figure to your own preference.
- Change the color scale of the bars to another Seaborn palette.

<details><summary>Hints</summary>


- _Calculate for each combination of..._ should remind you to the `groupby` functionality of Pandas to calculate statistics for each group.
- The exercise is still using the `catplot` function of Seaborn with `bar`s. Variables are used to vary the `hue` and `row`.
- Each subplot its own range is the same as not sharing axes (`sharey` argument).
- Seaborn in fact has six variations of matplotlib’s palette, called `deep`, `muted`, `pastel`, `bright`, `dark`, and `colorblind`. See https://seaborn.pydata.org/tutorial/color_palettes.html#qualitative-color-palettes
    
</details>

```{code-cell} ipython3
:clear_cell: true

density_mean = (tidy_experiment
                .groupby(['Bacterial_genotype','Phage_t', 'experiment_time_h'])['optical_density']
                .mean().reset_index())
```

```{code-cell} ipython3
:clear_cell: true

sns.catplot(data=density_mean, kind="bar",
            x='Bacterial_genotype', 
            y='optical_density', 
            hue='Phage_t', 
            row="experiment_time_h",
            sharey=False, 
            aspect=3, height=3,
            palette="colorblind")
```

## (Optional) Reproduce chart of the original paper

+++

Check Figure 2 of the original journal paper in the 'correction' part of the <a href="http://rsbl.royalsocietypublishing.org/content/roybiolett/12/5/20160064.full.pdf">pdf</a>:
    
<img src="https://royalsocietypublishing.org/cms/attachment/eb511c57-4167-4575-b8b3-93fbcf728572/rsbl20160064f02.jpg" width="500">    

```{code-cell} ipython3
falcor.head()
```

<div class="alert alert-success">

**EXERCISE**

We will first reproduce 'Figure 2' without the error bars:
    
- Make sure the `WT(2)` and `MUT(2)` categories are used as respectively `WT` and `MUT` by adjusting them with Pandas first.
- Use the __falcor__ data and the Seaborn package. The 'log10 mutation rate' on the figure corresponds to the `log10 Mc` column.

    
<details><summary>Hints</summary>

- To replace values using a mapping (dictionary with the keys the current values and the values the new values), use the Pandas `replace` method.
- This is another example of a `catplot`, using `point`s to represent the data. 
- The `join` argument defines if individual points need to be connected or not.
- One combination appears multiple times, so make sure to not yet use confidence intervals by setting `ci` to `Null`.

</details>

```{code-cell} ipython3
:clear_cell: true

falcor["Bacterial_genotype"] = falcor["Bacterial_genotype"].replace({'WT(2)': 'WT', 
                                                                     'MUT(2)': 'MUT'})
```

```{code-cell} ipython3
:clear_cell: true

sns.catplot(data=falcor, kind="point",
            x='Bacterial_genotype', 
            y='log10 Mc', 
            row="Phage",
            join=False, ci=None,
            aspect=3, height=3,
            color="black")
```

```{code-cell} ipython3
falcor.head()
```

Seaborn supports confidence intervals by different estimators when multiple values are combined (see [this example](https://seaborn.pydata.org/examples/pointplot_anova.html)). In this particular case, the error estimates are already provided and are not symmetrical. Hence, we need to find a method to use the lower `log10 LBc` and upper `log10 UBc` confidence intervals. 

Stackoverflow can help you with this, see [this thread](https://stackoverflow.com/questions/38385099/adding-simple-error-bars-to-seaborn-factorplot) to solve the following exercise.

+++

<div class="alert alert-success">

**EXERCISE**

Reproduce 'Figure 2' with the error bars using the information from [this Stackoverflow thread](https://stackoverflow.com/questions/38385099/adding-simple-error-bars-to-seaborn-factorplot). You do not have to adjust the order of the categories in the x-axis.
    
<details><summary>Hints</summary>

- Do not use the `catplot` function, but first create the layout of the graph by `FacetGrid` on the `Phage` variable.
- Next, map a custom `errorbar` function to the FactgGrid as the example from Stackoverflow.
- Adjust/Simplify the `errorbar` custom function for your purpose.
- Matplotlib uses the `capsize` to draw upper and lower lines of the intervals.

</details>

```{code-cell} ipython3
:clear_cell: true

falcor["Bacterial_genotype"] = falcor["Bacterial_genotype"].replace({'WT(2)': 'WT', 
                                                                     'MUT(2)': 'MUT'})
```

```{code-cell} ipython3
:clear_cell: true

def errorbar(x, y, low, high, **kws):
    """Utility function to link falcor data representation with the errorbar representation"""
    plt.errorbar(x, y, (y - low, high - y), capsize=3, fmt="o", color="black", ms=4)
```

```{code-cell} ipython3
:clear_cell: true

sns.set_style("ticks")
g = sns.FacetGrid(falcor, row="Phage", aspect=3, height=3)
g.map(errorbar, 
      "Bacterial_genotype", "log10 Mc", 
      "log10 LBc", "log10 UBc")
```

```{code-cell} ipython3

```
