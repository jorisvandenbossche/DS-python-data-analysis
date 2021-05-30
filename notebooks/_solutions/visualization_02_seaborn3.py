# Axes based
sns.violinplot(data=titanic, x="Pclass", y="Age", 
               hue="Sex", split=True,
               palette="Set2")
sns.despine(left=True)