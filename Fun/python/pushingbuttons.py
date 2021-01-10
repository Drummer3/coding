from selenium import webdriver
from time import sleep

url = "https://jenniferdewalt.com/click_challenge.html"

def get_cpf():
    driver = webdriver.Chrome()
    driver.get("https://jenniferdewalt.com/click_challenge.html")
    while(True):
        driver.find_element_by_id('counter').click()
        sleep(1)
get_cpf()