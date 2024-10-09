import json
import subprocess  # Für Signal Messenger
import time
import tkinter as tk
from datetime import datetime
from tkinter import messagebox
import requests
import schedule

# OpenWeatherMap API-Details
API_KEY = 'dein_openweathermap_api_key'
CITY = 'City'
URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'

# Telefonnummern für Signal
SIGNAL_PHONE_NUMBER = '+DEINE_SIGNAL_NUMMER'  # Deine registrierte Signal-Telefonnummer
TO_PHONE_NUMBER = '+EMPFÄNGER_NUMMER'  # Empfängernummer

# Funktion zum Senden einer Signal-Nachricht
def send_signal_message(message_body):
    try:
        cmd = [
            'signal-cli',
            '-u', SIGNAL_PHONE_NUMBER,
            'send', '-m', message_body, TO_PHONE_NUMBER
        ]
        subprocess.run(cmd, check=True)
        print(f"Nachricht erfolgreich an {TO_PHONE_NUMBER} gesendet.")
    except subprocess.CalledProcessError as e:
        print(f"Fehler beim Senden der Nachricht: {e}")

# GUI für To-Do-Liste, Geburtstagsliste und Echtzeitanfragen
class WeatherApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Wetter-, To-Do- und Geburtstags-Manager")
        self.geometry("400x700")

        # To-Do-Liste
        self.todo_list = tk.Listbox(self, height=10)
        self.todo_list.pack(pady=10)

        self.task_entry = tk.Entry(self, width=30)
        self.task_entry.pack(pady=5)

        self.add_task_button = tk.Button(self, text="Aufgabe hinzufügen", command=self.add_task)
        self.add_task_button.pack(pady=5)

        self.remove_task_button = tk.Button(self, text="Aufgabe entfernen", command=self.remove_task)
        self.remove_task_button.pack(pady=5)

        self.save_tasks_button = tk.Button(self, text="Aufgaben speichern", command=self.save_tasks)
        self.save_tasks_button.pack(pady=5)

        # Geburtstagsbereich
        self.birthday_list = tk.Listbox(self, height=10)
        self.birthday_list.pack(pady=10)

        self.birthday_entry_name = tk.Entry(self, width=20)
        self.birthday_entry_name.insert(0, "Name")
        self.birthday_entry_name.pack(pady=5)

        self.birthday_entry_date = tk.Entry(self, width=20)
        self.birthday_entry_date.insert(0, "dd-mm-yyyy")
        self.birthday_entry_date.pack(pady=5)

        self.add_birthday_button = tk.Button(self, text="Geburtstag hinzufügen", command=self.add_birthday)
        self.add_birthday_button.pack(pady=5)

        self.remove_birthday_button = tk.Button(self, text="Geburtstag entfernen", command=self.remove_birthday)
        self.remove_birthday_button.pack(pady=5)

        self.save_birthdays_button = tk.Button(self, text="Geburtstage speichern", command=self.save_birthdays)
        self.save_birthdays_button.pack(pady=5)

        # Wetterabfrage-Bereich
        self.weather_button = tk.Button(self, text="Wetter jetzt abfragen", command=self.fetch_weather)
        self.weather_button.pack(pady=20)

        # Initialisiere To-Do-Liste und Geburtstage
        self.load_tasks()
        self.load_birthdays()

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.todo_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def remove_task(self):
        selected_task_index = self.todo_list.curselection()
        if selected_task_index:
            self.todo_list.delete(selected_task_index)

    def save_tasks(self):
        tasks = self.todo_list.get(0, tk.END)
        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(f"{task}\n")
        messagebox.showinfo("Info", "Aufgaben gespeichert!")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                tasks = file.readlines()
                for task in tasks:
                    self.todo_list.insert(tk.END, task.strip())
        except FileNotFoundError:
            pass

    def add_birthday(self):
        name = self.birthday_entry_name.get()
        date = self.birthday_entry_date.get()
        if name != "" and date != "":
            try:
                datetime.strptime(date, "%d-%m-%Y")
                self.birthday_list.insert(tk.END, f"{name} - {date}")
                self.birthday_entry_name.delete(0, tk.END)
                self.birthday_entry_date.delete(0, tk.END)
            except ValueError:
                messagebox.showerror("Fehler", "Ungültiges Datum. Format: dd-mm-yyyy")
        else:
            messagebox.showwarning("Warnung", "Bitte fülle beide Felder aus!")

    def remove_birthday(self):
        selected_birthday_index = self.birthday_list.curselection()
        if selected_birthday_index:
            self.birthday_list.delete(selected_birthday_index)

    def save_birthdays(self):
        birthdays = self.birthday_list.get(0, tk.END)
        with open("birthdays.json", "w") as file:
            json.dump(birthdays, file)
        messagebox.showinfo("Info", "Geburtstage gespeichert!")

    def load_birthdays(self):
        try:
            with open("birthdays.json", "r") as file:
                birthdays = json.load(file)
                for birthday in birthdays:
                    self.birthday_list.insert(tk.END, birthday)
        except FileNotFoundError:
            pass

    def fetch_weather(self):
        try:
            # Wetterdaten von der API abrufen
            response = requests.get(URL)
            data = response.json()

            if data["cod"] != 200:
                messagebox.showerror("Fehler", f"Fehler beim Abrufen der Wetterdaten: {data.get('message', '')}")
                return

            # Wetterdaten extrahieren
            temp = data['main']['temp']
            weather_desc = data['weather'][0]['description']
            rain_prob = data.get('rain', {}).get('1h', 0)

            # Wetterinformationen anzeigen
            weather_info = f"Wetter für {CITY}:\n"
            weather_info += f"Temperatur: {temp}°C\n"
            weather_info += f"Wetter: {weather_desc}\n"
            weather_info += f"Regenwahrscheinlichkeit: {rain_prob}mm"
            messagebox.showinfo("Aktuelles Wetter", weather_info)

        except Exception as e:
            messagebox.showerror("Fehler", f"Fehler beim Abrufen der Wetterdaten: {e}")

def check_weather_and_send_message():
    try:
        # Wetterdaten von der API abrufen
        response = requests.get(URL)
        data = response.json()

        if data["cod"] != 200:
            print("Fehler beim Abrufen der Wetterdaten:", data.get("message", ""))
            return

        # Wetterdaten extrahieren
        temp = data['main']['temp']
        rain_prob = data.get('rain', {}).get('1h', 0)
        weather_desc = data['weather'][0]['description']

        # Nachricht vorbereiten
        message_body = f"Wetterbericht für {CITY}:\n"
        message_body += f"Temperatur: {temp}°C\n"
        message_body += f"Wetter: {weather_desc}\n"
        message_body += f"Regenwahrscheinlichkeit: {rain_prob}mm\n\n"

        if temp < 15:
            message_body += "Empfehlung: Zieh eine Jacke an.\n"
        elif temp yasd
            message_body += "Empfehlung: Du brauchst keine Jacke.\n"

        if rain_prob > 0:
            message_body += "Empfehlung: Nimm einen Regenschirm mit.\n"
        else:
            message_body += "Kein Regenschirm nötig.\n"

        # Lese die To-Do-Liste
        try:
            with open("tasks.txt", "r") as file:
                tasks = file.readlines()
                message_body += "\nTo-Do-Liste für den Tag:\n"
                for task in tasks:
                    message_body += f"- {task.strip()}\n"
        except FileNotFoundError:
            message_body += "\nKeine Aufgaben für den Tag gefunden.\n"

        # Prüfe Geburtstage
        today = datetime.today().strftime("%d-%m")
        try:
            with open("birthdays.json", "r") as file:
                birthdays = json.load(file)
                for birthday in birthdays:
                    name, date = birthday.split(" - ")
                    birthday_date = datetime.strptime(date, "%d-%m-%Y").strftime("%d-%m")
                    if birthday_date == today:
                        message_body += f"\n🎉 Heute hat {name} Geburtstag!\n"

        except FileNotFoundError:
            message_body += "\nKeine Geburtstagsdaten verfügbar.\n"

        # Nachricht über Signal Messenger senden
        send_signal_message(message_body)

    except Exception as e:
        print(f"Fehler: {e}")

# Wetter-Check und Geburtstags-Check jeden Tag um 7 Uhr morgens
schedule.every().day.at("07:00").do(check_weather_and_send_message)

# Wetter-Bot im Hintergrund ausführen
def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

# Starte den Bot und die GUI
if __name__ == "__main__":
    import threading

    # Starte den Wetter-Check in einem separaten Thread
    threading.Thread(target=run_schedule, daemon=True).start()

    # Starte die GUI
    app = WeatherApp()
    app.mainloop()

