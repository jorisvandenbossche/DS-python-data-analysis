titles['decade'] = titles['year'] // 10 * 10
hamlet = titles[titles['title'] == 'Hamlet']
hamlet.groupby('decade').size().plot.bar(color="orange")