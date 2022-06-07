mask = observations['species_ID'].isna() & observations['sex'].notna()
not_identified = observations[mask]