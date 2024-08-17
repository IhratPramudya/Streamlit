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


code = '''
    #drop kolom yang tidak digunakan
    drop_column = ['puskesmas', 'desa_kelurahan', 'persen']
    stunting_process.drop(drop_column, inplace=True, axis=1)
    stunting_process
'''

st.code(code, language='python')


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
