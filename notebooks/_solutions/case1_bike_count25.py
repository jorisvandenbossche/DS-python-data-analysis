newyear.plot()
newyear.rolling(10, center=True).mean().plot(linewidth=2)