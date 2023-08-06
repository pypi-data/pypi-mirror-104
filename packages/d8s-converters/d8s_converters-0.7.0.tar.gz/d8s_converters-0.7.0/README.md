# Democritus Converters

[![PyPI](https://img.shields.io/pypi/v/d8s-converters.svg)](https://pypi.python.org/pypi/d8s-converters)
[![CI](https://github.com/democritus-project/d8s-converters/workflows/CI/badge.svg)](https://github.com/democritus-project/d8s-converters/actions)
[![Lint](https://github.com/democritus-project/d8s-converters/workflows/Lint/badge.svg)](https://github.com/democritus-project/d8s-converters/actions)
[![codecov](https://codecov.io/gh/democritus-project/d8s-converters/branch/main/graph/badge.svg?token=V0WOIXRGMM)](https://codecov.io/gh/democritus-project/d8s-converters)
[![The Democritus Project uses semver version 2.0.0](https://img.shields.io/badge/-semver%20v2.0.0-22bfda)](https://semver.org/spec/v2.0.0.html)
[![The Democritus Project uses black to format code](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://choosealicense.com/licenses/lgpl-3.0/)

Democritus functions<sup>[1]</sup> for easily converting dates, times, temperatures, and distances.

[1] Democritus functions are <i>simple, effective, modular, well-tested, and well-documented</i> Python functions.

We use `d8s` as an abbreviation for `democritus` (you can read more about this [here](https://github.com/democritus-project/roadmap#what-is-d8s)).

## Functions

  - ```python
    def convert(quantity: Union[int, float], starting_unit: str, converted_unit: str):
        """Convert the quantity from the starting_unit to the converted_unit."""
    ```
  - ```python
    def seconds_to_minutes(seconds):
        """Convert seconds to minutes."""
    ```
  - ```python
    def seconds_to_hours(seconds):
        """Convert seconds to hours."""
    ```
  - ```python
    def seconds_to_days(seconds):
        """Convert seconds to days."""
    ```
  - ```python
    def seconds_to_weeks(seconds):
        """Convert seconds to weeks."""
    ```
  - ```python
    def seconds_to_fortnights(seconds):
        """Convert seconds to fortnights."""
    ```
  - ```python
    def seconds_to_years(seconds):
        """Convert seconds to years."""
    ```
  - ```python
    def seconds_to_months(seconds):
        """Convert seconds to months."""
    ```
  - ```python
    def seconds_to_centuries(seconds):
        """Convert seconds to centuries."""
    ```
  - ```python
    def seconds_to_millenniums(seconds):
        """Convert seconds to millenniums."""
    ```
  - ```python
    def minutes_to_seconds(minutes):
        """Convert minutes to seconds."""
    ```
  - ```python
    def minutes_to_hours(minutes):
        """Convert minutes to hours."""
    ```
  - ```python
    def minutes_to_days(minutes):
        """Convert minutes to days."""
    ```
  - ```python
    def minutes_to_weeks(minutes):
        """Convert minutes to weeks."""
    ```
  - ```python
    def minutes_to_fortnights(minutes):
        """Convert minutes to fortnights."""
    ```
  - ```python
    def minutes_to_years(minutes):
        """Convert minutes to years."""
    ```
  - ```python
    def minutes_to_months(minutes):
        """Convert minutes to months."""
    ```
  - ```python
    def minutes_to_centuries(minutes):
        """Convert minutes to centuries."""
    ```
  - ```python
    def minutes_to_millenniums(minutes):
        """Convert minutes to millenniums."""
    ```
  - ```python
    def hours_to_seconds(hours):
        """Convert hours to seconds."""
    ```
  - ```python
    def hours_to_minutes(hours):
        """Convert hours to minutes."""
    ```
  - ```python
    def hours_to_days(hours):
        """Convert hours to days."""
    ```
  - ```python
    def hours_to_weeks(hours):
        """Convert hours to weeks."""
    ```
  - ```python
    def hours_to_fortnights(hours):
        """Convert hours to fortnights."""
    ```
  - ```python
    def hours_to_years(hours):
        """Convert hours to years."""
    ```
  - ```python
    def hours_to_months(hours):
        """Convert hours to months."""
    ```
  - ```python
    def hours_to_centuries(hours):
        """Convert hours to centuries."""
    ```
  - ```python
    def hours_to_millenniums(hours):
        """Convert hours to millenniums."""
    ```
  - ```python
    def days_to_seconds(days):
        """Convert days to seconds."""
    ```
  - ```python
    def days_to_minutes(days):
        """Convert days to minutes."""
    ```
  - ```python
    def days_to_hours(days):
        """Convert days to hours."""
    ```
  - ```python
    def days_to_weeks(days):
        """Convert days to weeks."""
    ```
  - ```python
    def days_to_fortnights(days):
        """Convert days to fortnights."""
    ```
  - ```python
    def days_to_years(days):
        """Convert days to years."""
    ```
  - ```python
    def days_to_months(days):
        """Convert days to months."""
    ```
  - ```python
    def days_to_centuries(days):
        """Convert days to centuries."""
    ```
  - ```python
    def days_to_millenniums(days):
        """Convert days to millenniums."""
    ```
  - ```python
    def weeks_to_seconds(weeks):
        """Convert weeks to seconds."""
    ```
  - ```python
    def weeks_to_minutes(weeks):
        """Convert weeks to minutes."""
    ```
  - ```python
    def weeks_to_hours(weeks):
        """Convert weeks to hours."""
    ```
  - ```python
    def weeks_to_days(weeks):
        """Convert weeks to days."""
    ```
  - ```python
    def weeks_to_fortnights(weeks):
        """Convert weeks to fortnights."""
    ```
  - ```python
    def weeks_to_years(weeks):
        """Convert weeks to years."""
    ```
  - ```python
    def weeks_to_months(weeks):
        """Convert weeks to months."""
    ```
  - ```python
    def weeks_to_centuries(weeks):
        """Convert weeks to centuries."""
    ```
  - ```python
    def weeks_to_millenniums(weeks):
        """Convert weeks to millenniums."""
    ```
  - ```python
    def fortnights_to_seconds(fortnights):
        """Convert fortnights to seconds."""
    ```
  - ```python
    def fortnights_to_minutes(fortnights):
        """Convert fortnights to minutes."""
    ```
  - ```python
    def fortnights_to_hours(fortnights):
        """Convert fortnights to hours."""
    ```
  - ```python
    def fortnights_to_days(fortnights):
        """Convert fortnights to days."""
    ```
  - ```python
    def fortnights_to_weeks(fortnights):
        """Convert fortnights to weeks."""
    ```
  - ```python
    def fortnights_to_years(fortnights):
        """Convert fortnights to years."""
    ```
  - ```python
    def fortnights_to_months(fortnights):
        """Convert fortnights to months."""
    ```
  - ```python
    def fortnights_to_centuries(fortnights):
        """Convert fortnights to centuries."""
    ```
  - ```python
    def fortnights_to_millenniums(fortnights):
        """Convert fortnights to millenniums."""
    ```
  - ```python
    def years_to_seconds(years):
        """Convert years to seconds."""
    ```
  - ```python
    def years_to_minutes(years):
        """Convert years to minutes."""
    ```
  - ```python
    def years_to_hours(years):
        """Convert years to hours."""
    ```
  - ```python
    def years_to_days(years):
        """Convert years to days."""
    ```
  - ```python
    def years_to_weeks(years):
        """Convert years to weeks."""
    ```
  - ```python
    def years_to_fortnights(years):
        """Convert years to fortnights."""
    ```
  - ```python
    def years_to_months(years):
        """Convert years to months."""
    ```
  - ```python
    def years_to_centuries(years):
        """Convert years to centuries."""
    ```
  - ```python
    def years_to_millenniums(years):
        """Convert years to millenniums."""
    ```
  - ```python
    def months_to_seconds(months):
        """Convert months to seconds."""
    ```
  - ```python
    def months_to_minutes(months):
        """Convert months to minutes."""
    ```
  - ```python
    def months_to_hours(months):
        """Convert months to hours."""
    ```
  - ```python
    def months_to_days(months):
        """Convert months to days."""
    ```
  - ```python
    def months_to_weeks(months):
        """Convert months to weeks."""
    ```
  - ```python
    def months_to_fortnights(months):
        """Convert months to fortnights."""
    ```
  - ```python
    def months_to_years(months):
        """Convert months to years."""
    ```
  - ```python
    def months_to_centuries(months):
        """Convert months to centuries."""
    ```
  - ```python
    def months_to_millenniums(months):
        """Convert months to millenniums."""
    ```
  - ```python
    def centuries_to_seconds(centuries):
        """Convert centuries to seconds."""
    ```
  - ```python
    def centuries_to_minutes(centuries):
        """Convert centuries to minutes."""
    ```
  - ```python
    def centuries_to_hours(centuries):
        """Convert centuries to hours."""
    ```
  - ```python
    def centuries_to_days(centuries):
        """Convert centuries to days."""
    ```
  - ```python
    def centuries_to_weeks(centuries):
        """Convert centuries to weeks."""
    ```
  - ```python
    def centuries_to_fortnights(centuries):
        """Convert centuries to fortnights."""
    ```
  - ```python
    def centuries_to_years(centuries):
        """Convert centuries to years."""
    ```
  - ```python
    def centuries_to_months(centuries):
        """Convert centuries to months."""
    ```
  - ```python
    def centuries_to_millenniums(centuries):
        """Convert centuries to millenniums."""
    ```
  - ```python
    def millenniums_to_seconds(millenniums):
        """Convert millenniums to seconds."""
    ```
  - ```python
    def millenniums_to_minutes(millenniums):
        """Convert millenniums to minutes."""
    ```
  - ```python
    def millenniums_to_hours(millenniums):
        """Convert millenniums to hours."""
    ```
  - ```python
    def millenniums_to_days(millenniums):
        """Convert millenniums to days."""
    ```
  - ```python
    def millenniums_to_weeks(millenniums):
        """Convert millenniums to weeks."""
    ```
  - ```python
    def millenniums_to_fortnights(millenniums):
        """Convert millenniums to fortnights."""
    ```
  - ```python
    def millenniums_to_years(millenniums):
        """Convert millenniums to years."""
    ```
  - ```python
    def millenniums_to_months(millenniums):
        """Convert millenniums to months."""
    ```
  - ```python
    def millenniums_to_centuries(millenniums):
        """Convert millenniums to centuries."""
    ```
  - ```python
    def meters_to_centimeters(meters):
        """Convert meters to centimeters."""
    ```
  - ```python
    def meters_to_millimeters(meters):
        """Convert meters to millimeters."""
    ```
  - ```python
    def meters_to_kilometers(meters):
        """Convert meters to kilometers."""
    ```
  - ```python
    def meters_to_inches(meters):
        """Convert meters to inches."""
    ```
  - ```python
    def meters_to_hands(meters):
        """Convert meters to hands."""
    ```
  - ```python
    def meters_to_feet(meters):
        """Convert meters to feet."""
    ```
  - ```python
    def meters_to_yards(meters):
        """Convert meters to yards."""
    ```
  - ```python
    def meters_to_miles(meters):
        """Convert meters to miles."""
    ```
  - ```python
    def meters_to_light_years(meters):
        """Convert meters to light years."""
    ```
  - ```python
    def meters_to_astronomical_units(meters):
        """Convert meters to astronomical units."""
    ```
  - ```python
    def meters_to_parsecs(meters):
        """Convert meters to parsecs."""
    ```
  - ```python
    def meters_to_nautical_miles(meters):
        """Convert meters to nautical miles."""
    ```
  - ```python
    def meters_to_angstroms(meters):
        """Convert meters to angstroms."""
    ```
  - ```python
    def meters_to_microns(meters):
        """Convert meters to microns."""
    ```
  - ```python
    def meters_to_planck_lengths(meters):
        """Convert meters to planck lengths."""
    ```
  - ```python
    def centimeters_to_meters(centimeters):
        """Convert centimeters to meters."""
    ```
  - ```python
    def centimeters_to_millimeters(centimeters):
        """Convert centimeters to millimeters."""
    ```
  - ```python
    def centimeters_to_kilometers(centimeters):
        """Convert centimeters to kilometers."""
    ```
  - ```python
    def centimeters_to_inches(centimeters):
        """Convert centimeters to inches."""
    ```
  - ```python
    def centimeters_to_hands(centimeters):
        """Convert centimeters to hands."""
    ```
  - ```python
    def centimeters_to_feet(centimeters):
        """Convert centimeters to feet."""
    ```
  - ```python
    def centimeters_to_yards(centimeters):
        """Convert centimeters to yards."""
    ```
  - ```python
    def centimeters_to_miles(centimeters):
        """Convert centimeters to miles."""
    ```
  - ```python
    def centimeters_to_light_years(centimeters):
        """Convert centimeters to light years."""
    ```
  - ```python
    def centimeters_to_astronomical_units(centimeters):
        """Convert centimeters to astronomical units."""
    ```
  - ```python
    def centimeters_to_parsecs(centimeters):
        """Convert centimeters to parsecs."""
    ```
  - ```python
    def centimeters_to_nautical_miles(centimeters):
        """Convert centimeters to nautical miles."""
    ```
  - ```python
    def centimeters_to_angstroms(centimeters):
        """Convert centimeters to angstroms."""
    ```
  - ```python
    def centimeters_to_microns(centimeters):
        """Convert centimeters to microns."""
    ```
  - ```python
    def centimeters_to_planck_lengths(centimeters):
        """Convert centimeters to planck lengths."""
    ```
  - ```python
    def millimeters_to_meters(millimeters):
        """Convert millimeters to meters."""
    ```
  - ```python
    def millimeters_to_centimeters(millimeters):
        """Convert millimeters to centimeters."""
    ```
  - ```python
    def millimeters_to_kilometers(millimeters):
        """Convert millimeters to kilometers."""
    ```
  - ```python
    def millimeters_to_inches(millimeters):
        """Convert millimeters to inches."""
    ```
  - ```python
    def millimeters_to_hands(millimeters):
        """Convert millimeters to hands."""
    ```
  - ```python
    def millimeters_to_feet(millimeters):
        """Convert millimeters to feet."""
    ```
  - ```python
    def millimeters_to_yards(millimeters):
        """Convert millimeters to yards."""
    ```
  - ```python
    def millimeters_to_miles(millimeters):
        """Convert millimeters to miles."""
    ```
  - ```python
    def millimeters_to_light_years(millimeters):
        """Convert millimeters to light years."""
    ```
  - ```python
    def millimeters_to_astronomical_units(millimeters):
        """Convert millimeters to astronomical units."""
    ```
  - ```python
    def millimeters_to_parsecs(millimeters):
        """Convert millimeters to parsecs."""
    ```
  - ```python
    def millimeters_to_nautical_miles(millimeters):
        """Convert millimeters to nautical miles."""
    ```
  - ```python
    def millimeters_to_angstroms(millimeters):
        """Convert millimeters to angstroms."""
    ```
  - ```python
    def millimeters_to_microns(millimeters):
        """Convert millimeters to microns."""
    ```
  - ```python
    def millimeters_to_planck_lengths(millimeters):
        """Convert millimeters to planck lengths."""
    ```
  - ```python
    def kilometers_to_meters(kilometers):
        """Convert kilometers to meters."""
    ```
  - ```python
    def kilometers_to_centimeters(kilometers):
        """Convert kilometers to centimeters."""
    ```
  - ```python
    def kilometers_to_millimeters(kilometers):
        """Convert kilometers to millimeters."""
    ```
  - ```python
    def kilometers_to_inches(kilometers):
        """Convert kilometers to inches."""
    ```
  - ```python
    def kilometers_to_hands(kilometers):
        """Convert kilometers to hands."""
    ```
  - ```python
    def kilometers_to_feet(kilometers):
        """Convert kilometers to feet."""
    ```
  - ```python
    def kilometers_to_yards(kilometers):
        """Convert kilometers to yards."""
    ```
  - ```python
    def kilometers_to_miles(kilometers):
        """Convert kilometers to miles."""
    ```
  - ```python
    def kilometers_to_light_years(kilometers):
        """Convert kilometers to light years."""
    ```
  - ```python
    def kilometers_to_astronomical_units(kilometers):
        """Convert kilometers to astronomical units."""
    ```
  - ```python
    def kilometers_to_parsecs(kilometers):
        """Convert kilometers to parsecs."""
    ```
  - ```python
    def kilometers_to_nautical_miles(kilometers):
        """Convert kilometers to nautical miles."""
    ```
  - ```python
    def kilometers_to_angstroms(kilometers):
        """Convert kilometers to angstroms."""
    ```
  - ```python
    def kilometers_to_microns(kilometers):
        """Convert kilometers to microns."""
    ```
  - ```python
    def kilometers_to_planck_lengths(kilometers):
        """Convert kilometers to planck lengths."""
    ```
  - ```python
    def inches_to_meters(inches):
        """Convert inches to meters."""
    ```
  - ```python
    def inches_to_centimeters(inches):
        """Convert inches to centimeters."""
    ```
  - ```python
    def inches_to_millimeters(inches):
        """Convert inches to millimeters."""
    ```
  - ```python
    def inches_to_kilometers(inches):
        """Convert inches to kilometers."""
    ```
  - ```python
    def inches_to_hands(inches):
        """Convert inches to hands."""
    ```
  - ```python
    def inches_to_feet(inches):
        """Convert inches to feet."""
    ```
  - ```python
    def inches_to_yards(inches):
        """Convert inches to yards."""
    ```
  - ```python
    def inches_to_miles(inches):
        """Convert inches to miles."""
    ```
  - ```python
    def inches_to_light_years(inches):
        """Convert inches to light years."""
    ```
  - ```python
    def inches_to_astronomical_units(inches):
        """Convert inches to astronomical units."""
    ```
  - ```python
    def inches_to_parsecs(inches):
        """Convert inches to parsecs."""
    ```
  - ```python
    def inches_to_nautical_miles(inches):
        """Convert inches to nautical miles."""
    ```
  - ```python
    def inches_to_angstroms(inches):
        """Convert inches to angstroms."""
    ```
  - ```python
    def inches_to_microns(inches):
        """Convert inches to microns."""
    ```
  - ```python
    def inches_to_planck_lengths(inches):
        """Convert inches to planck lengths."""
    ```
  - ```python
    def hands_to_meters(hands):
        """Convert hands to meters."""
    ```
  - ```python
    def hands_to_centimeters(hands):
        """Convert hands to centimeters."""
    ```
  - ```python
    def hands_to_millimeters(hands):
        """Convert hands to millimeters."""
    ```
  - ```python
    def hands_to_kilometers(hands):
        """Convert hands to kilometers."""
    ```
  - ```python
    def hands_to_inches(hands):
        """Convert hands to inches."""
    ```
  - ```python
    def hands_to_feet(hands):
        """Convert hands to feet."""
    ```
  - ```python
    def hands_to_yards(hands):
        """Convert hands to yards."""
    ```
  - ```python
    def hands_to_miles(hands):
        """Convert hands to miles."""
    ```
  - ```python
    def hands_to_light_years(hands):
        """Convert hands to light years."""
    ```
  - ```python
    def hands_to_astronomical_units(hands):
        """Convert hands to astronomical units."""
    ```
  - ```python
    def hands_to_parsecs(hands):
        """Convert hands to parsecs."""
    ```
  - ```python
    def hands_to_nautical_miles(hands):
        """Convert hands to nautical miles."""
    ```
  - ```python
    def hands_to_angstroms(hands):
        """Convert hands to angstroms."""
    ```
  - ```python
    def hands_to_microns(hands):
        """Convert hands to microns."""
    ```
  - ```python
    def hands_to_planck_lengths(hands):
        """Convert hands to planck lengths."""
    ```
  - ```python
    def feet_to_meters(feet):
        """Convert feet to meters."""
    ```
  - ```python
    def feet_to_centimeters(feet):
        """Convert feet to centimeters."""
    ```
  - ```python
    def feet_to_millimeters(feet):
        """Convert feet to millimeters."""
    ```
  - ```python
    def feet_to_kilometers(feet):
        """Convert feet to kilometers."""
    ```
  - ```python
    def feet_to_inches(feet):
        """Convert feet to inches."""
    ```
  - ```python
    def feet_to_hands(feet):
        """Convert feet to hands."""
    ```
  - ```python
    def feet_to_yards(feet):
        """Convert feet to yards."""
    ```
  - ```python
    def feet_to_miles(feet):
        """Convert feet to miles."""
    ```
  - ```python
    def feet_to_light_years(feet):
        """Convert feet to light years."""
    ```
  - ```python
    def feet_to_astronomical_units(feet):
        """Convert feet to astronomical units."""
    ```
  - ```python
    def feet_to_parsecs(feet):
        """Convert feet to parsecs."""
    ```
  - ```python
    def feet_to_nautical_miles(feet):
        """Convert feet to nautical miles."""
    ```
  - ```python
    def feet_to_angstroms(feet):
        """Convert feet to angstroms."""
    ```
  - ```python
    def feet_to_microns(feet):
        """Convert feet to microns."""
    ```
  - ```python
    def feet_to_planck_lengths(feet):
        """Convert feet to planck lengths."""
    ```
  - ```python
    def yards_to_meters(yards):
        """Convert yards to meters."""
    ```
  - ```python
    def yards_to_centimeters(yards):
        """Convert yards to centimeters."""
    ```
  - ```python
    def yards_to_millimeters(yards):
        """Convert yards to millimeters."""
    ```
  - ```python
    def yards_to_kilometers(yards):
        """Convert yards to kilometers."""
    ```
  - ```python
    def yards_to_inches(yards):
        """Convert yards to inches."""
    ```
  - ```python
    def yards_to_hands(yards):
        """Convert yards to hands."""
    ```
  - ```python
    def yards_to_feet(yards):
        """Convert yards to feet."""
    ```
  - ```python
    def yards_to_miles(yards):
        """Convert yards to miles."""
    ```
  - ```python
    def yards_to_light_years(yards):
        """Convert yards to light years."""
    ```
  - ```python
    def yards_to_astronomical_units(yards):
        """Convert yards to astronomical units."""
    ```
  - ```python
    def yards_to_parsecs(yards):
        """Convert yards to parsecs."""
    ```
  - ```python
    def yards_to_nautical_miles(yards):
        """Convert yards to nautical miles."""
    ```
  - ```python
    def yards_to_angstroms(yards):
        """Convert yards to angstroms."""
    ```
  - ```python
    def yards_to_microns(yards):
        """Convert yards to microns."""
    ```
  - ```python
    def yards_to_planck_lengths(yards):
        """Convert yards to planck lengths."""
    ```
  - ```python
    def miles_to_meters(miles):
        """Convert miles to meters."""
    ```
  - ```python
    def miles_to_centimeters(miles):
        """Convert miles to centimeters."""
    ```
  - ```python
    def miles_to_millimeters(miles):
        """Convert miles to millimeters."""
    ```
  - ```python
    def miles_to_kilometers(miles):
        """Convert miles to kilometers."""
    ```
  - ```python
    def miles_to_inches(miles):
        """Convert miles to inches."""
    ```
  - ```python
    def miles_to_hands(miles):
        """Convert miles to hands."""
    ```
  - ```python
    def miles_to_feet(miles):
        """Convert miles to feet."""
    ```
  - ```python
    def miles_to_yards(miles):
        """Convert miles to yards."""
    ```
  - ```python
    def miles_to_light_years(miles):
        """Convert miles to light years."""
    ```
  - ```python
    def miles_to_astronomical_units(miles):
        """Convert miles to astronomical units."""
    ```
  - ```python
    def miles_to_parsecs(miles):
        """Convert miles to parsecs."""
    ```
  - ```python
    def miles_to_nautical_miles(miles):
        """Convert miles to nautical miles."""
    ```
  - ```python
    def miles_to_angstroms(miles):
        """Convert miles to angstroms."""
    ```
  - ```python
    def miles_to_microns(miles):
        """Convert miles to microns."""
    ```
  - ```python
    def miles_to_planck_lengths(miles):
        """Convert miles to planck lengths."""
    ```
  - ```python
    def light_years_to_meters(light_years):
        """Convert light years to meters."""
    ```
  - ```python
    def light_years_to_centimeters(light_years):
        """Convert light years to centimeters."""
    ```
  - ```python
    def light_years_to_millimeters(light_years):
        """Convert light years to millimeters."""
    ```
  - ```python
    def light_years_to_kilometers(light_years):
        """Convert light years to kilometers."""
    ```
  - ```python
    def light_years_to_inches(light_years):
        """Convert light years to inches."""
    ```
  - ```python
    def light_years_to_hands(light_years):
        """Convert light years to hands."""
    ```
  - ```python
    def light_years_to_feet(light_years):
        """Convert light years to feet."""
    ```
  - ```python
    def light_years_to_yards(light_years):
        """Convert light years to yards."""
    ```
  - ```python
    def light_years_to_miles(light_years):
        """Convert light years to miles."""
    ```
  - ```python
    def light_years_to_astronomical_units(light_years):
        """Convert light years to astronomical units."""
    ```
  - ```python
    def light_years_to_parsecs(light_years):
        """Convert light years to parsecs."""
    ```
  - ```python
    def light_years_to_nautical_miles(light_years):
        """Convert light years to nautical miles."""
    ```
  - ```python
    def light_years_to_angstroms(light_years):
        """Convert light years to angstroms."""
    ```
  - ```python
    def light_years_to_microns(light_years):
        """Convert light years to microns."""
    ```
  - ```python
    def light_years_to_planck_lengths(light_years):
        """Convert light years to planck lengths."""
    ```
  - ```python
    def astronomical_units_to_meters(astronomical_units):
        """Convert astronomical units to meters."""
    ```
  - ```python
    def astronomical_units_to_centimeters(astronomical_units):
        """Convert astronomical units to centimeters."""
    ```
  - ```python
    def astronomical_units_to_millimeters(astronomical_units):
        """Convert astronomical units to millimeters."""
    ```
  - ```python
    def astronomical_units_to_kilometers(astronomical_units):
        """Convert astronomical units to kilometers."""
    ```
  - ```python
    def astronomical_units_to_inches(astronomical_units):
        """Convert astronomical units to inches."""
    ```
  - ```python
    def astronomical_units_to_hands(astronomical_units):
        """Convert astronomical units to hands."""
    ```
  - ```python
    def astronomical_units_to_feet(astronomical_units):
        """Convert astronomical units to feet."""
    ```
  - ```python
    def astronomical_units_to_yards(astronomical_units):
        """Convert astronomical units to yards."""
    ```
  - ```python
    def astronomical_units_to_miles(astronomical_units):
        """Convert astronomical units to miles."""
    ```
  - ```python
    def astronomical_units_to_light_years(astronomical_units):
        """Convert astronomical units to light years."""
    ```
  - ```python
    def astronomical_units_to_parsecs(astronomical_units):
        """Convert astronomical units to parsecs."""
    ```
  - ```python
    def astronomical_units_to_nautical_miles(astronomical_units):
        """Convert astronomical units to nautical miles."""
    ```
  - ```python
    def astronomical_units_to_angstroms(astronomical_units):
        """Convert astronomical units to angstroms."""
    ```
  - ```python
    def astronomical_units_to_microns(astronomical_units):
        """Convert astronomical units to microns."""
    ```
  - ```python
    def astronomical_units_to_planck_lengths(astronomical_units):
        """Convert astronomical units to planck lengths."""
    ```
  - ```python
    def parsecs_to_meters(parsecs):
        """Convert parsecs to meters."""
    ```
  - ```python
    def parsecs_to_centimeters(parsecs):
        """Convert parsecs to centimeters."""
    ```
  - ```python
    def parsecs_to_millimeters(parsecs):
        """Convert parsecs to millimeters."""
    ```
  - ```python
    def parsecs_to_kilometers(parsecs):
        """Convert parsecs to kilometers."""
    ```
  - ```python
    def parsecs_to_inches(parsecs):
        """Convert parsecs to inches."""
    ```
  - ```python
    def parsecs_to_hands(parsecs):
        """Convert parsecs to hands."""
    ```
  - ```python
    def parsecs_to_feet(parsecs):
        """Convert parsecs to feet."""
    ```
  - ```python
    def parsecs_to_yards(parsecs):
        """Convert parsecs to yards."""
    ```
  - ```python
    def parsecs_to_miles(parsecs):
        """Convert parsecs to miles."""
    ```
  - ```python
    def parsecs_to_light_years(parsecs):
        """Convert parsecs to light years."""
    ```
  - ```python
    def parsecs_to_astronomical_units(parsecs):
        """Convert parsecs to astronomical units."""
    ```
  - ```python
    def parsecs_to_nautical_miles(parsecs):
        """Convert parsecs to nautical miles."""
    ```
  - ```python
    def parsecs_to_angstroms(parsecs):
        """Convert parsecs to angstroms."""
    ```
  - ```python
    def parsecs_to_microns(parsecs):
        """Convert parsecs to microns."""
    ```
  - ```python
    def parsecs_to_planck_lengths(parsecs):
        """Convert parsecs to planck lengths."""
    ```
  - ```python
    def nautical_miles_to_meters(nautical_miles):
        """Convert nautical miles to meters."""
    ```
  - ```python
    def nautical_miles_to_centimeters(nautical_miles):
        """Convert nautical miles to centimeters."""
    ```
  - ```python
    def nautical_miles_to_millimeters(nautical_miles):
        """Convert nautical miles to millimeters."""
    ```
  - ```python
    def nautical_miles_to_kilometers(nautical_miles):
        """Convert nautical miles to kilometers."""
    ```
  - ```python
    def nautical_miles_to_inches(nautical_miles):
        """Convert nautical miles to inches."""
    ```
  - ```python
    def nautical_miles_to_hands(nautical_miles):
        """Convert nautical miles to hands."""
    ```
  - ```python
    def nautical_miles_to_feet(nautical_miles):
        """Convert nautical miles to feet."""
    ```
  - ```python
    def nautical_miles_to_yards(nautical_miles):
        """Convert nautical miles to yards."""
    ```
  - ```python
    def nautical_miles_to_miles(nautical_miles):
        """Convert nautical miles to miles."""
    ```
  - ```python
    def nautical_miles_to_light_years(nautical_miles):
        """Convert nautical miles to light years."""
    ```
  - ```python
    def nautical_miles_to_astronomical_units(nautical_miles):
        """Convert nautical miles to astronomical units."""
    ```
  - ```python
    def nautical_miles_to_parsecs(nautical_miles):
        """Convert nautical miles to parsecs."""
    ```
  - ```python
    def nautical_miles_to_angstroms(nautical_miles):
        """Convert nautical miles to angstroms."""
    ```
  - ```python
    def nautical_miles_to_microns(nautical_miles):
        """Convert nautical miles to microns."""
    ```
  - ```python
    def nautical_miles_to_planck_lengths(nautical_miles):
        """Convert nautical miles to planck lengths."""
    ```
  - ```python
    def angstroms_to_meters(angstroms):
        """Convert angstroms to meters."""
    ```
  - ```python
    def angstroms_to_centimeters(angstroms):
        """Convert angstroms to centimeters."""
    ```
  - ```python
    def angstroms_to_millimeters(angstroms):
        """Convert angstroms to millimeters."""
    ```
  - ```python
    def angstroms_to_kilometers(angstroms):
        """Convert angstroms to kilometers."""
    ```
  - ```python
    def angstroms_to_inches(angstroms):
        """Convert angstroms to inches."""
    ```
  - ```python
    def angstroms_to_hands(angstroms):
        """Convert angstroms to hands."""
    ```
  - ```python
    def angstroms_to_feet(angstroms):
        """Convert angstroms to feet."""
    ```
  - ```python
    def angstroms_to_yards(angstroms):
        """Convert angstroms to yards."""
    ```
  - ```python
    def angstroms_to_miles(angstroms):
        """Convert angstroms to miles."""
    ```
  - ```python
    def angstroms_to_light_years(angstroms):
        """Convert angstroms to light years."""
    ```
  - ```python
    def angstroms_to_astronomical_units(angstroms):
        """Convert angstroms to astronomical units."""
    ```
  - ```python
    def angstroms_to_parsecs(angstroms):
        """Convert angstroms to parsecs."""
    ```
  - ```python
    def angstroms_to_nautical_miles(angstroms):
        """Convert angstroms to nautical miles."""
    ```
  - ```python
    def angstroms_to_microns(angstroms):
        """Convert angstroms to microns."""
    ```
  - ```python
    def angstroms_to_planck_lengths(angstroms):
        """Convert angstroms to planck lengths."""
    ```
  - ```python
    def microns_to_meters(microns):
        """Convert microns to meters."""
    ```
  - ```python
    def microns_to_centimeters(microns):
        """Convert microns to centimeters."""
    ```
  - ```python
    def microns_to_millimeters(microns):
        """Convert microns to millimeters."""
    ```
  - ```python
    def microns_to_kilometers(microns):
        """Convert microns to kilometers."""
    ```
  - ```python
    def microns_to_inches(microns):
        """Convert microns to inches."""
    ```
  - ```python
    def microns_to_hands(microns):
        """Convert microns to hands."""
    ```
  - ```python
    def microns_to_feet(microns):
        """Convert microns to feet."""
    ```
  - ```python
    def microns_to_yards(microns):
        """Convert microns to yards."""
    ```
  - ```python
    def microns_to_miles(microns):
        """Convert microns to miles."""
    ```
  - ```python
    def microns_to_light_years(microns):
        """Convert microns to light years."""
    ```
  - ```python
    def microns_to_astronomical_units(microns):
        """Convert microns to astronomical units."""
    ```
  - ```python
    def microns_to_parsecs(microns):
        """Convert microns to parsecs."""
    ```
  - ```python
    def microns_to_nautical_miles(microns):
        """Convert microns to nautical miles."""
    ```
  - ```python
    def microns_to_angstroms(microns):
        """Convert microns to angstroms."""
    ```
  - ```python
    def microns_to_planck_lengths(microns):
        """Convert microns to planck lengths."""
    ```
  - ```python
    def planck_lengths_to_meters(planck_lengths):
        """Convert planck lengths to meters."""
    ```
  - ```python
    def planck_lengths_to_centimeters(planck_lengths):
        """Convert planck lengths to centimeters."""
    ```
  - ```python
    def planck_lengths_to_millimeters(planck_lengths):
        """Convert planck lengths to millimeters."""
    ```
  - ```python
    def planck_lengths_to_kilometers(planck_lengths):
        """Convert planck lengths to kilometers."""
    ```
  - ```python
    def planck_lengths_to_inches(planck_lengths):
        """Convert planck lengths to inches."""
    ```
  - ```python
    def planck_lengths_to_hands(planck_lengths):
        """Convert planck lengths to hands."""
    ```
  - ```python
    def planck_lengths_to_feet(planck_lengths):
        """Convert planck lengths to feet."""
    ```
  - ```python
    def planck_lengths_to_yards(planck_lengths):
        """Convert planck lengths to yards."""
    ```
  - ```python
    def planck_lengths_to_miles(planck_lengths):
        """Convert planck lengths to miles."""
    ```
  - ```python
    def planck_lengths_to_light_years(planck_lengths):
        """Convert planck lengths to light years."""
    ```
  - ```python
    def planck_lengths_to_astronomical_units(planck_lengths):
        """Convert planck lengths to astronomical units."""
    ```
  - ```python
    def planck_lengths_to_parsecs(planck_lengths):
        """Convert planck lengths to parsecs."""
    ```
  - ```python
    def planck_lengths_to_nautical_miles(planck_lengths):
        """Convert planck lengths to nautical miles."""
    ```
  - ```python
    def planck_lengths_to_angstroms(planck_lengths):
        """Convert planck lengths to angstroms."""
    ```
  - ```python
    def planck_lengths_to_microns(planck_lengths):
        """Convert planck lengths to microns."""
    ```
  - ```python
    def celsius_to_fahrenheit(celsius_temperature):
        """Convert Celsius to Fahrenheit."""
    ```
  - ```python
    def celsius_to_kelvin(celsius_temperature):
        """Convert Celsius to Kelvin."""
    ```
  - ```python
    def fahrenheit_to_celsius(fahrenheit_temperature):
        """Convert Fahrenheit to Celsius."""
    ```
  - ```python
    def fahrenheit_to_kelvin(fahrenheit_temperature):
        """Convert Fahrenheit to Kelvin."""
    ```
  - ```python
    def kelvin_to_celsius(kelvin_temperature):
        """Convert Kelvin to Celsius."""
    ```
  - ```python
    def kelvin_to_fahrenheit(kelvin_temperature):
        """Convert Kelvin to Fahrenheit."""
    ```
  - ```python
    def celsius_to_felsius(celsius_temperature):
        """Convert the celsius_temperature into the Felsius temperature (see https://xkcd.com/1923/)."""
    ```
  - ```python
    def fahrenheit_to_felsius(fahrenheit_temperature):
        """Convert the fahrenheit_temperature into the Felsius temperature (see https://xkcd.com/1923/)."""
    ```
  - ```python
    def kelvin_to_felsius(kelvin_temperature):
        """Convert the kelvin_temperature into the Felsius temperature (see https://xkcd.com/1923/)."""
    ```

## Development

👋 &nbsp;If you want to get involved in this project, we have some short, helpful guides below:

- [contribute to this project 🥇][contributing]
- [test it 🧪][local-dev]
- [lint it 🧹][local-dev]
- [explore it 🔭][local-dev]

If you have any questions or there is anything we did not cover, please raise an issue and we'll be happy to help.

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and Floyd Hightower's [Python project template](https://github.com/fhightower-templates/python-project-template).

[contributing]: https://github.com/democritus-project/.github/blob/main/CONTRIBUTING.md#contributing-a-pr-
[local-dev]: https://github.com/democritus-project/.github/blob/main/CONTRIBUTING.md#local-development-
