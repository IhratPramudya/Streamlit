import streamlit as st
# Second Page

st.header("""Tentang Machine Learning""")
st.subheader("""Jenis Machine Learning""")
st.caption("""Pembahasan dalam model yang telah di buat ada beberapa metode yang digunakan""")
with st.expander("Supervised Learning"):
    st.write("Supervised Learning adalah salah satu pemebelajaran yang diawasi dari data yang memeiliki label tertentu yang dimana model memepelajari label yang ada")
with st.expander("Unsupervised Learning"):
    st.write("Develop ML Applications in Minutes!!!!")

st.header("""Model Machine Learning""")
st.subheader("""Supervised Learning""")
with st.expander("Naive Bayes"):
    st.write("Supervised Learning adalah salah satu pemebelajaran yang diawasi dari data yang memeiliki label tertentu yang dimana model memepelajari label yang ada")
with st.expander("Unsupervised Learning"):
    st.write("Develop ML Applications in Minutes!!!!")
    
st.subheader("""Unsupervised Learning""")
with st.expander("K-Means"):
    st.write("K-Means merupakan salah satu algoritma yang termasuk dalam unsupervised\
    learning yang bertujuan untuk mengelompokkan data ke dalam beberapa kluster\
    berdasarkan kesamaan atribut tertentu tanpa perlu adanya label kategori sebelumnya")
with st.expander("DBSCAN"):
    st.write("Develop ML Applications in Minutes!!!!")

st.header("""Cara Kerja Algoritma""")
st.subheader("""K-Means""")