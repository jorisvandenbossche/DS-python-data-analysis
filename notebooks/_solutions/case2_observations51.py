fig, ax = plt.subplots()
survey_data.groupby(survey_data["eventDate"].dt.weekday).size().plot(kind='barh', color='#66b266', ax=ax)

import calendar
xticks = ax.set_yticklabels(calendar.day_name)