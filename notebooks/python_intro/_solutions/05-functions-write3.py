pressures_hPa_1200 = []
for pressure in pressures_hPa:
    pressures_hPa_1200.append(barometric_formula(pressure, 1200))
pressures_hPa_1200