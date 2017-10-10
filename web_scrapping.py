import numpy as np
import requests
from lxml import html

USERNAME = 'vision87'
PASSWORD = 'Welcome123!'

LOGIN_URL = 'https://www.centraldispatch.com/login?uri=%2Fprotected%2F'
URL = 'https://www.centraldispatch.com/protected/listing-search'

def main():
    def login():
        session_requests = requests.session()

        # Get login csrf token
        result = session_requests.get(LOGIN_URL)
        tree = html.fromstring(result.text)
        authenticity_token = list(set(tree.xpath('//input[@name="CSRFToken"]/@value')))[0]

        # Create payload
        payload = {
            'Username': USERNAME, 
            'Password': PASSWORD, 
            'KeepLoggedIn':'on',
            'submit':'Log In',
            'CSRFToken': authenticity_token
        }

        # Perform login
        result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))
        print(result.url)
        
        # Scrape url
        select_page = session_requests.get(URL, headers = dict(referer = URL))
        print(select_page.url)
        # select = html.fromstring(select_page.content)

        # Get login csrf token
        #result = session_requests.get('https://www.centraldispatch.com/protected/listing-search')
        #print(result.url)
        tree_select = html.fromstring(select_page.text)
        authenticity_token_select = list(set(tree_select.xpath('//input[@name="CSRFToken"]/@value')))[0]
        print(authenticity_token_select)
        scemail_select = list(set(tree_select.xpath('//input[@name="scemail"]/@value')))[0]
        scpassword_select = list(set(tree_select.xpath('//input[@name="scpassword"]/@value')))[0]

        #create payload
        payload_select = {
            'routeBased':'0',  
            'scemail':scemail_select,
            'scpassword':scpassword_select,
            's':'',
            '_redirectAction':'/Knowledgebase/List',
            'origin[valid]':'1',
            'destination[valid]':'1',         
            'origin[region]': 'All', 
            'destination[region]': 'All', 
            'vehicleType':['4','5','6','8','10'],
            'readyToShip':'60',
            'minVehicles':'1',
            'numberToShow':'500',
            'primarySort':'5',
            'secondarySort':'7',
            'btnSearch':'Search Vehicles',
            'chkSaveSearch':'1',          
            'CSRFToken': authenticity_token_select
            
        }
        
        # Perform select
        result = session_requests.post(select_page.url, data = payload_select, headers = dict(referer = select_page.url))
        print(result.url)
        print(result.content)
    login()
    
    # def select():
    #     session_requests = requests.session()

    #     # Get login csrf token
    #     result = session_requests.get('https://www.centraldispatch.com/protected/listing-search')
    #     print(result.url)
    #     tree = html.fromstring(result.text)
    #     authenticity_token = list(set(tree.xpath('//input[@name="CSRFToken"]/@value')))[0]
    #     print(authenticity_token)
        
    #     #create payload
    #     payload = {
    #         'origin[region]': 'All', 
    #         'destination[region]': 'All', 
    #         'vehicleType':['4','5','6','8','10'],
    #         'readyToShip':'60',
    #         'minVehicles':'1',
    #         'numberToShow':'500',
    #         'primarySort':'5',
    #         'secondarySort':'7',            
    #         'CSRFToken': authenticity_token,
    #         'submit':'Search Vehicles'
    #     }
        
    #     # Perform select
    #     result = session_requests.post(URL, data = payload, headers = dict(referer = URL))
    #     #print(result.url)
    #     #print(result.content)


if __name__ == '__main__':
    main()

