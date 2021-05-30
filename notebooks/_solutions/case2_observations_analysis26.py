species_per_plot = survey_data.pivot_table(index="name",
                                           columns="verbatimLocality",
                                           values="datasetName",
                                           aggfunc='count')

# alternative ways to calculate this
#species_per_plot = survey_data.groupby(['name', 'verbatimLocality']).size().unstack(level=-1)
#pecies_per_plot = pd.crosstab(survey_data['name'], survey_data['verbatimLocality'])