n_plot_sex = subselection_sex.groupby(["sex", "verbatimLocality"]).size().unstack(level=0)
n_plot_sex.head()