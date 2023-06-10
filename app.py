import requests
from PIL import Image, ImageFilter
import imageio
import numpy as np
import streamlit as st
from io import BytesIO
import hashlib

# Function to download and process image
def process_image(img):
    # Edge Detection filter
    edges = img.filter(ImageFilter.FIND_EDGES)

    # Generate unique filenames based on the input image
    image_hash = hashlib.md5(img.tobytes()).hexdigest()
    filtered_filename = f"filtered_{image_hash}.jpg"
    animated_filename = f"animated_{image_hash}.gif"

    # Save the filtered image as jpg
    edges.save(filtered_filename)

    # Generate animated gif
    images = [img, edges]
    imageio.mimsave(animated_filename, [np.array(im) for im in images], duration=1000, loop=0)

    return filtered_filename, animated_filename

# Streamlit App
st.title('Image Filter App')

url = st.text_input('Enter the image URL:', value='https://www.chromethemer.com/google-backgrounds/batman/images/batman-google-chrome-background-0006-tiny.jpg')

uploaded_file = st.file_uploader("Or choose an image...", type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    filtered, animated = process_image(img)
    st.image(filtered, caption='Filtered image')
    st.image(animated, caption='Animated image')
elif url != '':
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    filtered, animated = process_image(img)
    st.image(filtered, caption='Filtered image')
    st.image(animated, caption='Animated image')
