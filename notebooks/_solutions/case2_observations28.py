heatmap_prep = observations.pivot_table(index='year', columns='month', 
                                        values="species_ID", aggfunc='count')
fig, ax = plt.subplots(figsize=(10, 8))
ax = sns.heatmap(heatmap_prep, cmap='Reds')