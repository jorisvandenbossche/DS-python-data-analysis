titanic = cast[(cast['title'] == 'Titanic') & (cast['year'] == 1997)]
titanic = titanic[titanic['n'].notna()]
titanic.sort_values('n')