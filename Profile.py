import streamlit as st
import base64

st.sidebar.radio("Apakah Kamu User Baru", ["Yes", "No"])



st.header("""Biografi""")
st.sidebar.subheader("""Foto Saya""")
# Function to set Image as Background

# Listing out animal images

col1,col2,col3=st.columns([2,2,2])

with col1:
    st.image('files/WhatsApp Image 2024-07-03 at 08.52.21_62e4c07a.jpg',width=100,use_column_width='never')
with col2:
    st.image('files/image.png',width=100,use_column_width='never')
with col3:
    st.image('files/vivien.png',width=100,use_column_width='never')

# Displaying Multiple images with width 150
# Displaying Multiple images with width 150

#Displaying Plain Text

st.header("""Team Visquad""")
st.text("""Selain itu saya juga di bantu oleh beberapa teman saya yang mahir dalam bidangnya""")
st.text("""untuk membangun skripsi ini dan saya banyak belajar dari prespektif yang berbeda""")
st.text("""Pengalaman saya dibentuk ketika saya mengikuti pembelajaran di luar kampus""")
st.text("""khususnya Kampus Merdeka yang di rancang oleh mentri kita yaitu bapak Nadiem makarim""")
