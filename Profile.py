import streamlit as st

col1, col2 = st.columns(2)

col2.audio("postmalone.mp3", format="audio/mpeg", loop=True, autoplay=True)
# st.title("Tim Visquad Data Mining")

st.header("""My Biografi""")

#Displaying Plain Text
st.text("Hay,\nsemua\t!!!!!!!!! Nama Saya Ihrat pramudya")
st.text('Selamat Datangg')
st.text("""Di pembahasan kali ini saya telah membangun model Machine Learning yang""")
st.text("""menjadi tugas akhir saya untuk menempuh jalur akhir dalam bidang Ilmu Komputer""")
st.text("""Senang rasanya ada orang yang ingin membaca tulisan saya walapun masih sedikit""")
st.text("""kekurangan tetapi saya merasa bersyukur dengan karunia tuhan Allah saya masih bisa """)
st.text("""diberikan kemampuan untuk menulis dan belajar.""")


st.header("""Team Visquad""")
st.text("""Selain itu saya juga di bantu oleh beberapa teman saya yang mahir dalam bidangnya""")
st.text("""untuk membangun skripsi ini dan saya banyak belajar dari prespektif yang berbeda""")
st.text("""Pengalaman saya dibentuk ketika saya mengikuti pembelajaran di luar kampus""")
st.text("""khususnya Kampus Merdeka yang di rancang oleh mentri kita yaitu bapak Nadiem makarim""")
st.header("""Tentang Machine Learning""")
st.subheader("""Jenis Machine Learning""")
st.caption("""Pembahasan dalam model yang telah di buat ada beberapa metode yang digunakan""")
with st.expander("Supervised Learning"):
    st.write("Supervised Learning adalah salah satu pemebelajaran yang diawasi dari data yang memeiliki label tertentu yang dimana model memepelajari label yang ada")
with st.expander("Unsupervised Learning"):
    st.write("Develop ML Applications in Minutes!!!!")
st.sidebar.radio("Apakah Kamu User Baru", ["Yes", "No"])

st.header("""Model Machine Learning""")
st.subheader("""Supervised Learning""")
with st.expander("Naive Bayes"):
    st.write("Supervised Learning adalah salah satu pemebelajaran yang diawasi dari data yang memeiliki label tertentu yang dimana model memepelajari label yang ada")
with st.expander("Unsupervised Learning"):
    st.write("Develop ML Applications in Minutes!!!!")