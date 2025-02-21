import pygame
import os

# Initialize the pygame mixer
pygame.mixer.init()

# Function to load and play music
def play_music(song):
    if os.path.exists(song):  # Check if the song exists
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()
        print(f"Playing: {song}")
    else:
        print("Song not found.")

# Function to stop music
def stop_music():
    pygame.mixer.music.stop()
    print("Music Stopped")

# Function to pause music
def pause_music():
    pygame.mixer.music.pause()
    print("Music Paused")

# Function to unpause music
def unpause_music():
    pygame.mixer.music.unpause()
    print("Music Resumed")

# Menu for the app
def music_player():
    print("Welcome to the Music App!")
    print("Commands: play <song_name>, pause, unpause, stop, quit")
    
    while True:
        command = input("Enter command: ").strip().lower()
        
        if command.startswith("play "):
            song_name = command[5:]
            play_music(song_name)
        elif command == "pause":
            pause_music()
        elif command == "unpause":
            unpause_music()
        elif command == "stop":
            stop_music()
        elif command == "quit":
            stop_music()
            break
        else:
            print("Invalid command. Try again.")

if __name__ == "__main__":
    music_player()
