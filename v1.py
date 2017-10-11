from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as soup
from lxml import html
import requests
import time
#import numpy as np
#import pandas as pd

USERNAME = 'vision87'
PASSWORD = 'Welcome123!'

LOGIN_URL = 'https://www.centraldispatch.com/login?uri=%2Fprotected%2F'
URL = 'https://www.centraldispatch.com/protected/listing-search'
def main():
    #perform login
    session_requests = requests.session()
    browser = webdriver.Chrome()
    browser.get(LOGIN_URL) 
    username = browser.find_element_by_id("pageUsername")
    password = browser.find_element_by_id("pagePassword")
    username.send_keys(USERNAME)
    password.send_keys(PASSWORD)
    login_attempt = browser.find_element_by_xpath("//input[@type='submit']")
    login_attempt.click()
    
    #filter and search data
    result = session_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath('//input[@name="CSRFToken"]/@value')))[0]
    url='https://www.centraldispatch.com/protected/listing-search/result?routeBased=0&corridorWidth=&routePickupCity=&routePickupState=&routePickupZip=&route_origination_valid=&routeDeliveryCity=&routeDeliveryState=&routeDeliveryZip=&route_destination_valid=&waypointCity%5B%5D=&waypointCity%5B%5D=&waypointCity%5B%5D=&waypointCity%5B%5D=&waypointCity%5B%5D=&waypointState%5B%5D=&waypointState%5B%5D=&waypointState%5B%5D=&waypointState%5B%5D=&waypointState%5B%5D=&waypointZip%5B%5D=&waypointZip%5B%5D=&waypointZip%5B%5D=&waypointZip%5B%5D=&waypointZip%5B%5D=&waypoint_valid=1&pickupCity=&pickupRadius=25&pickupState=&pickupZip=&pickupAreas%5B%5D=All&origination_valid=1&deliveryCity=&deliveryRadius=25&deliveryState=&deliveryZip=&deliveryAreas%5B%5D=All&destination_valid=1&FatAllowCanada=1&vehicleTypeIds%5B%5D=4&vehicleTypeIds%5B%5D=5&vehicleTypeIds%5B%5D=6&vehicleTypeIds%5B%5D=8&vehicleTypeIds%5B%5D=10&trailerType=&vehiclesRun=&minVehicles=1&maxVehicles=&shipWithin=60&paymentType=&minPayPrice=&minPayPerMile=&highlightOnTop=0&postedBy=&highlightPeriod=1&listingsPerPage=500&primarySort=5&secondarySort=7&filterBlocked=0&highlightPreferred=0&CSRFToken=b2232b7d40c49490ed40e4fd071ded7eb1a8f5fc823aa98126aa178978d6a0e4'+authenticity_token
#    uClient = uReq(url)
#    uClient.close()
    browser.get(url)
    element_present = EC.presence_of_element_located((By.CLASS_NAME, 'listingSummary'))
    WebDriverWait(browser, 30).until(element_present)
    compare = []
    #browser.find_elements_by_xpath("//button[@class='btn btn-sm btn-default btn-block samplePrices']").click()
    scheight = .1
    #while scheight < 9.9:
    #    browser.execute_script("window.scrollTo(0, document.body.scrollHeight/%s);" % scheight)
    #    scheight += .01
    compare = browser.find_elements_by_xpath("//button[@class='btn btn-sm btn-default btn-block samplePrices']")
    #print(compare)
    for x in compare:
        browser.execute_script("return arguments[0].scrollIntoView();", x)
        time.sleep(2)
        #x.click()
        #browser.execute_script("window.scrollTo(0, document.body.scrollHeight/%s);" % scheight)
        #time.sleep(1)
        #scheight += .1

    #print(compare)
    #for x in compare:
    #    x.click()
    #for x in range(0,len(compare)):
    #    if compare[x].is_displayed():
    #        compare[x].click()

    page_html = browser.page_source
    #ref=browser.find_element_by_xpath("//div[@class='col-sm-3 shipperCustomData hidden-xs']")
    page_soup = soup(page_html,"html.parser")
    print(page_soup)
    
    

if __name__ == '__main__':
    main()