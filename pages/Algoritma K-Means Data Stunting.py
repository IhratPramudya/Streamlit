import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans
from yellowbrick.cluster import SilhouetteVisualizer

st.title("Upload Dataset")
data_file = st.file_uploader(("Silahkan Upload"), type=["xlsx"])


if data_file is not None:
    file_detail = {
        "file_name": data_file.name,
        "file_type": data_file.type,
        "file_size": data_file.size
    }

    st.write(file_detail)
    df = pd.read_excel(data_file, engine='openpyxl')


    
    st.dataframe(df, use_container_width=True)
    st.title("Pengumpulan Data")
    st.sidebar.title("Pengumpulan Data")
    jenis_plot = st.sidebar.selectbox('Jenis Visualisasi',
        ('Scatter', 'Histogram', 'Boxplot'))
    
    if jenis_plot == "Scatter":
        dimensi = []
        numeric_cols = df.select_dtypes(include=['number'])
        string_cols = df.select_dtypes(include=['object'])
        if len(numeric_cols.columns) >= 2:
            dimensi = ['2 Dimensi', '3 Dimensi']
        else:
            dimensi = ['1 Dimensi']

        jumlah_dimensi = st.sidebar.selectbox('Pilih dimensi: ',
        (dimensi))
        if len(numeric_cols.columns) == 1:
            st.write("Tidak bisa menampilkan scatter dengan 1 dimensi silahkan gunakan Box Plot")
        else:
            if jumlah_dimensi == '2 Dimensi':
                column = []
                column_X = st.sidebar.selectbox('Masukkan Nilai X',
                (numeric_cols.columns))
                column_Y = st.sidebar.selectbox('Masukkan Nilai Y',
                (numeric_cols.columns))
                fig = px.scatter(numeric_cols, x=column_X, y=column_Y, title="Scatter Plot Dataframe Awal")
                st.plotly_chart(fig)
            else:
                column_X = st.sidebar.selectbox('Masukkan Nilai X',
                (numeric_cols.columns))
                column_Y = st.sidebar.selectbox('Masukkan Nilai Y',
                (numeric_cols.columns))
                column_Z = st.sidebar.selectbox('Masukkan Nilai Z',
                (numeric_cols.columns))
                column_label = st.sidebar.selectbox('Masukkan Nilai label',
                (string_cols.columns))
                fig = px.scatter_3d(df, x=column_X, y=column_Y, 
                    z=column_Z, color=column_label, 
                    color_discrete_sequence=px.colors.qualitative.Alphabet)
                st.plotly_chart(fig)

    st.title("Pengurangan Data")
    column_Outliers = st.selectbox('Masukkan Nilai Column Outlier',
    (numeric_cols.columns))
    try:
        with st.form(key='form treshold'):
            # model = st.selectbox('Pilih Model', ("DBSCAN", "K-Means"))
            treshold = st.number_input("Masukan Nilai Treshold", df[column_Outliers].min(), df[column_Outliers].max(), df[column_Outliers].max(), 1)
            submit_button = st.form_submit_button(label='Hapus')

        removed_treshold = df[df[str(column_Outliers)] <= treshold]
        fig2 = px.box(removed_treshold, y=str(column_Outliers))
        st.plotly_chart(fig2)
        st.write("Jumlah Data", len(removed_treshold))

        st.dataframe(removed_treshold, use_container_width=True)
        st.title("Data no Outlier Scatter")
        st.sidebar.title("Data no Outlier Scatter")
        numeric_cols = removed_treshold.select_dtypes(include=['number'])
        column_No_Outliers_x = st.sidebar.selectbox('Masukkan Nilai Column X',
        (numeric_cols.columns))
        column_No_Outliers_y = st.sidebar.selectbox('Masukkan Nilai Column Y',
        (numeric_cols.columns))
        fig4 = px.scatter(removed_treshold, x=column_No_Outliers_x, y=column_No_Outliers_y, title="Scatter Plot Dataframe no outlier")
        st.plotly_chart(fig4)
    except:
        st.write("Tipe data tidak cocok !!!!!")
    try:
        
        no_outlier_data_stunting = removed_treshold.copy()


        st.title("Pengujian Model")

        with st.form(key='form'):
            model = st.selectbox('Pilih Model', ("DBSCAN", "K-Means"))
            # Defining submit button
            submit_button = st.form_submit_button(label='Uji Model')

        # Tindakan setelah form disubmit
        if submit_button:
            st.write(f'Model yang dipilih: {model}')
            if model == "K-Means":
                st.write("Hello K-means")
                drop_column = ['puskesmas', 'desa_kelurahan', 'persen']
                no_outlier_data_stunting.drop(drop_column, inplace=True, axis=1)

                st.dataframe(no_outlier_data_stunting, use_container_width=True)

                sse_dist = []
                for i in range(1, 9):
                    model_K = KMeans(n_clusters=i) 
                    model_K.fit(no_outlier_data_stunting)
                    sse_dist.append(model_K.inertia_)
                    st.write("Sum of square error for {} clusters: {}".format(i, sse_dist[i-1]))


                sse = {}
                for k in range(1, 10):
                    model_k = KMeans(n_clusters=k).fit(no_outlier_data_stunting)
                    sse[k] = model_k.inertia_  # Inertia: Sum of distances of samples to their closest cluster center
                    

                fig_sse = go.Figure(go.Scatter(y=list(sse.values()), x=list(sse.keys())))

                fig_sse.update_layout(
                    title={
                        'text': "Plot Sum of Square Error"},
                    xaxis_title="Number of clusters",
                    yaxis_title="SSE"    
                    )

                fig_sse.update_yaxes(tickformat=".0f")
                st.plotly_chart(fig_sse)


                silhouette_scores = []
                for i in range(2, 11):    
                    model_k = KMeans(n_clusters = i)
                    model_k.fit(no_outlier_data_stunting)
                    silhouette_scores.append(silhouette_score(no_outlier_data_stunting, model_k.labels_))
                    st.write("Silhouette Score for {} clusters: {}".format(i, silhouette_scores[i-2]))

                fig_silhouette = go.Figure(go.Scatter(y=silhouette_scores, x=[i for i in range(2, 11)]))
                
                fig_silhouette.update_layout(
                    xaxis=dict(tickvals= [i for i in range(2, 11)]),
                    title={
                        'text': "Plot Silhouette Score"},
                    xaxis_title="Number of clusters",
                    yaxis_title="Silhouette Score"    
                    )

                st.plotly_chart(fig_silhouette)

            else:
                st.write("Model belum Tersedia")

    except Exception as e:
        st.write("Jenis error:", type(e))
        st.write("Pesan error:", e)
else:
    st.write("Silahkan Upload Data untuk menjalankan model")

