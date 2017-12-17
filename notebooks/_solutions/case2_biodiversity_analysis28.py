# inspired on the pivot table we already had:
species_per_plot = survey_data.reset_index().pivot_table(index="name", 
                                                         columns="verbatimLocality", 
                                                         values="occurrenceID", 
                                                         aggfunc='count')

fig, ax = plt.subplots(figsize=(6, 6))
species_per_plot.count().plot(kind="barh", ax=ax, color="lightblue")
ax.set_ylabel("plot number")

# Alternative option:
# survey_data.groupby(["plot_id"])["species"].nunique()