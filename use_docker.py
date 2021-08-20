import argparse
import json
import docker

parser = argparse.ArgumentParser(description="input container's name")
parser.add_argument('-n', '--name', default='')
args = parser.parse_args()
container_name = args.name


def jinzhi_convert(value):
    units = ["B", "KB", "MB", "GB", "TB", "PB"]
    size = 1024.0
    for i in range(len(units)):
        if (value / size) < 1:
            return "%.2f%s" % (value, units[i])
        value = value / size


class Memory:
    def __init__(self, stat_dict):
        self.stat_dict = stat_dict
        self.current_used_memory = self.get_used_memory()
        self.memory_total = self.get_total_memory()
        self.current_used_memory_percent = self.get_used_memory_perc()

    def get_used_memory(self):
        """get the container's current used memory"""
        return jinzhi_convert(self.stat_dict['memory_stats']['usage'])

    def get_total_memory(self):
        """get the container's limit memory"""
        return jinzhi_convert(self.stat_dict['memory_stats']['limit'])

    def get_used_memory_perc(self):
        """get the percentage of the used memory container"""
        used_memory_percent = self.stat_dict['memory_stats']['usage'] / self.stat_dict['memory_stats']['limit'] * 100
        return str(round(used_memory_percent, 2)) + "%"


class Cpu:
    def __init__(self, stat_dict):
        self.stat_dict = stat_dict
        self.current_used_cpu = self.get_used_cpu()

    def get_used_cpu(self):
        used_cpu = self.stat_dict['cpu_stats']['cpu_usage']['total_usage'] / 1000000000
        return str(round(used_cpu, 2)) + "s"


def main():
    # 构造一个client对象，指定连接远程docker服务器。ip地址加端口号
    client = docker.DockerClient(base_url='tcp://172.16.214.3:2375')
    con_obj = client.containers.get(container_name)  # 返回容器类对象
    stat_dict = con_obj.stats(stream=False)

    container_mem = Memory(stat_dict)
    container_cpu = Cpu(stat_dict)
    # 将容器资源消耗信息生成json格式
    info = {'container_name': container_name,
            'con_obj_id': con_obj.id,
            'current_used_memory': container_mem.current_used_memory,
            'memory_total': container_mem.memory_total,
            'current_used_memory_percent': container_mem.current_used_memory_percent,
            'current_used_cpu': container_cpu.current_used_cpu}
    info_json = json.dumps(info)
    print(info_json)


if __name__ == "__main__":
    main()
'''
con_1 = client.containers.run("centos:7", command='/bin/bash',name="my_centos",
                              tty=True,
                              remove=True,
                              detach=True)
print(con_1.short_id)  # 获取容器的id 只显示前10位
print(con_1.logs())  # 获取容器的日志信息
print(con_1.image)
print(con_1.name)
print(con_1.status)
print(json.dumps(con_1.stats(stream=False)))
json_str = json.dumps(con_1.stats(stream=False))
with open("./info.json", "w") as f:
    json.dump(json_str, f)
    print("加载入文件完成")
print(type(con_1.stats(stream=False)))
con_1.stop()
'''
