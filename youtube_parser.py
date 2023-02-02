import json
import time

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import re


def get_minute(param):
    date = param.split(':')
    if(len(date) == 3):
        result = int(date[0]) * 60 + int(date[1])
    else:
        result = int(date[0])
    return result


def parse_page(url, second):
    driver = webdriver.Chrome(executable_path="chrome_driver/chromedriver.exe")

    driver.get(url)
    end_time = time.time() + second
    j = 0
    while time.time() < end_time:
        driver.execute_script(f"window.scrollTo(0, {j});")
        print(j)
        j += 100

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
            pattern = re.compile(r'^([0-1]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$')
            pattern_two = re.compile(r'^([0-5][0-9]):[0-5][0-9]$')
            pattern_three = re.compile(r'^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$')
            if((pattern_two.match(split_text[0]))):
                minute = get_minute(split_text[0])
                text_line = f"[СТРИМ] {split_text[1]}%%{minute}\n"
                video_data.append(text_line)
            elif(pattern.match(split_text[0])):
                minute = get_minute(split_text[0])
                text_line = f"[СТРИМ] {split_text[1]}%%{minute}\n"
                video_data.append(text_line)
            elif (pattern_three.match(split_text[0])):
                minute = get_minute(split_text[0])
                text_line = f"[СТРИМ] {split_text[1]}%%{minute}\n"
                video_data.append(text_line)
            else:
                text_line = f"[СТРИМ] {split_text[0]}\n"
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
    MyFile = open('output.txt', 'w', encoding="utf-8")
    MyFile.writelines(data)
    MyFile.close()


def main():
    url = "https://www.youtube.com/@TheGideonGames/streams"
    text = input("Введите время (секунды): ")
    second = int(text)
    data = parse_page(url, second=second)
    print("\n\nзапись данных в файл\n\n")
    write_to_json(data)
    print(f"\n\nЗаписано {len(data)} видео\n\n")

if __name__ == '__main__':
    main()