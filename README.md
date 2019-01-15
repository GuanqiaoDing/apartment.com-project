# web-crawler

## Objective
Acquire as much data from https://www.apartments.com as possible. Scrape and organize data by state or county. The full list of zip_code, county and state can be found in [us_postal_codes.csv](./us_postal_codes.csv).

## Usage
- Two python library, [beautifulsoup4](https://pypi.org/project/beautifulsoup4/) and [pandas](http://pandas.pydata.org) are used in the program. Use `pip3 install` command to install the libraries if you do not have them yet.
- Execute scrapper.py with python3 in the format `python3 scrapper.py [arg1] [arg2] [arg3]`.
	- Example: `python3 scrapper.py county Dallas TX`
	- The first argument is either 'state' or 'county' which tells the program to scrape by state or county. The second and third arguments specify county name and state abbreviation respectively.
	- Make sure your working directory is in your Python's `sys.path`.

## Output
- The program generates a .csv file for each zip_code region which contains apartment (complex) name, address, link and listing data. The listing data is categorized based on the information on the website and it is a python dictionary object for easier processing.
- Note that the .csv files have similar names and can be concatenated simply by `cat *.csv > merged.csv` command.
- A number of zip codes are not documented in apartment.com (often represents tiny region or even single property). The program handles this exception by recording these zip codes in log.txt file.

## Test
Apartment data in Dallas and Collin county of Texas has been tested. (as of 09/16/2018)

## Acknowledgement
The project was assigned in the UTDevelopers Group. I truly appreciate the help from members in the group. Please give feedbakcs if there is any suggestions and comments.
