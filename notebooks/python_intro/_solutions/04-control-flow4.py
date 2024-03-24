for location, do in water_quality.items():
    if (do > 20) or (do < 5):
        print(f"Alert: Poor conditions measured at {location} with DO concentration of {do} mg/l.")