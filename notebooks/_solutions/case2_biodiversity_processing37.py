nrecords_by_weekday = survey_data_decoupled.groupby(survey_data_decoupled["eventDate"].dt.weekday).size()
ax = nrecords_by_weekday.plot(kind="barh", color="#00007f", figsize=(6, 6))
# I you want to represent the ticklabels as proper names, uncomment the following line
#ticklabels = ax.set_yticklabels(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])