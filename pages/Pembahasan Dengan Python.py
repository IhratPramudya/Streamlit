# Import Streamlit library
import streamlit as st

# Displaying Python Code
st. set_page_config(layout="wide") 

st.header("""Import Library yang digunakan""")
code = '''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import yellowbrick from SillhouetteScore

'''
st.code(code, language='python')
st.subheader("Penjelasan kode dari library yang digunakan")
st.write("")

st.header("PENGUMPULAN DATA")
code = '''
    # #mouting ke google drive
    from google.colab import drive
    drive.mount('/content/drive')
'''

st.code(code, language='python')
code = '''
    #raw_stunting = pd.read_excel('data-stunting.xlsx') #lokasi dataset di lokal
    raw_stunting = pd.read_excel('drive/MyDrive/TA (visquad)/Balita Stunting/Data/data-stunting.xlsx') #lokasi dataset di google drive
    raw_stunting
'''

st.code(code, language='python')
code = '''
    raw_stunting.sum().null()
'''
st.code(code, language='python')

code = '''
    raw_stunting.describe()

'''
st.code(code, language='python')

code = '''
    plt.fig(figsize=(13,100))
    fig = px.scatter(raw_stunting, x="jumlah_balita", y="stunting", title="scatter Plot Dataframe awal")
    fig.show()
'''

st.code(code, language='python')

code = '''
    stunting_process = raw_stunting.copy()
    stunting_process
'''

st.code(code, language='python')

code = '''
    drop_column = ['puskesmas', 'desa_kelurahan', 'persen']
    stunting_process.drop(drop_column, inplace=True, axis=1)
    stunting_process
'''

st.code(code, language='python')

code = '''
    drop_column = ['puskesmas', 'desa_kelurahan', 'persen']
    stunting_process.drop(drop_column, inplace=True, axis=1)
    stunting_process
'''

st.code(code, language='python')

code = '''
    #mencari nilai sum of square error
    sse_dist = []
    for i in range(1, 10):
        model = KMeans(n_cluster=i, n_init="auto")
        model.fit(stunting_process)
        sse_dist.append(model.inertia_)
        print("Sum of Square Error for {} clusters: {}".format(i, sse_dist[i-1]))
'''

st.code(code, language='python')


code = '''
    #membuat plot sse
    sse = {}
    for k in range(1, 10):
        model = KMeans(n_cluster=k, n_init="auto")
        model.fit(stunting_process)
        sse[k] = model.inertia_

    plt.figure()
    plt.plot(list(sse.keys()), list(sse.values()))
    plt.xlabel("Number of cluster")
    plt.ylabel("SSE")
    plt.title("Plot Sum of Square Erorr")
    plt.show()
'''

st.code(code, language='python')


code = '''
    SilhouetteScore = []
    for i in range(2, 10):
        model = KMeans(n_cluster=i, n_init="auto")
        model.fit(stunting_process)
        SilhouetteScore.append(silhouette_score(stunting_process, model.labels_))
        print("Silhouette Score for {} clusters: {}".format(i, SilhouetteScore[i-2]))
'''

st.code(code, language='python')

code = '''
    plt.figure(figsize=[12,8])
    fig = px.line(x=range(2, 11), y=SilhouetteScore)
    
'''