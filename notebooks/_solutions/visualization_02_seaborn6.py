victims_gender_hour_of_day = casualties.groupby([casualties["datetime"].dt.hour, "gender"], 
                                                dropna=False)["n_victims"].sum().reset_index()
victims_gender_hour_of_day.head()