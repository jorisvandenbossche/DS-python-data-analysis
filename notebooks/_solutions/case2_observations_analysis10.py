survey_data = survey_data_unique.dropna(subset=['species']).copy()
survey_data['name'] = survey_data['genus'] + ' ' + survey_data['species']