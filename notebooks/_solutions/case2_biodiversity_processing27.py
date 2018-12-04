unique_species["name"] = unique_species["genus"] + " " + unique_species["species"] 
# an alternative approach worthwhile to know:
#unique_species["name"] = unique_species["genus"].str.cat(unique_species["species"], " ")