import csv
from main_page_scrapping import main_page as mp
from apartment_page_scrapping import apartment_page as ap
from place_card import place_card as pc

def scrape(place_dict):
    """scrape all the apartment pages given a placecard dictionary"""
    
    mp(place_dict)
    with open(place_dict['links_file'], 'r') as file:
        links = [link.rstrip() for link in file.readlines()]
    
        data = []
        for link in links:
            apartment_result = ap(link)
            print(apartment_result.toDict())
            data.append(apartment_result.toDict())
        keys = data[0].keys()
        with open(place_dict['data_file'], 'w') as file:
            dict_writer = csv.DictWriter(file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)

# test in Richardson 75081
# test_place = pc('Richardson', 'TX', '75081').toDict()
# scrape(test_place)
