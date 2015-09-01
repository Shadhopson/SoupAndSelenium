import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
browser.get('https://mail.yahoo.com')
emailElem = browser.find_element_by_id('login-username')
emailElem.send_keys('hopson.shad')
passwordElem= browser.find_element_by_id('login-passwd')
passwordElem.send_keys('iguana')
time.sleep(2)
passwordElem.submit()
time.sleep(2)
htmlElem = browser.find_element_by_tag_name('html')
for i in range(0,10):
    for j in range(0,20):
        htmlElem.send_keys(Keys.DOWN)
    time.sleep(1)
    for k in range(0,20):
        htmlElem.send_keys(Keys.UP)
#passwordElem.submit()
