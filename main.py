import tkinter as tk
from tkinter import filedialog 

import pygame

# Hauptfenster erstellen
root = tk.Tk()
root.title("Musixxx - Musikplayer")

# Playlist erstellen (Listbox)
playlist = tk.Listbox(root)
playlist.pack(pady=20)

# Funktion zum Hinzufügen von Musikdateien
playlist_data = []

# Funktion zum Hinzufügen von Musikdateien
def add_music():
    # Dateiauswahl-Dialog öffnen
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])

    if file_path:
        # Überprüfung des Dateiformats
        if file_path.lower().endswith(('.mp3', '.wav')):
            # Hinzufügen zur Playlist-Datenstruktur
            playlist_data.append(file_path)
            
            # Aktualisierung der GUI-Playlist
            playlist.insert(tk.END, file_path)
        else:
            print("Ungültiges Dateiformat. Bitte wähle eine MP3- oder WAV-Datei.")

    #Update die Playlist, um die hinzugefügten Lieder in der Playlist widerzuspiegeln        
    update_playlist()

# Funktion zur Aktualisierung der Playlist-Anzeige
def update_playlist():
    # Lösche alle Einträge in der Playlist-Anzeige
    playlist.delete(0, tk.END)
    
    # Füge die aktuellen Einträge aus der Playlist-Datenstruktur hinzu
    for file_path in playlist_data:
        playlist.insert(tk.END, file_path)

# Funktion zum Abspielen der ausgewählten Musikdatei
def play_music():
    selected_index = playlist.curselection()
    if selected_index:
        selected_index = int(selected_index[0])
        selected_file = playlist_data[selected_index]

        # Initialisiere pygame, falls noch nicht geschehen
        pygame.init()

        # Lade die ausgewählte Musikdatei
        pygame.mixer.music.load(selected_file)

        # Starte die Wiedergabe
        pygame.mixer.music.play()

# Funktion zum Pausieren der Musikwiedergabe
def pause_music():
    pygame.mixer.music.pause()

# Funktion zum Fortsetzen der Musikwiedergabe
def resume_music():
    pygame.mixer.music.unpause()

# Funktion zum Löschen ausgewählter Tracks aus der Playlist
def delete_selected_tracks():
    selected_indices = playlist.curselection()
    if selected_indices:
        # Konvertiere die ausgewählten Indices zu Integer
        selected_indices = list(map(int, selected_indices))

        # Lösche die ausgewählten Tracks aus der Playlist-Datenstruktur
        for index in sorted(selected_indices, reverse=True):
            del playlist_data[index]

        # Aktualisiere die GUI-Playlist
        update_playlist()

# Button zum Hinzufügen von Musikdateien
add_button = tk.Button(root, text="Musik hinzufügen", command=add_music)
add_button.pack(pady=10)

# Weitere GUI-Elemente und Funktionalitäten können hinzugefügt werden

# Playlist-Anzeige erstellen (Listbox)
playlist = tk.Listbox(root)
playlist.pack(pady=20)

# Beispiel: Verknüpfung der Abspielfunktion mit einem Button
play_button = tk.Button(root, text="Musik abspielen", command=play_music)
play_button.pack(pady=10)

# Beispiel: Verknüpfung von Pause und Fortsetzen mit Buttons
pause_button = tk.Button(root, text="Pause", command=pause_music)
pause_button.pack(side=tk.LEFT, padx=5)
resume_button = tk.Button(root, text="Fortsetzen", command=resume_music)
resume_button.pack(side=tk.LEFT, padx=5)

# Beispiel: Verknüpfung der Löschfunktion mit einem Button
delete_button = tk.Button(root, text="Löschen", command=delete_selected_tracks)
delete_button.pack(pady=10)

# Starte die GUI-Schleife
root.mainloop()