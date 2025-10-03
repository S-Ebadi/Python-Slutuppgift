import psutil

def read_cpu():
    """Returnerar CPU-användning i procent."""
    return psutil.cpu_percent()

def read_memory():
    """Returnerar minnesanvändning som (procent, använt, totalt)."""
    mem = psutil.virtual_memory()
    return mem.percent, mem.used, mem.total

def read_disk():
    """Returnerar diskanvändning som (procent, använt, totalt)."""
    disk = psutil.disk_usage('/')
    return disk.percent, disk.used, disk.total
