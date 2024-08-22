import streamlit as st
from PIL import Image, ImageDraw, ImageOps
from bs4 import BeautifulSoup
from icecream import ic


st.set_page_config(page_title="Data Analysis Portfolio", page_icon=":material/edit:", layout="wide",
                   initial_sidebar_state="expanded")


st.sidebar.markdown(
    """
    <style>
    .custom-container {
        background-color: white;  /* Set your desired background color */
        font-family: Arial, Helvetica, sans-serif;
        h2 {
              color: black;
            }
        h1 {
              color: black;
            }
        p {
              color: black;
            }
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True
)


def add_rounded_corners(image, radius):
	# Create a mask with the same size as the image, filled with 0 (black)
	mask = Image.new('L', image.size, 0)

	# Create a white (255) rounded rectangle on the mask
	draw = ImageDraw.Draw(mask)
	draw.rounded_rectangle([(0, 0), image.size], radius=radius, fill=255)

	# Apply the rounded mask to the image
	rounded_image = ImageOps.fit(image, mask.size, centering=(0.5, 0.5))
	rounded_image.putalpha(mask)

	return rounded_image



st.sidebar.title("Data Analysis Portfolio")
st.sidebar.markdown(
    f"""
					<div class="custom-container">
						<h1 style="text-align: center;"><img src="" style="float:left">
						<p></p>
					</div>
					""", unsafe_allow_html=True
)


st.markdown(
    """
    <style>
    .custom-container {
        background-color: white;  /* Set your desired background color */
        font-family: Arial, Helvetica, sans-serif;
        h2 {
              color: black;
            }
        h1 {
              color: black;
            }
        p {
              color: black;
            }
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True
)

col1, col2, col3 = st.columns([1, 1, 1])

with col1:

    st.header('EPL Statistics')
    image = Image.open('data/epl.png')
    radius = 20
    rounded_image = add_rounded_corners(image, radius)
    st.image(rounded_image)

with col2:
    st.header('Chart Generator')
    image = Image.open('data/plot.png')
    radius = 20
    rounded_image = add_rounded_corners(image, radius)
    st.image(rounded_image)

with col3:
    st.header('Podcast Filter')
    image = Image.open('data/jre.png')
    radius = 20
    rounded_image = add_rounded_corners(image, radius)
    st.image(rounded_image)

col4, col5, col6 = st.columns([1, 1, 1])

with col4:
    st.header('Bucking Bull Sales')
    image = Image.open('data/epl.png')
    radius = 20
    rounded_image = add_rounded_corners(image, radius)
    st.image(rounded_image)

with col5:
    st.header('Bucking Bull Drinks')
    image = Image.open('data/epl.png')
    radius = 20
    rounded_image = add_rounded_corners(image, radius)
    st.image(rounded_image)

with col6:
    st.header('Column Renamer')
    image = Image.open('data/epl.png')
    radius = 20
    rounded_image = add_rounded_corners(image, radius)
    st.image(rounded_image)
