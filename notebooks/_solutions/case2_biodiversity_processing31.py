unique_species_annotated = pd.merge(unique_species, df_species_annotated_subset, 
                                    left_index=True, right_index=True)