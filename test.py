from selenium import webdriver
import time

webdriver = webdriver.Chrome(executable_path="C:\\Users\\worker\\PycharmProjects\\myshowsUploader\\chrome_driver\\chromedriver.exe")
url = "https://old.myshows.me/mt/"
try:
    webdriver.get(url=url)
    time.sleep(5)
except Exception as exept:
    print(exept)
finally:
    webdriver.close()
    webdriver.quit()