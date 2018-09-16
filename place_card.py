class place_card:
    """generate a place card containing the information used for scrapping"""
    
    def __init__(self, place, state, zip_code):
        self.place = place
        self.state = state
        self.zip_code = str(zip_code)
        self.url = self.getURL()
        self.links_file_name = self.linksFile()
        self.data_file_name = self.dataFile()
    
    def getURL(self):
        return "https://www.apartments.com/" + \
            self.place.lower() + "-" + self.state.lower() + "-" + self.zip_code + "/"

    def linksFile(self):
        return self.state + '_' + self.place + '_' + self.zip_code + '_' + 'links.txt'
    
    def dataFile(self):
        return self.state + '_' + self.place + '_' + self.zip_code + '_' + 'data.csv'
    
    def toDict(self):
        return {'state': self.state, 'place': self.place, 'zip_code': self.zip_code, 
            'url':self.url, 'links_file': self.links_file_name, 'data_file': self.data_file_name}