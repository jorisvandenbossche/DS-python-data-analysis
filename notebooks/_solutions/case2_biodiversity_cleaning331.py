survey_data_completed = pd.merge(survey_data_species, unique_species_annotated, 
                                 how='left', on= ["genus", "species"])