from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import datetime
import numpy as np
driver = webdriver.Chrome('chromedriver')
# use logging, catch partial msg from error
# timeout: https://www.pingshiuanchua.com/blog/post/error-handling-in-selenium-on-python
# use with to reduce number of "driver"




##animes = [
##    'shaman-king-2021',
##    'komi-san-wa-comyushou-desu',
##    'ousama-ranking']
##
##episodes = [36,11,10]


anime_long_list = np.full((len(animes), 4), None)
anime_long_list[:,0] = animes
anime_long_list = anime_long_list.tolist()



driver.get('https://myanimelist.net/login.php')
driver.implicitly_wait(3)

## login
driver.find_element(By.ID,'loginUserName').send_keys('guckyisme')
driver.find_element(By.ID,'login-password').send_keys('haf071197')
driver.find_element(By.CSS_SELECTOR,'input[type="submit"]').click()


## go to my ongoing list
driver.find_element(By.CSS_SELECTOR,'a[class="header-list-button "]').click()
driver.find_element(By.PARTIAL_LINK_TEXT,'Anime List').click()
driver.find_element(By.CSS_SELECTOR,'a[class="status-button watching "]').click()
driver.find_element(By.PARTIAL_LINK_TEXT,'Progress').click()

## get anime names
anime_list = [anime.get_attribute("text") for anime in driver.find_elements_by_xpath("//a[@class='link sort']")][5::2]


## get episode numbers
episode_list = []
for episode in driver.find_elements_by_xpath("//a[@class='link']"):
    try: episode_list.append(int(episode.get_attribute("text")))
    except: pass
episode_list = episode_list[1::2]
print(int(i.get_attribute('innerHTML')))

    
episode_list = driver.find_elements_by_xpath("//a[@class='link']")
for i in episode_list:
    try: print(int(i.get_attribute('innerHTML')))
    except: pass

## wrap error
##try:
##    driver.find_element(By.ID,'loginUserName').send_keys('guckyisme')
##except NoSuchElementException:
##    print("Element not found!")

driver.get('https://animeschedule.net/')
driver.find_element(By.ID,'search-icon').click()
driver.find_element(By.ID,'header-search-bar').send_keys('Shaman King (2021)')
driver.find_element(By.CSS_SELECTOR,'a[class="tt-suggestion tt-selectable"]').click()




def update_time(q = 'y'):
    try:
        for index,_ in enumerate(animes):
            driver.get(f'https://animeschedule.net/anime/{animes[index]}')
            driver.implicitly_wait(3)

            time = driver.find_element(By.XPATH, '//*[@id="countdown-wrapper"]/div/time').text
            time = driver.find_element(By.CSS_SELECTOR,'time[class="countdown-time countdown-time-raw"]').text
            print(time)
            
            for j in ('d','h','m'):
                if j not in time:
                    globals()[j] = 0
                else:
                    for i in time.split():
                        if i.find(j) != -1:
                            globals()[j] = int(i[:-1])

            time_delta = datetime.timedelta(days = d, hours = h, minutes = m)

            anime_long_list[index] = [animes[index], episodes[index], time, time_delta]
            
        anime_long_list.sort(key=lambda x: x[3])
        for anime_list in anime_long_list[:]:
            print('\t'+str(anime_list[:-1])+',')

        if q == 'y':
            driver.quit()
    except Exception as e:
        print(e)
        driver.quit()

updated_anime = [
	['komi-san-wa-comyushou-desu', 11, '2d 23h 41m'],
	['shaman-king-2021', 36, '3d 17h 36m'],
	['ousama-ranking', 10, '4d 36m'],
        ]









def play_anime():
    update_time(q = 'n')
    anime, episode, _, time_delta = anime_long_list[0]
    hours, remainder = divmod(time_delta.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)
    print(f"{int(hours)} hours, {int(minutes)} minutes left")
    if time_delta <= datetime.timedelta(hours = 1):
        if input(f"Ready for {anime} episode {episode}?: ").lower() == 'y':
            driver.get(f'https://www1.gogoanime.cm/{anime}-episode-{episode}')
    else:
        print("Be patient, weeb!")
        driver.quit()
        exit()
































