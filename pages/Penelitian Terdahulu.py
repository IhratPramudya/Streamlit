import streamlit as st

st.write("BEDAH PENELITIAN TERDAHULU")
st.write("JURNAL 1 (Cytry, Kode 1120)")
st.write("Judul : Penerapan Metode K-Means dalam Klasterisasi Status Desa terhadap Keluarga Beresiko Stunting")

st.write("Latar Belakang :")

st.write("Stunting kini telah menjadi isu nasional dan menjadi perhatian khusus bagi\
pemerintah untuk mengatasi resiko yang ditimbulkan, salah satu pencegahan yang\
dapat dilakukan pemerintah yaitu memberikan intervensi terhadap keluarga yang\
beresiko stunting.")

st.write("Tujuan :")

st.write("• Melakukan analisis kluster terhadap kelurahan atapun desa yang beresiko\
stunting.")
st.write("• Penelitian ini dapat berkontribusi untuk membantu pemerintah atau\
stakeholder dalam pemberian intervensi terhadap penyebaran resiko stunting")
st.write("Metodologi :")

st.write("• Dataset : Pendataan keluarga tahun 2022 di Kelurahan/desa Kota Pariaman.")
st.write("• Tools = RapidMiner")
st.write("• Algoritma K-means, 3 kluster (tinggi, sedang, rendah)")
st.write("• Metode menghitung jarak = Euclidean Distance")
st.write("Hasil Pembahasan :")

st.write("• Proses iterasi dilakukan dari iterasi kedua sampai iterasi sembilan,\
perhitungan iterasi dihentikan karena posisi kluster tidak berubah.")

st.write("• Kluster data yang dihasilkan yaitu kelurahan desa dengan resiko stunting\
rendah memiliki 32 data,kelurahan desa dengan resiko stunting sedang\
memiliki 36 data, dan kelurahan desa dengan resiko stunting tinggi memiliki 3")

st.write("data.Kesimpulan :")
st.write("Penentuan resiko stunting mendapatkan hasil keluaran yang cukup baik,\
menghasilkan informasi yang dapat dijadikan pengetahuan baru dalam bentuk\
knowledge based system, dan dapat digunakan oleh pemerintah untuk\
mengoptimalkan pemberian intervensi terhadap kelurahan desa yang beresiko\
stunting.")

st.write("Saran : Tidak ada")
st.write("JURNAL 2 (Handayani, Kode 2770-7854-1-PB)")
st.write("Judul : Performance Analysis Of Clustering Models Based On Machine Learning In\
Stunting Data Mapping (Analisis Kinerja Model Clustering Berbasis Machine\
Learning Pada Pemetaan Data Stunting)")

st.write("Latar Belakang :")

st.write("Pada lokasi penelitian yaitu Kabupaten Asahan, pemetaan daerah rawan\
peningkatan angka stunting belum dilakukan dengan optimal. Proses eksplorasi\
gudang data stunting ini berguna untuk menambah informasi yang dapat membantu\
pemerintah dalam mengambil kebijakan.")

st.write("Tujuan :")
st.write("Penelitian ini bertujuan melakukan pemetaan daerah rawan stunting di Kabupaten\
Asahan berdasarkan jumlah kasus stunting")
st.write("Metodologi :")

st.write("• Dataset : Dataset Private")
st.write("• Tools : Python")
st.write("• Metode :")
st.write("✓ K-Means (Melakukan klasterisasi)")
st.write("✓ Elbow Method (Menentukan nilai K yang terbaik)")
st.write("✓ Silhouette Score (Mengevaluasi hasil klasterisasi)")
st.write("✓ DBI (Davies-Bouldin Index) (Mengevaluasi hasil klasterisasi)")
st.write("✓ Normalisasi (Min-Max normalization) (normalisasi data)")
st.write("Menghitung jarak data ke pusat kluster (centroid):✓ Euclidean distance")
st.write("✓ Manhattan distance")
st.write("✓ Minkowski distance")
st.write("Pembahasan dan kesimpulan :")
st.write("")
st.write("Berdasarkan ketiga proses analisis yang dilakukan, yang hasilnya ditunjukkan pada\
tabel 2 di atas, dapat disimpulkan bahwa cluster terbaik yang dihasilkan adalah\
cluster 2 yang menunjukkan hasil pemetaan ke dalam 2 kelompok dengan DBI\
sebesar 0,51290 dan silhouette_score sebesar 0,71432.")

st.write("Saran : Tidak ada")
st.write("JURNAL 3 (Indra, Kode 3612-9412-1-PB)")
st.write("Judul : Perbandingan K-Means dan Hierarchical Clustering dalam Pengelompokan\
Daerah Beresiko Stunting")
st.write("Latar Belakang :")
st.write("Angka prevalensi di Indonesia masih berada pada kisaran 21.6%, sedangkan who\
menetapkan prevalensi stunting maksimal 20%. pemerintah dan pihak terkait telah\
melakukan berbagai upaya dan program intervensi, salah satunya adalah\
menentukan daerah yang menjadi prioritas penanganan stunting dengan melakukan\
klasterisasi.")
st.write("Tujuan :")
st.write("Penelitian ini bertujuan untuk membandingkan antara kluster yang terbentuk\
menggunakan Hierarchical Clustering dan K-Means.")
st.write("Metodologi :")

st.write("• Dataset : Hasil survey status gizi Indonesia (SSGI) tahun 2021.")
st.write("• Tools : Tidak dicantumkan")
st.write("• Metode/Algoritma :")
st.write("✓ K-Means")
st.write("✓ Hierarchical Clustering")
st.write("Matriks Evaluasi :✓ Silhouette Coefficient")

st.write("✓ Calinski-Harabasz Index")
st.write("✓ DBI (Davies-Bouldin Index)")
st.write("Hasil Pembahasan :")
st.write("Hasil perbandingan metode K-Means dan Hierarchical Clustering, diperoleh bahwa\
K-Means menghasilkan pengelompokan klaster yang lebih baik ditinjau dari nilai\
Silhouette Coefficient sebesar 0.48 dan Calinski-Harabasz index sebesar 10.49\
dengan jumlah klaster yang terbentuk sebanyak 2 klaster. Pada Algoritma\
Hierarchical Clustering, nilai Silhouette Coefficient yang dihasilkan adalah 0.47 dan\
Calinski-Harabasz index sebesar 9.54. dengan jumlah kluster 3.")
st.write("Kesimpulan :")
st.write("Daerah-daerah yang berada pada kluster kedua yaitu Provinsi Papua dan Papua\
Barat merupakan daerah dengan resiko stunting yang tinggi")

st.write("Saran :")

st.write("Penelitian dapat dikembangkan dengan menggunakan data dengan cakupan yang\
lebih spesifik seperti data per kabupaten untuk masing-masing provinsi di Indonesia\
serta menambahkan parameter-parameter lain yang berkaitan dengan stunting.")
