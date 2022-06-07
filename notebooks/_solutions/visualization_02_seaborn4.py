victims_hour_of_day = casualties.groupby(casualties["datetime"].dt.hour)["n_victims"].sum().reset_index()
victims_hour_of_day = victims_hour_of_day.rename(
    columns={"datetime": "Hour of the day", "n_victims": "Number of victims"}
)