n_plots_per_species = observations.groupby(["name"])["verbatimLocality"].nunique().sort_values()

fig, ax = plt.subplots(figsize=(10, 8))
n_plots_per_species.plot(kind="barh", ax=ax)
ax.set_xlabel("Number of plots");
ax.set_ylabel("");