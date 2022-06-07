cast['n_total'] = cast.groupby(['title', 'year'])['n'].transform('size') # transform will return an element for each row, so the size value is given to the whole group
cast.head()