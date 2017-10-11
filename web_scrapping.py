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
        print(authenticity_token)
        
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
        #scemail_select = list(set(tree_select.xpath('//input[@name="scemail"]/@value')))[0]
        #scpassword_select = list(set(tree_select.xpath('//input[@name="scpassword"]/@value')))[0]

        #create payload
        payload_select = {
            'routeBased':'0',
            'waypoint_valid':'1',
            'pickupRadius':'25',  
            #'scemail':scemail_select,
            #'scpassword':scpassword_select,
            #'s':'',
            #'_redirectAction':'/Knowledgebase/List',
            'origin[valid]':'1',
            'origination_valid':'1',
            'deliveryRadius':'25',
            'destination[valid]':'1',         
            'origin[region]': 'All', 
            'destination[region]': 'All',
            'destination_valid':'1',
            'FatAllowCanada':'1', 
            'vehicleType':['4','5','6','8','10'],
            'readyToShip':'60',
            'minVehicles':'1',
            'numberToShow':'500',
            'highlightOnTop':'0',
            'highlightPeriod':'0',
            'primarySort':'5',
            'secondarySort':'7',
            #'btnSearch':'Search Vehicles',
            'chkSaveSearch':'1',
            'filterBlocked':'0',
            'highlightPreferred':'0',          
            'CSRFToken': authenticity_token_select
            
        }
        
        # Perform select
        result = session_requests.post(select_page.url, data = payload_select, headers = dict(referer = select_page.url))
        print(result.url)

        url = 'https://www.centraldispatch.com/protected/listing-search/result?routeBased=0&corridorWidth=&routePickupCity=&routePickupState=&routePickupZip=&route_origination_valid=&routeDeliveryCity=&routeDeliveryState=&routeDeliveryZip=&route_destination_valid=&waypointCity%5B%5D=&waypointCity%5B%5D=&waypointCity%5B%5D=&waypointCity%5B%5D=&waypointCity%5B%5D=&waypointState%5B%5D=&waypointState%5B%5D=&waypointState%5B%5D=&waypointState%5B%5D=&waypointState%5B%5D=&waypointZip%5B%5D=&waypointZip%5B%5D=&waypointZip%5B%5D=&waypointZip%5B%5D=&waypointZip%5B%5D=&waypoint_valid=1&pickupCity=&pickupRadius=25&pickupState=&pickupZip=&pickupAreas%5B%5D=All&origination_valid=1&deliveryCity=&deliveryRadius=25&deliveryState=&deliveryZip=&deliveryAreas%5B%5D=All&destination_valid=1&FatAllowCanada=1&vehicleTypeIds%5B%5D=4&vehicleTypeIds%5B%5D=5&vehicleTypeIds%5B%5D=6&vehicleTypeIds%5B%5D=8&vehicleTypeIds%5B%5D=10&trailerType=&vehiclesRun=&minVehicles=1&maxVehicles=&shipWithin=60&paymentType=&minPayPrice=&minPayPerMile=&highlightOnTop=0&postedBy=&highlightPeriod=1&listingsPerPage=500&primarySort=5&secondarySort=7&filterBlocked=0&highlightPreferred=0&CSRFToken=b2232b7d40c49490ed40e4fd071ded7eb1a8f5fc823aa98126aa178978d6a0e4' + authenticity_token
        result = session_requests.get(url)
        print(result.url)
        print(result.content)
        #print(result.content)
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

if __name__ == '__main__':
    main()

