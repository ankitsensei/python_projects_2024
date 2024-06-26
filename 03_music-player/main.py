import pygame
import os
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC

pygame.init()

screen_width = 300
screen_height = 200
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Ankit's Music Player")

# Set the directory where your music files are located
music_directory = "C:/Users/Ankit Bhagat/Music"

# Get a list of all music files in the directory
music_files = os.listdir(music_directory)
# Filter out non-music files (if any)
music_files = [file for file in music_files if file.endswith(".mp3")]

current_track_index = 0
paused = False
volume = 0.5

def play_music(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()


# Function to render text
def render_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Function to render album art
def render_album_art(album_art_path):
    if os.path.exists(album_art_path):
        album_art_surface = pygame.image.load(album_art_path)
        album_art_surface = pygame.transform.scale(album_art_surface, (100, 100))
        screen.blit(album_art_surface, (screen_width - 110, 50))

font = pygame.font.SysFont(None, 24)

running = True
while running:
    # Clear the screen
    screen.fill((0, 0, 0))

    # Render text
    render_text("Track: " + music_files[current_track_index], font, (255, 255, 255), 10, 10)
    render_text("Volume: {:.1f}".format(volume), font, (255, 255, 255), 10, 30)
    render_text("Status: " + ("Playing" if not paused else "Paused"), font, (255, 255, 255), 10, 50)

    # Render album art
    file_path = os.path.join(music_directory, music_files[current_track_index])
    audio = MP3(file_path, ID3=ID3)
    if 'APIC:' in audio.tags:
        album_art = audio.tags['APIC:'].data
        with open("album_art.jpg", 'wb') as img_file:
            img_file.write(album_art)
        render_album_art("album_art.jpg")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    pygame.mixer.music.pause()
                    paused = True
            elif event.key == pygame.K_RIGHT:
                # Play the next track
                current_track_index = (current_track_index + 1) % len(music_files)
                play_music(os.path.join(music_directory, music_files[current_track_index]))
            elif event.key == pygame.K_LEFT:
                # Play the previous track
                current_track_index = (current_track_index - 1) % len(music_files)
                play_music(os.path.join(music_directory, music_files[current_track_index]))
            elif event.key == pygame.K_UP:
                # Volume up
                volume = min(volume + 0.1, 1.0)
                pygame.mixer.music.set_volume(volume)
            elif event.key == pygame.K_DOWN:
                # Volume down
                volume = max(volume - 0.1, 0.0)
                pygame.mixer.music.set_volume(volume)
    pygame.display.update()
pygame.quit()
