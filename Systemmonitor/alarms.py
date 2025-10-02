import os, json

# Storage-mapp för alla larm
STORAGE_DIR = os.path.join(os.path.dirname(__file__), "Storage")
os.makedirs(STORAGE_DIR, exist_ok=True)

ALARMS_FILE = os.path.join(STORAGE_DIR, "alarms.json")


class AlarmStore:
    def __init__(self):
        self.alarms = []
        self.load()

    def load(self):
        """Ladda in larm från alarms.json"""
        if os.path.exists(ALARMS_FILE):
            with open(ALARMS_FILE, "r") as f:
                try:
                    self.alarms = json.load(f)
                except:
                    self.alarms = []
        else:
            self.alarms = []

    def save(self):
        """Spara larm till alarms.json"""
        with open(ALARMS_FILE, "w") as f:
            json.dump(self.alarms, f, indent=2)

    def add(self, metric, threshold):
        """Lägg till ett nytt larm"""
        alarm = {"metric": metric, "threshold": threshold}
        self.alarms.append(alarm)
        self.save()

    def list(self):
        """Returnera alla larm sorterade på metric"""
        return sorted(self.alarms, key=lambda a: (a["metric"], a["threshold"]))

    def remove(self, index):
        """Ta bort ett larm baserat på index"""
        if 0 <= index < len(self.alarms):
            self.alarms.pop(index)
            self.save()

    def update(self, index, threshold):
        """Uppdatera threshold för ett larm"""
        if 0 <= index < len(self.alarms):
            self.alarms[index]["threshold"] = threshold
            self.save()

    def get_relevant(self, metric, value):
        """
        Returnera det närmaste larmet som ska triggas.
        Ex: Om CPU har larm 60/70/80 och värde=95 → endast 80 triggas.
        """
        relevant = [a for a in self.alarms if a["metric"] == metric and value >= a["threshold"]]
        if not relevant:
            return None
        return max(relevant, key=lambda a: a["threshold"])
