oz = cast[cast['name'] == 'Frank Oz']
oz_roles = oz.groupby(['character']).size()
oz_roles[oz_roles > 1].sort_values()