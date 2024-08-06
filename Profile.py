import streamlit as st
import base64

st.sidebar.radio("Apakah Kamu User Baru", ["Yes", "No"])



st.header("""My Biografi""")
st.sidebar.subheader("""Foto Saya""")
# Function to set Image as Background

# Listing out animal images
profil_image = [
    'files/Profile2.png',
]

# Displaying Multiple images with width 150
st.image(profil_image, width=150, output_format = "auto")

collection_image = [
    'files/galaxy.jpg',
    'files/galaxy2.jpg',
    'files/pexels-alex-andrews-271121-816608.jpg',
    'files/pexels-david-kopacz-3259639-4994765.jpg',
    'files/pexels-philippedonn-1257860.jpg',
    'files/pexels-pixabay-73873.jpg',
    'files/pexels-tobiasbjorkli-1819650.jpg',
]

# Displaying Multiple images with width 150
st.sidebar.image(collection_image, width=50, output_format = "auto")

#Displaying Plain Text
st.write("Hello, *Semua!!!!!* :sunglasses:")
st.text('Selamat Datangg')
st.text("""Di pembahasan kali ini saya telah membangun model Machine Learning yang""")
st.text("""menjadi tugas akhir saya untuk menempuh jalur akhir dalam bidang Ilmu Komputer""")
st.text("""Senang rasanya ada orang yang ingin membaca tulisan saya walapun masih sedikit""")
st.text("""kekurangan tetapi saya merasa bersyukur dengan karunia Allah saya masih bisa """)
st.text("""diberikan kemampuan untuk menulis dan belajar.""")


st.header("""Team Visquad""")
st.text("""Selain itu saya juga di bantu oleh beberapa teman saya yang mahir dalam bidangnya""")
st.text("""untuk membangun skripsi ini dan saya banyak belajar dari prespektif yang berbeda""")
st.text("""Pengalaman saya dibentuk ketika saya mengikuti pembelajaran di luar kampus""")
st.text("""khususnya Kampus Merdeka yang di rancang oleh mentri kita yaitu bapak Nadiem makarim""")
