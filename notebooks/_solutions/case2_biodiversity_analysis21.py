heatmap_tidy = heatmap_prep_sns.reset_index().melt(id_vars=["year"], value_name="count")
heatmap_tidy.head()