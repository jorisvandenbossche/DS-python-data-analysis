heatmap_prep_plotnine = survey_data.groupby([survey_data['eventDate'].dt.year, 
                                             survey_data['eventDate'].dt.month]).size()
heatmap_prep_plotnine.index.names = ["year", "month"]
heatmap_prep_plotnine = heatmap_prep_plotnine.reset_index(name='count')