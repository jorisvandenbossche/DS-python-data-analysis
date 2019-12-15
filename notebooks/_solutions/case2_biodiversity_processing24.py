def name_match(genus_name, species_name, strict=True):
    """
    Perform a GBIF name matching using the species and genus names
    
    Parameters
    ----------
    genus_name: str
        name of the genus of the species
    species_name: str
        name of the species to request more information
    strict: boolean
        define if the mathing need to be performed with the strict 
        option (True) or not (False)
    
    Returns
    -------
    message: dict
        dictionary with the information returned by the GBIF matching service
    """
    name = '{} {}'.format(genus_name, species_name)
    base_string = 'http://api.gbif.org/v1/species/match?'
    request_parameters = {'strict': strict, 'name': name} # use strict matching(!)
    message = requests.get(base_string, params=request_parameters).json()
    return message