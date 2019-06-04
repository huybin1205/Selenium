from selenium import webdriver
from time import sleep
import time

driver = webdriver.Chrome('D:/ProjectPython/Selenium/chromedriver.exe')
url = "https://www.facebook.com/"
username = ""
password = ""
driver.get(url)

emailelement = driver.find_element_by_xpath("""//*[@id="email"]""")
emailelement.send_keys(username)
passelement = driver.find_element_by_xpath("""//*[@id="pass"]""")
passelement.send_keys(password)
driver.find_element_by_xpath("""//*[@id="loginbutton"]""").click()
content = "khoa công nghệ thông tin - hutech";
driver.get("https://www.facebook.com/search/posts/?q="+content+"&epa=SERP_TAB")
time.sleep(5)
i = 0
count = 0
#POST
while True:
    posts = driver.find_elements_by_class_name("_5pbx")
    if i == 500:
        for post in posts:
            if post.text != "":
                print("*"*200)
                print(str(count)+" - "+post.text)
                count +=1
        break
    i+=1