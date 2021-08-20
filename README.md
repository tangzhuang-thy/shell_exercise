# use_docker.py
# 脚本功能：提取docker运行容器的内存、cpu资源消耗信息
# 脚本使用： python3 use_docker.py --name=serene_gould 
serene_gould 为docker容器的名字
# 运行结果
{"container_name": "serene_gould", "con_obj_id": "cdfa48ba87200fc290cf808e8c786748a9cfdd8a2332deca4e220045ea65f2d7", "current_used_memory": "1.07MB", "memory_total": "782.38MB", "current_used_memory_percent": "0.14%", "current_used_cpu": "0.09s"}

# 环境
宿主主机 系统mac
python版本 3.9.6
虚拟机系统 centos 8 安装docker

docker开放远程访问，在作为docker远程服务的centos8机器中配置远程访问：
# vim /usr/lib/systemd/system/docker.service  
[Service]  
ExecStart=/usr/bin/dockerd -H tcp://0.0.0.0:2375 -H unix://var/run/docker.sock  

