# system_info_reporter/monitor.py

import psutil

def get_system_info():
    cpu = psutil.cpu_percent(interval=1)

    memory = psutil.virtual_memory()
    total_memory = round(memory.total / (1024 ** 3), 2)
    used_memory = round(memory.used / (1024 ** 3), 2)

    disk = psutil.disk_usage('/')
    total_disk = round(disk.total / (1024 ** 3), 2)
    used_disk = round(disk.used / (1024 ** 3), 2)

    return {
        "cpu": cpu,
        "memory": (used_memory, total_memory, memory.percent),
        "disk": (used_disk, total_disk, disk.percent)
    }