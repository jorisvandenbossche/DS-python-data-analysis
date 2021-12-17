fig, ax = plt.subplots()
flowdata.mean().plot.bar(ylabel="mean discharge", ax=ax)