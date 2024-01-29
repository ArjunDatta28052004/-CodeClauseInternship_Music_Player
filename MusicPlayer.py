import os
import pygame
import tkinter as tk
from tkinter import filedialog, messagebox

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("Music Player")
        self.master.geometry("500x250")

        self.playlist = []
        self.current_index = 0
        self.paused = False

        self.initialize_ui()

    def initialize_ui(self):
        self.label = tk.Label(self.master, text="Music Player", font=("Helvetica", 14))
        self.label.pack(pady=5)

        self.btn_load = tk.Button(self.master, text="Load Playlist", command=self.load_playlist)
        self.btn_load.pack(pady=5)

        self.btn_play_pause = tk.Button(self.master, text="Play", command=self.toggle_play_pause)
        self.btn_play_pause.pack(pady=5)

        self.btn_stop = tk.Button(self.master, text="Stop", command=self.stop)
        self.btn_stop.pack(pady=5)

        self.btn_next = tk.Button(self.master, text="Next", command=self.next_song)
        self.btn_next.pack(pady=5)

        self.btn_prev = tk.Button(self.master, text="Previous", command=self.prev_song)
        self.btn_prev.pack(pady=5)

    def load_playlist(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.playlist = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.mp3')]
            if not self.playlist:
                messagebox.showinfo("Error", "No MP3 files found in the selected folder.")
            else:
                messagebox.showinfo("Success", "Playlist loaded successfully.")

    def toggle_play_pause(self):
        if not self.playlist:
            messagebox.showinfo("Error", "Playlist is empty. Load songs first.")
            return

        if pygame.mixer.music.get_busy():
            if self.paused:
                pygame.mixer.music.unpause()
                self.btn_play_pause.config(text="Pause")
                self.paused = False
            else:
                pygame.mixer.music.pause()
                self.btn_play_pause.config(text="Resume")
                self.paused = True
        else:
            self.play()

    def play(self):
        if not self.playlist:
            messagebox.showinfo("Error", "Playlist is empty. Load songs first.")
            return
        pygame.mixer.music.load(self.playlist[self.current_index])
        pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.stop()

    def next_song(self):
        self.current_index = (self.current_index + 1) % len(self.playlist)
        self.play()

    def prev_song(self):
        self.current_index = (self.current_index - 1) % len(self.playlist)
        self.play()

def main():
    pygame.init()
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
