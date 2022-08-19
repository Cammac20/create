import sys
import os
from selenium import webdriver

path = "/home/cameron/Documents/Projects/"
browser = webdriver.Firefox()
browser.maximize_window()
browser.get('https://github.com/login')

def create():
    folderName = str(sys.argv[1])
    os.makedirs(path + str(sys.argv[1]))
    python_button = browser.find_elements_by_xpath("//*[@id='login_field']")[0]
    python_button.send_keys("Cammac20")
    python_button = browser.find_elements_by_xpath("//*[@id='password']")[0]
    python_button.send_keys("cam20mac")
    python_button = browser.find_elements_by_xpath("/html/body/div[3]/main/div/div[4]/form/div/input[12]")[0]
    python_button.click()
    browser.get('https://github.com/new')
    python_button = browser.find_elements_by_xpath("//*[@id='repository_name']")[0]
    python_button.send_keys(folderName)
    python_button = browser.find_elements_by_css_selector('.btn-primary')[0]
    python_button.submit()

if __name__ == "__main__":
    create()