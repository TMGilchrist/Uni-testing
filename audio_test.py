import pygame
import numpy

pygame.init()
pygame.mixer.init()

running = True

main_screen = pygame.display.set_mode((800, 600))
main_screen.fill((255, 0, 0))
# pygame.mixer.music.load()   # play on key press
# pygame.mixer.music.play

laser_sound = pygame.mixer.Sound("Laser_Machine_Gun.wav")

laser_sound_array = pygame.sndarray.samples(laser_sound)

for sample in laser_sound_array:   # change volume <-- put into function
    sample *= 1

pygame.display.update()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                laser_sound.play(1)


