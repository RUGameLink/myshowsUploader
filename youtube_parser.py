import json
import time

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import re


def parse_page(url, second):
    # create a new chrome browser instance
    driver = webdriver.Chrome(executable_path="chrome_driver/chromedriver.exe")

    # navigate to youtube
    driver.get(url)
    end_time = time.time() + second
    j = 0
    while time.time() < end_time:
        driver.execute_script(f"window.scrollTo(0, {j});")
        print(j)
        j += 1

    # wait for the page to load
    print("перекур")
    sleep(10)
    print("парсинг данных...")

    try:
        # find all the video elements on the page
        videos = driver.find_elements(By.XPATH, '//*[@id="content"]')
        videos.pop(0)
        video_data = []
        i = 0
        while i < len(videos):
            if videos[i].text == "":
                return video_data
            line = str(videos[i].text)
            print(line)
            split_text = videos[i].text.splitlines()
            #print(split_text)
            pattern = re.compile(r'^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$')
            if(pattern.match(split_text[0])):
                text_line = f"{split_text[1]}%%{split_text[0]}\n"
                video_data.append(text_line)
            split_text.clear()
            i += 1
        return video_data
    except Exception as exept:
        print(exept)
    finally:
        driver.close()
        driver.quit()


def write_to_json(data):
    MyFile = open('output.txt', 'w')
    MyFile.writelines(data)
    MyFile.close()


def main():
    url = "https://www.youtube.com/GohaMedia/videos"
    text = input("Введите время (секунды): ")
    second = int(text)
    data = parse_page(url, second=second)
    print("\n\nзапись данных в файл\n\n")
    write_to_json(data)
    print(f"\n\nЗаписано {len(data)} видео\n\n")

if __name__ == '__main__':
    main()