gender_mapping = {"Vrouwelijk": "female", "Mannelijk": "male", "Onbekend": None}
casualties["SEX"] = casualties["SEX"].replace(gender_mapping)
casualties["SEX"].unique()