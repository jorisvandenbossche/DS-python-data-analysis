species_evolution = month_evolution.unstack(level=0)
axs = species_evolution.plot(subplots=True, figsize=(16, 8), sharey=True)