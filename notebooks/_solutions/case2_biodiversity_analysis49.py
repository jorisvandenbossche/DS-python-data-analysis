year_evolution = survey_data.groupby("taxa").resample('A', on='eventDate').size()
species_evolution = year_evolution.unstack(level=0)
axs = species_evolution.plot(subplots=True, figsize=(16, 8), sharey=False)