pressure_hPa = 1010
height = 2500

pressure_hPa * math.exp(-gravit_acc * molar_mass_earth * height/(gas_constant * standard_temperature))