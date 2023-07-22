import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image
st.set_page_config(
    page_title='Churn Predict',
    layout='wide',
    initial_sidebar_state='expanded'
)

def run():
    # membuat title
    st.title('Customer Churn Predict')
    # membuat subhead
    st.subheader('EDA untuk analisa dataset Churn')
    # menambahkan gambar
    image = Image.open('churn.jpg')
    st.image(image, caption='Churn Customer')
    #menambahkan deskripsi
    st.write('Page ini dibuat oleh Nurul Izzah')
    #membuat garis lurus
    st.markdown('---')
    #magic syntax
    '''
    pada page kali ini, penulis akan melakukan eksplorasi sederhana.
    dataset yang digunakan adalah dataset Churn.
    '''
    # Show dataframe
    df = pd.read_csv('churn.csv')
    st.dataframe(df)

    st.write('#### Melihat distribusi churn risk score')

    # Plot distribusi churn risk score
    fig, ax = plt.subplots(figsize=(12,8))
    ax.hist(df['churn_risk_score'], bins=5)
    ax.set_title('Distribusi Churn Risk Score')
    ax.set_xlabel('Churn Risk Score')
    ax.set_ylabel('Jumlah Customer')
    st.pyplot(fig)
    st.write('_berdasarkan visualisasi diatas, mayoritas customer memiliki risiko churn yang rendah, namun masih ada sejumlah customer yang memiliki risiko churn yang tinggi_')

    st.write('#### Melihat hubungan antara kolom')

    # Mengecek korelasi antar kolom
    corr_matrix = df.corr()

    fig, ax = plt.subplots(figsize=(12,8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)
    st.write('_Berdasarkan heatmap, korelasi positif tertinggi adalah antara churn risk score dengan variabel age dan avg_frequency_login_days, sedangkan korelasi negatif tertinggi adalah dengan variabel avg_transaction_value dan points_in_wallet_')

    st.write('#### Melihat hubungan antara usia dengan churn risk score')

    # membuat box plot churn risk score berdasarkan usia
    plt.figure(figsize=(15,8))
    sns.boxplot(x='age', y='churn_risk_score', data=df)
    st.pyplot()
    st.write('_berdasarkan visualisasi usia, dapat dilihat bahwa untuk semua data usia dari 10 sampai 64 memiliki nilai churn risk score di 1.0. Hal ini menunjukkan bahwa pada rentang usia tersebut, terdapat pola yang sama yaitu pelanggan cenderung memiliki churn risk score di angka 1.0_')

    st.write('#### Melihat apakah ada perbedaan perilaku antara laki-laki dan perempuan dalam menggunakan produk')

    # membuat groupping
    df_gender = df[['gender', 'churn_risk_score']]

    # membuat boxplot churn risk score berdasarkan jenis kelamin
    plt.figure(figsize=(12,8))
    sns.boxplot(x='gender', y='churn_risk_score', data=df_gender)
    plt.title('Churn Risk Score Berdasarkan Jenis Kelamin')
    plt.xlabel('Jenis Kelamin')
    plt.ylabel('Churn Risk Score')
    plt.show()
    st.pyplot()
    st.write('_berdasarkan visualisasi, kolom gender memiliki nilai churn risk score di angka 1.0 pada box plot. Hal ini menunjukkan bahwa baik pelanggan laki-laki maupun perempuan cenderung memiliki churn risk score yang sama yaitu di angka 1.0_')

    st.write('#### melihat apakah ada perbedaan perilaku antara customer di berbagai kategori wilayah')

    # visualisasi distribusi churn risk score berdasarkan kategori wilayah
    fig, ax = plt.subplots(figsize=(12,8))
    sns.boxplot(x='region_category', y='churn_risk_score', data=df, ax=ax)
    ax.set_title('Distribusi Churn Risk Score Berdasarkan Kategori Wilayah')
    st.pyplot(fig)
    st.write('_visualisasi tersebut menunjukan kategori wilayah memiliki nilai churn risk score di angka 1.0. Hal ini menunjukkan bahwa pada semua kategori wilayah, terdapat pola yang sama yaitu pelanggan cenderung memiliki churn risk score di angka 1.0_')

    st.write('#### melihat apakah customer yang jarang login lebih cenderung berhenti menggunakan produk daripada yang sering login')

    # Visualize relationship between churn risk score and frequency of login
    fig, ax = plt.subplots(figsize=(12,8))
    sns.boxplot(x="churn_risk_score", y="avg_frequency_login_days", data=df)
    ax.set_title("Relationship Between Churn Risk Score and Frequency of Login")
    st.pyplot(fig)
    st.write('_Berdasarkan visualisasi di atas, dapat disimpulkan bahwa tidak terdapat perbedaan signifikan dalam frekuensi login antara churn risk score class 0 dan class 1. Namun, churn risk score class 0 memiliki banyak outlier, yang berarti ada beberapa pelanggan yang memiliki frekuensi login yang sangat rendah atau sangat tinggi_')

    st.write('#### melihat apakah customer yang pernah mengajukan keluhan lebih cenderung berhenti menggunakan produk daripada yang tidak pernah mengajukan keluhan')

    # Menghitung jumlah customer yang mengajukan keluhan di masa lalu dan yang tidak
    complaint_count = df['past_complaint'].value_counts()

    # Membuat pie chart untuk menunjukkan persentase customer yang mengajukan keluhan
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.pie(complaint_count, labels=complaint_count.index, autopct='%1.1f%%')
    ax.set_title('Persentase Customer dengan Keluhan di Masa Lalu')
    st.pyplot(fig)
    st.write('_dari visualisasi dapat disimpulkan bahwa hampir setengah (49.7%) dari total customer pernah mengajukan keluhan di masa lalu, sedangkan sisanya sebanyak 50.3% tidak pernah mengajukan keluhan_')

if __name__ == '__main__':
    run()