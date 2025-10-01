import psutil

def read_cpu_percent() -> float:
    return psutil.cpu_percent(interval=0.1)

def read_memory() -> dict:
    vm = psutil.virtual_memory()
    return {"percent": vm.percent, "used": int(vm.used), "total": int(vm.total)}

def read_disk() -> dict:
    du = psutil.disk_usage("/")
    return {"percent": du.percent, "used": int(du.used), "total": int(du.total)}
