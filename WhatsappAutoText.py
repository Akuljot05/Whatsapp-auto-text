#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Akuljot Singh

"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

# Replace 'Friend's Name' with the name of your friend
# or the name of a group
target = '"<name of contact>"'

# Replace the below string with your own message
with open("Test.txt", "r+", encoding='utf-8') as f:
    line = f.read()


test = line.split('\n\n')

string = "Python Text"


group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
group_title.click()
inp_xpath = '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]'
input_box = wait.until(EC.presence_of_element_located((
    By.XPATH, inp_xpath)))
for i in test:
    input_box.send_keys(i + Keys.ENTER)
    # time.sleep(2)
