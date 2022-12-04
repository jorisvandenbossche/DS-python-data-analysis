# filter the data
compare_dead_30 = casualties.set_index("datetime")["2019":"2021"]
compare_dead_30 = compare_dead_30[compare_dead_30["road_user_type"].isin(
    ["Bicycle", "Passenger car", "Pedestrian", "Motorbike"])]

# Sum the victims and dead within 30 days victims for each year/road-user type combination
compare_dead_30 = compare_dead_30.groupby(
    ["road_user_type", compare_dead_30.index.year])[["n_dead_30days", "n_victims"]].sum().reset_index()

# create a new colum with the percentage deads
compare_dead_30["dead_prop"] = compare_dead_30["n_dead_30days"] / compare_dead_30["n_victims"] * 100