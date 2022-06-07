hamlets = titles[titles['title'].str.startswith('Hamlet')]
hamlets['title'].value_counts()