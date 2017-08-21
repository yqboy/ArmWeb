# 基于 psutil 做的 web 监控页面
Linux 环境需要 安装 psutil flask
可以 pip install psutil flask 或 apt install python-psutil python-flask

注意:

    如果网卡名 不为 'eth0' 你还需要 更改 sysinfo.py 中 第5行  eth = '你要检测流量的网卡名'
    如果CPU温度 一直为 0℃ 你还需要 更改 sysinfo.py 中 第95行 temp_file = '你系统 CPU温度 文件位置'

![](https://github.com/yqboy/ArmWeb/blob/master/WebSystemInfo/1.png)
![](https://github.com/yqboy/ArmWeb/blob/master/WebSystemInfo/2.png)
