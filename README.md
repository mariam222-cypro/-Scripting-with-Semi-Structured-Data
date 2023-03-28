# JSON to CSV Conversion Script
This project aims to convert JSON files to CSV files with specific columns using Python.

## Problem Description

In 2012, URL shortening service Bitly partnered with the US government website USA.gov to provide a feed of anonymous data gathered from users who shorten links ending with .gov or .mil. The text file comes in JSON format with various keys and their descriptions. The task is to transform these JSON files to CSV files with specific columns while ensuring that there are no NaN values in the final dataframes.

## Requirements

The following libraries are required for running the script:

- pandas
- json
- os


### The JSON file comes in the following format:


- a: Denotes information about the web browser and operating system
- tz: Time zone
- r: URL the user came from
- u: URL where the user headed to
- t: Timestamp when the user started using the website in UNIX format
- hc: Timestamp when the user exited the website in UNIX format
- cy: City from which the request was initiated
- ll: Longitude and Latitude


## Usage

- Place the JSON files in the data directory.
- Run the json_to_csv.py script.
- The CSV files will be saved in the output directory.

## Output

The CSV files generated will have the following columns:

- web_browser: The web browser that has requested the service
- operating_sys: The operating system that initiated this request
- from_url: The main URL the user came from
- to_url: The URL where the user headed to
- city: The city from which the request was sent
- longitude: The longitude where the request was sent
- latitude: The latitude where the request was sent
- time_zone: The time zone that the city follows
- time_in: Time when the request started
- time_out: Time when the request ended

If the retrieved URL was in a long format like http://www.facebook.com/l/7AQEFzjSi/1.usa.gov/wfLQtf, it will appear in the file in a short format like www.facebook.com. If any of the columns have NaN values, the script will ensure that they are filled before writing the final CSV files.

This project aims to transform JSON files of anonymous data gathered from users who shortened links ending with .gov or .mil by URL shortening service Bitly in partnership with the US government website USA.gov. 

The transformed data will be saved as separate CSV files in a target directory.





