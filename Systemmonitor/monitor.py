import psutil

def read_cpu():
    """Returnera CPU-användning i procent"""
    return psutil.cpu_percent(interval=1)

def read_memory():
    """Returnera minnesobjektet (psutil.virtual_memory)"""
    return psutil.virtual_memory()

def read_disk():
    """Returnera diskobjektet (psutil.disk_usage)"""
    return psutil.disk_usage('/')
