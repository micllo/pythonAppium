
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


【 配 置 Android 环 境 】

1.配置相关工具：
（1）android-sdk：提供adb命令、uiautomatorviewer 元素定位
（2）appium：提供appium服务、appium 元素定位

2.无线连接真机(使用一次USB)：
（1）通过USB将真机连接电脑
（2）让真机在5555端口监听TCP/IP连接：adb tcpip 5555
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



########################################################################################################################


【 Docker Centos7 相关 】


【 配 置 Android 环 境 】

备注：
    生产环境为了减少意外情况，尽量使用无线连接真机
    使用无线连接真机，则需要确保 Docker环境 与 真机 处于同一个网络下
    由于上述因素，考虑使用 win10 服务器作为生产监控环境：Appium服务(Docker)、监控服务(Docker)、真机

1.配置相关环境
（1）Win10 服务器 安装 Docker
（2）启动 appium docker服务：使用 budtmo/docker-android-real-device 镜像
（3）启动 监控 docker服务
（4）无线连接真机

2.Appium docker 无线连接真机(无需USB)：
（1）绑定真机（不进入容器）：docker exec -it appium_andriod adb connect 192.168.31.136:5555
（2）查看设备（不进入容器）：docker exec -it appium_andriod adb devices

3.安装待测试的apk包（不进入容器）：
  docker exec -it appium_andriod adb -s 192.168.31.136:5555 install yyb.apk

4.Appium docker 无线连接真机(使用一次USB)：
（1）使用这种方式时，docker容器的启动方式需要挂载USB接口目录（暂时未研究）

5.使用'Appium docker'中提供的'vnc'界面地址来查看'appium log'
http://docker_ip:6080


注意事项：******** 代码调试真机时，必须要在真机上进行授权（仅第一次需要）********








