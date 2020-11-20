import pygame

pygame.init()
pixel_size = 2
black = (255, 255, 255)
white = (0, 0, 0)
screen_width = 800
screen_height = 600
screen_display = pygame.display.set_mode((screen_width, screen_height))
screen_display.fill(black)
pygame.display.set_caption("DDA LINE")

def dda(x1, y1, x2, y2):
    screen_close = False
    while not screen_close:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                screen_close = True
        
        dx = x2-x1
        dy = y2-y1

        if(abs(dx) > abs(dy)):
            step = abs(dx)
        else:
            step = abs(dy)

        x = x1
        y = y1
        x_inc = dx/step
        y_inc = dy/step

        i=1
        while i <= step:
            pygame.draw.rect(screen_display, white,[x, y, pixel_size, pixel_size])
            x = x + x_inc
            y = y + y_inc
            i += 1
        pygame.display.update()

#driver code
x1 = y1 = 200
x2 = y2 = 550
dda(x1, y1, x2, y2)
pygame.quit()
