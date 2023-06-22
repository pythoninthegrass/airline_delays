#!/usr/bin/env python3

import json
import re
import requests
import signal
import sys
import threading
from pathlib import Path


def signal_handler(sig, frame):
    """Handles SIGINT signal and exits program."""
    print("\nGoodbye!")
    sys.exit(0)


# avoid KeyboardInterrupt error without using try/except
signal.signal(signal.SIGINT, signal_handler)
forever = threading.Event()

# download airlines.json
url = "https://think.cs.vt.edu/corgis/datasets/json/airlines/airlines.json"

if not Path("airlines.json").is_file():
    print("Downloading airlines.json...")
    response = requests.get(url)
    response.raise_for_status()
    with open("airlines.json", "wb") as f:
        f.write(response.content)
else:
    print("airlines.json already exists")

# read airlines.json
with open('airlines.json') as f:
    output = json.load(f)

# create airport code set
airport_codes = set()

# add all airport codes to set
[airport_codes.add(airport['Airport']['Code']) for airport in output]

# sort airport codes
airport_codes = sorted(airport_codes)

# initialize years set
years = set()

# get all available years and add to set
[years.add(airport['Time']['Year']) for airport in output]

# sort years
years = sorted(years)

# print available years on separate lines with list brackets stripped
print("Available years:")
[print(year) for year in years]

# prompt user for year
year = input("Enter a year: ")

# validate input
if year == "":
    year = years[-1]
    print(f"Using default year: {year}")
elif not re.match(r"^\d{4}$", year):
    year = input("Enter a valid year: ")

# filter json by Airport > Time > Year > <2004>
filtered_output = [airport for airport in output if airport['Time']['Year'] == int(year)]

# get percentage of delayed flights by Statistics > # of Delays > Security
delayed_flights = [airport['Statistics']['# of Delays']['Security'] for airport in filtered_output]
total_flights = [airport['Statistics']['Flights']['Total'] for airport in filtered_output]
percent_delayed_flights = [delayed_flights[i] / total_flights[i] for i in range(len(delayed_flights))]
percent_delayed_flights = [round(percent * 100, 2) for percent in percent_delayed_flights]
average_flights_delayed = sum(percent_delayed_flights) / len(percent_delayed_flights)

# round to 2 decimal places and with a % sign (e.g., 0.07928... > 7.93%)
average_flights_delayed = round(average_flights_delayed * 100, 2)
print(f"Average percentage of delayed flights: {average_flights_delayed}%")

# get average minutes delayed by Statistics > Minutes Delayed > Security
minutes_delayed = [airport['Statistics']['Minutes Delayed']['Security'] for airport in filtered_output]
average_minutes_delayed = [minutes_delayed[i] / delayed_flights[i] for i in range(len(minutes_delayed)) if delayed_flights[i] != 0]
average_minutes_delayed = [round(minutes, 2) for minutes in average_minutes_delayed]

# round to 2 decimal places et al
average_minutes_delayed = round(sum(average_minutes_delayed) / len(average_minutes_delayed), 2)
print(f"Average minutes delayed: {average_minutes_delayed} minutes")
