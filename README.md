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


````Bash 
pip install requests schedule

`````
Signal-CLI installieren
Für den Versand von Nachrichten über Signal musst du Signal-CLI installieren und einrichten. Eine detaillierte Anleitung findest du hier: Signal-CLI.

Konfiguration
1.OpenWeatherMap API Key: Registriere dich auf OpenWeatherMap und hole dir einen API-Schlüssel. Füge diesen in die API_KEY Variable ein.

````python
API_KEY = 'dein_openweathermap_api_key'
````
2.Signal Telefonnummern: Gib deine Signal-registrierte Telefonnummer und die Telefonnummer des Empfängers ein.
````python
SIGNAL_PHONE_NUMBER = '+DEINE_SIGNAL_NUMMER'  # Deine registrierte Signal-Telefonnummer
TO_PHONE_NUMBER = '+EMPFÄNGER_NUMMER'  # Empfängernummer
````

Verwendung
GUI starten
Das Programm startet eine grafische Oberfläche, über die du To-Do-Listen und Geburtstage verwalten kannst. Starte das Programm mit:

````bash
python app.py
````
Funktionen der GUI
To-Do-Liste: Aufgaben hinzufügen, entfernen und speichern.
Geburtstagsverwaltung: Geburtstage hinzufügen, löschen und speichern.
Wetterabfrage: Klicke auf den Button, um die Wetterdaten sofort abzurufen.
