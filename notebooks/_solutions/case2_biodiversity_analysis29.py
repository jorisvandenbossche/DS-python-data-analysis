species_per_plot2 = survey_data.reset_index().pivot_table(index="verbatimLocality",
                                                          columns="name",
                                                          values="occurrenceID",
                                                          aggfunc='count')
nplots_per_species = species_per_plot2.count().sort_values(ascending=False)

fig, ax = plt.subplots(figsize=(8, 8))
nplots_per_species.plot(kind="barh", ax=ax, color='0.4')

# Alternatives
#species_per_plot.count(axis=1).sort_values(ascending=False).plot(kind='bar')
#survey_data.groupby(["name"])["plot_id"].nunique().sort_values().plot(kind='bar')