import pandas
import sys
from place_card import place_card as pc
from scrape_by_placecard import scrape

def scrapeState(state):
    """scrape data in the given state"""
    
    df = pandas.read_csv('us_postal_codes.csv')
    state_df = df[df['abbr'] == state]
    county_names = set(state_df.county.tolist())
    for name in county_names:
        scrapeCounty(name, state)

def scrapeCounty(county_name, state):
    """scrape data in the given county"""

    df = pandas.read_csv('us_postal_codes.csv')
    county_df = df[(df['county'] == county_name) & (df['abbr'] == state)]
    for index, row in county_df.iterrows():
        place_card = pc(row['place'], row['abbr'], row['zip_code'])
        try:
            scrape(place_card.toDict())
        except Exception:
            with open ("log.txt", 'a') as file:
                file.writelines("There is something wrong with {}.\n".format(row['zip_code']))

# Example: python3 scrapper.py county Dallas TX
if __name__ == "__main__":
    if sys.argv[1].lower() == "state":
        scrapeState(sys.argv[2])
    elif sys.argv[1].lower() == "county":
        scrapeCounty(sys.argv[2], sys.argv[3])
    else:
        print("Invalid input.")