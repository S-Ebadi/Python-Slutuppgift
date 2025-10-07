# Utility Functions
import json
import os
import time

def save_session_data(data):
    # Make Storage folder if needed
    if not os.path.exists("Storage"):
        os.makedirs("Storage")
    
    # Get timestamp for filename
    timestamp = str(int(time.time()))
    filename = "Storage/session-" + timestamp + ".json"
    
    # Save data to file
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
    
    print("Session saved to:", filename)

def get_last_session_file():
    # Check if Storage folder exists
    if not os.path.exists("Storage"):
        return None
    
    # Get all files in Storage folder
    files = os.listdir("Storage")
    session_files = []
    
    # Find session files
    for file in files:
        if file.startswith("session-") and file.endswith(".json"):
            session_files.append(file)
    
    # Return None if no session files found
    if not session_files:
        return None
    
    # Sort files and return the newest one
    session_files.sort()
    newest_file = session_files[-1]
    return "Storage/" + newest_file

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pretty_print_status(cpu, ram, disk, reading_number=None):
    # Print reading number if provided
    if reading_number:
        print("Reading " + str(reading_number) + "/10:")
    
    # Print system status in consistent format
    status_line = "CPU: " + str(cpu) + "% | RAM: " + str(ram) + "% | DISK: " + str(disk) + "%"
    print(status_line)