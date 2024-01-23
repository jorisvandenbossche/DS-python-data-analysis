## Alternative option to calculate the species per plot:
## inspired on the pivot table we already had:
#species_per_plot = observations.reset_index().pivot_table(
#      index="species_ID", columns="verbatimLocality", values="occurrenceID", aggfunc='count')
#n_species_per_plot = species_per_plot.count()