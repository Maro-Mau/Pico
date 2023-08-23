import ntptime
import utime

class LocalTime:
    def __init__(self, timezone_offset):
        self.utime = utime
        self.ntptime = ntptime
        self.timezone_offset = timezone_offset
        self.update_time()

    def update_time(self):
        try:
            self.ntptime.settime()
            utc_time = self.utime.time()
            local_time = utc_time + self.timezone_offset
            self.local_time = self.utime.localtime(local_time)
        except Exception as e:
            print("Fehler beim Aktualisieren der Zeit:", e)

# Beispiel für die Verwendung der LocalTime-Klasse
if __name__ == "__main__":
    timezone_offset = 3600  # Beispiel: UTC+1 (3600 Sekunden)
    lt = LocalTime(timezone_offset)
    while True:
        try:
            lt.update_time()
            print("Aktuelle lokale Zeit:", lt.local_time)
            utime.sleep(1)  # Warte 1 Sekunde, bevor die Zeit erneut aktualisiert wird
        except KeyboardInterrupt:
            print("Programm wurde beendet.")
            break
        except Exception as e:
            print("Fehler aufgetreten:", e)
