import requests
from PIL import Image, ImageFilter
import imageio
import numpy as np
import streamlit as st
from io import BytesIO

# Function to download and process image
@st.cache_data(allow_output_mutation=True)
def process_image(img):
    # Edge Detection filter
    edges = img.filter(ImageFilter.FIND_EDGES)

    # Save the filtered image as jpg
    edges.save("filtered.jpg")

    # Generate animated gif
    images = [img, edges]
    imageio.mimsave('animated.gif', [np.array(im) for im in images], duration=1000, loop=0)

    return "filtered.jpg", "animated.gif"

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
