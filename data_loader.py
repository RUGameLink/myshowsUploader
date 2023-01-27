from selenium import webdriver
import time
import pickle

webdriver = webdriver.Chrome(executable_path="chrome_driver/chromedriver.exe")
url = "https://old.myshows.me/mt/"
try:
    # webdriver.get(url=url)
    #
    # time.sleep(40)
    # pickle.dump(webdriver.get_cookies(), open("cookies", "wb"))
    webdriver.get(url=url)
    time.sleep(5)
    for cookie in pickle.load(open("cookies", "rb")):
        webdriver.add_cookie(cookie)

    time.sleep(5)
    webdriver.get(url=url)
    time.sleep(5)

except Exception as exept:
    print(exept)
finally:
    webdriver.close()
    webdriver.quit()
