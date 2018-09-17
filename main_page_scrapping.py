import requests
from bs4 import BeautifulSoup

class main_page:
    """Scrape apartment links from city's search page"""
    
    def __init__(self, place_dict):
        self.Dict = place_dict
        self.pageObj = self.getPage(self.Dict['url'])
        self.links = self.getLinks()
        self.save()
    
    def getPage(self, url):
        """get bs object from url"""
        
        header = {'User-Agent': 'My user agent'}
        try:
            html = requests.get(url, headers=header)
        except requests.exceptions.RequestException:
            return None
        pageObj = BeautifulSoup(html.text, features='html5lib')
        return pageObj
    
    def getTotalPageNumber(self):
        """get the total number of pages that hold all the apartments"""
        
        try:
            ref = self.pageObj.find('div', {'id': "paging"}).find_all('a')
        except AttributeError:
            return 0
        return int(ref[-2].text)

    def getLinks(self):
        """get links from each page of the search result"""
        
        total = self.getTotalPageNumber()
        links = []
        for page in range(1, total + 1):
            number = len(links)
            print("Start scrapping on page {} of {}:".format(page, self.Dict['zip_code']))
            cur_url = self.Dict['url'] + str(page)
            html = self.getPage(cur_url)
            for item in html.find('div', {'id': 'placardContainer'}).ul.find_all('article'):
                if 'data-url' in item.attrs:
                    links.append(item.attrs['data-url'])
            print("Finished page {} of {}.".format(page, self.Dict['zip_code']))
            print("Added {} links from this page.".format(len(links) - number))
            print()
        return links
    
    def save(self):
        """save the links scrapped from the city's search page"""
        
        if len(self.links) != 0:
            with open(self.Dict['links_file'], 'w') as file:
                file.writelines("%s\n" % link for link in self.links)
