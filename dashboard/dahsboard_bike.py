import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Memuat Dataset
bike_sharing_df = pd.read_csv("dashboard/dataclean_bikesharing.csv")

# Pastikan kolom 'date' dalam format datetime
bike_sharing_df['date'] = pd.to_datetime(bike_sharing_df['date'])

# Set up Streamlit page
st.set_page_config(page_title="Dashboard Analisis Bike Sharing", layout="wide")
st.title("Dashboard Analisis Bike Sharing")

# Sidebar dengan filter waktu
st.sidebar.image("https://storage.googleapis.com/kaggle-datasets-images/4165290/7200983/7ab427725cb0c7b59c5b4e450ede9c1a/dataset-card.png?t=2023-12-15-10-05-39", use_container_width=True)
st.sidebar.header("Filter Data")
tanggal_awal = bike_sharing_df['date'].min().date()
tanggal_akhir = bike_sharing_df['date'].max().date()
rentang_tanggal = st.sidebar.date_input("Pilih Rentang Waktu", min_value=tanggal_awal, max_value=tanggal_akhir, value=[tanggal_awal, tanggal_akhir])

# Filter dataset sesuai rentang waktu yang dipilih
bike_sharing_df_filtered = bike_sharing_df[(bike_sharing_df['date'] >= pd.to_datetime(rentang_tanggal[0])) & (bike_sharing_df['date'] <= pd.to_datetime(rentang_tanggal[1]))]

# Section 1: Weather Condition Analysis
st.header("Analisis Kondisi Cuaca")

df_weathercond = bike_sharing_df_filtered.groupby('weather_condition')['instant'].nunique().reset_index()
df_weathercond.rename(columns={'instant': 'sum'}, inplace=True)

# Bar plot for total rentals based on weather condition
st.subheader("Total Sewa Sepeda Berdasarkan Kondisi Cuaca")
fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(data=df_weathercond.sort_values('weather_condition', ascending=False), x='weather_condition', y='sum', ax=ax, palette="Set2")
ax.set_title('Total Sewa Sepeda Berdasarkan Kondisi Cuaca', fontsize=10, weight='bold')
ax.set_xlabel('kondisi cuaca', fontsize=8)
ax.set_ylabel('Total Sewa Sepeda', fontsize=8)
plt.xticks(rotation=45, fontsize=8)
plt.tight_layout(pad=3.0)
st.pyplot(fig)

# Add space between plots
st.write("")  # Adding a blank line

# Separate barplots for casual and registered users
st.subheader("Sewa Sepeda oleh Pengguna Kasual dan Terdaftar")
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
sns.barplot(x='weather_condition', y='casual', data=bike_sharing_df_filtered, ax=axes[0], palette="Blues")
sns.barplot(x='weather_condition', y='registered', data=bike_sharing_df_filtered, ax=axes[1], palette="Greens")

axes[0].set_title('Sewa Sepeda Kasual Berdasarkan Cuaca', fontsize=10, weight='bold')
axes[1].set_title('Sewa Sepeda Terdaftar Berdasarkan Cuaca', fontsize=10, weight='bold')

for ax in axes:
    ax.set_xlabel('Kondisi Cuaca', fontsize=8)
    ax.set_ylabel('Total Sewa', fontsize=8)
    plt.setp(ax.get_xticklabels(), rotation=45, fontsize=8)
plt.tight_layout(pad=3.0)
st.pyplot(fig)

# Add space between sections
st.write("")  # Adding a blank line

# Section 2: Weekdays vs Weekends Analysis
st.header("Analisis Hari Kerja vs Akhir Pekan")

df_workingday = bike_sharing_df_filtered.groupby('workingday').instant.nunique().reset_index()
df_workingday.rename(columns={'instant': 'sum'}, inplace=True)

# Bar plot for rentals based on working day
st.subheader("Total Sewa Sepeda pada Hari Kerja vs Akhir Pekan")
fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(data=df_workingday.sort_values('workingday', ascending=False), x='workingday', y='sum', ax=ax, palette="Set1")
ax.set_title('Sewa Sepeda pada Hari Kerja vs Akhir Pekan', fontsize=10, weight='bold')
ax.set_xlabel('Hari Kerja (0: Hari Kerja, 1: Akhir Pekan)', fontsize=8)
ax.set_ylabel('Total Sewa Sepeda', fontsize=8)
plt.tight_layout(pad=3.0)
st.pyplot(fig)

# Add space between sections
st.write("")  # Adding a blank line

# Section 3: Holiday Impact on Rentals
st.header("Dampak Liburan pada Sewa Sepeda")

df_holiday = bike_sharing_df_filtered.groupby('holiday').instant.nunique().reset_index()
df_holiday.rename(columns={'instant': 'sum'}, inplace=True)

# Bar plot for rentals on holidays
st.subheader("Total Sewa Sepeda pada Hari Libur vs Non-Libur")
fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(data=df_holiday.sort_values('holiday', ascending=False), x='holiday', y='sum', ax=ax, palette="Pastel1")
ax.set_title('Sewa Sepeda pada Hari Libur vs Non-Libur', fontsize=10, weight='bold')
ax.set_xlabel('Libur (0: Non-Libur, 1: Libur)', fontsize=8)
ax.set_ylabel('Total Sewa Sepeda', fontsize=8)
plt.tight_layout(pad=3.0)
st.pyplot(fig)

# Add space between sections
st.write("")  # Adding a blank line

# Section 4: Day of the Week Analysis
st.header("Analisis Hari dalam Minggu")


# Bar plot for bike rentals by day of the week
st.subheader("Sewa Sepeda Berdasarkan Hari dalam Minggu")
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x='weekday', y='count', data=bike_sharing_df_filtered, ax=ax, ci=None, palette="coolwarm")
ax.set_title('Sewa Sepeda Berdasarkan Hari dalam Minggu', fontsize=10, weight='bold')
ax.set_xlabel('Hari dalam Minggu', fontsize=8)
ax.set_ylabel('Jumlah Sewa', fontsize=8)
plt.tight_layout(pad=3.0)
st.pyplot(fig)

# Add space before footer
st.write("")  # Adding a blank line

# Footer Section
st.markdown(""" 
    --- 
    Made with by **Era Syafina** | Laskar Ai 2025 Cohort Mahasiswa & Fresh Graduate
    """)
