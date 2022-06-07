casualties["week_day"] = pd.Categorical(casualties["DAY_OF_WEEK"], 
                                        categories=["Monday", "Tuesday", "Wednesday", "Thursday", 
                                                    "Friday", "Saturday", "Sunday"], 
                                        ordered=True)