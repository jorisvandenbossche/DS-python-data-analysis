monthly_victim_counts = casualties.resample("ME", on="datetime")[
    ["n_victims_ok", "n_slightly_injured", "n_seriously_injured", "n_dead_30days"]
].sum()