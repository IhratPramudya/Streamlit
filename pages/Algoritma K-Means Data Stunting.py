import streamlit as st
import pandas as pd
# import matplotlib.pyplot as plt
import plotly.express as px

st.title("Upload Dataset")
data_file = st.file_uploader((""), type=["xlsx"])


if data_file is not None:
    file_detail = {
        "file_name": data_file.name,
        "file_type": data_file.type,
        "file_size": data_file.size
    }

    st.write(file_detail)
    df = pd.read_excel(data_file)


    
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

    st.sidebar.title("Pengurangan Data")
    
    st.title("Pengurangan Data")
    column_Outliers = st.sidebar.selectbox('Masukkan Nilai Column Outlier',
    (numeric_cols.columns))
    try:
        treshold = st.sidebar.number_input("Masukan Nilai Treshold", df[column_Outliers].min(), df[column_Outliers].max(), df[column_Outliers].max(), 1)
        removed_treshold = df[df[str(column_Outliers)] <= treshold]
        fig2 = px.box(removed_treshold, y=str(column_Outliers))
        st.plotly_chart(fig2)
        st.write("Jumlah Data", len(removed_treshold))

        st.dataframe(removed_treshold, use_container_width=True)
        st.sidebar.title("Data no Outlier Scatter")
        numeric_cols = removed_treshold.select_dtypes(include=['number'])
        column_No_Outliers_x = st.sidebar.selectbox('Masukkan Nilai Column X',
        (numeric_cols.columns))
        column_No_Outliers_y = st.sidebar.selectbox('Masukkan Nilai Column Y',
        (numeric_cols.columns))
        fig4 = px.scatter(removed_treshold, x=column_No_Outliers_x, y=column_No_Outliers_y, title="Scatter Plot Dataframe no outlier")
        st.plotly_chart(fig4)
    except:
        st.sidebar.write("Tipe data tidak cocok !!!!!")
    no_outlier_data_stunting = removed_treshold.copy()

    st.sidebar.title("Pengurangan Variabel")
    
    st.title("Pengurangan Variabel")

    numeric_cols_no_outlier_data_stunting = no_outlier_data_stunting.select_dtypes(include=['number'])
    column_No_Outliers_x = st.sidebar.selectbox('hapus parameter',
    (numeric_cols_no_outlier_data_stunting.columns))

    
else:
    st.write("Tidak ada dataset yang di upload")

