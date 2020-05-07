from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# 获得机器屏幕大小x,y
def getSize(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    print(x, y)
    return x, y


# 屏幕向上滑动
def swipeUp(driver, t):
    l = getSize(driver)
    x1 = int(l[0] * 0.5)  # x坐标
    y1 = int(l[1] * 0.75)  # 起始y坐标
    y2 = int(l[1] * 0.25)  # 终点y坐标
    driver.swipe(x1, y1, x1, y2, t)


# 屏幕向下滑动
def swipeDown(driver, t):
    l = getSize(driver)
    x1 = int(l[0] * 0.5)  # x坐标
    y1 = int(l[1] * 0.25)  # 起始y坐标
    y2 = int(l[1] * 0.75)  # 终点y坐标
    driver.swipe(x1, y1, x1, y2, t)


# 屏幕向左滑动
def swipLeft(driver, t):
    l = getSize(driver)
    x1 = int(l[0] * 0.75)   # x 坐标
    y1 = int(l[1] * 0.5)    # y 坐标
    x2 = int(l[0] * 0.05)   # x 坐标
    driver.swipe(x1, y1, x2, y1, t)


# 屏幕向右滑动
def swipRight(driver, t):
    l = getSize(driver)
    x1 = int(l[0] * 0.05)
    y1 = int(l[1] * 0.5)
    x2 = int(l[0] * 0.75)
    driver.swipe(x1, y1, x2, y1, t)


desired_caps = {
    'platformName': 'Android',
    # 小米 5S
    # 'platformVersion': '7.0',
    # 'deviceName': '192.168.31.136:5555',

    # 锤子 旧
    'platformVersion': '7.1.1',
    'deviceName': '15a6c95a',

    # 应用宝 app
    'appPackage': 'com.tencent.android.qqdownloader',
    'appActivity': 'com.tencent.pangu.link.SplashActivity'
    # 唤醒屏幕
    # 'unlockType': "pattern"
    # 'unlockKey': "12589"
}

driver = webdriver.Remote('192.168.31.10:4723/wd/hub', desired_caps)

wait = WebDriverWait(driver, 30)

# 点击'我知道了'按钮
iknow_btn = wait.until(EC.presence_of_element_located((By.ID, "com.tencent.android.qqdownloader:id/a2y")))
iknow_btn.click()
time.sleep(2)

# 点击相关'允许'按钮
allow_btn1 = wait.until(EC.presence_of_element_located((By.ID, "android:id/button1")))
allow_btn1.click()
time.sleep(2)

allow_btn2 = wait.until(EC.presence_of_element_located((By.ID, "android:id/button1")))
allow_btn2.click()
time.sleep(2)

# 点击相关'X'按钮
close_btn = wait.until(EC.presence_of_element_located((By.ID, "com.tencent.android.qqdownloader:id/b3f")))
close_btn.click()
time.sleep(2)

# 获取搜索文本框1，并点击
search_text1 = wait.until(EC.presence_of_element_located((By.ID, "com.tencent.android.qqdownloader:id/awt")))
search_text1.click()
time.sleep(2)

# 获取搜索文本框2，并输入内容
search_text2 = wait.until(EC.presence_of_element_located((By.ID, "com.tencent.android.qqdownloader:id/yv")))
search_text2.send_keys("皇室战争")
time.sleep(2)

# 获取搜索按钮，并点击
search_btn = wait.until(EC.presence_of_element_located((By.ID, "com.tencent.android.qqdownloader:id/a5t")))
search_btn.click()
time.sleep(2)

# 上滑
swipeUp(driver, 1000)
time.sleep(2)

# 下滑
swipeDown(driver, 1000)
time.sleep(2)

# 获取"皇室战争"tab，并点击
hszz_tab = wait.until(EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.ImageView")))
hszz_tab.click()
time.sleep(2)

driver.quit()
time.sleep(2)