# using a tidy dataset and seaborn
data_weekend_BETR801_tidy = data_weekend['BETR801'].reset_index()

sns.lineplot(data=data_weekend_BETR801_tidy, x="hour", y="BETR801", hue="weekend")