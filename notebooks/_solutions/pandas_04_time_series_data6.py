subset = data['2011':'2012']['L06_347']
subset.resample('M').agg(['mean', 'median']).plot()