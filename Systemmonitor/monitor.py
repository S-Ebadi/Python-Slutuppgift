# Monitor - computer stats
import psutil

def get_cpu():
    return int(psutil.cpu_percent(interval=1))

def get_ram():
    return int(psutil.virtual_memory().percent)

def get_disk():
    return int(psutil.disk_usage('/').percent)

# Extra functions for more info
def read_cpu():
    return get_cpu()

def read_memory():
    mem = psutil.virtual_memory()
    percent = int(mem.percent)
    used_gb = int(mem.used / 1000000000)
    total_gb = int(mem.total / 1000000000)
    return percent, used_gb, total_gb

def read_disk():
    disk = psutil.disk_usage('/')
    percent = int(disk.percent)
    used_gb = int(disk.used / 1000000000)
    total_gb = int(disk.total / 1000000000)
    return percent, used_gb, total_gb
