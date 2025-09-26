import psutil
from typing import Dict

def read_status() -> Dict[str, float]:
    cpu = psutil.cpu_percent(interval=0.2)
    vm = psutil.virtual_memory()
    du = psutil.disk_usage("/")
    return {
        "cpu_percent": float(cpu),
        "mem_percent": float(vm.percent),
        "mem_used_gb": round(vm.used / (1024**3), 2),
        "mem_total_gb": round(vm.total / (1024**3), 2),
        "disk_percent": float(du.percent),
        "disk_used_gb": round(du.used / (1024**3), 2),
        "disk_total_gb": round(du.total / (1024**3), 2),
    }

def human_status(status: Dict[str, float]) -> str:
    return (
        f"CPU Användning: {status['cpu_percent']:.0f}%\n"
        f"Minnesanvändning: {status['mem_percent']:.0f}% "
        f"({status['mem_used_gb']:.1f} GB out of {status['mem_total_gb']:.1f} GB used)\n"
        f"Diskanvändning: {status['disk_percent']:.0f}% "
        f"({status['disk_used_gb']:.0f} GB out of {status['disk_total_gb']:.0f} GB used)"
    )
