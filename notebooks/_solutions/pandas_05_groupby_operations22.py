pink = cast[cast['title'] == 'The Pink Panther']
pink.groupby(['year'])[['n']].max()