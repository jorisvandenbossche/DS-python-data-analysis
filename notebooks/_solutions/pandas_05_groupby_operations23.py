oz = cast[cast['name'] == 'Frank Oz']
oz_roles = oz.groupby(['year', 'title']).size()
oz_roles[oz_roles > 1]