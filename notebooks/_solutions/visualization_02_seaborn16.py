# Using Pandas
daily_total_counts_2020 = casualties.set_index("datetime")["2020":"2021"].resample("D")["n_victims"].sum()
daily_total_counts_2020.plot.line(figsize=(12, 3))