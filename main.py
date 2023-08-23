import machine
import neopixel
import network
import time
from localTime import LocalTime
from wifi_manager import WiFiManager	# Importiere die WiFiManager-Klasse aus der Datei wifi_manager.py
#import lilaLed as lilaLed

# WiFi-Verbindung herstellen
wifi_manager = WiFiManager("TaDa", "Angelgirl_10.10.10!")
wifi_manager.connect()

#schleife die die Zeit abfragt und und zu gewissen Zeiten die LEDS ansteuert um zu unterschiedlichen zeiten unterschiedliche Farben zu haben

