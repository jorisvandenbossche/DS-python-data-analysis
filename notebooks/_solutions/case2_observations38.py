heatmap_prep = survey_data.pivot_table(index='year', columns='month', 
                                       values="ID", aggfunc='count')
fig, ax = plt.subplots(figsize=(10, 8))
ax = sns.heatmap(heatmap_prep, cmap='Reds')