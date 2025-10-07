
# System Monitor - Python Exam project

A professional system monitoring application that provides control over computer performance.  
Monitors CPU, RAM, and disk usage in real-time with alarm functionality and event logging.  
Built in Python using **psutil**.

*Developed as a final project in Python System Development course (DevOps program, Chas Academy).*

---

## Project Overview

System Monitor is a terminal-based monitoring tool that provides:

| Feature | Description |
|---------|-------------|
| **Monitoring** | Automated system monitoring with fixed duration (10 readings) |
| **Status Reports** | Display current CPU, RAM, and disk usage |
| **Alarm Management** | Create, view, edit, and delete alarms (CPU, RAM, Disk) |
| **Persistence** | Alarms saved in `Storage/alarms.json` between sessions |
| **Logging** | Events logged to `Storage/log.txt` with timestamps |
| **Session History** | Each monitoring session saved to `Storage/session-*.json` |
| **Simple Mode** | Quick 5-reading monitoring for basic system status |

---

## Architecture

The program is divided into modules for clarity and maintainability.

```
Systemmonitor/
├── main.py          # Main menu, monitoring logic and user flow
├── monitor.py       # Functions to measure CPU, RAM and Disk via psutil
├── alarms.py        # Alarm management: create, list, update, delete, evaluate alarms
├── utils.py         # Utility functions: session data and file operations
├── logger.py        # Write events to log file with timestamp
├── requirements.txt # contains psutil
└── Storage/         # Data files (auto-created)
    ├── alarms.json     # All active alarms
    ├── session-*.json  # Session data files
    └── log.txt         # Event log
```

### Design Philosophy
- **Separation of Concerns**: each module has clear responsibility
- **Hybrid Programming**: combines functional programming (main logic) with OOP (Alarm class)
- **Persistence**: JSON files ensure alarms and sessions are preserved between runs
- **Logging**: events are tracked with timestamps for transparency
- **Simplicity**: functions are kept small and understandable

---

## Functional Specification

### Main Menu (main.py)
The program offers these options:

1. **Start monitoring** – automated monitoring runs 10 times then stops automatically
2. **Show status** – displays current monitoring status and last recorded values
3. **Create alarm** – configure CPU/RAM/Disk alarms (1-100% thresholds)
4. **Show alarms** – list all active alarms from `Storage/alarms.json`
5. **Edit alarms** – update or delete existing alarms
6. **Show last session** – summary of most recent session from `Storage/session-*.json`
7. **Simple mode** – quick 5-reading monitoring mode
8. **Exit** – closes the program

### Monitor (monitor.py)
Responsible for fetching data with **psutil**:
```python
def get_cpu():    # Returns CPU usage in %
def get_ram():    # Returns RAM usage in %
def get_disk():   # Returns disk usage in %
```

### Alarms (alarms.py)
Hybrid approach using both OOP and functional programming:

**Alarm Class:**
```python
class Alarm:
    def __init__(self, alarm_type, threshold)
    def is_triggered(self, value)
    def __str__(self)
```

**Alarm Management Functions:**
- `create_new_alarm()` – create new alarm with user input (uses Alarm class)
- `show_all_alarms()` – list all configured alarms
- `edit_delete_alarms()` – modify or remove existing alarms
- `check_alarms(cpu, ram, disk)` – evaluate alarms using Alarm.is_triggered() method

### Utilities (utils.py)
- `save_session_data(data)` – save monitoring session to JSON file
- `get_last_session_file()` – retrieve path to most recent session file
- `clear_screen()` – clear terminal screen

### Logging (logger.py)
- Creates log entries in `Storage/log.txt`
- Uses simple timestamp format
- Logs: program events, alarm triggers, session data

---

## Data Flow & Persistence

### Session Data
Each monitoring session is saved to `Storage/session-*.json` with measurement points and triggered alarms.

Example:
```json
{
  "cpu": 45,
  "ram": 67,
  "disk": 23,
  "time": "1696281234"
}
```

### Event Log
Written to `Storage/log.txt`:
```
[1696281234] Monitoring started
[1696281235] CPU usage is 95% (threshold: 80%)
[1696281256] Monitoring stopped
```

---

## Usage Instructions

### Installation
1. Ensure Python 3.6+ is installed
2. Install dependencies:
   ```bash
   pip install -r Systemmonitor/requirements.txt
   ```

### Running the Application
```bash
python3 Systemmonitor/main.py
```

### Menu Options

**1. Start monitoring**
- Runs system monitoring for 10 readings
- Each reading shows CPU, RAM, and disk usage percentages
- Checks for alarm conditions and displays alerts
- Automatically saves session data to JSON file
- Waits 2 seconds between readings

**2. Show status** 
- Displays whether monitoring is currently active
- Shows last recorded system values if available

**3. Create alarm**
- Choose alarm type: CPU (1), RAM (2), or DISK (3)
- Set threshold percentage (1-100%)
- Alarm is saved to `Storage/alarms.json`

**4. Show alarms**
- Lists all configured alarms with their thresholds
- Shows format: "1. CPU >= 80%"

**5. Edit alarms**
- Select alarm by number
- Choose to change threshold or delete alarm
- Changes are saved immediately

**6. Show last session**
- Displays total measurements from most recent session
- Shows last 5 readings with timestamps and values

**7. Simple mode**
- Quick monitoring mode with 5 readings
- Shows basic CPU, RAM, disk status
- No alarm checking or data saving

**8. Exit**
- Safely closes the application
- Logs program termination

---

## Technical Details

### System Requirements
- Python 3.6+
- OS: Windows/macOS/Linux  
- Dependencies: `psutil`

### File Structure
All data files are automatically created in the `Storage/` directory:
- `alarms.json` - Persistent alarm configurations
- `session-[timestamp].json` - Monitoring session data
- `log.txt` - Event and error logging

### Code Architecture
The application demonstrates key programming concepts:
- **Modular Design**: Separation of concerns across multiple files
- **Hybrid Programming**: Object-Oriented Programming (Alarm class) combined with Functional Programming
- **File I/O**: Reading and writing JSON and text files
- **Error Handling**: Basic exception handling for user input
- **Data Structures**: Using lists and dictionaries for data management
- **External Libraries**: Integration with psutil for system monitoring

---

## Example Output

```
=== SYSTEM MONITOR ===
1. Start monitoring
2. Show status
3. Create alarm
4. Show alarms
5. Edit alarms
6. Show last session
7. Simple mode
8. Exit

Enter choice: 1

Starting system monitoring...
Monitoring will run 10 times, then stop automatically
Reading 1/10:
CPU: 45% | RAM: 67% | DISK: 23%
Waiting 2 seconds...
Reading 2/10:
CPU: 48% | RAM: 68% | DISK: 23%
ALERT: CPU usage is 48% (threshold: 40%)
...
```

---

## Learning Outcomes

Building this system monitor demonstrates understanding of:
- **File Operations**: JSON and text file handling
- **User Interface**: Menu-driven program design
- **Data Persistence**: Saving and loading application state
- **Error Handling**: Input validation and exception management
- **Module Organization**: Clean code structure and separation of concerns
- **External Libraries**: Using psutil for system monitoring

---

## Reflection

This project showcases practical Python programming skills suitable for a DevOps environment. The clean, modular design makes the code easy to understand, modify, and extend. The application successfully combines system monitoring, data persistence, and user interaction in a professional yet accessible way.

---

**Said Ebadi - DevOps/Class of 2025 - Chas Academy**
