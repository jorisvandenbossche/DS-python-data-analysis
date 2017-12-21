exceedances = exceedances.groupby(exceedances.index.year).sum()
ax = exceedances.plot(kind='bar')