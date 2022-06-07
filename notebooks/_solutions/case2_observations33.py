# Alternative option to calculate the species per plot:
# inspired on the pivot table we already had:
# species_per_plot = survey_data.reset_index().pivot_table(
#      index="name", columns="verbatimLocality", values="ID", aggfunc='count')
# n_species_per_plot = species_per_plot.count()