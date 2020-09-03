from .constants import *
from  selenium import webdriver
from .config import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
"profile.default_content_setting_values.media_stream_mic": 1, 
"profile.default_content_setting_values.media_stream_camera": 1,
"profile.default_content_setting_values.geolocation": 1, 
"profile.default_content_setting_values.notifications": 1 
})


def main():
    driver = webdriver.Chrome(chrome_options=opt, executable_path=r'chromedriver')    
    driver.get('https://accounts.google.com/signin/v2/identifier?ltmpl=meet&continue=https%3A%2F%2Fmeet.google.com%3Fhs%3D193&_ga=2.57642083.850847125.1599156917-360711165.1599156917&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    #driver.find_element_by_css_selector('body > header > div.glue-header__bar.glue-header__bar--desktop.glue-header__drawer > div > div.glue-header__container.glue-header__container--cta > div.primary-meet-cta.tbd > div > span:nth-child(1) > a').click()
    driver.find_element_by_id("identifierId").send_keys(platform_pass['meet']['user'])
    driver.find_element_by_css_selector("#identifierNext > div > button").click()
    driver.implicitly_wait(10)   
    driver.find_element_by_css_selector("#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input").send_keys(platform_pass['meet']['pass'])
    driver.implicitly_wait(2)   
    driver.find_element_by_css_selector("#passwordNext > div > button").click()
    driver.implicitly_wait(20)
    time.sleep(5)
    driver.get('https://meet.google.com/jic-usuh-smk')
    time.sleep(5)
    driver.refresh()
    time.sleep(5)
         # Turning off video 
    driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[1]/div[1]/div[3]/div[2]/div/div").click()
    time.sleep(5)
        # turning off audio
    driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[1]/div[1]/div[3]/div[1]/div/div/div").click()
    time.sleep(4)
        # Join class
    driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span").click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[4]/div[3]/div[6]/div[3]/div/div[2]/div[1]').click()
    time.sleep(2)
    count = driver.find_element_by_class_name('rua5Nb').text
    print("Number of people connencted ",count)

if __name__ == '__main__':
    main()
    