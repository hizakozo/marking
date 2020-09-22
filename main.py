# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from os.path import join, dirname
from dotenv import load_dotenv
# コメントテスト
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

lastIndex = 0

# clickして戻る
def clickAndReturn(userId):
    isErr = False
    try:
        driver.find_element_by_id(userId).click()
    except:
        isErr = True
        print("要素なし")
        pass
    # time.sleep(0.5)
    
    try:
        ele = driver.find_element_by_xpath('/html/body/center/h1')
        if(ele.text == '502 Bad Gateway'):
            print('502 Bad Gateway')
            isErr = True
            driver.refresh()
            time.sleep(3)
    except:
        pass

    if(isErr == False):
        global count
        count += 1
        print("-- click to: " + userId + " --- count: " + str(count) +" / " + every_one)
        driver.back()

#1,クリック対象ユーザーの作成
def createUserList():
    global lastIndex
    userList = []
    for i, g in enumerate(driver.find_elements_by_class_name("link-area")):
        id = g.get_attribute("id")
        userList.append(id)
    del userList[:lastIndex]
    print(userList)
    lastIndex = len(userList)
    if(len(userList) == []):
        print("user list is enpty")
        driver.refresh()
    return userList

#2,ターゲットを全てクリック
def marking(userList):
    for userId in userList:
        if(count == int(every_one[:len(every_one)-2]) + 100):
            driver.close()
        clickAndReturn(userId)

#3,ページのロード
def loadPage():
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, -50);")
    time.sleep(4)

#1,2,3を繰り返す
while True:
    userList = createUserList()
    marking(userList)
    loadPage()