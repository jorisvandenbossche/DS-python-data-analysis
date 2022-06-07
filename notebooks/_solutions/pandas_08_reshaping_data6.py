facet = sns.relplot(x="time", y="consumption", col="Energie",
                    data=df_overall, kind="line")
facet.set(ylim=(0, None))