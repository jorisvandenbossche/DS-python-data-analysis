pivoted = n_plot_sex.pivot_table(columns="sex", index="verbatimLocality", values="count")
pivoted.head()