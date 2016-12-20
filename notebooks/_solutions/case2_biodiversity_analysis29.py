species_per_plot2 = survey_data.reset_index().pivot_table(index="plot_id",
                                                                  columns="name",
                                                                  values="occurrenceID",
                                                                  aggfunc='count')
nplots_per_species = species_per_plot2.count().sort_values(ascending=False)

fig, ax = plt.subplots(figsize=(8, 8))
nplots_per_species.plot(kind="bar", ax=ax)

# Alternatives
#species_per_plot.count(axis=1).sort_values(ascending=False).plot(kind='bar')
#survey_data.groupby(["name"])["plot_id"].nunique().sort_values().plot(kind='bar')