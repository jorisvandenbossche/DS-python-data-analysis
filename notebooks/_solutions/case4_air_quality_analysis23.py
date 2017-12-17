data['weekday'] = data.index.weekday
data['weekend'] = data['weekday'].isin([5, 6])