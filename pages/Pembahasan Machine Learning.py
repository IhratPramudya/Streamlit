import streamlit as st
import pandas as pd
# Second Page

st.header("""Tentang Machine Learning""")
st.subheader("""Jenis Machine Learning""")
st.caption("""Pembahasan dalam model yang telah di buat ada beberapa metode yang digunakan""")
with st.expander("Supervised Learning"):
    st.write("Supervised learning adalah kategori machine learning yang menggunakan set data berlabel untuk melatih algoritma guna memprediksi hasil dan mengenali pola. ")
with st.expander("Unsupervised Learning"):
    st.write("Unsupervised learning dalam kecerdasan buatan adalah jenis machine learning yang belajar dari data tanpa pengawasan manusia. Tidak seperti supervised learning, model unsupervised machine learning diberi data tidak berlabel dan diizinkan untuk menemukan pola dan insight tanpa panduan atau instruksi eksplisit. ")


st.header("""Apa itu Klusterisasi Dengan K-Means""")
st.subheader("""K-Means""")

st.write("K-Means salah satu metode untuk mengelola data yang bekerja dengan cara mengelompokkan\
    ke dalam kelompok tertentu")
st.write("""Mengapa bisa seperti itu,  *ya!!!!!* :sunglasses:""")

st.write("Misalkan jika kita memiliki 10 data Buah - buahan dimana dari data tersebut ada beberapa jenis\
    contohnya seperti Apel, Mangga, dan jeruk sudah terbayangkan bagimana cara untuk mengelompokkan data tersebut\
        yaitu kita menentukan dari kluster terbaik yang di hasilkan misalkan untuk data yang memiliki jenis\
            terdiri dari 3 buah Apel sedangkan untuk jenis Mangga terdiri dari 5 buah dan jeruk 2 buah kita bisa\
                asumsikan data tersebut terdiri dari 3 kelompok ")
st.write("""Nah apakah sekarang sudah mengerti,  *belum!!!!!* :sunglasses:""")

st.write("Nah tidak sampai di situ ketika kita ingin mengelompokkan buah buahan tersebut kita harus mengetahui\
    titik pusat dari masing masing kelompok buah yang ada. Bagimana tuh? jadi kita memilih salah satu buah yang\
        ada di dalam kelompok jenis seacara acak. jadi kita bisa menghitung jarak antara titik buah tersebut ke semua buah yang\
            ada dan kira kira manakah buah yang paling terdekat dengan nilai centroid. Jika buah yang terdekat\
                dengan centoid kita bisa asumsikan buah tersebut berada di anggota di kluster tersebut")

st.subheader("""Langkah langkah cara kerja Algoritma K-means""")
st.write("""Langkah ini dibuat dengan menggunakan contoh dataset buah-buahan contoh dataset tersebut\
    dapat di lihat di bawah ini.""")

df = pd.read_excel("files/example-fruits-dataset.xlsx", engine="openpyxl")
# defining data in table
df["Ukuran (cm)"].astype(float)

st.dataframe(df)
# st.table(new_dataset)

st.write("1. Langkah pertama yaitu dengan cara menentukan nilai K untuk menemukan kluster yang akan di bentuk.\
    Pilih centroid secara acak dari data yang ada.")

st.write("2. Mengukur atau menghitung jarak setiap data dengan centroid yang sudah di tetapkan dengan menghitung\
    menggunakan rumus Euclidean Distance. Berikut contoh rumus yang di berikan")
st.latex("𝐷𝑒 = √(𝑥𝑖 − 𝑠𝑗)2 + (𝑦𝑖 − 𝑡𝑗)2")

st.write("Penjelasan dari rumus tersebut")
st.write("𝐷𝑒     = Euclidean Distance")
st.write("𝑥𝑖,𝑦𝑖   = item yang ada pada data contoh 𝑥𝑖 = Berat (gram), 𝑦𝑖 = Ukuran (cm)")
st.write("𝑠𝑗,𝑡𝑗   = ini adalah kordinat centroid dari data yang ada dengan memilih secara \
        acak dari 2 kolom 𝑠𝑗 = Berat (gram), 𝑡𝑗 = Ukuran (cm)")
st.write("3. Mengelompokkan setiap item dari dataset yang ada dengan jarak yang paling mendekati\
         kordinat centroid contoh dari keseluruhan data. Manakah ? item data 𝑥𝑖,𝑦𝑖 yang paling mendekati\
         𝑠𝑗,𝑡𝑗 ?")
st.write("4. Memperbarui nilai centroid dari data yang ada. Misalkan jika kita menentukan kluster\
         sebanyak 2 kemudian untuk mendapatkan Nilai centroid tersebut kita bisa menghitung rata rata\
         item data.")
st.write("Contoh pada kluster 1 𝑥𝑖,𝑦𝑖 yang di rata-ratakan mendapatkan centroid 𝑥𝑖 = Berat (gram) = 0.23, \
         𝑦𝑖 = Ukuran (cm) = 7.1, sedangkan untuk kluster 2 mendapatkan nilai 𝑥𝑖,𝑦𝑖 yang di rata-ratakan mendapatkan\
         centroid 𝑥𝑖 = Berat (gram) = 0.1, 𝑦𝑖 = Ukuran (cm) = 2.")

st.latex(r'''
    t_{ij} = \frac{1}{N_i} \sum_{k=0}^{N_i} X_{kj}
''')