heatmap_prep = survey_data.pivot_table(index=survey_data['eventDate'].dt.year,
                                       columns=survey_data['eventDate'].dt.month,
                                       values='species', aggfunc='count')
fig, ax = plt.subplots(figsize=(10, 8))
ax = sns.heatmap(heatmap_prep, cmap='Reds')