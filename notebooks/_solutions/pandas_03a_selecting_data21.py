brad = cast[cast['name'] == 'Brad Pitt']
brad = brad[brad['year'] // 10 == 199]
brad = brad[brad['n'] == 2]
brad.sort_values('year')