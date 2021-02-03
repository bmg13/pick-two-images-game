"""
Class responsible to run the game.
"""
import pygame
import game_config as config

# use the pygame lib
from pygame import display, event, image
from club import Club
from time import sleep

pygame.init()

def find_index(x, y):
    """
    Find the tile index based on mouse clicked.
    """
    row = y // config.IMAGE_SIZE
    col = x // config.IMAGE_SIZE
    index = row * config.NUM_TILES_SIDE + col
    return index


display.set_caption('Club Game')
screen = display.set_mode((512, 512))

matched = image.load("other_assets/matched.png")
# set the coordinates to start on the top left corner
screen.blit(matched, (0,0))
# the display will not show the updated screen until it is flipped
display.flip()

# keep the game runnin
running = True

tiles = [Club(i) for i in range(0, config.NUM_TILES_TOTAL)]
current_images = []

while running:
    current_envents = event.get()

    for e in current_envents:
        if e.type == pygame.QUIT:
            # stop the game 
            running = False
        
        # check pressed keyboard key
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                running = False
        
        # check mouse button pressed
        if e.type == pygame.MOUSEBUTTONDOWN:
            # get the index of the clicked tile
            mouse_x, mouse_y = pygame.mouse.get_pos()
            index = find_index (mouse_x, mouse_y)
            # the following if blocks the user of winnig just by double pressing the same tile
            if index not in current_images:
                current_images.append(index)
            if len(current_images) > 2:
                current_images = current_images[1:]
    
    screen.fill((255, 255, 255))

    total_skipped = 0

    for i, tile in enumerate(tiles):
        image_i = tile.image if i in current_images else tile.box
        if not tile.skip:
            screen.blit(image_i, (tile.col * config.IMAGE_SIZE + config.MARGIN, tile.row * config.IMAGE_SIZE + config.MARGIN))
        else:
            total_skipped += 1

    # confirm the selected tiles are the same and, if so, remove them
    if len(current_images) == 2:
        idx1, idx2 = current_images
        if tiles[idx1].name == tiles[idx2].name:
           tiles[idx1].skip = True
           tiles[idx2].skip = True
           # since both images are the same, a celebratory message is shown. The sleep method allows to "prolong" the effect, nothing else
           sleep(0.5)
           screen.blit(matched, (0, 0))
           display.flip()
           sleep(0.5)
           current_images = []
    
    # when all tiles are found, the game is closed
    if total_skipped == len(tiles):
        running = False

    # as mentioned, changes will only be shown after the display is flipped
    display.flip()

print('Thank you, champion!')