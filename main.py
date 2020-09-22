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
    noErr = True
    try:
        driver.find_elements_by_class_name("user-card-small_main-photo")
    except:
        print("真っ白エラー")
        driver.refresh()
        noErr = False
        time.sleep(3)
        pass

    try:
        driver.find_element_by_id(userId).click()
        time.sleep(0)
    except:
        noErr = False
        print("要素なし")
        pass
    
    try:
        ele = driver.find_element_by_xpath('/html/body/center/h1')
        if(ele.text == '502 Bad Gateway'):
            print('502 Bad Gateway')
            noErr = False
            driver.refresh()
            time.sleep(3)
    except:
        pass

    if(noErr):
        global count
        count += 1
        print("-- click to: " + userId + " --- count: " + str(count) +" / " + every_one)
        driver.back()

def subCreateUserList():
    userList = []
    for i, g in enumerate(driver.find_elements_by_class_name("link-area")):
        id = g.get_attribute("id")
        userList.append(id)
    del userList[:lastIndex]
    print(userList)
    return userList

#1,クリック対象ユーザーの作成
def createUserList():
    global lastIndex
    userList = subCreateUserList()
    lastIndex = len(userList)
    if(len(userList) == []):
        driver.refresh()
        subCreateUserList()
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
    time.sleep(2)

#1,2,3を繰り返す
while True:
    userList = createUserList()
    marking(userList)
    loadPage()