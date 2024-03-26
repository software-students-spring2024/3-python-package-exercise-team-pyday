How to use the service
Use links of the following types in order to access bulks files:
To get Current and Forecast bulks files:

https://bulk.openweathermap.org/snapshot/{BULK_FILE_NAME}?appid={API key}

To get access to 7-days archive of current and forecasts bulk files:

https://bulk.openweathermap.org/archive/{BULK_FILE_NAME}?appid={API key}

Parameters
{BULK_FILE_NAME}	required	Specified in the "File name" table column in the "Types of bulk files" section
appid	required	Your unique API key (you can always find it on your account page under the "API key" tab)
All bulk files available both in JSON and CSV formats. File names provided in the tables below are relevant for JSON format. If you want to upload data in the CSV formate, please change json on csv in the file name.

Examples:

JSON file name: weather_16.json.gz
CSV file name: weather_16.csv.gz

Unpack the downloaded file by using any suitable archiver software. After this is done, you will have a JSON or CSV format file that is ready to use. The file implies line-by-line processing.

Examples of bulk files can be found here: bulk samples.

To download updated weather data, please also use the same link. Data in the files get updated in accordance with the schedule found in the "Updated" column of the downloaded file.

Please note that weather data in the fill is rewritten regularly.

Types of bulk files
There are 3 types of bulk files: Current bulk, Forecasts bulks and 7-days archive weather bulks.

Please note that scheduled update times are specified in UTC.

Current weather bulks
With Current weather bulk you can upload bulk file of current weather for chosen city lists and ZIP codes locations lists.

Examples of bulk files can be found here: bulk samples. Please pay attention that weather_14.json.gz and weather_16.json.gz files refer for current weather.

File name	Number of locations	Updated, UTC time
weather_14.json.gz	22,635 cities	1 time/hour
(00:10, 01:10, 02:10,...)
weather_16.json.gz	209,579 cities	1 time/hour
(00:20, 01:20, 02:20,...)
weather_zip_eu.json.gz	153,952
EU ZIP codes	1 time/hour
(00:20, 01:20, 02:20,...)
weather_zip_us.json.gz	41,959
US ZIP codes	1 time/hour
(00:20, 01:20, 02:20,...)
weather_zip_uk.json.gz	15,225
UK ZIP codes	1 time/hour
(00:20, 01:20, 02:20,...)
Example of link to download bulk file in CSV format

https://bulk.openweathermap.org/snapshot/weather_zip_us.csv.gz?appid={API key}


If you are interested in to get Current bulk files for 7 previous days, please read "7-day archives of bulk files" section.

Forecast bulks
WIth Forecast bulk you can upload bulk file of Forecast weather with a variable data granulation for chosen cities and ZIP codes locations.

Examples of bulk files can be found here: bulk samples. Please pay attention that hourly_14.json.gz, hourly_16.json.gz, daily_14.json.gz and daily_16.json.gz files refer for forecast weather.

Hourly forecast for 4 days ahead
File name	Number of locations	Updated, UTC time
hourly1h_14.json.gz	22,635 cities	4 times/day
(03:00, 09:00, 15:00, 21:00)
hourly1h_16.json.gz	209,579 cities	4 times/day
(03:00, 09:00, 15:00, 21:00)
hourly1h_zip_eu.json.gz	153,952
EU ZIP codes	2 times/day
(08:00, 20:00)
hourly1h_zip_us.json.gz	41,959
US ZIP codes	2 times/day
(08:00, 20:00)
hourly1h_zip_uk.json.gz	15,225
UK ZIP codes	2 times/day
(08:00, 20:00)
Example of link to download bulk file in CSV format

https://bulk.openweathermap.org/snapshot/hourly1h_zip_eu.csv.gz?appid={API key}


Daily forecast for 16 days ahead
File name	Number of locations	Updated, UTC time
daily_14.json.gz	22,635 cities	2 times/day
(07:00, 19:00)
daily_16.json.gz	209,579 cities	2 times/day
(07:00, 19:00)
daily_zip_eu.json.gz	153,952
EU ZIP codes	2 times/day
(08:00, 20:00)
daily_zip_us.json.gz	41,959
US ZIP codes	2 times/day
(08:00, 20:00)
daily_zip_uk.json.gz	15,225
UK ZIP codes	2 times/day
(08:00, 20:00)
Example of link to download bulk file in CSV format

https://bulk.openweathermap.org/snapshot/daily_zip_uk.csv.gz?appid={API key}


3-hour step forecast for 5 days ahead
File name	Number of locations	Updated, UTC time
hourly_14.json.gz	22,635 cities	1 time/hour
(00:10, 01:10, 02:10,...)
hourly_16.json.gz	209,579 cities	2 times/day
(07:00, 19:00)
hourly_zip_eu.json.gz	153,952
EU ZIP codes	2 times/day
(08:00, 20:00)
hourly_zip_us.json.gz	41,959
US ZIP codes	2 times/day
(08:00, 20:00)
hourly_zip_uk.json.gz	15,225
UK ZIP codes	2 times/day
(08:00, 20:00)
Example of link to download bulk file in CSV format

https://bulk.openweathermap.org/snapshot/hourly_zip_eu.csv.gz?appid={API key}


If you are interested in to get Forecasts bulk files for 7 previous days, please read "7-day archives of bulk files" section.

7-day archive of current and forecast weather bulks files
You can get all weather bulks files for the 7 previous days. The structure of data the same as for current and forecasts bulks files.

7-day archive of current weather bulk files
File name	Number of locations	Available data per day,
UTC time
weather_14_mmddyy_hhmm.json.gz
Example of file name: weather_14_011020_0200.json.gz

22,635 cities	01:00, 02:00, 03:00, 04:00, 05:00, 06:00, 07:00, 08:00, 09:00, 10:00, 11:00, 12:00, 13:00, 14:00, 15:00, 16:00, 17:00, 18:00, 19:00, 20:00, 21:00, 22:00, 23:00, 00:00
weather_16_mmddyy_hhmm.json.gz
Example of file name: weather_16_011020_0200.json.gz

209,579 cities	01:00, 02:00, 03:00, 04:00, 05:00, 06:00, 07:00, 08:00, 09:00, 10:00, 11:00, 12:00, 13:00, 14:00, 15:00, 16:00, 17:00, 18:00, 19:00, 20:00, 21:00, 22:00, 23:00, 00:00
weather_zip_eu_mmddyy_hhmm.json.gz
Example of file name: weather_zip_eu_011020_2000.json.gz

153,952
EU ZIP codes	01:00, 02:00, 03:00, 04:00, 05:00, 06:00, 07:00, 08:00, 09:00, 10:00, 11:00, 12:00, 13:00, 14:00, 15:00, 16:00, 17:00, 18:00, 19:00, 20:00, 21:00, 22:00, 23:00, 00:00
weather_zip_us_mmddyy_hhmm.json.gz
Example of file name: weather_zip_us_011020_2000.json.gz

41,959
US ZIP codes	01:00, 02:00, 03:00, 04:00, 05:00, 06:00, 07:00, 08:00, 09:00, 10:00, 11:00, 12:00, 13:00, 14:00, 15:00, 16:00, 17:00, 18:00, 19:00, 20:00, 21:00, 22:00, 23:00, 00:00
weather_zip_uk_mmddyy_hhmm.json.gz
Example of file name: weather_zip_uk_011020_2000.json.gz

15,225
UK ZIP codes	01:00, 02:00, 03:00, 04:00, 05:00, 06:00, 07:00, 08:00, 09:00, 10:00, 11:00, 12:00, 13:00, 14:00, 15:00, 16:00, 17:00, 18:00, 19:00, 20:00, 21:00, 22:00, 23:00, 00:00
Example of link to download bulk file in CSV format

https://bulk.openweathermap.org/archive/weather_zip_uk_011020_2000.csv.gz?appid={API key}


7-day archive of hourly forecast for 4 days ahead
File name	Number of locations	Available data per day,
UTC time
hourly1h_14_mmddyy_hhmm.json.gz
Example of file name: hourly1h_14_011020_0200.json.gz

22,635 cities	02:00, 08:00, 14:00, 20:00
hourly1h_16_mmddyy_hhmm.json.gz
Example of file name: hourly1h_16_011020_0200.json.gz

209,579 cities	02:00, 08:00, 14:00, 20:00
hourly1h_zip_eu_mmddyy_hhmm.json.gz
Example of file name: hourly1h_zip_eu_011020_2000.json.gz

153,952
EU ZIP codes	07:00, 19:00
hourly1h_zip_us_mmddyy_hhmm.json.gz
Example of file name: hourly1h_zip_us_011020_2000.json.gz

41,959
US ZIP codes	07:00, 19:00
hourly1h_zip_uk_mmddyy_hhmm.json.gz
Example of file name: hourly1h_zip_uk_011020_2000.json.gz

15,225
UK ZIP codes	07:00, 19:00
7-day archive of daily forecast for 16 days ahead
File name	Number of locations	Available data per day,
UTC time
daily_14_mmddyy_hhmm.json.gz
Example of file name: daily_14_011020_0200.json.gz

22,635 cities	06:00, 18:00
daily_16_mmddyy_hhmm.json.gz
Example of file name: daily_16_011020_0200.json.gz

209,579 cities	06:00, 18:00
daily_zip_eu_mmddyy_hhmm.json.gz
Example of file name: daily_zip_eu_011020_2000.json.gz

153,952
EU ZIP codes	07:00, 19:00
daily_zip_us_mmddyy_hhmm.json.gz
Example of file name: daily_zip_us_011020_2000.json.gz

41,959
US ZIP codes	07:00, 19:00
daily_zip_uk_mmddyy_hhmm.json.gz
Example of file name: daily_uk_011020_2000.json.gz

15,225
UK ZIP codes	07:00, 19:00
7-day archive of 3-hour step forecast for 5 days ahead
File name	Number of locations	Available data per day,
UTC time
hourly_14_mmddyy_hhmm.json.gz
Example of file name: hourly_14_011020_0200.json.gz

22,635 cities	01:00, 02:00, 03:00, 04:00, 05:00, 06:00, 07:00, 08:00, 09:00, 10:00, 11:00, 12:00, 13:00, 14:00, 15:00, 16:00, 17:00, 18:00, 19:00, 20:00, 21:00, 22:00, 23:00, 00:00
hourly_16_mmddyy_hhmm.json.gz
Example of file name: hourly_16_011020_0200.json.gz

209,579 cities	06:00, 18:00
hourly_zip_eu_mmddyy_hhmm.json.gz
Example of file name: hourly_zip_eu_011020_2000.json.gz

153,952
EU ZIP codes	07:00, 19:00
hourly_zip_us_mmddyy_hhmm.json.gz
Example of file name: hourly_zip_us_011020_2000.json.gz

41,959
US ZIP codes	07:00, 19:00
hourly_zip_uk_mmddyy_hhmm.json.gz
Example of file name: hourly_uk_011020_2000.json.gz

15,225
UK ZIP codes	07:00, 19:00
Location lists
There are 5 lists of locations for each type of weather data:

List of major cities across the globe - 22,635 cities. You can download the full list of cities here
Extended cities list across the globe - 209,579 cities. You can download the full list of cities here
Full list of the US ZIP codes
Full list of the UK ZIP codes
Full list of the all europe ZIP codes
Bulk file samples
Samples of bulk files can be downloaded here: bulk samples.

Please pay attention that:

weather_14.json.gz and weather_16.json.gz files refer for current weather
hourly_14.json.gz, hourly_16.json.gz, daily_14.json.gz and daily_16.json.gz files refer for forecast weather
