import streamlit as st
import pandas as pd
import os


# Konfigurasi Halaman
st.set_page_config(page_title="toko satrio", layout="wide")


# 1. Tampilkan Banner Canva
if os.path.exists("toko stario.png"):
    st.image("toko stario.png", use_container_width=True)


st.title(" toko Serba Ada Mas Satrio")
st.divider()


try:
    if os.path.exists("data_satrio.csv"):
        df = pd.read_csv("data_satrio.csv")
        df = df.dropna(subset=['foto'])
        
        daftar_kategori = df['kategori'].unique()
        
        for kat in daftar_kategori:
            st.header(f" jenis barang: {kat.capitalize()}")
            data_per_kat = df[df['kategori'] == kat]
            
            cols = st.columns(4)
            
            for index, row in data_per_kat.reset_index().iterrows():
                nama_foto = str(row['foto']).strip()
                
                with cols[index % 4]:
                    if os.path.exists(nama_foto):
                        st.image(nama_foto, use_container_width=True)
                        st.subheader(row['nama'])
                        
                        # --- HARGA & STATUS DENGAN FONT LEBIH BESAR ---
                        st.markdown(f"### **Rp {row['harga']:,}**") 
                        st.markdown(f"**Status:** {row['status']}")
                    else:
                        st.warning(f"Foto {nama_foto} tidak ditemukan")
            st.divider()
            
    else:
        st.error("File 'data_satrio.csv' tidak ditemukan!")


except Exception as e:
    st.error(f"Terjadi kesalahan: {e}")


# --- BAGIAN KONTAK & ALAMAT (FOOTER) ---
st.write("") # Memberi ruang kosong
st.write("")
st.divider()
st.subheader("📍 Hubungi Kami")
col_info1, col_info2 = st.columns(2)


with col_info1:
    st.markdown("""
    **Alamat Galeri:** Jl. Anggrek Indah No. 123,  
    Kecamatan Bunga, Kota Flora,  
    Yogyakarta.
    """)


with col_info2:
    # Ganti nomor HP di bawah ini dengan nomor Anda (gunakan format 62)
    no_hp = "6282146215936" 
    pesan_wa = "Halo, saya tertarik memesan sembako di katalog Anda."
    link_wa = f"https://wa.me/{no_hp}?text={pesan_wa.replace(' ', '%20')}"
    
    st.markdown(f"**WhatsApp:**")
    st.link_button("📱 Pesan Sekarang via WhatsApp", link_wa)


st.caption("© 2026 Toko Serba Ada | Satrio32 - Semua Hak Dilindungi")
