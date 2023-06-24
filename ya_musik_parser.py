from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time

url = "https://music.yandex.ru/album/10431351?activeTab=track-list&dir=asc"

# Установка опций для Chrome WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Запуск браузера в фоновом режиме

# Создание экземпляра Chrome WebDriver
driver = webdriver.Chrome(executable_path="chrome_driver/chromedriver.exe")

# Загрузка страницы
driver.get(url)

# Получение содержимого страницы
page_content = driver.page_source

j = 0
while time.time() < 200: #Заменить 200
    driver.execute_script(f"window.scrollTo(0, {j});")
    print(j)
    j += 100
    try:
        # find all the video elements on the page
        videos = driver.find_elements(By.XPATH, '/html/body/div[1]/div[13]/div[2]/div/div/section[2]/div[3]/div/div[1]')
        videos.pop(0)
        video_data = []
        i = 0
        while i < len(videos):
            print(videos[i].text)
    except Exception as exept:
        print(exept)
    finally:
        driver.close()
        driver.quit()