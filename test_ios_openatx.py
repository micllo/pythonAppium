import wda
import time

wda.DEBUG = False  # 显示每个HTTP请求的信息
wda.HTTP_TIMEOUT = 60.0  # default 60.0 seconds

c = wda.Client('http://localhost:8100')
print(c.status())
print()

# Wait WDA ready
c.wait_ready(timeout=300)  # 等待300s，默认120s

# # Press home button
# c.home()
#
# # Hit healthcheck
# c.healthcheck()
#
# # 截屏
# c.screenshot('test_wda.png')
# c.screenshot().save("test_wda2.jpg")
#
# # Get page source
# print(c.source())  # format XML
# print()
# c.source(accessible=True)  # default false, format JSON
#
# print(c.locked())  # true of false
# print()
# c.lock()  # lock screen
# c.unlock()  # unlock

###################################################################################

# 打开应用 方式一：
# with c.session('com.apple.Health') as s:
#     print(s.orientation)
#     time.sleep(2)

# 打开应用 方式二：
# s = c.session('com.apple.Health', alert_action="accept")
# print(s.orientation)
# time.sleep(2)
# s.close()


# 打开sfari浏览器 指定的页面
# s = c.session('com.apple.mobilesafari', ['-u', 'https://www.baidu.com/'])
# print(s.orientation)
# time.sleep(2)
# s.close()

###################################################################################

# 【 在不终止应用的情况下启动 】

# s = c.session("com.apple.Health", alert_action="accept")
#
# # 启动应用
# c.session().app_activate("com.apple.Health")
#
# # 查看应用状态： value ( 1 -> die、2 -> background、4 -> running )
# print(c.session().app_state("com.apple.Health"))
#
# # 显示当前app的信息 {"pid": 1281, "bundleId": "com.netease.cloudmusic"}
# print(c.app_current())
# time.sleep(2)
#
# # 终止应用 (指定应用的bundleId)
# c.session().app_terminate("com.apple.Health")
# print(c.session().app_state("com.apple.Health"))
# time.sleep(2)

###################################################################################

with c.session('com.apple.Health') as s:
    print(s.orientation)
    # 设置默认的元素定位超时时间30秒
    s.implicitly_wait(30.0)

    # 当前的 bundleId 和 sessinId (会话id)
    print(s.bundle_id, s.id)

    # 锁屏
    s.lock()
    print(s.locked())
    time.sleep(2)

    # 解锁
    s.unlock()
    print(s.locked())
    time.sleep(2)



