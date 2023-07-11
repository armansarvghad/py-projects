from PIL import Image
import numpy as np
import os
import random

# Set the dimensions of the tiles in the mosaic
TILE_WIDTH = 32
TILE_HEIGHT = 32

# Set the path to the input image and the directory containing the tile images
input_image_path = 'path_to_input_image.jpg'
tiles_directory = 'path_to_tiles_directory'

# Load the input image and convert it to RGB mode
input_image = Image.open(input_image_path).convert('RGB')

# Resize the input image to a multiple of the tile dimensions
input_image = input_image.resize((
    input_image.width // TILE_WIDTH * TILE_WIDTH,
    input_image.height // TILE_HEIGHT * TILE_HEIGHT
))

# Get the dimensions of the resized input image
input_width, input_height = input_image.size

# Create an empty canvas for the mosaic
mosaic = Image.new('RGB', (input_width, input_height))

# Iterate over each tile in the input image
for y in range(0, input_height, TILE_HEIGHT):
    for x in range(0, input_width, TILE_WIDTH):
        # Extract the region of the input image corresponding to the tile
        region = input_image.crop((x, y, x + TILE_WIDTH, y + TILE_HEIGHT))

        # Calculate the average color of the region
        average_color = np.array(region).mean(axis=(0, 1)).astype(int)

        # Find a random tile image that closely matches the average color
        tile_images = os.listdir(tiles_directory)
        random.shuffle(tile_images)
        for tile_image in tile_images:
            tile_path = os.path.join(tiles_directory, tile_image)
            tile = Image.open(tile_path).convert('RGB')
            tile_average_color = np.array(tile).mean(axis=(0, 1)).astype(int)
            if np.allclose(average_color, tile_average_color, atol=10):
                break

        # Resize the tile to match the dimensions of the input tile
        tile = tile.resize((TILE_WIDTH, TILE_HEIGHT))

        # Paste the tile onto the mosaic canvas
        mosaic.paste(tile, (x, y))

# Save the mosaic image
mosaic.save('path_to_save_mosaic.jpg')
