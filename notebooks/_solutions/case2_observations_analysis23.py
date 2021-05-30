pivoted = n_plot_sex.pivot(columns="sex", index="verbatimLocality", values="count")
pivoted.head()