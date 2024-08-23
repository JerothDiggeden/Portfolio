import streamlit as st
from PIL import Image, ImageDraw, ImageOps


st.set_page_config(page_title="Data Analysis Portfolio", page_icon=":material/edit:", layout="wide",
				   initial_sidebar_state="expanded")


st.sidebar.markdown(
	"""
	<style>
	.custom-container {
		background-color: white;  /* Set your desired background color */
		font-family: Arial, Helvetica, sans-serif;
		align-items: center;
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
image = Image.open('data/me.png')
radius = 20
rounded_image = add_rounded_corners(image, radius)
st.sidebar.image(rounded_image)
st.sidebar.write("""This is the data analysis & python portfolio of Jeroth Diggeden. I am new to Data Analysis & Python
but am passionate and looking for work in related industries.
""")

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
	col7, col8, col9 = st.columns([1, 6, 1])
	with col8:
		st.page_link('http://18.215.151.200:8501/', label="EPL Statistics")
		image = Image.open('data/epl.png')
		radius = 20
		rounded_image = add_rounded_corners(image, radius)
		st.image(rounded_image)
		st.write('A dynamic and live web app/dashboard developed with python and streamlit, with information and statistics '
				 'about the top 10 English Premier League teams.')

with col2:
	col10, col11, col12 = st.columns([1, 6, 1])
	with col11:
		st.page_link('https://drive.proton.me/urls/7Q8JV0F6J0#CgMZl0WpDspl', label="Chart Generator")
		image = Image.open('data/charts.png')
		radius = 20
		rounded_image = add_rounded_corners(image, radius)
		st.image(rounded_image)
		st.write('A python script to generate Plot, Bar, Pie and Scatter charts from CSV or Excel files.')

with col3:
	col13, col14, col15 = st.columns([1, 6, 1])
	with col14:
		st.page_link('http://54.226.148.170:8501/', label="Podcast Filter")
		image = Image.open('data/jre.png')
		radius = 20
		rounded_image = add_rounded_corners(image, radius)
		st.image(rounded_image)
		st.write('A web app developed with python & streamlit, with user accounts(passwords and user data encrypted), '
				 'to filter the last 300 Joe Rogan Experience podcast episodes by keyword or guest name.')

col4, col5, col6 = st.columns([1, 1, 1])

with col4:
	col16, col17, col18 = st.columns([1, 6, 1])
	with col17:
		st.header('')
		st.page_link('https://drive.proton.me/urls/BH23B0N37W#Hq4XZZD74REF', label="Bucking Bull Sales")
		image = Image.open('data/sales.png')
		radius = 20
		rounded_image = add_rounded_corners(image, radius)
		st.image(rounded_image)
		st.write('An executable file generated from a python script, developed using customtkinter, for Bucking Bull '
				 'to explore data from daily sales reports.')

with col5:
	col19, col20, col21 = st.columns([1, 6, 1])
	with col20:
		st.header('')
		st.page_link('https://github.com/JerothDiggeden/Drinks-Order-GUI', label="Bucking Bull Drinks")
		image = Image.open('data/drinks.png')
		radius = 20
		rounded_image = add_rounded_corners(image, radius)
		st.image(rounded_image)
		st.write('A script developed with python and customtkinter for Bucking Bull to create a pdf file with a drinks '
				 'order based on a drinks count in store.')

with col6:
	col22, col23, col24 = st.columns([1, 6, 1])
	with col23:
		st.header('')
		st.page_link('https://github.com/JerothDiggeden/CSV-XLSX-Cleaner', label="Column Renamer")
		image = Image.open('data/rename.png')
		radius = 20
		rounded_image = add_rounded_corners(image, radius)
		st.image(rounded_image)
		st.write('A command line script developed with python to rename and cleanup CSV and Excel files for processing.')
