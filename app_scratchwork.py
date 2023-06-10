import requests
from PIL import Image, ImageFilter
import imageio
import numpy as np
import os

# Image URL
url = "https://cdn.discordapp.com/attachments/984632424610824222/1116496097557368883/wolfram_krishna__radha_in_vrindavan_9833b8eb-ca61-4db1-b657-c86bae601436.png"

# Download Image
response = requests.get(url)
filename = "downloaded.png"
with open(filename, 'wb') as out_file:
    out_file.write(response.content)

# Load image using PIL
img = Image.open(filename)

# Edge Detection filter
edges = img.filter(ImageFilter.FIND_EDGES)

# Save the filtered image as jpg
edges.save("filtered.jpg")

# Generate animated gif
images = [img, edges]
imageio.mimsave('animated.gif', [np.array(im) for im in images], duration=1000)  # use duration instead of fps

print("Image processing complete. 'filtered.jpg' and 'animated.gif' generated.")
