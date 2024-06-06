import pygame
pygame.init()
# Setting game window dimensions
window_width = 1000
window_height = 1000
game_display = pygame.display.set_mode((window_width, window_height))
# Loading the image
bg_image = pygame.image.load('images\duplicate.jpg')
# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Drawing image at position (0,0)
    game_display.blit(bg_image, (0, 0))
    pygame.display.update()
pygame.quit()