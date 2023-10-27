import datetime
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

#Fix
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# set options to be headless, ..
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()

# Adding argument to disable the AutomationControlled flag 
options.add_argument("--disable-blink-features=AutomationControlled") 
 
# Exclude the collection of enable-automation switches 
options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
 
# Turn-off userAutomationExtension 
options.add_experimental_option("useAutomationExtension", False) 

options.add_argument('--ignore-certificate-errors')

# open it, go to a website, and get results
wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#wd.get(input("Enter your bigc url : "))

wd.get("https://shopee.co.th/big_c")
input()

#wd.get("https://shopee.co.th/big_c")
file_name = "test"

print(wd.page_source)  # results

from bs4 import BeautifulSoup
product_name = []
base_price_lis = []
sell_price_lis = []
link_lis = []
quant_lis = []
soup = BeautifulSoup(wd.page_source,'html.parser')
for i in soup.find_all('div',{'class':'shop-search-result-view__item col-xs-2-4'}): 
        name = i.find('div',{'class':'_3Gla5X _2j2K92 _3j20V6'}).text 
        product_name.append(name)
        print(name)


        link = "https://shopee.co.th"+i.find('a',{'data-sqe':'link'})['href']
        link_lis.append(link)
        print(link)

        amount = i.find('div',{'class':'_2Tc7Qg _2R-Crv'}).text
        quant_lis.append(amount)
        print(amount)

        sell_price = i.find('span',{'class':'_3TJGx5'}).text 
        sell_price_lis.append(sell_price)
        print(sell_price)

        dummy_len = len('<div class="_3w3Slt _2aeaHz _1Rbwjx">')
        base_price = str(i.find('div',{'class':'_3w3Slt _2aeaHz _1Rbwjx'}))[len('<div class="_3w3Slt _2aeaHz _1Rbwjx">'):].replace("</div>","")
        print(type(base_price))
        base_price_lis.append(base_price) 
        print(base_price)

import pandas as pd
df = pd.DataFrame()
df['ชื่อสินค้า'] = product_name 
df['ราคาเริ่มต้น'] = base_price_lis 
df['ราคาขาย'] = sell_price_lis 
df['ลิงค์สินค้า'] = link_lis 
df['จำนนสินค้า'] = quant_lis 



df.to_excel("{}.xlsx".format(file_name))
df.head(20)