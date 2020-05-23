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

# # 点击相关'允许'按钮
# driver.find_element_by_id("android:id/button1").click()
# time.sleep(2)
# driver.find_element_by_id("android:id/button1").click()
# time.sleep(2)
#
# # 点击相关'X'按钮
# driver.find_element_by_id("com.tencent.android.qqdownloader:id/b3f").click()
# time.sleep(2)
#
# # 获取搜索文本框1，并点击
# driver.tap([(150, 120)])
# # driver.find_element_by_id("com.tencent.android.qqdownloader:id/awt").click()
# time.sleep(2)
#
# # 获取搜索文本框2，并输入内容
# search_text2 = driver.find_element_by_id("com.tencent.android.qqdownloader:id/yv")
# search_text2.send_keys("皇室战争")
# time.sleep(2)
#
# # 获取搜索按钮，并点击
# driver.find_element_by_id("com.tencent.android.qqdownloader:id/a5t").click()
# time.sleep(2)

# 上滑
swipeUp(driver, 1000)
time.sleep(2)

# 下滑
swipeDown(driver, 1000)
time.sleep(2)


print("+++++++++++++++++")
print("driver.page_source -> " + str("皇室战争" in driver.page_source))
print("+++++++++++++++++")

# 获取"皇室战争"tab (通过text文本定位的第二个)
hszz_ele_list = driver.find_elements_by_android_uiautomator('new UiSelector().text("皇室战争")')

hszz_tab = hszz_ele_list[1]
print(hszz_tab.text)
print(hszz_tab.location)  # {'x': 144, 'y': 90}
print(hszz_tab.get_attribute("text"))
print(hszz_tab.get_attribute("bounds"))  # str -> [144,90][780,198]
hszz_tab.click()
time.sleep(2)

driver.quit()
time.sleep(2)

# 截屏
driver.get_screenshot_as_file("test1.png")


# sync_run_case.py

# @async
# def suite_sync_run_case(pro_name):
#     """
#     同时执行不同用例（ 通过动态修改'suite.py'文件中'TestSuite'类中的'run'方法，使得每个线程中的结果都可以记录到测试报告中 ）
#     :param pro_name: 项目名称
#
#         【 备 注 】
#         1.suite 实例对象（包含了所有的测试用例实例，即继承了'unittest.TestCase'的子类的实例对象 test_instance ）
#         2.启动 Android 设备中的 APP 应用（每个用例执行一次）：在每个'测试类'的 setUp 方法中执行 ( 继承 ParaCase 父类 )
#         3.关闭 Android 设备中的 APP 应用 （每个用例执行一次）：在每个'测试类'的 tearDown 方法中执行 ( 继承 ParaCase 父类 )
#
#         【 保 存 截 屏 图 片 ID 的 逻 辑 】
#         1.为实例对象'suite'<TestSuite>动态添加一个属性'screen_shot_id_dict' -> screen_shot_id_dict = {}
#         2.每个测试方法中将所有截屏ID都保存入'screen_shot_id_list' -> screen_shot_id_dict = ['aaa', 'bbb', 'ccc']
#         3.实例对象'suite'在重写的'new_run'方法中 将'screen_shot_id_list'添加入'screen_shot_id_dict'
#         4.screen_shot_id_dict = { "测试类名.测试方法名":['aaa', 'bbb'], "测试类名.测试方法名":['cccc'] }
#
#         【 并 发 线 程 数 逻 辑 】
#         1.通过ssh连接到 SDK 服务器
#         2.通过adb命令判断指定设备的连接情况：返回 已连接设备信息列表
#          [ { "thread_index": 1, "device_name": "小米5S", "platform_version": "7.0", "device_udid": "192.168.31.136:5555", "appium_server": "http://127.0.0.1:4724/wd/hub" } } ,
#            { "thread_index": 2, "device_name": "坚果Pro", "platform_version": "7.1.1", "device_udid": "192.168.31.253:4444", "appium_server": "http://127.0.0.1:4723/wd/hub" } } ]
#         3.返回的列表数量 作为 线程数量
#
#         【 每 个 用 例 使 用 Android 设 备 逻 辑 】
#         通过'当前线程名的索引'和'已连接设备列表' 获取 Appium 服务启动应用所需的能力参数 (指定设备，指定应用)
#
#     """
#     # （定时任务）需要判断 是否存在运行中的用例
#     if is_exist_start_case(pro_name):
#         send_DD_for_FXC(title=pro_name, text="#### '" + pro_name + "' 项目存在<运行中>的用例而未执行测试（定时任务）")
#         return "Done"
#
#     # 获取 已连接的 Android 设备信息列表
#     connected_android_device_list = get_connected_android_devices_info(pro_name)
#     # 列表数量 作为 线程数量
#     thread_num = len(connected_android_device_list)
#     log.info("\n线程数量 ： " + str(thread_num))
#     log.info("已连接的Android设备信息列表：" + str(connected_android_device_list) + "\n")
#
#     if thread_num == 0:
#         send_DD_for_FXC(title=pro_name, text="#### '" + pro_name + "' 项目 未连接任何 Android 设备")
#         return "Done"
#
#     # 将'测试类'中的所有'测试方法'添加到 suite 对象中（每个'测试类'实例对象包含一个'测试方法'）
#     from TestBase.test_case_unit import ParaCase
#     suite, on_line_test_method_name_list = ParaCase.get_online_case_to_suite(pro_name, connected_android_device_list)
#
#     if suite != "mongo error":
#         if is_null(on_line_test_method_name_list):
#             send_DD_for_FXC(title=pro_name, text="#### '" + pro_name + "' 项目<没有上线>的用例而未执行测试（定时任务）")
#         else:
#             # 为实例对象'suite'<TestSuite>动态添加一个属性'screen_shot_id_dict'（目的：保存截图ID）
#             setattr(suite, "screen_shot_id_dict", {})
#
#             # 为实例对象'suite'<TestSuite>动态添加一个属性'android_device_name_dict'（目的：保存使用的Android设备名称）
#             setattr(suite, "android_device_name_dict", {})
#
#             # 为实例对象'suite'<TestSuite>动态添加一个属性'thread_num'（目的：控制多线程数量）
#             setattr(suite, "thread_num", thread_num)
#
#             # 为实例对象'suite'<TestSuite>动态添加两个方法'run_test_custom'、'show_result_custom'（ 目的：供多线程中调用 ）
#             suite.run_test_custom = MethodType(run_test_custom, suite)
#             suite.show_result_custom = MethodType(show_result_custom, suite)
#
#             # 为实例对象'suite'<TestSuite>动态修改实例方法'run'（ 目的：启用多线程来执行case ）
#             suite.run = MethodType(new_run, suite)
#
#             # 运行测试，并生成测试报告
#             test_result, current_report_file = generate_report(pro_name=pro_name, suite=suite, title='Android自动化测试报告 - ' + pro_name,
#                                                                description='详细测试用例结果', tester="自动化测试", verbosity=2)
#
#             # 测试后发送预警
#             # send_warning_after_test(test_result, current_report_file)

########################################################################################################


# test_case_unit.py


# # -*- coding:utf-8 -*-
# import unittest
# from Common.com_func import log
# from Config import global_var as gv
# from Tools.mongodb import MongodbUtils
# from Env import env_config as cfg
# from Common.test_func import mongo_exception_send_DD
# from TestBase.app_action import get_android_driver
#
#
# class ParaCase(unittest.TestCase):
#
#     def __init__(self, pro_name, test_method="test_", connected_android_device_list=[]):
#         """
#         【 用 例 对 象 初 始 化 】
#         :param pro_name :
#         :param test_method : 这个参数必须是测试类中存在的以'test_'开头的方法
#         :param connected_android_device_list : 已连接设备信息列表
#         """
#         super(ParaCase, self).__init__(test_method)
#         self.log = log
#         self.pro_name = pro_name
#         self.test_method = test_method
#         self.connected_android_device_list = connected_android_device_list
#         # 截图ID列表
#         self.screen_shot_id_list = []
#         # 获取当前的'类名.方法名' (作用：每个用例的截图ID列表名称、每个用例使用的Android设备名称)
#         self.class_method_name = self.__class__.__name__ + "." + test_method
#         # 获取当前的'类名/方法名/'(作用：提供截屏路径)
#         self.class_method_path = self.__class__.__name__ + "/" + test_method + "/"
#         # 记录当前线程名的索引（目的：不同线程使用不同的登录账号）
#         self.current_thread_name_index = 0
#
#     def setUp(self):
#         """
#         【 每个用例对象执行前，需要进行如下配置 】
#         :return:
#         """
#         from Config.pro_config import get_login_accout
#         # 通过线程名的索引 获取登录账号
#         self.user, self.passwd = get_login_accout(self.current_thread_name_index)
#
#         # 获取'Android'驱动 和 设备名称
#         self.driver, self.device_name = get_android_driver(self.pro_name, self.current_thread_name_index,
#                                                            self.connected_android_device_list)
#         # 隐式等待时间
#         self.driver.implicitly_wait(gv.IMPLICITY_WAIT)
#
#     def tearDown(self):
#         """
#         【 每个用例对象执行后，需要进行如下配置 】
#         :return:
#         """
#         # 关闭应用
#         self.driver.quit()
#
#     @staticmethod
#     def get_online_case_to_suite(pro_name, connected_android_device_list=[]):
#         """
#         将'测试类'列表中的'上线'的'测试方法'添加入 suite 实例对象中
#         :param pro_name:
#         :param connected_android_device_list: 已连接设备信息列表
#         :return:
#         【 添 加 步 骤 】
#         1.从mongo中获取'上线'状态的'测试用例'列表
#         2.重置 上线用例的'运行状态：pending、开始时间：----、运行时间：----'
#         3.通过'项目名称'获取'测试类'列表
#         4.循环获取'测试类'列表中的所有'测试方法名称'
#         5.将这些'测试方法名称'与mongo中'上线'的'测试方法名称'作比较
#         6.匹配成功的，则实例化'测试类'时，并添加入'suite'实例对象中
#         【 备 注 】
#           实例化'测试类'时，必须带上该类中存在的以'test_'开头的方法名
#         """
#         with MongodbUtils(ip=cfg.MONGODB_ADDR, database=cfg.MONGODB_DATABASE, collection=pro_name) as pro_db:
#             try:
#                 # 获取上线用例列表
#                 query_dict = {"case_status": True}
#                 results = pro_db.find(query_dict, {"_id": 0})
#                 on_line_test_method_name_list = [result.get("test_method_name") for result in results]
#                 # 重置 上线用例的'运行状态：pending、开始时间：----、运行时间：----'
#                 update_dict = {"$set": {"run_status": "pending", "start_time": "----", "run_time": "----"}}
#                 pro_db.update(query_dict, update_dict, multi=True)
#             except Exception as e:
#                 on_line_test_method_name_list = []
#                 mongo_exception_send_DD(e=e, msg="获取'" + pro_name + "'项目'上线'测试用例数据")
#                 return "mongo error", on_line_test_method_name_list
#
#         from Config.pro_config import get_test_class_list
#         test_class_list = get_test_class_list(pro_name)
#         test_loader = unittest.TestLoader()
#         suite = unittest.TestSuite()
#         for test_class in test_class_list:
#             test_methods_name = test_loader.getTestCaseNames(test_class)
#             for test_method_name in test_methods_name:
#                 if test_method_name in on_line_test_method_name_list:  # 匹配'测试方法'名称
#                     test_instance = test_class(pro_name=pro_name, test_method=test_method_name,
#                                                connected_android_device_list=connected_android_device_list)
#                     suite.addTest(test_instance)
#         return suite, on_line_test_method_name_list
#


########################################################################################################


# app_action.py

#
# def get_android_driver(pro_name, current_thread_name_index, connected_android_device_list):
#     """
#     【 获取 Android 设备驱动 】
#     :param pro_name
#     :param current_thread_name_index: 当前线程名字的索引
#     :param connected_android_device_list: 已连接设备信息列表
#     [ { "thread_index": 1, "device_name": "小米5S", "platform_version": "7.0", "device_udid": "192.168.31.136:5555", "appium_server": "http://127.0.0.1:4723/wd/hub" } } ,
#       { "thread_index": 2, "device_name": "坚果Pro", "platform_version": "7.1.1", "device_udid": "15a6c95a", "appium_server": "http://127.0.0.1:4724/wd/hub" } } ]
#     :return:
#
#     【 步 骤 】
#     1.获取 Appium 服务启动应用所需的能力参数 (指定设备，指定应用)
#     2.通过'当前线程名索引' 获取已连接设备列表中对应的'Android'设备信息和'Appium'服务
#     3.获取设备驱动
#     """
#
#     # 获取 Appium 服务启动应用所需的能力参数 (指定设备，指定应用)
#     from Config.pro_config import get_app_info
#     app_info = get_app_info(pro_name)
#     desired_caps = dict()
#     desired_caps["platformName"] = "Android"
#     desired_caps["appPackage"] = app_info["appPackage"]
#     desired_caps["appActivity"] = app_info["appActivity"]
#     # 使用哪个自动化引擎
#     desired_caps["automationName"] = "UiAutomator2"
#     # Appium 等待接收从客户端发送的新命令的超时时长，超时后Appium会终止会话
#     desired_caps["newCommandTimeout"] = 30
#     # Android 等待设备就绪的超时时长，以秒为单位
#     desired_caps["deviceReadyTimeout"] = 30
#     # Android 在启动后等待设备就绪的超时时长，以秒为单位
#     desired_caps["androidDeviceReadyTimeout"] = 30
#
#     # appium 启动时进程保存的原因（有待验证）
#     # desired_caps["adbExecTimeout"] = 20000
#     # desired_caps["uiautomator2ServerLaunchTimeout"] = 30000
#
#     # 唤醒屏幕（效果不理想）
#     # desired_caps["unlockType"] = "pattern"
#     # desired_caps["unlockKey"] = "12589"
#
#     # 通过'当前线程名索引' 获取已连接设备列表中对应的'Android'设备信息和'Appium'服务
#     device_name = None
#     appium_server = None
#     for connected_android_devices_dict in connected_android_device_list:
#         if current_thread_name_index == connected_android_devices_dict["thread_index"]:
#             desired_caps["platformVersion"] = connected_android_devices_dict["platform_version"]
#             desired_caps["deviceName"] = connected_android_devices_dict["device_udid"]
#             device_name = connected_android_devices_dict["device_name"]
#             appium_server = connected_android_devices_dict["appium_server"]
#             break
#     log.info("\n\n")
#     log.info("device_name -> " + device_name)
#     log.info("appium_server -> " + appium_server)
#     log.info("\n\n")
#     # 获取设备驱动
#     try:
#         driver = webdriver.Remote(appium_server, desired_caps)
#     except Exception as e:
#         log.error(("显示异常：" + str(e)))
#         if "Failed to establish a new connection" in str(e):
#             error_msg = "Appium 服务(" + appium_server + ")未启动"
#         elif "Could not find a connected Android device" in str(e):
#             error_msg = "Android 设备(" + device_name + ")未连接"
#         elif "Failed to launch Appium Settings app" in str(e):
#             error_msg = "Appium Setting 应用启动超时"
#         else:
#             error_msg = "启动 Appium 服务的其他异常情况"
#         send_DD_for_FXC(title=pro_name, text="#### " + error_msg + "")
#         raise Exception(error_msg)
#     return driver, device_name

