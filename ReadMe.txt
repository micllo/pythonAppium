
########################################################################################################################


【 本地 Mac 相关 】

1.uWSGI配置文件：./vassals/mac_app_uwsgi.ini
（1）启动 uWSGI 命令 在 ./start_uwsgi_local.sh 脚本
（2）停止 uWSGI 命令 在 ./stop_uwsgi.sh 脚本

2.上传 GitHub 需要被忽略的文件
（1）Logs、Reports -> 临时生产的 日志、报告
（2）vassals_local、venv -> 本地的 uWSGI配置、python3虚拟环境
（3）node_modules、gulpfile.js、package.json、package-lock.json -> 供本地启动使用的gulp工具

3.访问地址（ server.py 启动 ）：
（1）接口地址 -> http://127.0.0.1:6062/
               http://127.0.0.1:6062/API/index
               http://127.0.0.1:6062/API/get_project_case_list/<pro_name>

4.访问地址（ uwsgi 启动 ）：
（1）用例模板 -> http://localhost:7060/api_case_tmpl
（2）测试报告 -> http://localhost:7060/test_report_local/<pro_name>/[API_report]<pro_name>.xls
（3）页面首页 -> http://localhost:7060/api_local/API/index
（4）接口地址 -> http://localhost:7060/api_local/API/xxxxxxx
   （ 备注：uwgsi 启动 6061 端口、nginx 配置 6050 反向代理 6061 ）

5.本地相关服务的启动操作（ gulpfile.js 文件 ）
（1）启动服务并调试页面：gulp "html debug"
（2）停止服务命令：gulp "stop env"
（3）部署docker服务：gulp "deploy docker"


【 备 注 】
MAC本地安装的 nginx 相关路径
默认安装路径：/usr/local/Cellar/nginx/1.15.5/
默认配置文件路径：/usr/local/etc/nginx/
sudo nginx
sudo nginx -t
sudo nginx -s reload


【 虚拟环境添加依赖 】
1.创建虚拟环境：virtualenv -p /usr/local/bin/python3 venv （-p：指明python3所在目录）
2.切换到虚拟环境：source venv/bin/activate
3.退出虚拟环境：deactivate
4.添加依赖：
pip3 install -v flask==0.12 -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com


#########################################################


【 配 置 Android 环 境 】

1.配置相关工具：
（1）android-sdk：提供adb命令、uiautomatorviewer 元素定位
（2）appium：提供appium服务、appium 元素定位

2.无线连接真机(使用一次USB)：
（1）通过USB将真机连接电脑
（2）让真机在5555端口监听TCP/IP连接：adb -s 设备ID tcpip 5555
（3）找到真机的ip地址：设置 -> 关于本机 -> 本机状态信息 -> IP地址
（4）通过ip地址连接真机：adb connect 192.168.31.56:5555
    （ 断开连接设备：adb disconnect 192.168.31.56:5555 ）

3.无线连接真机(无需USB)：
  前提：先将真机刷机获取root权限（ 通过win上使用'奇兔刷机'软件）
       在真机上安装超级终端模拟器（ Terminal_Emulator.apk ）：adb install Terminal_Emulator.apk
（1）使用真机在终端模拟器上输入下面两行
     su
     setprop service.adb.tcp.port 5555
     备注：有些设备（小米 5S）可能需要重启adbd服务：restart adbd（ 若无效 则：先 stop adbd  再 start adbd ）
（2）找到 设备的ip地址：设置 -> 关于本机 -> 本机状态信息 -> IP地址
（3）通过ip地址连接设备：adb connect 192.168.31.136:5555

4.安装待测试的apk包：
  adb -s 192.168.31.136:5555 install yyb.apk


注意事项：******** 代码调试真机时，必须要在真机上进行授权（仅第一次需要）********



#########################################################


【 配 置 IOS 环 境 】

1.使用 Openatx/Facebook-wda 自动化框架
  需要开启：
 （1）模拟器：WDA服务（端口自动映射）
 （2）真机：WDA服务、映射端口


2.使用 appium iOS 自动化框架
  需要开启：WDA服务、appium服务


------------------------------------------


【 终端启动 WebDriverAgent 服务命令 】
命令：xcodebuild -project ../WebDriverAgent.xcodeproj -scheme WebDriverAgentRunner -destination "id=$UDID" test
    （ $$UDID -> 表示 模拟器 或 真机 的UDID ）

举 例：
< iPhone 8 模拟器>
xcodebuild -project /Users/micllo/Documents/works/GitHub/WebDriverAgent/WebDriverAgent.xcodeproj -scheme WebDriverAgentRunner -destination "id=647616B3-44E3-4198-8578-E22FFD8EE43D" test
< iPhone 11 模拟器>
xcodebuild -project /Users/micllo/Documents/works/GitHub/WebDriverAgent/WebDriverAgent.xcodeproj -scheme WebDriverAgentRunner -destination "id=5F302EEC-C5AA-489D-924D-45FB91C9C894" test
# 打开模拟器应用（ 若模拟器未打开的情况 ）
open "/Applications/Xcode.app/Contents/Developer/Applications/Simulator.app/"

< iPhone 7 真机>
xcodebuild -project /Users/micllo/Documents/works/GitHub/WebDriverAgent/WebDriverAgent.xcodeproj -scheme WebDriverAgentRunner -destination "id=3cbb25d055753f2305ec70ba6dede3dca5d500bb" test


【 端口映射命令（设备与电脑） 】
终端执行：iproxy 8100 8100
验证地址：http://localhost:8100/status
< 备 注 >
（1）若使用模拟器：则不需要执行该命令（启动WDA时会自动映射）
（2）若使用真机：则需要手动执行映射命令


【 终端启动 appium desktop 服务命令 】
1.使用 appium desktop ---> node /Applications/Appium.app/Contents/Resources/app/node_modules/appium/build/lib/main.js --port 4723
2.使用 appium server  ---> appium appium -a 127.0.0.1 -p 4723 --session-override &
< 备 注 >
（1）若使用真机：则不能启动端口映射


------------------------------------------


【 ios 模拟器管理工具 simctl 】

# 查看模拟器可用列表
xcrun simctl list
xcrun simctl list devices

# 创建一个模拟器：（ 通过 list 命令 配置 SimDeviceType、SimRuntime ）
xcrun simctl create "my_iPhone_11" "com.apple.CoreSimulator.SimDeviceType.iPhone-11" "com.apple.CoreSimulator.SimRuntime.iOS-13-4"

# 为模拟器 重命名
xcrun simctl rename "A51C1FE6-104E-495B-A839-FDECEB201C9B" "new_iPhone"

# 启动模拟器（通过 list 命令 查看 相应模拟器后面 显示 booted 表示 启动成功）
xcrun simctl boot "A51C1FE6-104E-495B-A839-FDECEB201C9B"
（ 关闭 shutdown、删除 delete ）

# 打开模拟器应用
open "/Applications/Xcode.app/Contents/Developer/Applications/Simulator.app/"

# 安装应用程序（通过.app 文件）
xcrun simctl install booted /Users/micllo/Downloads/appium/ios/TestApp.app
xcrun simctl install "647616B3-44E3-4198-8578-E22FFD8EE43D" /Users/micllo/Downloads/appium/ios/Taobao4iPhone.app

# 启动应用（通过 bundle identifier）
xcrun simctl launch booted "com.taobao.taobao4iphone"
xcrun simctl launch "A51C1FE6-104E-495B-A839-FDECEB201C9B" "com.taobao.taobao4iphone"
（ 关闭 terminate、卸载  uninstall ）

# 打开网页
xcrun simctl openurl booted "https://www.sogou.com"
xcrun simctl openurl "A51C1FE6-104E-495B-A839-FDECEB201C9B" "https://www.sogou.com”



########################################################################################################################


【 Docker Centos7 相关 】


【 配 置 Android 环 境 】

备注：
    生产环境为了减少意外情况，尽量使用无线连接真机
    使用无线连接真机，则需要确保 Docker环境 与 真机 处于同一个网络下

未解决的问题：
    'appium docker'中无法获取通过'USB'连接的真机设备

环境配置 方案一：
    若 有些监控的真机无法获取root权限(刷机失败)
    则 在 linux 上启动一个容器：监控服务(Docker)、
       在 win10 | mac_mini 上安装两个服务：appium、android sdk

    Appium服务 无线连接设备
    （1）绑定真机 ：adb connect 192.168.31.136:5555
    （2）查看设备 ：adb devices
    （3）安装待测试apk ：adb -s 192.168.31.136:5555 install yyb.apk

环境配置 方案二：
    若 待监控的真机全部都可以获取root权限(刷机成功)
    则 在 linux | win10 | mac_mini 上启用两个容器：监控服务(Docker)、Appium服务(Docker) - budtmo/docker-android-real-device
      ( 备注：若 使用 linux 则要确保 linux 与 手机 处于同一网络 )

    Appium服务(Docker) 无线连接设备
    （1）绑定真机（不进入容器）：docker exec -it appium_andriod adb connect 192.168.31.136:5555
    （2）查看设备（不进入容器）：docker exec -it appium_andriod adb devices
    （3）安装待测试apk（不进入容器）：docker exec -it appium_andriod adb -s 192.168.31.136:5555 install yyb.apk

    Appium服务(Docker)中提供的'noVNC'界面地址来查看'appium log'
    http://docker_ip:6080


注意事项：******** 代码调试真机时，必须要在真机上进行授权（仅第一次需要）********
