fig, ax = plt.subplots()
merriami.groupby(merriami['eventDate'].dt.year).size().plot(ax=ax)
ax.set_xlabel("")
ax.set_ylabel("number of occurrences")