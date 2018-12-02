n_species_per_plot = survey_data.groupby(["verbatimLocality"])["name"].nunique()

fig, ax = plt.subplots(figsize=(6, 6))
n_species_per_plot.plot(kind="barh", ax=ax, color="lightblue")
ax.set_ylabel("plot number")

# Alternative option:
# inspired on the pivot table we already had:
# species_per_plot = survey_data.reset_index().pivot_table(
#     index="name", columns="verbatimLocality", values="occurrenceID", aggfunc='count')
# n_species_per_plot = species_per_plot.count()