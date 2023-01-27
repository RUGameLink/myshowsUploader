from selenium import webdriver
import time
import pickle
from selenium.webdriver.common.by import By

def main():
    driver = webdriver.Chrome(executable_path="chrome_driver/chromedriver.exe")
    url = "https://old.myshows.me/mt/"
#try:
    # driver.get(url=url)
    #
    # time.sleep(40)
    # pickle.dump(driver.get_cookies(), open("cookies", "wb"))
    driver.get(url=url)
    time.sleep(5)
    for cookie in pickle.load(open("cookies", "rb")):
        driver.add_cookie(cookie)

    time.sleep(5)
    driver.get(url=url)
    time.sleep(5)
    video_info = []
    data_videos = open("output.txt", "r")
    for video in data_videos:
        data = video.split('%%')
        video_info.append(data)
    video_info.reverse()
    video_info.pop(0)
    table_episode = driver.find_element(By.XPATH, '/html/body/div/main/div[4]/table/tbody/tr[2]/td[7]/a[1]').click()
    time.sleep(5)

    for info in video_info:

        button_add = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/a').click()
        time.sleep(2)

        title_input = driver.find_element(By.ID, 'title')
        title_input.clear()
        title_input.send_keys(info[0])
        time.sleep(2)

        episode_input = driver.find_element(By.ID, 'episodeNumber')
        episode_input.clear()
        episode_input.send_keys("0")
        time.sleep(2)

        season_input = driver.find_element(By.ID, 'seasonNumber')
        season_input.clear()
        season_input.send_keys("2023")
        time.sleep(2)

        runtime_input = driver.find_element(By.ID, 'runtime')
        runtime_input.clear()
        runtime_input.send_keys(info[1])
        time.sleep(2)

        try:
            button_save = driver.find_element(By.XPATH, '//*[@id="data-form"]/div[2]/div[1]/div[2]/button').click()
        except Exception as exept:
            print(exept)






# except Exception as exept:
#     print(exept)
# finally:
    driver.close()
    driver.quit()

if __name__ == '__main__':
    main()
