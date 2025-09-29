import psutil




def read_cpu_percent() -> float:
    # 0.5s genomsnitt ger stabilare värde
    return psutil.cpu_percent(interval=0.5)




def read_memory() -> dict:
    vm = psutil.virtual_memory()
    return {"percent": vm.percent, "used": vm.used, "total": vm.total}




def read_disk() -> dict:
    du = psutil.disk_usage("/")
    return {"percent": du.percent, "used": du.used, "total": du.total}