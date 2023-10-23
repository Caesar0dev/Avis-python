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

driver.get('https://www.avis.com/en/locations/us')

time.sleep(2)

stateName = '//*[@id="avisHome"]/div[2]/div[2]/div/section/div[2]/ul'
stateElement = driver.find_element(By.XPATH, stateName)
children = stateElement.find_elements(By.XPATH, './li')
with open('state.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    # writer.writerow(["stateName", "stateHref"])
    for c in range(0, len(children)):
        stateName = children[c].find_element(By.XPATH, './a').get_attribute("innerHTML")
        stateHref = children[c].find_element(By.XPATH, './a').get_attribute("href")
        print(stateName)
        print(stateHref)
        writer.writerow([stateName, stateHref])

driver.close()    