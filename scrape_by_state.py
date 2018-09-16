import pandas
from place_card import place_card as pc
from scrape_by_placecard import scrape

def scrapeState(state):
    """scrape data in the given state"""
    
    df = pandas.read_csv('us_postal_codes.csv')
    state_df = df[df['abbr'] == state]
    county_names = set(state_df.county.tolist())
    for name in county_names:
        scrapeCounty(name)

def scrapeCounty(county_name):
    """scrape data in the given county"""

    df = pandas.read_csv('us_postal_codes.csv')
    county_df = df[df['county'] == county_name]
    for row in county_df.iterrows():
        place_card = pc(row['place'], row['abbr'], row['zip_code'])
        try:
            scrape(place_card.toDict())
        except Exception:
            with open ("log.txt", 'w') as file:
                file.writelines("There is something wrong with {}.\n".format(row['zip_code']))
        
# test in Collin
# scrapeCounty('Collin')
        
