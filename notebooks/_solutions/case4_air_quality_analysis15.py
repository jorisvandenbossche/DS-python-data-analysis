data['weekend'] = data.index.dayofweek.isin([5, 6])
data['weekend'] = data['weekend'].replace({True: 'weekend', False: 'weekday'})
data['hour'] = data.index.hour