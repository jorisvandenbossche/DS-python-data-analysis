survey_data_processed = pd.read_csv("survey_data_completed.csv", 
                                    parse_dates=['eventDate'], index_col="occurrenceID")