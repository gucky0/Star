# run this section once before the actual day, then comment it to make it faster
##import os
##os.system("py -m pip install selenium")
##os.system("py -m pip install webdriver-manager")
##from selenium import webdriver
##from webdriver_manager.chrome import ChromeDriverManager
##driver = webdriver.Chrome(ChromeDriverManager().install())



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta

driver = webdriver.Chrome('chromedriver')

# write your NTU username and password
username = ""
password = ""

# write your registration date and time in this format "YYYY MM DD HH MM SS"
registration_time = "2021 12 13 14 00 00"
registration_time = [int(_) for _ in registration_time.split(" ")]
registration_time = datetime(*registration_time)
start_time = registration_time - timedelta(seconds=2)

while True:
    try:
        driver.get('https://wish.wis.ntu.edu.sg/pls/webexe/ldap_login.login?w_url=https://wish.wis.ntu.edu.sg/pls/webexe/aus_stars_planner.main')
        driver.implicitly_wait(3)

        mouse = driver.find_element(By.ID, 'UID')
        mouse.send_keys(username)
        mouse.send_keys(Keys.ENTER)

        mouse = driver.find_element(By.CSS_SELECTOR, 'input[type="password"]')
        mouse.send_keys(password)
        while True:
            if datetime.now() >= start_time:
                #Login
                mouse.send_keys(Keys.ENTER)
                
                while datetime.now() >= registration_time:
                    #Add course
                    mouse = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
                    mouse.click()

                    #Confirm
                    mouse = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
                    mouse.click()

                    #Back to timetable
                    mouse = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
                    mouse.click()           
    except:
        continue



