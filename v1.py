import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from lxml import html
from selenium.webdriver.common.keys import Keys


USERNAME = 'vision87'
PASSWORD = 'Welcome123!'

LOGIN_URL = 'https://www.centraldispatch.com/login?uri=%2Fprotected%2F'
URL = 'https://www.centraldispatch.com/protected/listing-search'
def main():
    browser = webdriver.Chrome('C:/Users/Siyu/chromedriver.exe')
    browser.get(LOGIN_URL) 
    username = browser.find_element_by_id("pageUsername")
    password = browser.find_element_by_id("pagePassword")
    username.send_keys(USERNAME)
    password.send_keys(PASSWORD)
    login_attempt = browser.find_element_by_xpath("//input[@type='submit']")
    login_attempt.click()
    
    browser.get(URL)
    select1 = Select(browser.find_element_by_id('originRegion'))
    select1.select_by_value('All')
    
    select2 = Select(browser.find_element_by_id('destinationRegion'))
    select2.select_by_value('All')
    
    browser.get(URL+'#page-vehicle-spec-control')
    select3 = Select(browser.find_element_by_id('vehicleType'))
    select3.select_by_value('4')
    select3.select_by_value('5')
    select3.select_by_value('6')
    select3.select_by_value('8')
    select3.select_by_value('10')
    
    browser.get(URL+'#page-date-pricing-control')
    select4 = Select(browser.find_element_by_id('readyToShip'))
    select4.select_by_value('60')
    
    browser.get(URL+'#page-search-results-options-control')
    select5 = Select(browser.find_element_by_id('numberToShow'))
    select5.select_by_value('500')
    
    select6 = Select(browser.find_element_by_id('primarySort'))
    select6.select_by_value('5')
    
    select5 = Select(browser.find_element_by_id('secondarySort'))
    select5.select_by_value('7')
    
    driver.find_element_by_id("btnSearch").click()
if __name__ == '__main__':
    main()