import tkinter as tk
from tkinter import filedialog
import pygame
import os

# Variable zum Speichern des Pausenstatus
paused = False
current_track = None

# Funktion zum Hinzufügen von Musikdateien
def add_music():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
    if file_path:
        if file_path.lower().endswith(('.mp3', '.wav')):
            playlist_data.append(file_path)
            update_playlist()

# Funktion zur Aktualisierung der Playlist-Anzeige
def update_playlist():
    playlist.delete(0, tk.END)
    for file_path in playlist_data:
        # Zeige nur den Dateinamen an
        filename = os.path.basename(file_path)
        playlist.insert(tk.END, filename)

# Funktion zum Abspielen der ausgewählten Musikdatei
def play_music():
    global current_track
    selected_index = playlist.curselection()
    if selected_index:
        selected_index = int(selected_index[0])
        selected_file = playlist_data[selected_index]
        pygame.init()
        if paused and current_track == selected_file:
            # Wenn die Musik pausiert wurde und die gleiche Datei ausgewählt ist, fortsetzen
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.load(selected_file)
            pygame.mixer.music.play()
        current_track = selected_file

# Funktion zum Pausieren der Musikwiedergabe
def pause_music():
    global paused
    pygame.mixer.music.pause()
    paused = True

# Funktion zum Löschen ausgewählter Tracks aus der Playlist
def delete_selected_tracks():
    global current_track
    selected_indices = playlist.curselection()
    if selected_indices:
        selected_indices = list(map(int, selected_indices))
        for index in sorted(selected_indices, reverse=True):
            del playlist_data[index]
        update_playlist()
        # Setze die aktuelle Datei zurück, wenn sie gelöscht wurde
        current_track = None

# GUI erstellen
root = tk.Tk()
root.title("Musixxx - Musikplayer")

# Buttons für die Steuerung hinzufügen
add_button = tk.Button(root, text="Musik hinzufügen", command=add_music)
add_button.pack(pady=0, padx=100)  # Füge einen horizontalen Abstand von 100 hinzu

# Playlist-Anzeige erstellen (Listbox)
playlist = tk.Listbox(root)
playlist.pack(pady=0, padx=100)  # Füge einen horizontalen Abstand von 100 hinzu

# Playlist-Datenstruktur
playlist_data = []

play_button = tk.Button(root, text="Musik abspielen", command=play_music)
play_button.pack(pady=0, padx=100)  # Füge einen horizontalen Abstand von 100 hinzu

pause_button = tk.Button(root, text="Pause", command=pause_music)
pause_button.pack(pady=0, padx=100)  # Füge einen horizontalen Abstand von 100 hinzu

delete_button = tk.Button(root, text="Löschen", command=delete_selected_tracks)
delete_button.pack(pady=(0, 50), padx=100)  # Füge einen vertikalen Abstand von 50 hinzu, nur nach unten

# GUI-Schleife starten
root.mainloop()
