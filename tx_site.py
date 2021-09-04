import json
import time
import datetime
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import (NoSuchElementException,StaleElementReferenceException,TimeoutException)
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.common.exceptions import NoSuchElementException
import re
from pandas import DataFrame

def new_driver():
    driver = webdriver.Chrome(executable_path=r"/Users/meghanmokate/Desktop/dated date/chromedriver 3")
    driver.maximize_window()  
    return driver

#def link(driver):
 #   report = driver.find_element_by_xpath('/html/body/div[1]/div/header/div/div[2]/section/div[1]/div/div/a[2]')
  #  report.click()

def distrupt(driver): 
    try:
        wait = WebDriverWait(driver, 30)
        element = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/article/div/div/div/div/div/div/div[2]/div/form/div[2]/div/div/textarea')))
        box_1 = element.find_element_by_xpath('/html/body/div[1]/div/div/div/article/div/div/div/div/div/div/div[2]/div/form/div[2]/div/div/textarea')
        box_1.send_keys('Sam, the first night at BED when you left, Ron made out with two girls and put his head between a cocktail waitresss breasts. [He] also was grinding with multiple fat women. When you left crying at Klutch, Ron was holding hands and dancing with a female and took down her number. Multiple people in the house know, therefore you should know the truth.') 
        box_2 = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/article/div/div/div/div/div/div/div[2]/div/form/div[3]/div/div/input')
        box_2.send_keys('peepeepoopoo')
        box_3 = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/article/div/div/div/div/div/div/div[2]/div/form/div[4]/div/div/input')
        box_3.send_keys('Dr. Spaceman')
        box_4 = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/article/div/div/div/div/div/div/div[2]/div/form/div[5]/div/div/input')
        box_4.send_keys('MY SWAMP')
        box_5 = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/article/div/div/div/div/div/div/div[2]/div/form/div[6]/div/div/input')
        box_5.send_keys('TX')
        box_6 = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/article/div/div/div/div/div/div/div[2]/div/form/div[7]/div/div/input')
        box_6.send_keys('69420')
        box_7 = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/article/div/div/div/div/div/div/div[2]/div/form/div[8]/div/div/input')
        box_7.send_keys('USA')
    except:
        print("issues with entries")

def verify(driver):
    option = webdriver.ChromeOptions()
    option.add_argument('--disable-notifications')
    option.add_argument("--mute-audio")
   # driver.find_element_by_class_name('recaptcha-checkbox goog-inline-block recaptcha-checkbox-unchecked rc-anchor-checkbox')
   # driver.find_element_by_css_selector("div.recaptcha-checkbox-checkmark").click()

def submit(driver):
    try:
        submit_button = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/article/div/div/div/div/div/div/div[2]/div/form/div[12]/div/div/button')
        submit_button.click()
    except:
        print("submit button not there")


# execute functions on webpage
if __name__ == "__main__":
    driver = new_driver()
    for i in range(2000):
        try:
          #  link(driver)
            distrupt(driver)
            verify(driver)
            submit(driver)                
        except Exception as e: 
                print(e) 
                     
        # every 10 iterations to track
        if i % 10 == 0:
            print("number of bogus reports sent: ", i)

        #driver.get('https://prolifewhistleblower.com/')
        driver.get('https://prolifewhistleblower.com/anonymous-form/')