titles['decade'] = titles['year'] // 10 * 10
hamlet = titles[titles['title'] == 'Hamlet']
hamlet.groupby('decade').size().plot(kind='bar', color="orange")