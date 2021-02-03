"""
Project configuration data. 
Contains main properties.
"""
import os

IMAGE_SIZE = 128
SCREEN_SIZE = 512
NUM_TILES_SIDE = 4
NUM_TILES_TOTAL = 16
MARGIN = 4

## retrieve the images
ASSET_DIR = "assets"
ASSET_FILES = [x for x in os.listdir(ASSET_DIR) if x[-3:].lower() == "png"]

# confirm the correct number of images
assert len(ASSET_FILES) == 8