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


# options = webdriver.ChromeOptions()
# # options.add_argument('headless')
# options.add_argument('window-size=1920x1080')
# options.add_argument("disable-gpu")
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=options)

resultAddress = ""

driver = Driver(uc=True)
driver.maximize_window()

with open('location1.csv', mode='r') as file:
    reader = csv.reader(file)
    with open('fullLocation.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        for row in reader:
            driver.get(row[2])
            time.sleep(0.3)

            headerPath = '//*[@id="avisHome"]/div[3]/div/div/div[1]/div[1]/div/div[2]/div[1]/div/div[1]/div[1]/h2/span'
            locationCodePath = '//*[@id="avisHome"]/div[3]/div/div/div[1]/div[1]/div/div[2]/div[1]/div/div[1]/div[1]/h2/text()'
            locationPath = '//*[@id="avisHome"]/div[3]/div/div/div[1]/div[1]/div/div[2]/div[1]/div/div[1]/div[1]/h2'
            streetPath = '//*[@id="avisHome"]/div[3]/div/div/div[1]/div[1]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[1]/p[2]/span[1]'
            cityPath = '//*[@id="avisHome"]/div[3]/div/div/div[1]/div[1]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[1]/p[2]'

            ulPath = '//*[@id="avisHome"]/div[3]/div/div/div/div[4]/div/div/div[1]/div[1]/div/div/form/div/div[3]/ul'
            if len(driver.find_elements(By.XPATH, headerPath)) == 0:
                if len(driver.find_elements(By.XPATH, ulPath)) != 0:
                    liElement = driver.find_element(By.XPATH, ulPath).find_elements(By.TAG_NAME, 'li')
                    for c in range(0, len(liElement)):
                        addressPath = './div[2]/div/div/div/div[1]/p[2]'
                        headerPath1 = './div[1]/div/a/b'
                        header = liElement[c].find_element(By.XPATH, headerPath1).get_attribute('innerHTML')
                        address = liElement[c].find_element(By.XPATH, addressPath).get_attribute('innerHTML')
                        resultAddress = address
                        # print(row[0])
                        # print(row[1])
                        # print(row[2])
                        # print(header)
                        print(address)
                        writer.writerow([row[0], row[1], row[2], header, header + resultAddress])
                        
            else:
                header = driver.find_element(By.XPATH, headerPath).get_attribute('innerHTML')
                locationCode = driver.find_element(By.XPATH, locationPath).text
                street = driver.find_element(By.XPATH, streetPath).get_attribute('innerHTML')
                cities = driver.find_element(By.XPATH, cityPath).find_elements(By.TAG_NAME, 'span')
                city = ''
                for c in range(0, len(cities)):
                    city = city + cities[c].get_attribute('innerHTML')
                # print(row[0])
                # print(row[1])
                # print(row[2])
                # print(header)
                # print(street)
                print(locationCode[locationCode.find("(")+1:locationCode.find(")")])
                writer.writerow([row[0], row[1], row[2], locationCode[locationCode.find("(")+1:locationCode.find(")")], locationCode + street + city])
driver.close()    
