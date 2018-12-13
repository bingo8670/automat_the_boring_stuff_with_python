from selenium import webdriver

browser = webdriver.Chrome('/usr/local/bin/chromedriver')
browser.get('http://inventwithpython.com')
linkElem = browser.find_element_by_link_text('Read Online for Free')
type(linkElem)
# <class 'selenium.webdriver.remote.webelement.WebElement'>
linkElem.click() # follows the "Read It Online" link
