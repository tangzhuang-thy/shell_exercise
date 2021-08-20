# use_docker.py
# 脚本功能：提取docker运行容器的内存、cpu资源消耗信息
# 脚本使用： python3 use_docker.py --name=serene_gould 
serene_gould 为docker容器的名字
# 环境
宿主主机 系统mac
python版本 3.9.6
虚拟机系统 centos 8 安装docker

docker开放远程访问，在作为docker远程服务的centos8机器中配置远程访问：
# vim /usr/lib/systemd/system/docker.service  
[Service]  
ExecStart=/usr/bin/dockerd -H tcp://0.0.0.0:2375 -H unix://var/run/docker.sock  

