species_per_plot = survey_data.reset_index().pivot_table(index="name", 
                                                         columns="verbatimLocality", 
                                                         values="occurrenceID", 
                                                         aggfunc='count')

# alternative ways to calculate this
#species_per_plot =  survey_data.groupby(['name', 'plot_id']).size().unstack(level=-1)
#species_per_plot = pd.crosstab(survey_data['name'], survey_data['plot_id'])