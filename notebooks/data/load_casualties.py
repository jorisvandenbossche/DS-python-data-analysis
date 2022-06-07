import argparse
import urllib
import logging
from tempfile import tempdir
from pathlib import Path

import pandas as pd
import numpy as np


def clean_casualties_data(casualties_raw):
    """Convert raw casualties data to english and restructured format"""
    casualties = (
        casualties_raw
        .drop(columns=[col for col in casualties_raw.columns
                        if col.endswith("_FR")])
        .drop(columns=[col for col in casualties_raw.columns
                        if col.startswith("CD_") and not col.endswith("_REFNIS")])
        .rename(columns={name: name.removeprefix("TX_").removesuffix("_DESCR_NL")
                        for name in casualties_raw.columns})
        .replace("Onbekend", None)
    )
    casualties["gender"] = casualties["SEX"].replace(
        {"Vrouwelijk": "female", "Mannelijk": "male"}
    )

    casualties["DT_HOUR"] = casualties["DT_HOUR"].replace(99, 0)
    casualties["datetime"] = pd.to_datetime(
        casualties["DT_DAY"] + " " + casualties["DT_HOUR"].astype(str) + ":00"
    )

    casualties["age"] = casualties["AGE_CLS"].str.replace(
        " tot ", " - ").str.removesuffix("jaar").str.strip()
    casualties["age"] = casualties["age"].replace(
        {"": None, "75 jaar en meer": ">75", ' ': None})

    casualties["DAY_OF_WEEK"] = casualties["DAY_OF_WEEK"].replace({
        "maandag": "Monday", "dinsdag": "Tuesday", "woensdag": "Wednesday",
        "donderdag": "Thursday", "vrijdag": "Friday", "zaterdag": "Saturday",
        "zondag": "Sunday"})
    casualties["week_day"] = pd.Categorical(
        casualties["DAY_OF_WEEK"],
        categories=["Monday", "Tuesday", "Wednesday",
                    "Thursday", "Friday", "Saturday", "Sunday"],
        ordered=True
    )

    casualties["victim_type"] = casualties["VICT_TYPE"].replace({
        "Bestuurder": "Driver", "Bromfietser": "Moped driver",
        "Passagier": "Passenger", "Motorfietser": 'Motorcyclist',
        "Fietser": "Cyclist", "Voetganger": "Pedestrian",
        "Autres victimes": None})

    casualties["build_up_area"] = casualties["BUILD_UP_AREA"].replace({
        "Binnen bebouwde kom": "Inside built-up area",
        "Buiten bebouwde kom": "Outside built-up area",
        " ": None})

    casualties["ROAD_USR_TYPE"] = casualties["ROAD_USR_TYPE"].replace({
        'Personenauto': 'Passenger car',
        'Auto voor dubbel gebruik': 'Dual-purpose vehicle',
        'Lichte vrachtauto': 'Light truck',
        'Bromfiets': 'Moped',
        'Bromfiets A (tweewielige)': 'Moped',
        'Bromfiets B (tweewielige)': 'Moped',
        'Bromfiets met 3 of 4 wielen': 'Moped',
        'Motorfiets': 'Motorbike',
        'Motorfiets meer dan 400 cc': 'Motorbike',
        'Motorfiets niet meer dan 400 cc': 'Motorbike',
        'Fiets': 'Bicycle',
        'Elektrische fiets': 'Electric bicycle',
        'Fiets met elektrische hulpmotor (<=250W en <=25km/u)': 'Electric bicycle',
        'Gemotoriseerde fiets (<=1000W en <=25km/u)': 'Electric bicycle',
        'Speed pedelec (<= 4000W en <=45km/u)': 'Speed pedelec',
        'Gemotoriseerd voortbewegingstoestel (<=18km/u)': 'Electric bicycle',
        'Trekker + aanhangwagen': 'Trailer',
        'Trekker alleen': 'Trailer',
        'Vrachtwagen': 'Truck',
        'Ruiter': 'Horse rider',
        'Bespannen voertuig': 'Horse rider',
        'Andere voetganger': 'Pedestrian',
        'Gehandicapte in rolstoel': 'Disabled person in a wheelchair',
        'Voetganger die zijn (brom)fiets duwt': 'Pedestrian',
        'Trolleybus, Tram': 'Tram',
        'Minibus': 'Van',
        'Autobus': 'Bus',
        'Autocar': 'Bus',
        'Autobus/Autocar': 'Bus',
        'Kampeerwagen': 'Campervan',
        'Landbouwtractor': 'Tractor',
        'Andere weggebruiker': None,
        'Niet ingevuld': None,
        np.nan: None
    })

    casualties["LIGHT_COND"] = casualties["LIGHT_COND"].replace(
        {'Bij klaarlichte dag': 'In broad daylight',
         'Nacht, ontstoken openbare verlichting': 'Night, public lighting lit',
         'Dageraad - schemering': 'Dawn',
         'Nacht, openbare verlichting aanwezig, maar niet ontstoken': 'Night, no public lighting',
         'Nacht, geen openbare verlichting': 'Night, no public lighting',
         ' ': None
        })

    casualties["ROAD_TYPE"] = casualties["ROAD_TYPE"].replace({
        'Gemeenteweg': 'Municipal road',
        'Gewestweg': 'Regional road',
        'Autosnelweg': 'Motorway'
    })

    casualties["RGN"] = casualties["RGN"].replace({
        'Vlaams Gewest': 'Flemish Region',
        'Brussels Hoofdstedelijk Gewest': 'Brussels-Capital Region',
        'Waals Gewest': 'Walloon Region'
    })
    casualties["CD_RGN_REFNIS"] = casualties["CD_RGN_REFNIS"].replace(
        {'02000': 2000, '03000': 3000, '04000': 4000, ' ': None}
    )

    casualties = casualties.replace(" ", None)
    casualties = casualties.rename(columns={
        "MS_VICT": "n_victims",
        "MS_VIC_OK": "n_victims_ok",
        "MS_SLY_INJ": "n_slightly_injured",
        "MS_SERLY_INJ": "n_seriously_injured",
        "MS_DEAD_30_DAYS": "n_dead_30days",
        "ROAD_USR_TYPE": "road_user_type",
        "LIGHT_COND": "light_conditions",
        "ROAD_TYPE": "road_type",
        "RGN": "region",
        "CD_RGN_REFNIS": "refnis_region",
        "CD_MUNTY_REFNIS": "refnis_municipality",
        "MUNTY": "municipality"
    })
    casualties_clean = casualties.drop(
        columns=[
            "DT_DAY", "DT_HOUR", "DAY_OF_WEEK", "SEX", "VICT_TYPE",
            "BUILD_UP_AREA", "AGE_CLS", "CD_PROV_REFNIS", "PROV",
            "CD_DSTR_REFNIS", "ADM_DSTR"]
    )

    return casualties_clean


def main(start_year=2005, end_year=2020,
         processed_file_name="casualties.csv"):
    """Download casualties data, run cleaning function, concat and save as CSV

    Parameters
    ----------
    start_year : int, default 2005
        Start year to download data from.
    end_year : int, default 2021
        End year to download data from.
    processed_file_name : str
        File name of the concatenated clean data set.
    """
    download_folder = Path(tempdir) / "casualties"
    download_folder.mkdir(exist_ok=True)

    logger.info("Start processing causalties Belgium open data from {start_year} till {end_year}.")
    casualties_all = []
    for year in range(start_year, end_year+1):
        logger.info(f"Handling year {year}")
        file_name = download_folder / f"TF_ACCIDENTS_VICTIMS_{year}_.zip"
        if not file_name.exists():
            logger.info(f"Download year {year}.")
            urllib.request.urlretrieve(
                f"https://statbel.fgov.be/sites/default/files/files/opendata/Verkeersslachtoffers/TF_ACCIDENTS_VICTIMS_{year}.zip",
                file_name)
        casualties = pd.read_csv(file_name, compression='zip',
                                 sep="|", low_memory=False)
        try:
            casualties_clean = clean_casualties_data(casualties)
            casualties_all.append(casualties_clean)
        except:
            logger.error(f"Data processing of year {year} failed")
    logger.info("All casualties raw data set donwloads ready.")

    logger.info("Combining individual years to single DataFrame.")
    casualties_all = pd.concat(casualties_all).sort_values("datetime")

    if 'n_victims_ok' in casualties_all.columns:
        casualties = casualties_all[["datetime", "week_day",
                    "n_victims", "n_victims_ok", "n_slightly_injured",
                    "n_seriously_injured", "n_dead_30days",
                    "road_user_type", "victim_type", "gender", "age",
                    "road_type", "build_up_area", "light_conditions",
                    "refnis_municipality", "municipality",
                    "refnis_region", "region"
                ]]
    else:
        casualties = casualties_all[["datetime", "week_day",
                    "n_victims", "n_slightly_injured",
                    "n_seriously_injured", "n_dead_30days",
                    "road_user_type", "victim_type", "gender", "age",
                    "road_type", "build_up_area", "light_conditions",
                    "refnis_municipality", "municipality",
                    "refnis_region", "region"
                ]]

    logger.info("Writing combined casualties data file to disk.")
    casualties.to_csv(Path("./data") / processed_file_name, index=False)

    logger.info("Combined casualties data file ready.")


if __name__ == "__main__":

    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(
        description='Collect and prepare casualties open data Belgium.'
    )
    parser.add_argument('start_year', metavar='start-year', type=int, default=2015,
                        help='First year to download casualties data.')
    parser.add_argument('end_year', metavar='end-year', type=int, default=20210,
                        help='Last year to download casualties data.')

    args = parser.parse_args()

    print("Start casualties data preparation...")
    main(args.start_year, args.end_year)
    print("...done!")