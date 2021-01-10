from selenium import webdriver
import time

browser = webdriver.Firefox()

def startTouch(browser):
    minute = time.time() + 60 * 1
    while time.time() < minute:
        browser.find_element_by_id('counter').click()
        time.sleep(1)
browser.get('https://jenniferdewalt.com/click_challenge.html')
browser.find_element_by_id('start').click()
startTouch(browser)
browser.close()