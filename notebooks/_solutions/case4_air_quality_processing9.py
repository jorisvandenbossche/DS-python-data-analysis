# rename the remaining column to the name of the measurement station
# (this is 0 or 'value' depending on which method was used)
data_stacked = data_stacked.rename(columns={0: 'BETR801'})