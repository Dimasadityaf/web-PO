import streamlit as st
import pandas as pd

# Inisialisasi file Excel jika belum ada
excel_file = 'Input.xlsx'
try:
    df = pd.read_excel(excel_file)
except FileNotFoundError:
    df = pd.DataFrame(columns=['Tanggal', 'Nama Barang', 'Quantity', 'Bulan PO', 'Keterangan'])
    df.to_excel(excel_file, index=False)

# Judul aplikasi
st.title('FORM INPUT BARANG')

# Membuat form input
tanggal = st.text_input('Tanggal (YYYY-MM-DD)')
nama_barang = st.text_input('Nama Barang')
quantity = st.text_input('Quantity')
bulan_po = st.text_input('Bulan PO')
keterangan = st.text_input('Keterangan')

if st.button('Submit'):
    # Membaca input pengguna
    new_data = pd.DataFrame({
        'Tanggal': [tanggal],
        'Nama Barang': [nama_barang],
        'Quantity': [quantity],
        'Bulan PO': [bulan_po],
        'Keterangan': [keterangan]
    })

    # Menggabungkan data baru dengan dataframe yang sudah ada
    df = pd.concat([df, new_data], ignore_index=True)

    # Menyimpan dataframe ke file Excel
    df.to_excel(excel_file, index=False)

    # Menampilkan pesan sukses
    st.success('Data berhasil disimpan!')
