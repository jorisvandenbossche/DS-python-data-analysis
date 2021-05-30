nrecords_by_dayofweek = survey_data_decoupled.groupby(survey_data_decoupled["eventDate"].dt.dayofweek).size()

fig, ax = plt.subplots(figsize=(6, 6))
nrecords_by_dayofweek.plot(kind="barh", color="#00007f", ax=ax);
# If you want to represent the ticklabels as proper names, uncomment the following line:
# ax.set_yticklabels(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]);

# Python standard library has a lot of useful functionalities! So why not use them?
#import calendar
#ax.set_yticklabels(calendar.day_name);