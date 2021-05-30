n_plots_per_species = survey_data.groupby(["name"])["verbatimLocality"].nunique().sort_values()

fig, ax = plt.subplots(figsize=(8, 8))
n_plots_per_species.plot(kind="barh", ax=ax, color='0.4')
ax.set_xlabel("Number of plots");
ax.set_ylabel("");