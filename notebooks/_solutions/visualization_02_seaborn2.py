# Figure based
sns.catplot(data=titanic, x="Pclass", y="Age", 
            hue="Sex", split=True,
            palette="Set2", kind="violin")
sns.despine(left=True)