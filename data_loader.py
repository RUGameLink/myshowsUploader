from selenium import webdriver
import time
import pickle
from selenium.webdriver.common.by import By

def upload_episodes(season_n, episode_n, path, channel_name, max_ep):
    driver = webdriver.Chrome(executable_path="chrome_driver/chromedriver.exe")
    url = "https://old.myshows.me/mt/"

    # driver.get(url=url)
    #
    # time.sleep(40)
    # pickle.dump(driver.get_cookies(), open("cookies", "wb"))

    #=======
    try:
        driver.get(url=url)
        time.sleep(5)
        for cookie in pickle.load(open("cookies", "rb")):
            driver.add_cookie(cookie)

        time.sleep(5)
        driver.get(url=url)
        time.sleep(5)
        video_info = []
        data_videos = open(f"{channel_name}.txt", "r", encoding='utf-8')
        for video in data_videos:
            data = video.split('%%')
            video_info.append(data)
        video_info.reverse()
        video_info.pop(0)
        table_episode = driver.find_element(By.XPATH, f'{path}').click()
        time.sleep(5)
        season_num = season_n
        episode_num = episode_n + 1
        for info in video_info:

        #    episode_number = driver.find_element(By.XPATH, '/html/body/div/main/div[4]/table/tbody/tr[1]/td[2]').text
        #    new_neumber = int(episode_number) + 1
        #    time.sleep(1)

            driver.find_element(By.XPATH, '/html/body/div/main/div[2]/a').click()
            time.sleep(1)

            title_input = driver.find_element(By.ID, 'title')
            title_input.clear()
            title_input.send_keys(info[0])
            time.sleep(1)

            episode_input = driver.find_element(By.ID, 'episodeNumber')
            episode_input.clear()
            episode_input.send_keys(f"{episode_num}")
            time.sleep(1)

            season_input = driver.find_element(By.ID, 'seasonNumber')
            season_input.clear()
            season_input.send_keys(F"{season_num}")
            time.sleep(1)
            if(episode_num == max_ep):
                episode_num = 0
                season_num += 1
            episode_num += 1
            if len(info) == 2:
                runtime_input = driver.find_element(By.ID, 'runtime')
                runtime_input.clear()
                runtime_input.send_keys(info[1])
                time.sleep(1)
            else:
                try:
                    driver.find_element(By.XPATH, '//*[@id="data-form"]/div[2]/div[1]/div[2]/button').click()
                    time.sleep(2)
                except Exception as exept:
                    print("Ошибка! Файл Печенек устрарел!")
    except Exception as exept:
        print(exept)
    finally:
        driver.close()
        driver.quit()


def cookies():
    driver = webdriver.Chrome(executable_path="chrome_driver/chromedriver.exe")
    url = "https://old.myshows.me/mt/"

    driver.get(url=url)

    time.sleep(40)
    pickle.dump(driver.get_cookies(), open("cookies", "wb"))


    driver.close()
    driver.quit()


class Data_Loader:
    def upload_to_myshows(self, channel_name, path, max_ep):
        season = input("Введите номер сезона:")
        season_n = int(season)
        episode = input("Введите номер последнего загруженного эпизода (если эпизодов нет -> 0):")
        episode_n = int(episode)
        upload_episodes(season_n, episode_n, path, channel_name, max_ep)

    def save_cookies(self):
        cookies()

