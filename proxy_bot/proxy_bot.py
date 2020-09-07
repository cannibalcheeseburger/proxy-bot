from .constants import *
import selenium.common.exceptions
from  selenium import webdriver
from .config import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from .recording import *
from .scheduler import *


init = get_time()

today = get_day()

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
    print("\t\t\tProgram Init and Date: "+init+" "+today+"\n\n")
    print("\t\t\tToday's Schedule\n")
    
    for t in  schedule[today].keys():
        print(t+" "+schedule[today][t][0]) 
    
    curr,next_cl = next_class(today,init)

    print("\n\nCurrent class : ",curr[0])
    print("\n\nNext Class: ",next_cl[0])

    while True:
        last_time = get_time()
        curr,next_cl = next_class(today,last_time)

        print("\n\nCurrent class : ",curr[0])
        print("\n\nNext Class: ",next_cl[0])

        print("\n\n\t\t\tCurrent Time: "+last_time)
        
        if curr[1]!='NA':
                
            ret =  start_session(curr,last_time)
            
            if ret :
                print('Session unsuccesful')
            else:
                print('Session Successful')

        else:

            print("\n\nNo session online right now\n Sleeping for 5 min")    

        time.sleep(5*60)


def start_session(current,last_time):
    try:
        driver = webdriver.Chrome(chrome_options=opt, executable_path=r'chromedriver.exe')    
        driver.get('https://accounts.google.com/signin/v2/identifier?ltmpl=meet&continue=https%3A%2F%2Fmeet.google.com%3Fhs%3D193&_ga=2.57642083.850847125.1599156917-360711165.1599156917&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
        driver.find_element_by_id("identifierId").send_keys(platform_pass['user'])
        driver.find_element_by_css_selector("#identifierNext > div > button").click()
        driver.implicitly_wait(10)   
        driver.find_element_by_css_selector("#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input").send_keys(platform_pass['pass'])
        driver.implicitly_wait(2)   
        driver.find_element_by_css_selector("#passwordNext > div > button").click()
        driver.implicitly_wait(20)
        time.sleep(5)
       #Replace this
        print('\n\n\t\t Opening session for ',current[0])
        driver.get(current[1])
      
        time.sleep(5)
        link = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div[1]/div[1]/div/div[2]/div[2]/span/a/div').text

        print("Linked For google meet:"+ link)
        driver.get(link)
        time.sleep(5)
        driver.refresh()
        time.sleep(5)
            # Turning off video 
        driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[1]/div[1]/div[3]/div[2]/div/div").click()
        time.sleep(5)
            #  off audioturning
        driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[1]/div[1]/div[3]/div[1]/div/div/div").click()
        time.sleep(4)
            # Join class
        driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span").click()
        time.sleep(3)
        start_rec()
        driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[4]/div[3]/div[6]/div[3]/div/div[2]/div[1]').click()
        time.sleep(2)
        count = driver.find_element_by_class_name('rua5Nb').text
        members = int(count[1:-1])
        print("Number of people connencted ",members)
        while members > 7:
            count = driver.find_element_by_class_name('rua5Nb').text
            members = int(count[1:-1])
            print("Number of people connencted ",members)
            time.sleep(5*60)


        print("\n\n\t\tMembers less than 7...quitting....")
        stop_rec()
        driver.close()
        new_time = get_time()
        print("Session Time: ",(int(new_time[:2]) - int(last_time[:2]))*60 +( 60 - int(last_time[2:]) ) )
    # handles all exceptions cuz me lazy
    except:
        print
        driver.close()
        return 1
    
    return 0

if __name__ == '__main__':
    main()
    