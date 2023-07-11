import pygame

def play_music(file_path):
    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load and play the music file
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    # Wait until the music finishes playing
    while pygame.mixer.music.get_busy():
        continue

    # Clean up after the music finishes
    pygame.mixer.quit()

# Example usage
music_file = 'path_to_music_file.mp3'
play_music(music_file)
