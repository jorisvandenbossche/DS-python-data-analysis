cast.pivot_table(index='year', columns='type', values="character", aggfunc='count').plot() 
# for the values column to use in the aggfunc, take a column with no NaN values in order to count effectively all values
# -> at this stage: aha-erlebnis about crosstab function(!)