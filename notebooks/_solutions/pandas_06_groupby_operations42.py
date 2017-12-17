cast['n_total'] = cast.groupby('title')['n'].transform('max') # transform will return an element for each row, so the max value is given to the whole group
cast.head()