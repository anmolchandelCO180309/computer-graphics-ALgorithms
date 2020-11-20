import pygame
import math

pygame.init()
pixel_size = 2
black = (255, 255, 255)
white = (0, 0, 0)
screen_width = 800
screen_height = 600
screen_display = pygame.display.set_mode((screen_width, screen_height))
screen_display.fill(black)
pygame.display.set_caption("Midpoint Circle")

def mp_circle(Cx, Cy, rad):
    screen_close = False
    while not screen_close:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                screen_close = True

        x = 0
        y = rad
        p = 5/4 - rad

        while x <= rad / math.sqrt(2):

            pygame.draw.rect(screen_display, white, [Cx + y, Cy - x, pixel_size, pixel_size])
            pygame.draw.rect(screen_display, white, [Cx + x, Cy - y, pixel_size, pixel_size])
            pygame.draw.rect(screen_display, white, [Cx - x, Cy - y, pixel_size, pixel_size])
            pygame.draw.rect(screen_display, white, [Cx - y, Cy - x, pixel_size, pixel_size])
            pygame.draw.rect(screen_display, white, [Cx - y, Cy + x, pixel_size, pixel_size])
            pygame.draw.rect(screen_display, white, [Cx - x, Cy + y, pixel_size, pixel_size])
            pygame.draw.rect(screen_display, white, [Cx + x, Cy + y, pixel_size, pixel_size])
            pygame.draw.rect(screen_display, white, [Cx + y, Cy + x, pixel_size, pixel_size])

            if (p < 0):
                p = p + 2 * x + 3

            else:
                p = p + 2 * x - 2 * y + 5
                y -= 1

            x += 1

        pygame.display.update()

#driver code
x = 350
y = 280
r = 250
mp_circle(x, y, r)
pygame.quit()
