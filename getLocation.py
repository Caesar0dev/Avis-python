import csv
import threading

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import undetected_chromedriver as uc
import pandas as pd
import time
import re
import csv
from datetime import datetime
from datetime import date
from seleniumbase import Driver

driver = Driver(uc=True)

with open('state.csv', mode='r') as file:
    reader = csv.reader(file)
    with open('location.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in reader:
            print(row)
            print(row[0])
            print(row[1])
            driver.get(row[1])
            time.sleep(2)

            citiesClass = 'location-list-ul'
            cities = driver.find_elements(By.CLASS_NAME, citiesClass)
            for c in range(0, len(cities)):
                cities1 = cities[c].find_elements(By.TAG_NAME, 'li')
                for c1 in range(0, len(cities1)):
                    if cities1[c1].get_attribute('class') == '':
                        city = cities1[c1].find_element(By.TAG_NAME, 'a').get_attribute('innerHTML')
                        citylink = cities1[c1].find_element(By.TAG_NAME, 'a').get_attribute('href')
                        writer.writerow([row[0], city, citylink])
                        print(city)
                        print(citylink)
driver.close()    
