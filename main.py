from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import re
import random
import pandas as pd



f = pd.read_excel("data.xlsx")
data = pd.DataFrame(f, columns=['Name'])
print(data)

def khoitao():
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    #chrome_options.headless = True
    return webdriver.Chrome('chromedriver.exe',chrome_options=chrome_options)

driver = khoitao()
for kkk in keyz:
    try:
        kkk = re.sub(' ','+',kkk)
    except:
        pass
    url = 'https://www.google.com.vn/search?q='+kkk+'&tbm=isch&ved=2ahUKEwiC4sKUrMLzAhWRIqYKHYyiBAsQ2-cCegQIABAA&oq=hi&gs_lcp=CgNpbWcQAzIHCCMQ7wMQJzIHCCMQ7wMQJzIICAAQsQMQgwEyBQgAEIAEMggIABCxAxCDATIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQMyCAgAEIAEELEDOgoIIxDvAxDqAhAnOgQIABBDOgsIABCABBCxAxCDAVCAjwFYrMYBYOTJAWgCcAB4AIABYogBsAGSAQEymAEAoAEBqgELZ3dzLXdpei1pbWewAQrAAQE&sclient=img&ei=JCxkYYLAIZHFmAWMxZJY&bih=935&biw=1876'
    scrip = 'window.open("'+url+'","_blank");'
    print(scrip)
    driver.execute_script(scrip)
