FR_station = data['FR04012'] # select the specific data series
FR_station = FR_station[(FR_station.notnull()) & (FR_station != 0.0)]  # exclude the Nan and zero values