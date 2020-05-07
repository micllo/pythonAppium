from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
import time

desired_caps = {
    # 基本
    'platformName': 'IOS',
    'automationName': 'xcuitest',

    # 应用APP
    'app': 'com.apple.Health',  # 已存在的应用 直接用 bundleId
    # 'app': '/Users/micllo/Downloads/appium/ios/TestApp.app'  #  .app包路径
           
    # 模拟器 8
    # 'platformVersion': '13.4',
    # 'deviceName': 'iPhone 8',
    # 'udid': '647616B3-44E3-4198-8578-E22FFD8EE43D'

    # 模拟器 11
    'platformVersion': '13.4',
    'deviceName': 'iPhone 11',
    'udid': '5F302EEC-C5AA-489D-924D-45FB91C9C894'

    # 真机
    # 'platformVersion': '10.3',
    # 'deviceName': 'iPhone 7',
    # 'udid': '3cbb25d055753f2305ec70ba6dede3dca5d500bb'

}

driver = webdriver.Remote('192.168.31.10:4723/wd/hub', desired_caps)
driver.implicitly_wait(3)





# # 输入第一个数字
# input_1 = driver.find_element_by_xpath("//XCUIElementTypeTextField[@name=\"IntegerA\"]")
# input_1.click()
# input_1.send_keys(1)
# time.sleep(1)
#
# # 输入第二个数字
# input_2 = driver.find_element_by_xpath("//XCUIElementTypeTextField[@name=\"IntegerB\"]")
# input_2.click()
# input_2.send_keys(2)
# time.sleep(1)
#
# # 点击 计算按钮
# sum_btn = driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"ComputeSumButton\"]")
# sum_btn.click()
# time.sleep(1)
#
# # 获取计算结果
# answer_el = driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name=\"Answer\"]")
# print(answer_el.text)
# # 隐藏键盘
# driver.hide_keyboard()
# # 截屏
# driver.get_screenshot_as_file("test1.png")
#
#
# # 点击 弹框按钮 并确认
# popup_btn = driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"Check calendar authorized\"]")
# popup_btn.click()
# time.sleep(2)
# driver.get_screenshot_as_file("test2.png")
#
# ok_btn = driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"OK\"]")
# ok_btn.click()
# time.sleep(1)
#
# # 获取拖动条元素
# seekbar_el = driver.find_element_by_xpath("//XCUIElementTypeSlider[@name=\"AppElem\"]")
# print(seekbar_el.text)
#
#
# # # 获取拖动条 高度与宽度
# # width = seekbar_el.size.get("width")
# # height = seekbar_el.size.get("height")
# # print("width : " + str(width))
# # print("height : " + str(height))
# #
# # # 获取拖动条 坐标
# # x = seekbar_el.location.get("x")
# # y = seekbar_el.location.get("y")
# # x2 = int(width * 0.75)
# # print("x : " + str(x))
# # print("y : " + str(y))
# # print("x2 : " + str(x2))
#
# # 滑动条：右滑
# # driver.swipe(x, y, x2, y, 1000)
# # TouchAction(driver).press(x=149, y=303).move_to(x=189, y=305).release().perform()
#
# # time.sleep(2)
# # print(seekbar_el.text)
#
# # 退出应用
# driver.quit()
# time.sleep(2)

