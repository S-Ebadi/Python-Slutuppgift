# Log Writer
import datetime, os

def write_log(message):
    import os, time
    
    # Make Storage folder if needed
    if not os.path.exists("Storage"): 
        os.makedirs("Storage")
    
    # Get current time as simple text
    current_time = str(int(time.time()))
    
    # Write message to log file
    with open("Storage/log.txt", "a") as f:
        f.write(f"[{current_time}] {message}\n")


