from . import constants
from  selenium import webdriver




def main():
    
    driver.get(url)
    driver.find_element_by_id("Email").send_keys(mail_address)
    driver.find_element_by_id("next").click()
    driver.find_element_by_id("Passwd").send_keys(password)
    driver.find_element_by_id("signIn").click()


if __name__ == '__main__':
    main()
    