import requests
from lxml import html

USERNAME = 'vision87'
PASSWORD = 'Welcome123!'

LOGIN_URL = 'https://www.centraldispatch.com/login?uri=%2Fprotected%2F'
URL = 'https://www.centraldispatch.com/protected/listing-search/result?routeBased=0&corridorWidth=&routePickupCity=&routePickupState=&routePickupZip=&route_origination_valid=&routeDeliveryCity=&routeDeliveryState=&routeDeliveryZip=&route_destination_valid=&waypointCity%5B%5D=&waypointCity%5B%5D=&waypointCity%5B%5D=&waypointCity%5B%5D=&waypointCity%5B%5D=&waypointState%5B%5D=&waypointState%5B%5D=&waypointState%5B%5D=&waypointState%5B%5D=&waypointState%5B%5D=&waypointZip%5B%5D=&waypointZip%5B%5D=&waypointZip%5B%5D=&waypointZip%5B%5D=&waypointZip%5B%5D=&waypoint_valid=1&pickupCity=&pickupRadius=25&pickupState=&pickupZip=&pickupAreas%5B%5D=All&origination_valid=1&deliveryCity=&deliveryRadius=25&deliveryState=&deliveryZip=&deliveryAreas%5B%5D=All&destination_valid=1&FatAllowCanada=1&vehicleTypeIds%5B%5D=4&vehicleTypeIds%5B%5D=5&vehicleTypeIds%5B%5D=6&vehicleTypeIds%5B%5D=8&vehicleTypeIds%5B%5D=10&trailerType=&vehiclesRun=&minVehicles=1&maxVehicles=&shipWithin=60&paymentType=&minPayPrice=&minPayPerMile=&highlightOnTop=0&postedBy=&highlightPeriod=0&listingsPerPage=500&primarySort=5&secondarySort=7&filterBlocked=0&highlightPreferred=0&CSRFToken=fd748062bebddee17464850e94758361b4632465e69e37f12d47bacfb93807da'

def main():
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

    # Scrape url
    result = session_requests.get(URL, headers = dict(referer = URL))
    
#     #tree = html.fromstring(result.content)
#     #bucket_names = tree.xpath("//div[@class='repo-list--repo']/a/text()")

    print(result.content)

if __name__ == '__main__':
    main()











# import urllib
# from urllib.parse import urlencode, quote_plus
# from urllib.request import urlopen
# # import requests
# # from lxml import html

# USERNAME = 'vision87'
# PASSWORD = 'Welcome123'

# # session_requests = requests.session()

# #     # Get login csrf token
# # LOGIN_URL = 'https://www.centraldispatch.com/login?uri=%2Fprotected%2F'
# # result = session_requests.get(LOGIN_URL)
# # tree = html.fromstring(result.text)
# # authenticity_token = list(set(tree.xpath('//input[@name="CSRFToken"]/@value')))[0]
# # print(authenticity_token)

# payload = {
#         'Username': USERNAME, 
#         'Password': PASSWORD 
#         # 'KeepLoggedIn':'on',
#         # 'submit':'Log In',
#         # 'CSRFToken': authenticity_token
#     }


# encoded_data = urlencode(payload, quote_via=quote_plus)
# print(encoded_data)
# content = urlopen('https://www.centraldispatch.com/login?uri=%2Fprotected%2F',encoded_data)
# print(content)
#with requests.Session() as c:
#	url = 'https://www.centraldispatch.com/'
#	USERNAME = 'vision87'
#	PASS = 'vision87'
#	c.get(url)
#	csrftoken = c.cookies['csrftoken']
#	login_data = dict(username = USERNAME, password = PASS, csrfmiddlewaretoken = csrftoken)
#	c.post(url, data = login_data)
#	page = c.get('https://www.centraldispatch.com/protected/profile')
#	print(page.content)

#payload = {'Username' : 'vision87', 'Password' : 'Welcome123!', 'KeepLoggedIn': true, 'CSRFToken':'fd748062bebddee17464850e94758361b4632465e69e37f12d47bacfb93807da'}
#session_requests = requests.session()
#url = 'https://www.centraldispatch.com/'
#import sys
#with requests.Session() as c:
#	c.post('https://www.centraldispatch.com/', data = login_data)
#	r = c.get('https://www.centraldispatch.com/protected/profile')
#	print(r.content)
	#print ('vision87') in r.content