import psutil

def cpu():  return psutil.cpu_percent(0.1)

def mem():
    m = psutil.virtual_memory()
    return m.percent, m.used, m.total

def disk():
    d = psutil.disk_usage("/")
    return d.percent, d.used, d.total
