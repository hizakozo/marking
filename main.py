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
lastIndex = 0


def element_check_index(class_name):
    not_is_exist = True
    while not_is_exist:
        try:
            if (WebDriverWait(driver, 1).until(
                    EC.visibility_of_element_located((By.CLASS_NAME, class_name))).is_displayed()):
                not_is_exist = False
        except:
            print('ページリロード')
            driver.refresh()
            time.sleep(2)
            pass


def element_check_profile(class_name):
    number_of_trials = 0
    not_is_exist = True
    while number_of_trials != 3 and not_is_exist:
        try:
            if (WebDriverWait(driver, 1).until(
                    EC.visibility_of_element_located((By.CLASS_NAME, class_name))).is_displayed()):
                not_is_exist = False
        except:
            number_of_trials += 1
            print('プロフィールページリロード')
            driver.refresh()
            time.sleep(2)
            pass
    if number_of_trials >= 3:
        driver.back()


# clickして戻る
def click_and_return(user_id):
    no_err = True
    element_check_index('user-card-small_main-photo')
    try:
        driver.find_element_by_id(user_id).click()
    except:
        no_err = False
        print("要素なし")
        pass

    try:
        ele = driver.find_element_by_xpath('/html/body/center/h1')
        if ele.text == '502 Bad Gateway':
            print('502 Bad Gateway')
            no_err = False
            driver.refresh()
    except:
        pass

    if no_err:
        global count
        count += 1
        print("-- click to: " + user_id + " --- count: " + str(count) + " / " + every_one)
        element_check_profile('profile-thumb_photo_img')
        driver.back()


# 1,クリック対象ユーザーの作成
def create_user_list():
    global lastUserId
    global lastIndex
    user_list = []
    for i, g in enumerate(driver.find_elements_by_class_name("link-area")):
        user_list.append(g.get_attribute("id"))
    if lastUserId != '':
        try:
            del user_list[:user_list.index(lastUserId) + 1]
        except:
            print("last user id is empty")
            del user_list[:lastIndex]
            pass
    print(user_list)
    if len(user_list) > 0:
        lastUserId = user_list[-1]
    lastIndex = len(user_list)
    return user_list


# 2,ターゲットを全てクリック
def marking(user_list):
    for userId in user_list:
        if count == int(every_one[:len(every_one) - 2]) + 20:
            driver.close()
        click_and_return(userId)


# 3,ページのロード
def load_page():
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, -50);")
    time.sleep(2)


# 1,2,3を繰り返す
while True:
    userList = create_user_list()
    marking(userList)
    load_page()
