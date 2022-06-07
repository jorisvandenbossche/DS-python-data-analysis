titles['decade'] = titles['year'] // 10 * 10
hamlet = titles[titles['title'].str.contains('Hamlet')]
hamlet.groupby('decade').size().plot(kind='bar', color="lightblue")