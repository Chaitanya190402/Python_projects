import speech_recognition as sr
import webbrowser
import os
import subprocess

def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

def process_query(query):
    if "play" in query and "song" in query:
        play_song(query)
    elif "search" in query or "google" in query:
        google_search(query)
    elif "volume" in query:
        adjust_volume(query)
    elif "brightness" in query:
        adjust_brightness(query)
    elif "open" in query and ("application" in query or "notepad" in query):
        open_notepad()
    elif "open" in query and("application" in query or "spotify" in query):
        open_spotify()
    elif "play" in query and ("salaar" in query or "movie" in query):
        Salaar()
    else:
        print("Command not recognized.")

def google_search(query):
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)

def play_song(query):
    song_name = query.replace("play", "").replace("song", "").strip()
    youtube_url = f"https://www.youtube.com/results?search_query={song_name}"
    webbrowser.open(youtube_url)

def adjust_volume(query):
    try:
        volume_level = int(query.split()[-1])  # Extract the volume level from the query
    except ValueError:
        print("Invalid volume level.")
        return

    if "increase" in query:
        subprocess.run(["nircmd", "changesysvolume", f"+{volume_level}"])
        print(f"Increased volume by {volume_level} points.")
    elif "decrease" in query:
        subprocess.run(["nircmd", "changesysvolume", f"-{volume_level}"])
        print(f"Decreased volume by {volume_level} points.")
    else:
        print("Volume command not recognized.")



def adjust_brightness(query):
    try:
        brightness_level = int(query.split()[-1])
    except ValueError:
        print("Invalid brightness level.")
        return

    if "increase" in query:
        subprocess.run(["powershell", f"(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1, (Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightness).CurrentBrightness + {brightness_level})"])
        print(f"Increased brightness by {brightness_level} points.")
    elif "decrease" in query:
        subprocess.run(["powershell", f"(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1, (Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightness).CurrentBrightness - {brightness_level})"])
        print(f"Decreased brightness by {brightness_level} points.")
    else:
        print("Brightness command not recognized.")



def open_notepad():
    os.system("start notepad")

def open_spotify():
    os.system("start Spotify")

def Salaar():
    os.system("C:\\Users\\ASUS\\Videos\\Salaar-Part-1-Telugu-drh8i-2023.mp4")





if __name__ == "__main__":
    search_query = speech_to_text()

    if search_query:
        process_query(search_query)
