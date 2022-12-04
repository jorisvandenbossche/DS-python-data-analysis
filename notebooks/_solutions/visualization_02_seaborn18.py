# weekly proportion of deadly victims for each light condition
weekly_victim_dead_lc = (
    casualties
    .groupby("light_conditions")
    .resample("W", on="datetime")[["datetime", "n_victims", "n_dead_30days"]]
    .sum()
    .reset_index()
 )
weekly_victim_dead_lc["dead_prop"] = weekly_victim_dead_lc["n_dead_30days"] / weekly_victim_dead_lc["n_victims"] * 100

# .. and the same for each road type
weekly_victim_dead_rt = (
    casualties
    .groupby("road_type")
    .resample("W", on="datetime")[["datetime", "n_victims", "n_dead_30days"]]
    .sum()
    .reset_index()
)
weekly_victim_dead_rt["dead_prop"] = weekly_victim_dead_rt["n_dead_30days"] / weekly_victim_dead_rt["n_victims"] * 100