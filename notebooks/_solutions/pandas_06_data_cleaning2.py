gender_mapping = {"Vrouwelijk": "female", "Mannelijk": "male", "Onbekend": None}
casualties_raw["TX_SEX_DESCR_NL"] = casualties_raw["TX_SEX_DESCR_NL"].replace(gender_mapping)
casualties_raw["TX_SEX_DESCR_NL"].unique()