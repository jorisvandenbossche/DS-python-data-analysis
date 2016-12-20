year_evolution = survey_data.set_index("eventDate").groupby("taxa").resample('A').size()
species_evolution = year_evolution.unstack(level=0)
axs = species_evolution.plot(subplots=True, figsize=(16, 8), sharey=False)