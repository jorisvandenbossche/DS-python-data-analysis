ax = survey_data_decoupled.groupby(survey_data_decoupled["eventDate"].dt.weekday).size().plot(kind="barh")
# I you want to represent the ticklabels as proper names, uncomment the following line
#ticklabels = ax.set_yticklabels(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])