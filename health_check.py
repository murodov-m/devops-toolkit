import datetime
import psutil

def check_system():
	print(f"[{datetime.datetime.now()}] System Health Report")
	print(f"CPU Usage:		{psutil.cpu_percent(interval=1)}%")
	print(f"RAM Usage: 		{psutil.virtual_memory().percent}%")
	print(f"Disk Usage: 	{psutil.disk_usage('/').percent}%")

if __name__ == "__main__":
	check_system()