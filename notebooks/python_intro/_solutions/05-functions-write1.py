import math

def barometric_formula(pressure_sea_level, height=2500):
    """Apply barometric formula
    
    Apply the barometric formula to calculate the air pressure on a given height
    
    Parameters
    ----------
    pressure_sea_level : float
        pressure, measured as sea level (hPa)
    height : float
        height above sea level (m)
    
    Notes
    ------
    see https://www.math24.net/barometric-formula/ or 
    https://en.wikipedia.org/wiki/Atmospheric_pressure
    """
    standard_temperature = 288.15
    gas_constant = 8.3144598
    gravit_acc = 9.81
    molar_mass_earth = 0.02896
    
    pressure_altitude = pressure_sea_level * math.exp(-gravit_acc * molar_mass_earth* height/(gas_constant*standard_temperature))
    return pressure_altitude

barometric_formula(1010), barometric_formula(1010, 2750)