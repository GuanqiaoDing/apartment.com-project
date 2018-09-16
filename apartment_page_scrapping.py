import requests
import bs4

class apartment_page:
    """scrape apartment information"""
    
    def __init__(self, url):
        self.url = url
        self.pageObj = self.getPage()
        self.name = self.getName()
        self.address = self.getAddress()
        self.data = self.getData()
    
    def getPage(self):
        """get bs object"""
        
        header = {'User-Agent': 'My user agent'}
        try:
            html = requests.get(self.url, headers=header)
        except requests.exceptions.RequestException:
            return None
        pageObj = bs4.BeautifulSoup(html.text, features='html5lib')
        return pageObj
    
    def getName(self):
        """get apartment name"""
        return self.pageObj.find('h1', {'class': 'propertyName'}).text.strip()
    
    def getAddress(self):
        """get apartment address"""
        
        address = ""
        strings = self.pageObj.find('div', {'class': 'propertyAddress'}).h2.find_all('span')
        for strs in strings:
            address += strs.text
            address += ","
        address = address.rstrip(',')
        return address

    def getData(self):
        """get apartment data"""
        
        data = {}
        rent_info = self.pageObj.find_all('span', {'class': 'rentRollup'})
        for item in rent_info:
            key = item.find('span', {'class': 'shortText'}).text.strip()
            string = "".join([t for t in item.contents if type(t) == bs4.element.NavigableString])
            value = string.strip()
            data[key] = value
        return data
    
    def toDict(self):
        """orgnize the apartment's information into a dictionary"""
        return {'Name': self.name, 'Address': self.address, 'url': self.url, 'Data': self.data}