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

options = webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=options)

with open('fullLocation.csv', mode='r') as file:
    reader = csv.reader(file)
    with open('car.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in reader:
            driver.get('https://www.avis.com')
            time.sleep(1)

            addressPath = '//*[@id="PicLoc_value"]'
            driver.find_elements(By.XPATH, addressPath)[0].clear()
            driver.find_elements(By.XPATH, addressPath)[0].send_keys(row[3])
            time.sleep(1)
            driver.find_elements(By.XPATH, addressPath)[0].send_keys(Keys.ENTER)
            # selectMyCarPath = '//*[@id="res-home-select-car"]'
            # if len(driver.find_elements(By.XPATH, selectMyCarPath)) == 0:
            #     driver.find_elements(By.XPATH, addressPath)[0].send_keys(Keys.ENTER)
            # else:
            #     driver.find_element(By.XPATH, selectMyCarPath).click()
            time.sleep(8)

            selectThisLocationPath1 = '/html/body/div[7]/div[2]/div/footer/div[3]/div/div[1]/div/div/div[2]/div[2]/ul/li/div[2]/a'
            selectThisLocationPath2 = '/html/body/div[4]/div[5]/div/footer/div[3]/div/div[1]/div/div/div[2]/div[2]/ul/li/div[2]/a'
            selectThisLocationPath3 = '/html/body/div[4]/div[5]/div/footer/div[3]/div/div[1]/div/div/div[2]/div[2]/ul/li[1]/div[2]/a'
            if len(driver.find_elements(By.XPATH, selectThisLocationPath1)) > 0:
                driver.find_elements(By.XPATH, selectThisLocationPath1)[0].click()
            elif len(driver.find_elements(By.XPATH, selectThisLocationPath2)) > 0:
                driver.find_elements(By.XPATH, selectThisLocationPath2)[0].click()
            elif len(driver.find_elements(By.XPATH, selectThisLocationPath3)) > 0:
                driver.find_elements(By.XPATH, selectThisLocationPath3)[0].click()
            # else:
            #     continue
            time.sleep(8)

            dateClass = 'day-time-info'

            availableCarBoxClassPath = 'available-car-box'
            featuredCarBoxClassPath = 'featured-car-box'

            featuredClass1 = './div[2]/div/div/h3'
            featuredClass2 = './div[2]/div/h3'
            featuredType1 = './div[2]/div/div/p'
            featuredType2 = './div[2]/div/p'
            featuredPL = 'payamntp'
            featuredPN = 'payamntr'
            
            availableClass = './div/div[1]/div[2]/h3'
            availableType = './div/div[1]/div[2]/p[1]'
            availablePL = 'payamntp'
            availablePN = 'payamntr'

            DateClasses = driver.find_elements(By.CLASS_NAME, dateClass)
            featuredCarBoxClass = driver.find_elements(By.CLASS_NAME, featuredCarBoxClassPath)
            availableCarBoxClass = driver.find_elements(By.CLASS_NAME, availableCarBoxClassPath)
            if len(DateClasses) > 0:
                pickupDate = DateClasses[0].text
            else:
                pickupDate = date.today()
            if len(featuredCarBoxClass) > 0:
                print('featured car is exist')
                for c in range(0, len(featuredCarBoxClass)):
                    if len(featuredCarBoxClass[c].find_elements(By.XPATH, featuredClass1)) > 0:
                        carClass = featuredCarBoxClass[c].find_elements(By.XPATH, featuredClass1)[0].text
                    elif len(featuredCarBoxClass[c].find_elements(By.XPATH, featuredClass2)) > 0:
                        carClass = featuredCarBoxClass[c].find_elements(By.XPATH, featuredClass2)[0].text
                    else:
                        carClass = 'Full-Size**'

                    if len(featuredCarBoxClass[c].find_elements(By.XPATH, featuredType1)) > 0:
                        carType = featuredCarBoxClass[c].find_elements(By.XPATH, featuredType1)[0].text
                    elif len(featuredCarBoxClass[c].find_elements(By.XPATH, featuredType2)) > 0:
                        carType = featuredCarBoxClass[c].find_elements(By.XPATH, featuredType2)[0].text
                    else:
                        carType = 'Toyota Camry or similar**'
                    if len(featuredCarBoxClass[c].find_elements(By.CLASS_NAME, featuredPL)) > 0:
                        carPL = featuredCarBoxClass[c].find_element(By.CLASS_NAME, featuredPL).text
                    else:
                        carPL = '-'
                    if len(featuredCarBoxClass[c].find_elements(By.CLASS_NAME, featuredPN)) > 0:
                        carPN = featuredCarBoxClass[c].find_element(By.CLASS_NAME, featuredPN).text
                    else:
                        carPN = '-'
                    print(carClass, carType, carPL, carPN)
                    writer.writerow([row[0], row[1], row[2], row[3], row[4], carClass, carType, carPL, carPN, pickupDate])
            if len(availableCarBoxClass) > 0:
                print('car is available')
                for c in range(0, len(availableCarBoxClass)):
                    carClass = availableCarBoxClass[c].find_element(By.XPATH, availableClass).text
                    carType = availableCarBoxClass[c].find_element(By.XPATH, availableType).text
                    if len(availableCarBoxClass[c].find_elements(By.CLASS_NAME, availablePL)) > 0:
                        carPL = availableCarBoxClass[c].find_element(By.CLASS_NAME, availablePL).text
                    else:
                        carPL = '-'
                    if len(availableCarBoxClass[c].find_elements(By.CLASS_NAME, availablePN)) > 0:
                        carPN = availableCarBoxClass[c].find_element(By.CLASS_NAME, availablePN).text
                    else:
                        carPN = '-'
                    print(carClass, carType, carPL, carPN)
                    writer.writerow([row[0], row[1], row[2], row[3], row[4], carClass, carType, carPL, carPN, pickupDate])
            
driver.close()    
