# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

options = webdriver.chrome.options.Options()
options.add_argument('--user-data-dir=' + os.environ.get("PROFILE_PATH"))
driver = webdriver.Chrome(executable_path=os.environ.get("DRIVER_PATH"), options=options)

driver.get(os.environ.get("TARGET_PAGE"))

time.sleep(2)

every_one = driver.find_element_by_xpath('/html/body/div[5]/div[4]/div[2]/div/div[2]/span').text

count = 0

# clickして戻る
def clickAndReturn(userId):
    time.sleep(int(os.environ.get("SLEEP_TIME")))
    nonErr = True
    try:
        driver.find_element_by_id(userId).click()
    except:
        print("要素無し")
        nonErr = False
        pass
    global count
    count += 1
    print("-- click to: " + userId + " --- count: " + str(count) +" / " + every_one)
    if nonErr:
        driver.back()

#ページのlink要素全て取得
def createUserList():
    userList = []
    for i, g in enumerate(driver.find_elements_by_class_name("link-area")):
        id = g.get_attribute("id")
        userList.append(id)
    return userList

#ターゲットのリストを全てクリック
def marking(userList):
    for userId in userList:
        clickAndReturn(userId)
def loadPage():
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, -50);")
    time.sleep(6)
# 要素削る
def editList(lastIndex, userList):
    del userList[:lastIndex]
    return userList

def firstCicle():
    userList = createUserList()
    print(userList)
    marking(userList)
    loadPage()
    return len(userList)

def markCicle(lastIndex):
    userList = createUserList()
    editList(lastIndex, userList)
    print(userList)
    marking(userList)
    loadPage()
    return len(userList)

lastIndex = 0
lastIndex = firstCicle()

def secondCicle():
    global lastIndex
    for i in range(500):
        lastIndex = markCicle(lastIndex)

secondCicle()