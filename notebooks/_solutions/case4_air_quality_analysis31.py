# tidy dataset that still includes all stations

data_weekend_tidy = pd.melt(data_weekend.reset_index(), id_vars=['weekend', 'hour'],
                            var_name='station', value_name='no2')
data_weekend_tidy.head()