#!/usr/bin/python

import sys, pygame
pygame.init()

NATIVE_RESOLUTION = width, height = [240, 160]
SCREEN_RESOLUTION = 960, 720
black = (0, 0, 0)

caption = "Native Scaling - FPS: "
pygame.display.set_caption(caption)
screen = pygame.display.set_mode(SCREEN_RESOLUTION)
native_screen = pygame.Surface(NATIVE_RESOLUTION)

clock = pygame.time.Clock()
average_fps = 0
fps_sample_size = 100
fps_history = list()

asteroid = pygame.image.load("asteroid.png")
asteroid_pos = [0, 0]
asteroid_speed = [160, 160]  # pixels per second move speed

while True:
    dt = clock.tick() / 1000.
    fps = clock.get_fps()
    pygame.display.set_caption(caption + str(fps))
    fps_history.append(fps)
    if len(fps_history) > fps_sample_size:
        average_fps = sum(fps_history) / float(len(fps_history))
        print("Average FPS: " + str(average_fps))
        fps_history = list()

    if asteroid_pos[0] < 0 or asteroid_pos[0] + asteroid.get_width() > width:
        asteroid_speed[0] = -asteroid_speed[0]
    if asteroid_pos[1] < 0 or asteroid_pos[1] + asteroid.get_height() > height:
        asteroid_speed[1] = -asteroid_speed[1]

    asteroid_pos[0] += asteroid_speed[0] * dt
    asteroid_pos[1] += asteroid_speed[1] * dt

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    native_screen.fill(black)
    native_screen.blit(asteroid, asteroid_pos)
    surface = pygame.transform.scale(native_screen, SCREEN_RESOLUTION)
    screen.blit(surface, (0, 0))
    pygame.display.flip()
