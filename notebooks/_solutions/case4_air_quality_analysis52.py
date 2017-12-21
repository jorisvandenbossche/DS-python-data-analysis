# when using pandas to plot, the different boxplots should be different columns
# therefore, pivot table so that the weekdays are the different columns
data_daily['week'] = data_daily.index.week
data_pivoted = data_daily['2012'].pivot_table(columns='weekday', index='week', values='BETR801')
data_pivoted.head()
data_pivoted.boxplot();