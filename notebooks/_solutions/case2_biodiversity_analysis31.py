n_plot_sex = subselection_sex.groupby(["sex", "plot_id"]).size().unstack(level=0)
n_plot_sex