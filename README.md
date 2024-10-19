# ADHD Assistant
 
Wetter-, To-Do- und Geburtstags-Manager mit Signal-Benachrichtigungen
Dieses Projekt ist eine einfache Desktop-Anwendung, die Wetterberichte abruft, eine To-Do-Liste verwaltet und Geburtstage trackt. Zusätzlich kann das Programm über den Signal Messenger Benachrichtigungen zu Wetter und Geburtstagen senden. Die Daten, wie z.B. Geburtstage und Aufgaben, werden lokal in Textdateien gespeichert.

Funktionen
Wetterabfrage: Abfrage des aktuellen Wetters für eine vordefinierte Stadt (Standard: Berlin) mit Temperatur, Wetterbeschreibung und Regenwahrscheinlichkeit über die OpenWeatherMap API.
To-Do-Liste: Füge Aufgaben hinzu, speichere sie in einer Textdatei und entferne erledigte Aufgaben.
Geburtstags-Erinnerung: Geburtstage können hinzugefügt und verwaltet werden. Das Programm prüft jeden Tag, ob jemand Geburtstag hat und sendet gegebenenfalls eine Nachricht.
Signal-Nachrichten: Das Programm sendet täglich eine Benachrichtigung über den aktuellen Wetterbericht, anstehende Aufgaben und Geburtstage über den Signal Messenger.
Lokale Speicherung: Aufgaben und Geburtstage werden in Textdateien gespeichert.
Voraussetzungen
Python 3.x
Signal-CLI: Ein Tool zur Integration von Signal in Skripte.
Tkinter: Wird für die GUI verwendet (standardmäßig in Python enthalten).
Requests: Für die API-Abfrage von OpenWeatherMap.
Schedule: Für das tägliche Ausführen von Aufgaben.

Python-Bibliotheken installieren
pip install requests schedule

