import network
import time

class WiFiManager:
    def __init__(self, ssid, password):
        self.ssid = ssid
        self.password = password
        self.wlan = network.WLAN(network.STA_IF)

    def connect(self):
        self.wlan.active(True)
        self.wlan.connect(self.ssid, self.password)
        while not self.wlan.isconnected():
            time.sleep(1)
        print('Connected to WiFi')
        print('Network config:', self.wlan.ifconfig())

    def disconnect(self):
        self.wlan.disconnect()
        self.wlan.active(False)
        print('Disconnected from WiFi')

# Beispiel für die Verwendung der WiFiManager-Klasse
if __name__ == "__main__":
    wifi_manager = WiFiManager("Your_SSID", "Your_Password")
    wifi_manager.connect()
    # Führe hier den Rest deines Programms aus
