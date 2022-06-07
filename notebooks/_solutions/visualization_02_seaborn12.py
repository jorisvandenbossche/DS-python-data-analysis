# Optional solution with tidy data representation (providing x and y)
monthly_victim_counts_melt = monthly_victim_counts.reset_index().melt(
    id_vars="datetime", var_name="victim_type", value_name="count"
)

sns.relplot(
    data=monthly_victim_counts_melt,
    x="datetime", 
    y="count",
    hue="victim_type",
    kind="line",
    palette="colorblind",
    height=3, aspect=4,
)