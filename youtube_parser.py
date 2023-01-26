import json
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

def parse_page(url):
    # create a new chrome browser instance
    driver = webdriver.Chrome(executable_path="C:\\Users\\worker\\PycharmProjects\\myshowsUploader\\chrome_driver\\chromedriver.exe")

    # navigate to youtube
    driver.get(url)
    j = 0
    while j < 1000:
        driver.execute_script(f"window.scrollTo(0, {j});")
        print(j)
        j += 1

    # wait for the page to load
    sleep(10)


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
            text_line = f"title: {split_text[1]} time: {split_text[0]}\n"
        #    print(text_line)
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
    data = parse_page(url)
    write_to_json(data)

if __name__ == '__main__':
    main()