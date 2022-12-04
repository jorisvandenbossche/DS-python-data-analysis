casualties_motorway_trucks = casualties[
    (casualties["road_type"] == "Motorway")
    & casualties["road_user_type"].isin(["Light truck", "Truck"])
]