import streamlit as st
import time
# import base64

# st. set_page_config(layout="wide") 

def displayPDF(url):
    # Opening file from file path
    # with open(file, "rb") as f:
    #     base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # # Embedding PDF in HTML
    # pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="100%" height="1000px" type="application/pdf"/>'

    pdf_display = f'<iframe src="{url}" width="1000" height="1000px" style="margin-left: -70px;"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)
    # Displaying File
    # st.markdown(pdf_display, unsafe_allow_html=True)



st.header("""Prediksi Pertanyaan Sidang Skripsi""")

st.write("1. Pertanyaan pertama")
st.write("A. Mengapa kamu mengambil judul penelitian tersebut ?")
st.write("Jawab :")
st.write("- Karena kasus stunting Kab.Batang masih tinggi oleh karena itu kami\
         melakukan pemetaan untuk membantu pemerintah agar mengetahui\
         daerah mana yang perlu diprioritaskan.")
st.write("- Karena sejauh ini belum ada yang melakukan penelitian mengenai\
         klasterisasi tingkat kasus stunting di Kabupaten Batang")
st.write("B. Apa definisi konsep utama dalam penelitian (yang ada di judul) ?")
st.write("Jawab:")
st.write("- Implementasi: Menurut KBBI implementasi yaitu\
         pelaksanaan/penerapan. Dimana arti umum, implementasi merupakan\
         sebuah pelaksanaan/penerapan sebuah rencana untuk mencapai tujuan\
         tertentu")
st.write("- Algoritma : Menurut KBBI, algoritma adalah suatu prosedur sistematis\
         untuk menyelesaikan masalah matematika dalam langkah-langkah\
         terbatas atau urutan pengambilan keputusan yang logis untuk\
         memecahkan masalah tersebut.")
st.write("- Klasterisasi : Adalah pembentukan sesuatu menjadi kluster.\
         Pengelompokkan sesuatu berdasarkan kesamaan, fungsi dan\
         sebagainya.")
st.write("- Stunting : Stunting berasal dari Bahasa inggris yang berarti\
         pengerdilan. Sementara arti kerdil menurut KBBI selalu kecil saja, tidak\
         dapat menjadi besar (tentang orang, binatang, tumbuhan, dan\
         sebagainya) karena kekurangan gizi atau karena keturunan.")
st.write("2. Kenapa penelitian kamu mengambil topik stunting itu ?")
st.write("Jawab :")
st.write("- Karena presentase kasus stunting di Indonesia masih terbilang cukup tinggi.\
         Berdasarkan Survei Status Gizi Indonesia (SSGI) oleh Kementerian\
         Kesehatah Republik Indonesia tahun 2022 presentase kasus stunting di\
         Indonesia adalah 21,6. (website resmi Kemenkes 'Standard WHO terkait \
         prevalensi stunting harus angka kurang dari 20%').")
st.write("3. Kenapa memilih lokasi tersebut ?")
st.write("Jawab :")
st.write("- Karena presentase kasus stunting di Kabupaten Batang tergolong tinggi\
         dengan angka 23,5 persen pada tahun 2022 (SSGI 2022 survei status gizi\
         indonesia). (website resmi Kemenkes 'Standard WHO terkait prevalensi\
         stunting harus di angka kurang dari 20%')")
st.write("4. Penelitian kamu ini termasuk penelitian jenis apa ?")
st.write("Jawab:")
st.write("- Penelitian kami termasuk ke penelitian kuantitatif karena penelitian kami\
         menggunakan data dalam bentuk angka, yang dapat diuji secara statistik.\
         (Pengertian statistik : data berupa angka yang dapat dianalisis untuk\
         mendapatkan informasi dari suatu masalah).")
st.write("5. Manfaat dari penelitian kalian ini apa ?")
st.write("6. Seberapa penting penelitian kalian ini untuk direalisasikan ?")
st.write("Jawab no 5 & 6 :")
st.write("Untuk membantu pemerintahaan dalam merumuskan kebijakan yang lebih\
         efektif tingkat keparahan kasus dan untuk mengetahui skala prioritas untuk\
         penanganan dan pencegahan kasus stunting di Kabupaten Batang.")
st.write("7. Apa hipotesis dari penelitian ini ?")
st.write("Jawab :")
st.write("Penggunaan algoritma K-Means dalam pengklasteran tingkat kasus stunting\
         di Kabupaten Batang akan menghasilkan struktur yang baik dilihat dari\
         Silhouette Score.")
st.write("8. Tujuan teoritis")
st.write("A.1. Kenapa bagian tujuan penelitian terbagi jadi dua tujuan ? teoretis\
         dan praktis ?")
st.write("Jawab :")
st.write("- Alasanya yaitu karena kami ingin mengetahui penelitian ini dari dua sisi\
         yang berbeda, teoritis dan praktis.")
st.write("A.2. Dari kedua sisi itu memang apa yang menjadi\
         pembedanya atau yang membedakan ?")
st.write("Jawab :")
st.write("- Pembedanya dari teoritis adalah kami ingin mengetahui dari proses\
         klasterisasi menggunakan k-means (mengetahui cara kerja, metodenya).\
         Sedangkan pembeda dari analisis penelitian ini dapat digunakan sebagai acuan untuk\
         membantu pemerintah untuk merumuskan kebijakan.")
st.write("B.1. Apa yang ingin kamu ketahui dari proses klasterisasi ?")
st.write("Jawab :")
st.write("- Untuk mengetahui hasil dari klasterisasi menggunakan metode Elbow\
         dan Silhouette Score, apakah sudah menunjukkan kluster dan struktur\
         yang baik.")
st.write("C.1. Mengapa kamu memilih menggunakan parameter stunting dan\
         jumlah balita ?")
st.write("Jawab :")
st.write("- Karena kami ingin mengetahui tingkat kasus stunting pada setiap daerah\
         di Kabupaten Batang.")
st.write("C.2. Mengapa kamu tidak menggunakan parameter selain dari kedua parameter tersebut ?")
st.write("Jawab :")
st.write("- Karena hasil parameter lain tidak sesuai dengan tujuan kami,\
         lalu harus menambahkan proses lagi untuk mengubah data\
         bentuk string menjadi angka.")
st.write("- Karena algoritma K-Means hanya membaca data dalam bentuk angka.")
st.write("C.3. Kenapa parameter persen tidak digunakan ?")
st.write("Jawab :")
st.write("Karena presentase hanya mewakili persentase kasus stunting dari\
         setiap data (baris data).")
st.write("9. Tujuan Praktis")
st.write("Maksud dari kamu menganalisis dan mengidentifikasi tingkat keparahan\
         kasus stunting apa ?")
st.write("Jawab :")
st.write("- Untuk mengetahui daerah mana saja yang perlu diprioritaskan untuk\
         mendapatkan penanganan masalah stunting berdasarkan tingkat kasus\
         stunting kasusnya")
st.write("10. Menurut kamu, apakah hasil dari penelitian kamu sudah mencapai\
         tujuan penelitian ini ?")
st.write("Jawab :")
st.write("Sudah memenuhi. Karena kami jadi mengetahui :")
st.write("- Bagimana proses penggunaan metode algoritma k-means untuk\
         mengelompokkan tingkat keparahan kasus stunting.")
st.write("- Pengelompokkan daerah menjadi 2 kluster berdasarkan tingkat\
         keparahan kasus stunting.")
st.write("11. Tentang Metode/Algoritma")
st.write("A1. Alasan memilih algoritma k-means ?")
st.write("Jawab :")
st.write("Karena metode ini relatif sederhana dan mudah ditetapkan, dapat\
         digunakan untuk dataset dalam jumlah besar dan telah digunakan secara\
         luas untuk menyelesaikan berbagai persoalan komputasi, mampu\
         mengelompokkan data besar dengan sangat cepat.(Ada di dalam jurnal 1379)")

st.button("Tutup Jurnal", type=("primary"))

if st.button("Buka Jurnal 1379.pdf"):
    with st.spinner("Loading Dulu Gais..."):
        time.sleep(3)
    displayPDF("https://coral-kassey-1.tiiny.site")
else:
    st.write("Silahkan Buka Jurnal")
st.write("A2. Dikatakan dari mana kalau penggunaan metode ini relatif mudah ?")
st.write("Jawab :")
st.write("- Karena dibandingkan dengan metode klusterisasi lainnya,\
         algoritma k-means ccukup menentukan nilai K dan nilai centroid.")
st.write("- Kami melakukan riset mengenai metode lain yaitu DBSCAN.\
         DBSCCAN butuh menentukan feature (variable), nilai epsilon,\
         min_samples")

st.write("B1. Centroid itu apa ?")
st.write("Jawab: ")
st.write("- Centroid merupakan nilai pusat (center) dari sebuah kluster")
st.write("B2. Apa itu Euclidean distance ?")
st.write("Jawab :")
st.write("- Euclidean distance digunakan untuk menghitung jarak ukur antara dua\
         titik dengan menghitung akar kuadrat dari jumlah selisih kuadrat antara\
         keduanya.")
st.header("BAB I")
st.subheader("12. State of The Art")
st.write("A. Dari penelitian terdahulu apa yang membedakan parameter yang\
         digunakan dengan penelitian kamu ?")
st.write("Jawab :")
st.write("Parameter yang penelitian ini gunakan hanya Jumlah balita dan stunting sementara")
st.write("1. Cytry, 2023 =")
st.write("- (A), Jumlah keluarga yang memiliki bayi dibawah dua tahun")
st.write("- (B), Jumlah keluarga yang memiliki bayi dibawah lima tahun")
st.write("- (C), Jumlah keluarga yang memiliki ibu hamil")
st.write("- (D), Jumlah keluarga dengan sanitasi tidak layak")
st.write("- (E), Jumlah keluarga dengan sumber air tidak layak.")
st.write("2. Handayani, 2023 =")
st.write("- Rating pengeluaran tahunan (yearly expense rating)")
st.write("- Pendapatan tahunan (yearly salary)")
st.write("3. Indra, 2023 =")
st.write("- X1, Persentase anak usia 12-23 bulan yang mendapatkan\
imunisasi dasar lengkap.")
st.write("- X2, Proporsi stunting (TB/U) pada balita.")
st.write("- X5, Cakupan bayi baru lahir yang mendapat inisiasi menyusui\
dini.")
st.write("- X6, Cakupan pemberian kapsul vitamin A.")
st.write("- X7, Cakupan pemberian tablet tambah darah.")
st.write("- X8, Persentase rumah tangga dengan akses terhadap sanitasi\
yang layak.")
st.write("- X9, Persentase rumah tangga dengan akses terhadap air\
minum yang layak.")
st.write("Variabel yang tidak digunakan :")
st.write("- X3, Persentase rerata balita umur 6-59 bulan ditimbang\
perbulan.")
st.write("- X4, Cakupan imunisasi dasar lengkap.")
st.write("B. Apa kelebihan penelitian kamu dibandingkan penelitian terdahulu ?")

st.write("B. Apa kelebihan penelitian kamu dibandingkan penelitian terdahulu\
?")
st.write("Jawab: ")
st.write("• Cyntry (Jurnal 1)")
st.write("Penelitian cyntry memiliki memiliki kekurangan karena tidak\
menggunakan metode untuk validasi nilai k (karena tidak\
tercantum pada jurnal). Sedangkan penelitian kami\
menggunakan metode silhouette score dan elbow method untuk\
mencari dan validasi nilai k.")
st.write("• Handayani (Jurnal 2) / (Referensi/dasar penelitian)\
Hasil yang didapatkan penelitian ini menunjukan bahwa k-\
means memiliki performa klasterisasi yang kuat. (bukan\
perbandingan tapi dasar penelitian)")
st.write("• Indra (Jurnal 3) / (Referensi/dasar penelitian)\
Penelitian indra silhouette score = 0.48 (Variabel yang\
digunakan pada indra lebih banyak), penelitian kami silhouette\
score = 0,6083.")
st.write("13. Metodologi Penelitian")
st.write("A. Metode apa yang saudara gunakan ?")

st.write("Jawab:")
st.write("• K-Means = melakukan klasterisasi.")
st.write("• Boxplot = merupakan metode pelengkap untuk membantu\
         proses penelitian ini dalam menghilangkan nilai outlier.")
st.write("• Elbow Method = menentukan banyak nilai k")
st.write("• Silhouette Score = menentukan banyak nilai k, dan validasi nilai\
k.")

st.write("B. Mengapa menggunakan metode tersebut ?")
st.write("Jawab:")

st.write("• K-Means = karena metode ini relatif sederhana dan mudah\
diterapkan, dapat digunakan untuk dataset dalam jumlah besar\
dan telah digunakan secara luas untuk menyelesaikan berbagai\
persoalan komputasi, mampu mengelompokkan data besardengan sangat cepat (jurnal kode 1379). Salah satu penguat\
menggunakan metode ini dari jurnal penelitian terdahulu ke 2\
(Handayani) dan jurnal 3 (Indra).")


st.write("• Boxplot = Karena penggunaan boxplot menghasilkan hasil\
silhouette visualizer yang lebih baik (Buktikan perbandingan\
antara pake boxplot dan tidak)")
st.write("• Silhouette score = untuk menentukan nilai k dan validasi nilai k.")
st.write("• Elbow method = untuk menentukan nilai k.")

st.write("14. Penelitian anda menggunakan data primer atau sekunder ?")
st.write("Jawab:")
st.write("Sekunder, karena data yang didapatkan berasal dari pihak lain, bersifat publik\
dari website resmi Satu Data Indonesia.")
st.write("15. Apa teknik pengumpulan data yang digunakan ?")
st.write("Jawab:")
st.write("Teknik yang kami lakukan untuk pengumpulan data yaitu observasi daring,\
dimana kami melakukan riset secara daring ke laman resmi Satu Data\
Indonesia.")
st.write("16. Apa arti unsupervised learning ?")
st.write("Jawab:")
st.write("Teknik dalam machine learning dimana algoritma menentukan/menemukan\
pola dan strukturnya sendiri dalam data yang tidak berlabel.")
st.write("17. Apa perbedaan supervised learning dan unsupervised learning ?")
st.write("Jawab:")

st.write("• Supervised memiliki label/kelas sedangkan unsupervised tidak memiliki label/kelas.")
st.write("• Supervised memiliki tujuan prediksi dan klasifikasi sedangkan\
unsupervised tidak memiliki tujuan prediksi yang spesifik, namun lebih\
ke eksplorasi dan pemahaman data.")
st.write("• Supervised mengidentifikasi pola memerlukan bantuan eksternal\
         seperti label/kelas, sedangkan unsupervised tanpa bantuan eksternal.")

st.write("18. Apa pengertian rumus Sum of Square Error (SSE) ?")

st.write("Jawab:")

st.write("SSE adalah sebuah persamaan yang digunakan untuk mengukur perbedaan\
dari nilai antar jumlah klaster atau selisih antara nilai yang diamati dan nilai\
prediksi.")

st.write("19. Pengertian Box plot ?")
st.write("Jawab:")

st.write("Box plot adalah cara standar untuk menampilkan distribusi data berdasarkan\
lima ringkasan angka: nilai minimum (batas nilai ekstrem bawah), kuartil\
pertama (Q1), median (Q2), kuartil ketiga (Q3), dan nilai maksimum (batas\
nilai ekstrem atas).")

st.write("BAB III")

st.write("20. Bagaimana hasil penelitian saudara ?")
st.write("Jawab:")

st.write("Berdasarkan hasil analisis klasterisasi, pengelompokkan yang optimal berada\
pada nilai k = 2, ditunjukkan dengan nilai Silhouette Coefficient sebesar\
0,60830 yang berarti struktur yang dihasilkan baik, dengan kluster 0\
berjumlah 170 desa atau kelurahan yang tergolong tingkat kasus stunting\
sedang dan kluster 1 berjumlah 68 desa atau kelurahan yang tergolong\
tingkat kasus stunting tinggi.")

st.write("21. Apa itu data oulier ?")

st.write("Jawab:")

st.write("Data ourlier adalah nilai yang jauh berbeda dari nilai lainnya dalam kumpulan\
data. (penyebab: kesalahan pengukuran, variasi alami, kejadian langka, atau\
karena faktor lain yang tidak terduga.).")

st.write("22. Apa itu threshold ?")

st.write("Jawab:")

st.write("Threshold adalah nilai ambang batas yang diterapkan sebagai standar dalam")

st.write("melakukan analisis data.23. Kenapa kamu menentukan nilai threshold sebesar 360 ?")

st.write("Jawab:")

st.write("Karena dilihat pada boxplot awal, gambar boxplot menunjukan pada nilai\
sekitar 360, sudah tidak terdapat outlier.")

st.write("24. Apa yang dimaksud jangkauan interkuartil ?")

st.write("Jawab:")

st.write("Jangkauan interkuartil adalah jarak atau selisih antara kuartil bawah (Q1) dan\
kuartil atas (Q3).")

st.write("25. Apa yang dimaksud scatter plot ?")

st.write("Jawab:")

st.write("Scatter plot adalah jenis grafik yang digunakan dalam statistik dan analisis\
data untuk menampilkan serta menganalisis hubungan antara dua variabel\
numerik.")

st.write("26. Kenapa ada copy-an baru dataframe yaitu “stunting_process”, untuk\
apa ?")

st.write("Jawab:")

st.write("Dibuat supaya dataframe utamanya tidak diubah, karena proses elbow\
method dan silhouette score, kolom yang tipe datanya string harus di drop,\
sementara kolom tersebut diperlukan untuk mengetahui anggota tiap\
klusternya dibagian akhir nanti.")

st.write("27. Kenapa kamu bisa menentukan kalau cluster 0 itu kasus stunting\
sedang, dan cluster 1 itu kasus stunting tinggi ? (PENTING BGT)")

st.write("Jawab:")

st.write("Karena dilihat dari hasil rata-rata kasus stunting disetiap clusternya pada\
dataframe agregasi data.")

st.write("28. Hasil analisis penelitian")

st.write("A. Alasan kamu pakai hasil analisis di akhir bab 3 kenapa ?")

st.write("Jawab:")

st.write("Untuk menyimpulkan hasil dari penelitian kami di bab 3")


st.write("B. Apa bedanya dengan kesimpulan ?")

st.write("Jawab:")

st.write("Pembedanya kalau kesimpulan itu berdasarkan hasil dari keseluruhan\
dan menjawab dari tujuan penelitian.")

st.write("BAB IV")
st.write("29. Apakah kesimpulan yang kamu berikan sudah menjawab tujuan\
penelitian kamu ? (hubungan antara masalah, tujuan penelitian dan\
kesimpulan)")
st.write("Jawab: Sudah menjawab. (kesimpulan no 1-3 untuk tujuan teoritis, no 4-5\
untuk tujuan praktis)")
st.write("30. Apa alasan kamu memberikan saran untuk menggunakan algoritma k-\
medoids, DBSCAN? (harus memberikan alasan serta hasilnya juga) ?")
st.write("Jawab:")
st.write("A. DBSCAN")
st.write("• DBSCAN Tahan terhadap outlier.")
st.write("• DBSCAN Tidak perlu menentukan nilai cluster terlebih dahulu.")
st.write("• Bisa menentukan cluster secara otomatis.")
st.write("B. K-Medoids")
st.write("• K-Medoids tahan terhadap outlier")
st.write("31. Apa alasan kamu memberikan saran untuk menggunakan tools yang\
berbeda seperti pada penelitian? (harus memberikan alasan serta\
hasilnya juga)")


st.write("Jawab:")
st.write("• Supaya lebih memudahkan proses penelitian pada penelitian\
selanjutnya.")
st.write("• Untuk membandingkan hasil dari penelitian menggunakan tools lainnya.\
PERTANYAAN TAMBAHAN")
st.write("1. Apa rumusan masalah dari penelitian kamu ? (buat lebih terperinci\
masalahnya berdasarkan tujuan penelitian)")
st.write("Jawab:")
st.write("A. Teoritis")
st.write("• Bagaimana proses klasterisasi tingkat kasus stunting di Kabupaten\
Batang menggunakan algoritma k-means?")
st.write("• Apakah data outlier mempengaruhi hasil klasterisasi menggunakan\
algoritma k-means ? (Dapat mempengaruhi, karena algoritma k-means\
sensitif terhadap outlier *jika ditanya jawabannya*)B. Praktis")
st.write("• Bagaimana hasil pemetaan tingkat kasus stunting pada setiap daerah\
di Kabupaten Batang ?")
st.write("2. Selain penggunaan boxplot, metode apa saja yang dapat mengatasi data\
outlier ?")
st.write("Jawab:")
st.write("Ada beberapa metode yang bisa digunakan :")

st.write("• Standar scaler")
st.write("• Min Max scaler")
st.write("• Boxplot IQR (interkuartil).")
st.write("3. Apa Batasan masalah dari penelitian kamu ?")
st.write("Jawab:")
st.write("• Data yang diolah merupakan data sekunder yaitu Jumlah Balita\
Stunting Per Desa pada periode Desember 2023.")

st.write("• Pengambilan data didapatkan dari laman resmi Satu Data Indonesia")
st.write("• Pengujian hasil klasterisasi data menggunakan bahasa pemrograman\
python untuk mendapatkan hasil yang baik.")




