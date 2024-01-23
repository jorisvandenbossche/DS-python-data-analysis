n_plot_sex = observations.groupby(["sex", "verbatimLocality"]).size().rename("count").reset_index()
n_plot_sex.head()