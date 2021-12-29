from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import csv
import pandas
import pyautogui
import scrapy
import os
from scrapy import cmdline
from scrapy import Request

get_data,get_main_name,get_postal_code = {},{},{}
df_counter = df_counter2 = counter = 0
timeout=15
get_search_bar=""
#df = pandas.read_csv('SG POI Normalisation Working Sheet - List 4.csv', dtype=str) #csv file
df = pandas.read_csv('9Copy of SG POI Normalisation Working Sheet - List 4.csv', dtype=str) #csv file
count_row = len(df) #get length of csv rows
'''
#retrive all rows from column header named 'GT link' and append to get_data dictionary
while df_counter != 310:
    get_data[df_counter] = df.at[df_counter, 'GT link']
    df_counter += 1

'''
#reminder: please manually save one first to set the download path, the rest will be automatic
'''
while counter != len(get_data):
    options = Options()
    options.add_argument("user-data-dir=/Users/ftt.farit.ismeth/Library/Application Support/Google/Chrome")
    chrome = webdriver.Chrome(executable_path="/Users/ftt.farit.ismeth/Desktop/selenium_and_scrapy/chromedriver", options=options)
    chrome.get(get_data[counter])
    #time.sleep(8) #wait for page to fully load
    try:
        element_present = EC.presence_of_element_located((By.XPATH, "/html/body/div[@id='root']/section/div[@class='ant-layout']/div[@class='ant-layout ant-layout-has-sider']/div[@class='ant-layout']/div[@class='ant-layout-content']/div[@class='ant-layout']/section[@class='ops-tools-content']/div[@class='ops-tools-page-header-pro']/div[@class='ops-tools-page-header-pro-detail']/div[@class='page-header-pro-detail-main']/div[@class='page-header-pro-detail-main-row']/h1[@class='page-header-pro-detail-main-title']/span/span[1]"))
        WebDriverWait(chrome, timeout).until(element_present)
        pyautogui.keyDown('command')
        pyautogui.press('s')
        pyautogui.keyUp('command') #simulates saving the page
        time.sleep(4) #wait for dialog box to fully load
        pyautogui.write(f'9page{counter+1}',interval=0.1) #input file name
        time.sleep(1)
        pyautogui.press('return')
        time.sleep(5)
    except TimeoutException:
        print(f"Unable to get {get_data[counter]}")
        with open('failed_pages.csv', 'a') as myfile: #if mode=a; append to file. else if mode=w; overwrite file
            myfile.write(f'{get_data[counter]}\n')
    #chrome.save_screenshot(f"/Users/ftt.farit.ismeth/Desktop/selenium_and_scrapy/screenshots/{counter+1}.png")
    chrome.quit()
    counter += 1
'''

#open new window in terminal and type the first part of the command to run our spider
pyautogui.keyDown('command')
pyautogui.press('t')
pyautogui.keyUp('command')
time.sleep(2)
pyautogui.write(f'scrapy runspider --output data2.csv ',interval=0.1)

#search for selenium folder in spotlight
pyautogui.keyDown('command')
pyautogui.press('space')
pyautogui.keyUp('command')
pyautogui.write(f'selenium',interval=0.1)
time.sleep(3)
pyautogui.press('return')
time.sleep(2)

#navigate to geotools_spider.py file
pyautogui.press('tab', presses=13)
time.sleep(1)

#copy file path
pyautogui.keyDown('option')
pyautogui.keyDown('command')
pyautogui.press('c')
pyautogui.keyUp('option')
pyautogui.keyUp('command')

#search for terminal via Spotlight
pyautogui.keyDown('command')
pyautogui.press('space')
pyautogui.keyUp('command')
pyautogui.write(f'terminal',interval=0.1)
time.sleep(1)
pyautogui.press('return')

#paste filepath in terminal
time.sleep(1)
pyautogui.keyDown('command')
pyautogui.press('v')
pyautogui.keyUp('command')
time.sleep(1)
pyautogui.press('return')
'''
#switch window back to main
pyautogui.keyDown('command')
pyautogui.keyDown('shift')
pyautogui.press('left')
pyautogui.keyUp('command')
pyautogui.keyUp('shift')
print("Spider is fetching data, please wait...")
time.sleep(30)
print("Data compiled")
time.sleep(2)

#start search_result.py
pyautogui.keyDown('command')
pyautogui.press('t')
pyautogui.keyUp('command')
time.sleep(1)
pyautogui.write(f'python3 se',interval=0.1)
pyautogui.press('tab')
pyautogui.press('return')
'''