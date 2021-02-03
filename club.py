"""
Data regarding the football club
"""
import os
import random
import game_config as config

from pygame import image, transform

# create a dictionary with the available clubs
clubs_count = dict((a, 0) for a in config.ASSET_FILES)

def available_clubs():
    return [c for c, a in clubs_count.items() if a < 2]


class Club:
    def __init__(self, index):
        self.index = index
        # since this is a 4x4 table, the row and column are set like the following
        self.row = index // config.NUM_TILES_SIDE
        self.col = index % config.NUM_TILES_SIDE
        # set the name randomly, considering the available number clubs
        self.name = random.choice(available_clubs())
        clubs_count[self.name] += 1
        # load the club image from the file
        self.image_path = os.path.join(config.ASSET_DIR, self.name)
        self.image = image.load(self.image_path)
        # scale the image for the display
        self.image = transform.scale(self.image, (config.IMAGE_SIZE - 2*config.MARGIN, config.IMAGE_SIZE - 2*config.MARGIN))
        # make a copy of the image
        self.box = self.image.copy()
        self.box.fill((200, 200, 200))
        # if both club images have already been found, we set the following flag as True
        self.skip = False