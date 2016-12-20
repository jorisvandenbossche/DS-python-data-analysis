# Alternative
#survey_data['year'] = survey_data['eventDate'].dt.year
#survey_data['month'] = survey_data['eventDate'].dt.month

#heatmap_prep = survey_data.reset_index().pivot_table(index='year',
#                                                     columns='month',
#                                                     values="occurrenceID", aggfunc='count')