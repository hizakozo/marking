# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-controller_summary')))
every_one = driver.find_element_by_xpath('/html/body/div[5]/div[4]/div[2]/div/div[2]/span').text

count = 0

lastUserId = ''

# clickして戻る
def clickAndReturn(userId):
    noErr = True
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'user-card-small_main-photo')))
    try:
        driver.find_element_by_id(userId).click()
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
    except:
        pass

    if(noErr):
        global count
        count += 1
        print("-- click to: " + userId + " --- count: " + str(count) +" / " + every_one)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "profile-thumb_photo_img")))
        driver.back()

#1,クリック対象ユーザーの作成
def createUserList():
    global lastUserId
    userList = []
    for i, g in enumerate(driver.find_elements_by_class_name("link-area")):
        id = g.get_attribute("id")
        userList.append(id)
    if (lastUserId != ''):
        del userList[:userList.index(lastUserId) + 1]
    print(userList)
    lastUserId = userList[-1]
    return userList

#2,ターゲットを全てクリック
def marking(userList):
    for userId in userList:
        if(count == int(every_one[:len(every_one)-2]) + 20):
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