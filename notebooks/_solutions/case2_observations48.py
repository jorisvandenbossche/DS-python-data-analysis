year_evolution = survey_data.groupby("taxa").resample('YE', on='eventDate').size()
year_evolution.name = "counts"
year_evolution = year_evolution.reset_index()