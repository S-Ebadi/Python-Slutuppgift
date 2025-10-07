# Simple Alarms with OOP Enhancement
import json
import os

class Alarm:
    """Representerar ett enskilt larm med typ och tröskelvärde."""
    def __init__(self, alarm_type, threshold):
        self.type = alarm_type
        self.threshold = threshold

    def is_triggered(self, value):
        """Returnerar True om värdet överskrider tröskeln."""
        return value >= self.threshold

    def __str__(self):
        return f"{self.type} alarm {self.threshold}%"

alarms = []

def create_new_alarm():
    print("\n=== Create New Alarm ===")
    print("1. CPU alarm")
    print("2. RAM alarm") 
    print("3. DISK alarm")
    
    choice = input("Choose type (1-3): ")
    if choice not in ["1", "2", "3"]:
        print("Invalid choice!")
        return
    
    try:
        threshold = int(input("Enter threshold (1-100): "))
        if threshold < 1 or threshold > 100:
            print("Must be between 1-100!")
            return
    except:
        print("Must be a number!")
        return
    
    if choice == "1": alarm_type = "CPU"
    elif choice == "2": alarm_type = "RAM"
    else: alarm_type = "DISK"
    
    # Skapa Alarm-objekt och spara som dict för JSON
    new_alarm = Alarm(alarm_type, threshold)
    alarms.append(new_alarm.__dict__)
    save_alarms()
    print("Alarm created:", alarm_type, ">=", threshold, "%")

def show_all_alarms():
    load_alarms()
    if len(alarms) == 0:
        print("No alarms found.")
        input("Press Enter to continue...")
        return
    
    print("\n=== All Alarms ===")
    counter = 1
    for alarm in alarms:
        print(str(counter) + ". " + alarm["type"] + " >= " + str(alarm["threshold"]) + "%")
        counter = counter + 1
    input("Press Enter to continue...")

def edit_delete_alarms():
    load_alarms()
    if len(alarms) == 0:
        print("No alarms to edit.")
        input("Press Enter to continue...")
        return
    
    print("\n=== Edit/Delete Alarms ===")
    counter = 1
    for alarm in alarms:
        print(str(counter) + ". " + alarm["type"] + " >= " + str(alarm["threshold"]) + "%")
        counter = counter + 1
    
    try:
        choice = int(input("Select alarm number: "))
        if choice < 1 or choice > len(alarms):
            print("Invalid number!")
            return
    except:
        print("Must be a number!")
        return
    
    print("1. Change threshold")
    print("2. Delete alarm")
    action = input("Choose action (1-2): ")
    
    selected_alarm = choice - 1
    
    if action == "1":
        try:
            new_threshold = int(input("Enter new threshold (1-100): "))
            if new_threshold >= 1 and new_threshold <= 100:
                alarms[selected_alarm]["threshold"] = new_threshold
                print("Threshold updated!")
            else:
                print("Must be between 1-100!")
                return
        except:
            print("Must be a number!")
            return
    elif action == "2":
        deleted_alarm = alarms.pop(selected_alarm)
        print("Deleted alarm:", deleted_alarm["type"])
    else:
        print("Invalid action!")
        return
    
    save_alarms()
    input("Press Enter to continue...")

def save_alarms():
    # Make Storage folder if needed
    if not os.path.exists("Storage"):
        os.makedirs("Storage")
    
    # Save alarms to file
    with open("Storage/alarms.json", "w") as f:
        json.dump(alarms, f)

def load_alarms():
    global alarms
    alarms = []
    
    # Check if file exists
    if os.path.exists("Storage/alarms.json"):
        try:
            with open("Storage/alarms.json", "r") as f:
                alarms = json.load(f)
        except:
            pass

def check_alarms(cpu, ram, disk):
    load_alarms()
    messages = []
    
    for alarm_data in alarms:
        # Skapa Alarm-objekt från sparad data
        alarm = Alarm(alarm_data["type"], alarm_data["threshold"])
        
        if alarm.type == "CPU":
            value = cpu
        elif alarm.type == "RAM":
            value = ram
        else:
            value = disk
        
        # Använd objektets is_triggered() metod
        if alarm.is_triggered(value):
            message = alarm.type + " usage is " + str(value) + "% (threshold: " + str(alarm.threshold) + "%)"
            messages.append(message)
    
    return messages



