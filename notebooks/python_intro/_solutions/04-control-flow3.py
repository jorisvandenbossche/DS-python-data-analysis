indices = []
for j, pressure in enumerate(pressures_hPa):
    if pressure < 1000:
        indices.append(j)
indices        