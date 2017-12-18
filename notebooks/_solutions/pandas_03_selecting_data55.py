titanic = cast[(cast['title'] == 'Titanic') & (cast['year'] == 1997)]
titanic = titanic[titanic['n'].notnull()]
titanic.sort_values('n')