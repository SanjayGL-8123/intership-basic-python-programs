import pygame
# pip install pygame

import time

pygame.mixer.init()


pygame.mixer.music.load("Thalapathy Vetri Kondan.mp3")


pygame.mixer.music.play()


# 4. Keep script running while music plays
# Otherwise, the script ends and the sound stops immediately
while pygame.mixer.music.get_busy():
    time.sleep(1)