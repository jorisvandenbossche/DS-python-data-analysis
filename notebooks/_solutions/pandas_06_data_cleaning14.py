unique_combinations = ["DT_DAY", "DT_HOUR",  "CD_MUNTY_REFNIS", "BUILD_UP_AREA","LIGHT_COND", "ROAD_TYPE"]
casualties.drop_duplicates(subset=unique_combinations).shape