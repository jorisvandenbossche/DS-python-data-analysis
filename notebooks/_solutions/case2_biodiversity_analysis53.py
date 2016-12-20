fig, ax = plt.subplots()
count_weekday_years.median(axis=0).plot(kind='barh', ax=ax)
xticks = ax.set_yticklabels(['Monday', 'Tuesday', 'Wednesday', "Thursday", "Friday", "Saturday", "Sunday"])