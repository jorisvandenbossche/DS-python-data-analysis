df.groupby('Pclass')['Survived'].mean().plot(kind='bar', color="blue") #and what if you would compare the total number of survivors?