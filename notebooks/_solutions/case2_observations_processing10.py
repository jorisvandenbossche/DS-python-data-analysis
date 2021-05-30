(survey_data_decoupled["year"]
     .value_counts(sort=False)
     .sort_index()
     .plot(kind='barh', color="#00007f", figsize=(10, 10)));