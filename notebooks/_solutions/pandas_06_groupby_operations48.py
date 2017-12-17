cast2000 = cast[cast['year'] // 10 == 200]
cast2000 = cast2000[cast2000['n'] == 1]
cast2000['type'].value_counts()