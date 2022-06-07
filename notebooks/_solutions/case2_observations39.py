species_per_plot = survey_data.reset_index().pivot_table(index="name", 
                                                         columns="verbatimLocality", 
                                                         values="ID", 
                                                         aggfunc='count')
species_per_plot.head()