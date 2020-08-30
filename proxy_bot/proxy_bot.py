from .constants import *
from  selenium import webdriver
from .config import *
from selenium.webdriver.support.ui import WebDriverWait



def main():
    driver = webdriver.Chrome('chromedriver.exe')
    
    driver.get(platform_url['meet'])
    driver.find_element_by_css_selector('body > header > div.glue-header__bar.glue-header__bar--desktop.glue-header__drawer > div > div.glue-header__container.glue-header__container--cta > div.primary-meet-cta.tbd > div > span:nth-child(1) > a').click()
    driver.find_element_by_id("identifierId").send_keys(platform_pass['meet']['user'])
    driver.find_element_by_css_selector("#identifierNext > div > button").click()
    driver.implicitly_wait(10)   
    driver.find_element_by_css_selector("#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input").send_keys(platform_pass['meet']['pass'])
    driver.implicitly_wait(2)   
    driver.find_element_by_css_selector("#passwordNext > div > button").click()
    driver.implicitly_wait(20)

if __name__ == '__main__':
    main()
    