# Import Streamlit library
import streamlit as st

# Displaying Python Code
st. set_page_config(layout="wide") 

st.header("""IMPORT LIBRARY""")
code = '''
    import pandas as pd
    import matplotlib.pyplot as plt
    import plotly.express as px
    import seaborn as sns
    from sklearn.metrics import silhouette_score
    from sklearn.cluster import KMeans
    from yellowbrick.cluster import SilhouetteVisualizer
'''
st.code(code, language='python')
st.subheader("Penjelasan kode dari library yang digunakan")
st.write("Pandas (import pandas as pd):\
Pandas adalah library Python yang digunakan untuk manipulasi dan analisis data. Dengan Pandas, data dapat diorganisasikan dalam bentuk struktur data seperti Series dan DataFrame, yang memungkinkan operasi seperti penggabungan, pemfilteran, dan agregasi data secara efisien.")

st.write("Matplotlib (import matplotlib.pyplot as plt):\
Matplotlib adalah library visualisasi data yang memberikan antarmuka untuk membuat berbagai macam grafik dan plot. pyplot adalah sub-modul dari Matplotlib yang menyediakan fungsi untuk membuat grafik secara interaktif dan statis, seperti garis, batang, histogram, dan scatter plot.")

st.write("Plotly (import plotly.express as px):\
Plotly adalah library visualisasi interaktif yang mendukung visualisasi data kompleks dan dinamis. plotly.express adalah modul yang menyederhanakan pembuatan grafik dengan cara yang lebih langsung dan intuitif, mendukung berbagai jenis visualisasi seperti scatter plot, line chart, dan bar chart, yang dapat dengan mudah diekspor atau diintegrasikan ke dalam aplikasi web.")

st.write("Seaborn (import seaborn as sns):\
Seaborn adalah library visualisasi statistik yang dibangun di atas Matplotlib dan dirancang untuk membuat visualisasi yang lebih informatif dan menarik secara estetika. Seaborn memudahkan pembuatan plot kompleks seperti heatmap, boxplot, dan pairplot, serta secara otomatis menangani agregasi data dan tampilan statistik.")

st.write("Sklearn (from sklearn.metrics import silhouette_score):\
Scikit-learn (sering disingkat sklearn) adalah library Python untuk machine learning dan analisis data. silhouette_score adalah fungsi dari modul metrics yang digunakan untuk mengevaluasi kualitas cluster dalam algoritma clustering. Nilai silhouette score memberikan gambaran seberapa baik objek dalam satu cluster dibandingkan dengan objek di cluster lainnya.")

st.write("KMeans (from sklearn.cluster import KMeans):\
KMeans adalah algoritma clustering dari Scikit-learn yang digunakan untuk membagi data ke dalam k kelompok (cluster) berdasarkan karakteristiknya. Algoritma ini berusaha meminimalkan jarak intra-cluster dan memaksimalkan jarak inter-cluster untuk mengelompokkan data secara efektif.")

st.write("Yellowbrick (from yellowbrick.cluster import SilhouetteVisualizer):\
Yellowbrick adalah library visualisasi untuk evaluasi model machine learning. SilhouetteVisualizer adalah alat yang digunakan untuk memvisualisasikan skor silhouette, yang membantu dalam menilai kualitas cluster yang dihasilkan oleh algoritma clustering seperti KMeans. Visualisasi ini memudahkan pemahaman tentang seberapa baik data dikelompokkan dalam setiap cluster.")


st.header("PENGUMPULAN DATA")
code = '''
    # #mouting ke google drive
    from google.colab import drive
    drive.mount('/content/drive')
'''

st.code(code, language='python')

st.write("Kode yang kamu berikan adalah skrip Python yang digunakan di Google Colab untuk menghubungkan atau 'mount' Google Drive ke dalam lingkungan Google Colab. Berikut penjelasannya secara ilmiah namun sederhana:")

st.write("Google Colab adalah layanan berbasis cloud yang memungkinkan kamu menjalankan kode Python di server Google. Ini sering digunakan untuk analisis data, machine learning, dan pengolahan teks.")

st.write("Google Drive adalah layanan penyimpanan file online dari Google yang memungkinkan kamu menyimpan dan mengakses file secara cloud.")

st.write("Kode from google.colab import drive:")

st.write("Ini adalah perintah untuk mengimpor modul drive dari library google.colab. Modul ini berisi fungsi-fungsi yang memungkinkan kamu untuk berinteraksi dengan Google Drive dari dalam notebook Colab.\
Kode drive.mount('/content/drive'):")
st.write("Fungsi drive.mount() digunakan untuk menghubungkan Google Drive kamu ke lingkungan Google Colab.\
Path '/content/drive' adalah lokasi di mana Google Drive akan 'dipasang' (mounted) di dalam sistem file Colab. Setelah di-mount, kamu bisa mengakses file di Google Drive seolah-olah mereka ada di direktori lokal di server Colab.")



code = '''
    #extract dataset ke dalam dataframe
    #raw_stunting = pd.read_excel('data-stunting.xlsx') #lokasi dataset di lokal
    raw_stunting = pd.read_excel('drive/MyDrive/TA (visquad)/Balita Stunting/Data/data-stunting.xlsx') #lokasi dataset di google drive
    raw_stunting
'''


st.code(code, language='python')
st.write("Kode diatas berfungsi untuk mengimpor dataset tentang stunting pada balita dari file Excel yang disimpan di Google Drive. Data tersebut kemudian dimuat ke dalam DataFrame Pandas (raw_stunting), yang memungkinkan pengguna untuk melakukan analisis dan manipulasi data lebih lanjut menggunakan berbagai fungsi Pandas.")

code = '''
    #memeriksa data null
    raw_stunting.isnull().sum()
'''
st.code(code, language='python')
st.write("Kode raw_stunting.isnull().sum() adalah alat yang efisien untuk mengidentifikasi dan menghitung missing values dalam dataset. Ini adalah langkah awal yang penting dalam analisis data yang memastikan bahwa data yang digunakan lengkap dan siap untuk diproses lebih lanjut.")

code = '''
    #informasi statistik dataset
    raw_stunting.describe()
'''
st.code(code, language='python')
st.write("Kode raw_stunting.describe() memberikan ringkasan statistik dasar dari kolom-kolom numerik dalam DataFrame raw_stunting. Ringkasan ini mencakup jumlah data (count), rata-rata (mean), simpangan baku (std), nilai minimum (min), nilai maksimum (max), serta persentil (25%, 50%, 75%).")
code = '''
    #menampilkan scatter plot dataframe awal
    plt.figure(figsize=[12, 8])
    fig = px.scatter(raw_stunting, x="jumlah_balita", y="stunting", title="Scatter Plot Dataframe Awal")
    fig.show()
'''

st.code(code, language='python')
st.subheader("Penjelasan Kode :")
st.write("plt.figure(figsize=[12, 8]): Mengatur ukuran figur plot yang akan dibuat menggunakan Matplotlib dengan lebar 12 dan tinggi 8 inci.")
st.write("fig = px.scatter(raw_stunting, x='jumlah_balita', y='stunting', title='Scatter Plot Dataframe Awal'): Menggunakan Plotly Express untuk membuat scatter plot, di mana setiap titik pada plot merepresentasikan pasangan data jumlah_balita dan stunting. title menambahkan judul pada plot.")
st.write("fig.show(): Menampilkan scatter plot yang telah dibuat.")


st.subheader("PENENTUAN VARIABLE")

code = '''
    #mengecek dan menghapus data outlier dengan box plot
    def removal_box_plot(df, column, threshold):
        sns.boxplot(df[column])
        plt.title(f'Original Box Plot of {column}')
        plt.show()

        removed_outliers = df[df[column] <= threshold]

        sns.boxplot(removed_outliers[column])
        plt.title(f'Box Plot without Outliers of {column}')
        plt.show()
        return removed_outliers

    threshold_value = 360
    no_outliers_data = removal_box_plot(raw_stunting, 'jumlah_balita', threshold_value) #kolom jumlah_balita
'''

st.code(code, language='python')

st.write("Kode tersebut membuat fungsi untuk mengidentifikasi dan menghapus outlier dari suatu kolom pada DataFrame menggunakan box plot. Pertama, box plot asli ditampilkan untuk memperlihatkan distribusi data dan outliernya. Kemudian, data yang melebihi nilai ambang batas (threshold) dihapus, dan box plot baru ditampilkan untuk memperlihatkan distribusi data tanpa outlier. Akhirnya, fungsi ini mengembalikan DataFrame yang telah dibersihkan dari outlier.")

code = '''
    #membuat dataframe baru setelah menghapus data outlier
    new_stunting = no_outliers_data.copy()
    new_stunting
'''

st.code(code, language='python')

st.write("Kode tersebut digunakan untuk membuat salinan dari DataFrame yang telah dibersihkan dari outlier. Berikut penjelasannya:")

st.write("no_outliers_data.copy(): Membuat salinan dari DataFrame no_outliers_data, yang merupakan data asli yang sudah dihapus outliernya.\
new_stunting: Menyimpan salinan tersebut ke dalam variabel new_stunting, sehingga perubahan lebih lanjut pada new_stunting tidak akan memengaruhi DataFrame asli no_outliers_data.\
Dengan melakukan ini, kamu memiliki DataFrame baru (new_stunting) yang berisi data yang sudah bebas dari outlier dan siap digunakan untuk analisis lebih lanjut.")


code = '''
    #menampilkan scatter plot setelah menghapus data outlier
    plt.figure(figsize=[12, 8])
    fig = px.scatter(new_stunting, x="jumlah_balita", y="stunting", title="Scatter Plot Tanpa Data Outlier")
    fig.show()
'''

st.code(code, language='python')

st.subheader("Penjelasan kode di atas")

st.write("Kode tersebut digunakan untuk membuat dan menampilkan scatter plot (grafik sebar) dari data yang telah dibersihkan dari outlier. Berikut penjelasan ilmiahnya:")

st.write("plt.figure(figsize=[12, 8]):")

st.write("Ini menetapkan ukuran figure atau kanvas untuk plot. Ukuran yang ditetapkan adalah 12 inci lebar dan 8 inci tinggi. Meskipun plt.figure() digunakan di sini, sebenarnya tidak langsung memengaruhi plotly yang digunakan untuk membuat scatter plot, tetapi bisa membantu dalam mengatur konteks visual jika menggunakan matplotlib.\
fig = px.scatter(new_stunting, x='jumlah_balita', y='stunting', title='Scatter Plot Tanpa Data Outlier'):")

st.write("px.scatter adalah fungsi dari library Plotly Express (px) yang digunakan untuk membuat scatter plot.\
new_stunting: DataFrame yang digunakan untuk plot, yang sudah dibersihkan dari outlier.\
x='jumlah_balita' dan y='stunting': Menentukan sumbu x dan sumbu y untuk scatter plot. Dalam hal ini, 'jumlah_balita' diplot di sumbu x dan 'stunting' di sumbu y.\
title='Scatter Plot Tanpa Data Outlier': Menambahkan judul ke scatter plot untuk memberikan konteks bahwa plot ini tidak mengandung data outlier.\
fig.show():")

st.write("Ini adalah perintah untuk menampilkan scatter plot yang telah dibuat. Plotly menghasilkan plot interaktif, sehingga hasilnya dapat di-zoom, disorot, atau dipindahkan.")



code = '''
    #membuat dataframe khusus untuk pengolahan data
    stunting_process = new_stunting.copy()
    stunting_process
'''

st.code(code, language='python')

st.subheader("Penjelasan kode di atas")
st.write("1. Membuat Salinan Data:")
st.write("stunting_process = new_stunting.copy(): Kode ini membuat salinan dari DataFrame new_stunting dan menyimpannya dalam variabel baru bernama stunting_process.\
Mengapa Disalin?: Dengan membuat salinan, Anda bisa melakukan berbagai pengolahan atau perubahan pada stunting_process tanpa mengubah data asli di new_stunting. Ini berguna agar data asli tetap aman dan tidak terpengaruh oleh perubahan yang Anda lakukan.")

st.write("2. Menampilkan Data:")

st.write("stunting_process: Ketika Anda memanggil variabel ini, data yang ada di dalam stunting_process akan ditampilkan. Anda bisa melihat isinya untuk memastikan data sudah siap untuk diolah lebih lanjut.")
st.write("3. Manfaatnya:")
st.write("Keamanan Data: Data asli tetap utuh dan tidak berubah.\
Fleksibilitas: Anda bebas melakukan modifikasi pada salinan data untuk keperluan analisis atau pengolahan lebih lanjut.")



code = '''
    #drop kolom yang tidak digunakan
    drop_column = ['puskesmas', 'desa_kelurahan', 'persen']
    stunting_process.drop(drop_column, inplace=True, axis=1)
    stunting_process
'''

st.code(code, language='python')
st.subheader("Penjelasan kode di atas")
st.write("1. Menentukan Kolom yang Akan Dihapus:")
st.write("- drop_column = ['puskesmas', 'desa_kelurahan', 'persen']:")

st.write("- Anda membuat daftar berisi nama-nama kolom yang ingin dihapus dari DataFrame. Dalam hal ini, kolom puskesmas, desa_kelurahan, dan persen dipilih untuk dihapus karena mungkin tidak diperlukan untuk analisis lebih lanjut.")

st.write("2. Menghapus Kolom dari DataFrame:")
st.write("- stunting_process.drop(drop_column, inplace=True, axis=1):")
st.write("- drop(): Fungsi ini digunakan untuk menghapus baris atau kolom dari DataFrame.")
st.write("- drop_column: Ini adalah daftar kolom yang Anda tentukan sebelumnya untuk dihapus.")
st.write("- inplace=True: Argumen ini memastikan bahwa perubahan dilakukan langsung pada DataFrame stunting_process, tanpa perlu membuat salinan baru. Jika inplace=False, DataFrame asli tidak akan berubah, dan Anda perlu menyimpan hasilnya ke dalam variabel baru.")

st.write("- axis=1: Ini menunjukkan bahwa Anda ingin menghapus kolom (bukan baris). Dalam Pandas, axis=0 berarti baris, dan axis=1 berarti kolom.")

st.write("3. Menampilkan DataFrame yang Sudah Diperbarui:")

st.write("- stunting_process: Setelah penghapusan, Anda memanggil variabel ini untuk menampilkan DataFrame stunting_process yang sekarang tidak lagi memiliki kolom puskesmas, desa_kelurahan, dan persen.")

st.write("4. Tujuan Penghapusan Kolom:")

st.write("- Efisiensi: Menghapus kolom yang tidak relevan dapat membuat DataFrame lebih ringkas dan fokus pada data yang penting untuk analisis.")
st.write("- Kebersihan Data: Dengan menghapus kolom yang tidak digunakan, DataFrame menjadi lebih mudah diinterpretasikan dan diolah lebih lanjut.")




code = '''
    #mencari nilai sum of square error
    sse_dist = []
    for i in range(1, 10):
        model = KMeans(n_clusters=i, n_init="auto")
        model.fit(stunting_process)
        sse_dist.append(model.inertia_)
        print("Sum of square error for {} clusters: {}".format(i, sse_dist[i-1]))
'''

st.code(code, language='python')
st.subheader("Penjelasan kode di atas")

st.write("1. Inisialisasi Daftar untuk Menyimpan SSE:")
st.write("- sse_dist = []: Ini adalah daftar kosong yang akan digunakan untuk menyimpan nilai Sum of Square Error (SSE) untuk setiap jumlah klaster yang diuji.")

st.write("2. Loop untuk Menghitung SSE dengan Berbagai Jumlah Klaster:")

st.write("- for i in range(1, 10):\
Ini adalah loop yang akan berjalan dari i = 1 hingga i = 9. Setiap iterasi loop ini akan menjalankan proses K-Means dengan jumlah klaster (n_clusters) yang berbeda, mulai dari 1 hingga 9.")

st.write("3. Membangun Model K-Means dan Melatihnya:")

st.write("- model = KMeans(n_clusters=i, n_init='auto'):")

st.write("KMeans(n_clusters=i, n_init='auto'): Di sini, Anda membuat objek model K-Means dari sklearn.cluster.KMeans, dengan jumlah klaster (n_clusters) yang diatur berdasarkan nilai i dalam loop.")

st.write("- n_clusters=i: Menentukan jumlah klaster yang akan dibentuk oleh model.")
st.write("- n_init='auto': Parameter ini mengatur berapa kali algoritma K-Means dijalankan dengan inisialisasi yang berbeda-beda untuk memastikan solusi terbaik ditemukan. Versi 'auto' akan memilih pengaturan yang paling sesuai secara otomatis.")
st.write("- model.fit(stunting_process):")
st.write("- fit(stunting_process): Melatih model K-Means menggunakan data stunting_process. Proses ini melibatkan penentuan posisi centroid (pusat klaster) untuk setiap klaster yang diminta.")
st.write("4. Menghitung dan Menyimpan SSE:")
st.write("- sse_dist.append(model.inertia_):\
model.inertia_: Setelah model K-Means dilatih, inertia_ adalah metrik yang mengukur total Sum of Square Error (SSE), yaitu jumlah jarak kuadrat antara titik data dan centroid terdekat. Nilai ini disimpan ke dalam daftar sse_dist.")
st.write("- Mengapa SSE penting?: SSE mengukur seberapa baik data telah dikelompokkan ke dalam klaster. Nilai SSE yang lebih rendah menunjukkan klaster yang lebih kompak dan lebih baik dalam mengelompokkan data.")
st.write("5. Menampilkan Hasil SSE untuk Setiap Klaster:")
st.write("print('Sum of square error for {} clusters: {}''.format(i, sse_dist[i-1])):")
st.write("- format(i, sse_dist[i-1]): Ini adalah pernyataan format yang akan mencetak jumlah klaster saat ini (i) dan nilai SSE yang terkait (sse_dist[i-1]).")
st.write("Mengapa Dicetak?: Mencetak SSE untuk setiap jumlah klaster membantu Anda melihat bagaimana SSE berubah saat jumlah klaster bertambah. Ini berguna untuk menentukan jumlah klaster yang optimal.")
st.write("6. Tujuan Analisis:")
st.write("Menentukan Jumlah Klaster Optimal: Salah satu cara umum untuk memilih jumlah klaster yang tepat adalah dengan menggunakan Metode Elbow. Dalam metode ini, Anda membuat grafik jumlah klaster terhadap SSE, dan mencari 'elbow' (titik di mana penurunan SSE mulai melambat). Jumlah klaster pada titik ini sering dipilih sebagai jumlah klaster optimal karena menyeimbangkan antara kompleksitas model dan representasi data yang baik.")


code = '''
    #membuat plot SSE
    sse = {}
    for k in range(1, 10):
        model = KMeans(n_clusters=k, n_init="auto").fit(stunting_process)
        sse[k] = model.inertia_  # Inertia: Sum of distances of samples to their closest cluster center

    plt.figure()
    plt.plot(list(sse.keys()), list(sse.values()))
    plt.xlabel("Number of cluster")
    plt.ylabel("SSE")
    plt.title("Plot Sum of Square Error")
    plt.show()
'''

st.code(code, language='python')


st.subheader("1. Penjelasan kode di atas")
st.write("- sse = {}:")

st.write("sse adalah dictionary kosong yang akan digunakan untuk menyimpan nilai SSE untuk setiap jumlah klaster (dengan jumlah klaster sebagai kunci dan nilai SSE sebagai nilai).")

st.write("2. Loop untuk Menghitung SSE dengan Berbagai Jumlah Klaster:")

st.write("- for k in range(1, 10):")

st.write("Loop ini berjalan dari k = 1 hingga k = 9. Setiap iterasi akan menghitung SSE untuk model K-Means dengan jumlah klaster k.")

st.write("3. Membangun dan Melatih Model K-Means:")

st.write("- model = KMeans(n_clusters=k, n_init='auto').fit(stunting_process):")

st.write("-KMeans(n_clusters=k, n_init='auto'): Membuat model K-Means dengan k klaster.")

st.write("- fit(stunting_process): Melatih model menggunakan data stunting_process.")
st.write("- sse[k] = model.inertia_:")
st.write("- model.inertia_: Setelah model dilatih, nilai inertia (SSE) disimpan dalam dictionary sse dengan kunci k. Inertia mengukur jumlah jarak kuadrat antara data dan klaster terdekat.")
st.write("4. Membuat dan Mengatur Plot:")
st.write("- plt.figure(): Ini memulai pembuatan plot baru.")
st.write("- plt.plot(list(sse.keys()), list(sse.values())):")
st.write("- list(sse.keys()): Mengambil jumlah klaster dari dictionary sse sebagai sumbu-x.")
st.write("- list(sse.values()): Mengambil nilai SSE yang sesuai sebagai sumbu-y.")
st.write("Plot ini menggambarkan bagaimana SSE berubah dengan jumlah klaster.\
plt.xlabel('Number of cluster''):")
st.write("- Menambahkan label 'Number of cluster' pada sumbu-x.\
plt.ylabel('SSE'):")
st.write("- Menambahkan label 'SSE' pada sumbu-y.\
plt.title('Plot Sum of Square Error'):")
st.write("- Memberikan judul pada plot: 'Plot Sum of Square Error''.\
plt.show():")
st.write("- Menampilkan plot yang telah dibuat.")
st.write("5. Tujuan dan Manfaat:")
st.write("Metode Elbow: Tujuan dari plot ini adalah untuk membantu Anda menggunakan Metode Elbow untuk menentukan jumlah klaster yang optimal. Dalam plot, Anda mencari titik di mana penurunan SSE mulai melambat (membentuk 'elbow'). Jumlah klaster pada titik ini sering dipilih sebagai jumlah klaster optimal, karena menyeimbangkan antara kompleksitas model dan representasi data yang baik.")




code = '''
    #mencari silhouette score
    silhouette_scores = []
    for i in range(2, 11):
        model = KMeans(n_clusters = i, n_init="auto")
        model.fit(stunting_process)
        silhouette_scores.append(silhouette_score(stunting_process, model.labels_))
        print("Silhouette Score for {} clusters: {}".format(i, silhouette_scores[i-2]))
'''

st.code(code, language='python')

st.subheader("Penjelasan kode di atas")

st.write("1. Inisialisasi Daftar untuk Menyimpan Silhouette Score:")
st.write("- silhouette_scores = []: \
         Daftar kosong ini digunakan untuk menyimpan nilai Silhouette Score untuk setiap jumlah klaster yang diuji.")



st.write("2. Loop untuk Menghitung Silhouette Score dengan Berbagai Jumlah Klaster:")

st.write("- for i in range(2, 11): \
         Loop ini berjalan dari i = 2 hingga i = 10. Setiap iterasi menghitung Silhouette Score untuk model K-Means dengan jumlah klaster i.")

st.write("- Mengapa mulai dari 2?: Silhouette Score memerlukan minimal dua klaster untuk dihitung, karena metrik ini mengukur seberapa mirip titik data dengan klaster mereka sendiri dibandingkan dengan klaster lain.")

st.write("3. Membangun dan Melatih Model K-Means:")

st.write("- model = KMeans(n_clusters = i, n_init='auto'):")

st.write("- KMeans(n_clusters = i, n_init='auto'): Membuat model K-Means dengan i klaster.")

st.write("- model.fit(stunting_process): Melatih model K-Means menggunakan data stunting_process. Setelah model dilatih, setiap titik data akan dialokasikan ke salah satu klaster yang dihasilkan oleh model.")

st.write("4. Menghitung dan Menyimpan Silhouette Score:")

st.write("- silhouette_scores.append(silhouette_score(stunting_process, model.labels_)):")

st.write("- silhouette_score(stunting_process, model.labels_): Fungsi ini menghitung Silhouette Score untuk data stunting_process berdasarkan label klaster (model.labels_) yang dihasilkan oleh model K-Means.")

st.write("Apa itu Silhouette Score?: Nilai Silhouette Score berkisar antara -1 dan 1. Nilai mendekati 1 menunjukkan bahwa titik-titik data dikelompokkan dengan baik (klaster yang padat dan terpisah dengan jelas). Nilai mendekati 0 menunjukkan bahwa titik-titik data berada di batas antara dua klaster, dan nilai mendekati -1 menunjukkan bahwa titik-titik data mungkin telah dialokasikan ke klaster yang salah.\
Nilai Silhouette Score yang dihitung kemudian ditambahkan ke daftar silhouette_scores.")

st.write("5. Menampilkan Hasil Silhouette Score:")

st.write("print('Silhouette Score for {} clusters: {}'.format(i, silhouette_scores[i-2])):")

st.write("- format(i, silhouette_scores[i-2]): Pernyataan ini digunakan untuk mencetak jumlah klaster saat ini (i) dan nilai Silhouette Score yang sesuai (silhouette_scores[i-2]).")

st.write("- i-2: Karena indeks di Python dimulai dari 0, dan loop dimulai dari 2, maka untuk mengambil nilai dari daftar silhouette_scores, Anda menggunakan indeks i-2.")

st.write("6. Tujuan Analisis:")

st.write("- Evaluasi Klasterisasi: Silhouette Score membantu Anda mengevaluasi seberapa baik klasterisasi yang dilakukan oleh model K-Means. Anda dapat membandingkan nilai Silhouette Score untuk berbagai jumlah klaster untuk menemukan jumlah klaster yang memberikan nilai tertinggi, yang sering dianggap sebagai jumlah klaster yang optimal.")



code = '''
    #membuat plot silhouette score
    plt.figure(figsize=[12, 8])
    fig = px.line(x=range(2, 11), y=silhouette_scores)

    fig.update_layout(
        xaxis = dict(tickvals = list(range(2, 11))),
        title="Plot Silhouette Score",
        xaxis_title="Number of Clusters",
        yaxis_title="Silhouette Score")

    fig.show()
'''

st.code(code, language='python')
st.write("1. Mengatur Ukuran Plot:")
st.write("- plt.figure(figsize=[12, 8]):\
         Ini mengatur ukuran figur plot menggunakan Matplotlib. Meskipun tidak diperlukan untuk Plotly Express, ini bisa menjadi langkah tambahan jika Anda menggunakan Matplotlib dalam konteks lain. Untuk Plotly Express, ukuran plot diatur dalam parameter fig.update_layout().")
st.write("2. Membuat Plot dengan Plotly Express:")
st.write("- fig = px.line(x=range(2, 11), y=silhouette_scores):")
st.write("- px.line(): Fungsi dari Plotly Express untuk membuat plot garis.")
st.write("- x=range(2, 11): Menentukan sumbu-x plot, yang menunjukkan jumlah klaster (dari 2 hingga 10).")
st.write("- y=silhouette_scores: Menentukan sumbu-y plot, yang berisi nilai Silhouette Score yang telah dihitung sebelumnya.")
st.write("3. Mengatur Tata Letak Plot:")
st.write("- fig.update_layout():")
st.write("- xaxis = dict(tickvals = list(range(2, 11))):\
         Mengatur nilai-nilai pada sumbu-x (jumlah klaster) untuk ditampilkan pada plot.")
st.write("- title='Plot Silhouette Score':\
         Memberikan judul pada plot: 'Plot Silhouette Score'.")
st.write("- xaxis_title='Number of Clusters':\
         Menambahkan label 'Number of Clusters' pada sumbu-x.")
st.write("- yaxis_title='Silhouette Score':\
         Menambahkan label 'Silhouette Score' pada sumbu-y.")
st.write("4. Menampilkan Plot:")
st.write("- fig.show():")

st.write("Menampilkan plot interaktif yang telah dibuat. Ini memungkinkan Anda untuk berinteraksi dengan plot, seperti melakukan zoom in/out atau melihat nilai-nilai secara detail.")



code = '''
    #membuat silhouette score visualizer
    model = KMeans(n_clusters=2, n_init="auto")
    visualizer = SilhouetteVisualizer(model, size=(1050, 600))
    visualizer.fit(stunting_process)
    visualizer.show()
    plt.show()
'''

st.code(code, language='python')
code = '''
    #membuat scatter plot hasil clustering
    plt.figure(figsize=[12, 8])
    cluster_color = model.labels_.astype('str')
    fig = px.scatter(new_stunting, x="jumlah_balita", y="stunting", color=cluster_color, title='Scatter Plot Hasil Clustering')

    fig.show()
'''

st.code(code, language='python')
code = '''
    #menampilkan koordinat terakhir centroid dari masing - masing cluster
    df_centroid = pd.DataFrame({
        'Koordinat': ['X', 'Y'],
        'Cluster 0': model.cluster_centers_[0],
        'Cluster 1': model.cluster_centers_[1],
    })

    df_centroid
'''

st.code(code, language='python')
code = '''
    #masukkan label cluster ke dalam dataframe utama
    new_stunting['cluster'] = model.labels_.astype('str')
    new_stunting

'''

st.code(code, language='python')
code = '''
    #menampilkan jumlah data setiap kluster
    new_stunting["cluster"].value_counts() #tidak dimasukkan ke dalam laporan
'''

st.code(code, language='python')
code = '''
    #menampilkan anggota kluster 0
    print("Stunting Cluster 0 :", new_stunting[new_stunting['cluster'] == "0"]['desa_kelurahan'].tolist())
    print("Stunting Cluster 0 :", new_stunting[new_stunting['cluster'] == "0"]['desa_kelurahan'].count())

'''

st.code(code, language='python')

code = '''
    #menampilkan anggota kluster 1
    print("Stunting Cluster 1 :", new_stunting[new_stunting['cluster'] == "1"]['desa_kelurahan'].tolist())
    print("Stunting Cluster 1 :", new_stunting[new_stunting['cluster'] == "1"]['desa_kelurahan'].count())
'''

st.code(code, language='python')


code = '''
    #menghitung jumlah anggota dari setiap kluster
    df_agg = new_stunting.groupby('cluster', as_index=False).agg(
        count_member=('desa_kelurahan', 'count'),
        avg_jumlah_balita=('jumlah_balita', 'mean'),
        avg_stunting=('stunting', 'mean'),
        avg_percent=('persen', 'mean')
    ).sort_values('cluster', ascending=True)

    #dataframe khusus agregasi data
    df_agg
'''
st.code(code, language='python')

code = '''
    #membuat bar chart dataframe hasil agregasi
    for column in df_agg.columns[2:5]:
        fig, ax = plt.subplots()
        count = df_agg[column]
        bar_colors = ['tab:red','tab:blue']

        ax.bar(x=['cluster 0', 'cluster 1'], height=count, width=0.7, color=bar_colors)
        ax.set_ylabel(f'{column}')
        ax.set_title(f'Bar chart {column}')
        plt.show()
'''

st.code(code, language='python')
