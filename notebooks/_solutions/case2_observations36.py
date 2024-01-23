# alternative solution
birds_85_89 = survey_data[(survey_data["eventDate"].dt.year >= 1985)
                          & (survey_data["eventDate"].dt.year <= 1989) 
                          & (survey_data['taxa'] == 'Bird')]
birds_85_89.head()