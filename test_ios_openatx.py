import wda
import time

wda.DEBUG = False  # 显示每个与WDA服务的HTTP请求的信息
wda.HTTP_TIMEOUT = 60.0  # 设置与WDA服务的HTTP请求超时时间

c = wda.Client('http://localhost:8100')
print(c.status())
print()

# 等待 WDA 服务启动
c.wait_ready(timeout=300)  # 等待300s，默认120s


"""
    测 试 步 骤
    1.从屏幕底部往上划
    2.点击 Browse 图标
    3.输入框搜索 Heart
    4.等待"Categories"内容消失
    5.判断是否存在"Heart Rate"内容
    6.点击"Heart Rate"进入
    7.点击"Add Data"
    8.在'BPM'中输入 33 
    9.点击'Add' 并选择 confirm
"""
with c.session('com.apple.Health') as s:

    # 设置默认的元素定位超时时间5秒
    s.implicitly_wait(5.0)

    # 当前的 bundleId 和 sessinId (会话id)
    print(s.bundle_id, s.id)

    # 1.从屏幕底部往上划
    s.swipe_up()
    time.sleep(2)

    # 2.点击 Browse 图标
    # s.tap(315, 846)
    s(xpath='//XCUIElementTypeButton[@name="Browse"]').click_exists(timeout=3.0)
    time.sleep(2)

    # 3.输入框搜索 Heart
    search_input = s(xpath='//XCUIElementTypeSearchField[@name="Search"]')
    # search_input = s(label="Search")
    search_input.click_exists(timeout=3.0)
    time.sleep(1)
    search_input.set_text("Heart")
    time.sleep(2)

    # 4.等待"Nutrition"内容消失
    s(text='Nutrition').wait_gone(timeout=3.0)
    print("内容 Nutrition 是否存在: " + str(s(text="Nutrition").exists))
    time.sleep(2)

    # 5.判断是否存在"Heart Rate"内容
    print("内容 Heart Rate 是否存在：" + str(s(text="Heart Rate").exists))
    time.sleep(2)

    # 6.点击"Heart Rate"进入
    s(xpath='(//XCUIElementTypeOther[@name="feeditem_identifier"])[1]/XCUIElementTypeButton').click()
    time.sleep(2)

    # 7.点击"Add Data"
    # s.tap(360, 70)
    s(xpath='//XCUIElementTypeButton[@name="Add Data"]').click()
    # s(name="Add Data").click()
    time.sleep(2)

    # 8.在'BPM'中输入 66
    bpm_input = s(xpath='//XCUIElementTypeTextField[@name="BPM"]')
    # bpm_input = s(label="BPM")
    bpm_input.click()
    bpm_input.set_text("66")
    time.sleep(2)

    # 9.点击'Add'
    s(xpath='//XCUIElementTypeButton[@name="Add"]').click()
    # s(label="Add").click()
    time.sleep(5)












################################################################################

# # Press home button
# c.home()
#
# # Hit healthcheck
# c.healthcheck()
#

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

# with c.session('com.apple.Health') as s:

    # # 设置默认的元素定位超时时间30秒
    # s.implicitly_wait(30.0)
    #
    # # 当前的 bundleId 和 sessinId (会话id)
    # print(s.bundle_id, s.id)

    # # 锁屏
    # s.lock()
    # print(s.locked())
    # time.sleep(1)
    #
    # # 解锁
    # s.unlock()
    # print(s.locked())
    # time.sleep(1)
    #
    # print(s.battery_info())  # return like {"level": 1, "state": 2}
    # print(s.device_info())  # return like {"currentLocale": "zh_CN", "timeZone": "Asia/Shanghai"}
    #
    # # 显示当前app的信息  {'processArguments': {'env': {}, 'args': []}, 'name': '', 'pid': 1493, 'bundleId': 'com.apple.Health'}
    # print(s.app_current())  # current app info
    #
    # # 设置剪贴板
    # s.set_clipboard("Hello world")
    #
    # # 截屏
    # print(s.screenshot('test_wda.png'))
    # print(s.screenshot().save("test_wda2.jpg"))
    #
    # # 截屏后逆时针旋转90度
    # from PIL import Image
    # s.screenshot().transpose(Image.ROTATE_90).save("test_wda3.png")

    # # 停用app 2秒
    # s.deactivate(2.0)

    # # 获取 width height
    # print(s.window_size())
    # res = s.window_size()
    # print("width: " + str(res.width))
    # print("height: " + str(res.height))
    #
    # print("模拟触摸")
    # time.sleep(2)
    # s.tap(200, 200)  # 从左上角开始计算（猜测）
    #
    # print("click 类似 tap 但支持小数")
    # time.sleep(2)
    # s.click(200, 200)
    #
    # print("双击")
    # time.sleep(2)
    # s.double_tap(370, 85)
    # time.sleep(2)

    # 滑动：从 (x1,y1) 划向 (x2,y2)
    # s.swipe(x1, y1, x2, y2, 0.5)  # 0.5秒
    # s.swipe(0.5, 0.5, 0.5, 1.0)
    # time.sleep(2)
    #
    # # 从屏幕右边往左划
    # s.swipe_left()
    # # 从屏幕左边往右划
    # s.swipe_right()
    # # 从屏幕底部往上划
    # s.swipe_up()
    # # 从屏幕顶部往下划
    # s.swipe_down()
    #
    # # 长按 1秒
    # # s.tap_hold(x, y, 1.0)
    #
    # # 隐藏键盘（在模拟器中可能无效）
    # s.keyboard_dismiss()

    ###################################################################################

    # 【 定 位 元 素 】

    # print(s(id="URL").exists)  # return True or False
    #
    # # using id or other query conditions
    # print(s(id='URL'))
    #
    # # using className
    # s(className="Button")
    #
    # # using name
    # s(name='URL')
    # s(nameContains='UR')
    # s(nameMatches=".RL")
    #
    # # using label
    # s(label="label")
    # s(labelContains="URL")
    #
    # # using value
    # s(value="Enter")
    # s(valueContains="RL")
    #
    # # using  visible, enabled
    # s(visible=True, enabled=True)
    #
    # # 若有多个元素，可以使用索引定位，0 表示第一个
    # s(name='URL', index=0)
    #
    # # 组合查询
    # s(className='Button', name='URL', visible=True, labelContains="Addr")
    #
    # s(xpath='//Button[@name="URL"]')
    # s.xpath('//Button[@name="URL"]')
    #
    # s(predicate='name LIKE "UR*"')
    # s('name LIKE "U*L"')  # predicate is the first argument, without predicate= is ok
    # s(classChain='**/Button[`name == "URL"`]')
    #
    # # 获取元素属性值
    # s(text='京东超市').text
    # s(text='京东超市').class_name
    # s(text='京东超市').value
    # s(text='京东超市').bounds
    #
    # # 查找元素 等待10秒
    # e = s(text='Dashboard').get(timeout=10.0)
    # e.tap()
    # # 先判断是否存在，再点击
    # s(text='京东超市').click_exists()  # 如果没有找到标签则立即返回
    # s(text='京东超市').click_exists(timeout=5.0)  # 等待5s
    #
    # # 判断标签是否存在
    # s(text='京东超市').exists
    # s(text='京东超市')[1].exists
    #
    # # 找到所有匹配的标签， 返回数组
    # e_array = s(text='京东超市').find_elements()
    # len(e_array)

    # e = s(xpath='(//XCUIElementTypeButton[@name="Show All Health Data"])[2]').get(timeout=10.0)
    # # properties (bool)
    # # print(e.accessible)
    # print(e.displayed)
    # print(e.enabled)
    #
    # # properties (str)
    # print(e.text)  # ex: Dashboard
    # print(e.className)  # ex: XCUIElementTypeStaticText
    # print(e.value)  # ex: github.com
    #
    # # Bounds return namedtuple
    # rect = e.bounds  # ex: Rect(x=144, y=28, width=88.0, height=27.0)
    # print(rect.x)  # expect 144
    #
    # time.sleep(2)
    # s.tap(36, 289)
    # time.sleep(2)
    # s.tap(64, 68)
    # time.sleep(2)

    # # Check if elements exists
    # print(s(text="No Data").exists)
    #
    # # Find all matches elements, return Array of Element object
    # s(text='No Data').find_elements()
    #
    # # Use index to find second element
    # s(text='No Data')[1].exists
    #
    # # Use child to search sub elements
    # s(text='No Data').child(className='Cell').exists

    # # do element operations
    # e.tap()
    # e.click()  # alias of tap
    # e.clear_text()
    # e.set_text("Hello world")
    # e.tap_hold(2.0)  # tapAndHold for 2.0s
    #
    # e.scroll()  # scroll to make element visiable
    #
    # # directions can be "up", "down", "left", "right"
    # # swipe distance default to its height or width according to the direction
    # e.scroll('up')
    #
    # # Set text
    # e.set_text("Hello WDA")  # normal usage
    # e.set_text("Hello WDA\n")  # send text with enter
    # e.set_text("\b\b\b")  # delete 3 chars
    #
    # # Wait element gone
    # s(text='Dashboard').wait_gone(timeout=10.0)
    #
    # # Swipe
    # s(className="Image").swipe("left")
    #
    # # Pinch
    # s(className="Map").pinch(2, 1)  # scale=2, speed=1
    # s(className="Map").pinch(0.1, -1)  # scale=0.1, speed=-1 (I donot very understand too)
    #











