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
df = pandas.read_csv('input.csv', dtype=str) #csv file
count_row = len(df) #get length of csv rows

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
