data_stacked = pd.melt(data, id_vars=['date'], var_name='hour')
data_stacked.head()