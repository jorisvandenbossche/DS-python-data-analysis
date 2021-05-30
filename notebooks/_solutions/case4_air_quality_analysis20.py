# when still having multiple factors, it becomes useful to convert to tidy dataset and use seaborn
sns.relplot(data=data_weekend_tidy, x="hour", y="no2", kind="line",
            hue="weekend", col="station", col_wrap=2)