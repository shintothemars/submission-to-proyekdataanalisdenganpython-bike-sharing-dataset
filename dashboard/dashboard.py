import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
day_df = pd.read_csv("dashboard/day_clean.csv")
hour_df = pd.read_csv("dashboard/hour_clean.csv")

# Membuat dashboard
st.title("Analisis Penyewaan Sepeda")
st.title("made by shinta arum imaniyah ")

# Tampilkan data
#st.write("Data Penyewaan Sepeda")
#st.write(day_df)

# Tampilkan grafik
st.write("Grafik Penyewaan Sepeda")
fig, ax = plt.subplots()
ax.bar(day_df['season'], day_df['cnt'])
ax.set_xlabel('Musim')
ax.set_ylabel('Jumlah Penyewaan')
ax.set_title('Grafik Penyewaan Sepeda')
st.pyplot(fig)


# Tampilkan informasi
st.write("Informasi Penyewaan Sepeda")
st.write("Musim dengan jumlah penyewaan tertinggi: ", day_df['season'].value_counts().idxmax())
st.write("Jumlah penyewaan rata-rata per hari: ", day_df['cnt'].mean())
