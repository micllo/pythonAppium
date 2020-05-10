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


# 屏幕向上滑动（效果：屏幕往'下'翻动）
def swipeUp(driver, t=1000):
    l = getSize(driver)
    x = int(l[0] * 0.5)    # 固定 x 坐标
    y1 = int(l[1] * 0.75)  # 起始 y 坐标
    y2 = int(l[1] * 0.25)  # 终点 y 坐标
    driver.swipe(x, y1, x, y2, t)


# 屏幕向下滑动（效果：屏幕往'上'翻动）
def swipeDown(driver, t=1000):
    l = getSize(driver)
    x = int(l[0] * 0.5)    # 固定 x 坐标
    y1 = int(l[1] * 0.25)  # 起始 y 坐标
    y2 = int(l[1] * 0.75)  # 终点 y 坐标
    driver.swipe(x, y1, x, y2, t)


# 屏幕向左滑动（效果：屏幕往'右'翻动）
def swipLeft(driver, t=1000):
    l = getSize(driver)
    y = int(l[1] * 0.5)     # 固定 y 坐标
    x1 = int(l[0] * 0.75)   # 起始 x 坐标
    x2 = int(l[0] * 0.05)   # 终点 x 坐标
    driver.swipe(x1, y, x2, y, t)


# 屏幕向右滑动（效果：屏幕往'左'翻动）
def swipRight(driver, t=1000):
    l = getSize(driver)
    y = int(l[1] * 0.5)    # 固定 y 坐标
    x1 = int(l[0] * 0.05)  # 起始 x 坐标
    x2 = int(l[0] * 0.75)  # 终点 x 坐标
    driver.swipe(x1, y, x2, y, t)


desired_caps = {
    'platformName': 'Android',
    # 小米 5S
    'platformVersion': '7.0',
    'deviceName': '192.168.31.136:5555',

    # 锤子 旧
    # 'platformVersion': '7.1.1',
    # 'deviceName': '15a6c95a',

    # 应用宝 app
    'appPackage': 'com.tencent.android.qqdownloader',
    'appActivity': 'com.tencent.pangu.link.SplashActivity'
    # 唤醒屏幕
    # 'unlockType': "pattern"
    # 'unlockKey': "12589"
}

driver = webdriver.Remote('192.168.31.10:4723/wd/hub', desired_caps)

driver.implicitly_wait(3)


# 点击'我知道了'按钮
driver.tap([(250, 1300)])  # 触摸点击
time.sleep(2)

# 点击相关'允许'按钮
driver.find_element_by_id("android:id/button1").click()
time.sleep(2)
driver.find_element_by_id("android:id/button1").click()
time.sleep(2)

# 点击相关'X'按钮
driver.find_element_by_id("com.tencent.android.qqdownloader:id/b3f").click()
time.sleep(2)

# 获取搜索文本框1，并点击
driver.tap([(150, 120)])
# driver.find_element_by_id("com.tencent.android.qqdownloader:id/awt").click()
time.sleep(2)

# 获取搜索文本框2，并输入内容
search_text2 = driver.find_element_by_id("com.tencent.android.qqdownloader:id/yv")
search_text2.send_keys("皇室战争")
time.sleep(2)

# 获取搜索按钮，并点击
driver.find_element_by_id("com.tencent.android.qqdownloader:id/a5t").click()
time.sleep(2)

# 上滑
swipeUp(driver, 1000)
time.sleep(2)

# 下滑
swipeDown(driver, 1000)
time.sleep(2)

# 获取"皇室战争"tab，并点击
hszz_tab = driver.find_element_by_android_uiautomator('new UiSelector().text("皇室战争")')
print(hszz_tab.text)
print(hszz_tab.location)  # {'x': 144, 'y': 90}
print(hszz_tab.get_attribute("text"))
print(hszz_tab.get_attribute("bounds"))  # str -> [144,90][780,198]
hszz_tab.click()
time.sleep(2)

driver.quit()
time.sleep(2)

# 截屏
# driver.get_screenshot_as_file("test1.png")
