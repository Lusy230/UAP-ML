import streamlit as st
import tensorflow as tf
import numpy as np
from pathlib import Path
import joblib

# Menentukan direktori model
models_dir = Path(__file__).resolve().parent / 'models'

# Memuat model 
try:
    fnn_model = tf.keras.models.load_model(models_dir / 'fnn.h5')
    rf_model = joblib.load(models_dir / 'rf.joblib')
except Exception as e:
    st.error(f"Terjadi kesalahan saat memuat model: {e}")

# Fungsi untuk memprediksi risiko stunting
def predict_risk(features, model_type):
    try:
        if model_type == 'FNN':
            # FNN menggunakan semua 7 fitur
            features_array = np.array([features], dtype=np.float32)  # Pastikan input berupa array 2D
            prediction = fnn_model.predict(features_array)[0][0]  # Ambil nilai skalar dari output FNN
        else:
            # Random Forest hanya menerima 5 fitur yang relevan (misalnya umur, berat_badan, panjang_badan, jenis_kelamin, dll)
            features_rf = features[:5]  # Mengambil hanya 5 fitur pertama untuk Random Forest
            features_array = np.array([features_rf], dtype=np.float32)  # Pastikan input berupa array 2D
            prediction = rf_model.predict(features_array)  # Hasil prediksi berupa array
            prediction = prediction[0]  # Ambil nilai skalar dari array hasil prediksi
        return prediction
    except Exception as e:
        st.error(f"Terjadi kesalahan saat melakukan prediksi: {e}")
        return None

# Fungsi untuk memprediksi status stunting berdasarkan prediksi
def predict_stunting_status(prediction, model_type):
    # Pastikan prediction adalah nilai skalar, jika itu adalah array
    if isinstance(prediction, np.ndarray):
        if prediction.size == 1:
            prediction = prediction.item()  # Ambil nilai scalar dari array jika ukuran array adalah 1
        else:
            prediction = prediction[0]  # Ambil elemen pertama jika array lebih besar

    if model_type == 'FNN':  # Jika menggunakan model FNN (output kontinu)
        if prediction < 0.25:
            return "Underweight"
        elif prediction < 0.5:
            return "Normal"
        elif prediction < 0.75:
            return "Risk of Overweight"
        else:
            return "Severely Underweight"
    elif model_type == 'Random Forest':  # Jika menggunakan model Random Forest (output diskrit)
        # Menangani hasil prediksi Random Forest dengan memeriksa nilai yang lebih tepat
        if prediction == 0:
            return "Underweight"
        elif prediction == 1:
            return "Normal"
        elif prediction == 2:
            return "Risk of Overweight"
        elif prediction == 3:
            return "Severely Underweight"
        else:
            return "Tidak Diketahui"  # Periksa apakah hasilnya diluar ekspektasi
    else:
        return "Tidak Diketahui"


# Tampilan antarmuka pengguna
st.set_page_config(page_title="Prediksi Risiko Stunting", layout="wide")
st.title("Prediksi Risiko Stunting pada Balita")
st.write(""" 
Aplikasi ini digunakan untuk memprediksi risiko stunting pada balita berdasarkan data input yang diberikan. 
Silakan masukkan data yang relevan untuk melakukan prediksi.
""")

# Form untuk input data
with st.form(key='data_input_form'):
    umur = st.slider("Umur Balita (bulan)", min_value=0, max_value=60, value=24)
    berat_badan = st.number_input("Berat Badan (kg)", min_value=0.5, max_value=30.0, value=10.0)
    panjang_badan = st.number_input("Panjang Badan (cm)", min_value=50.0, max_value=110.0, value=75.0)
    jenis_kelamin = st.radio("Jenis Kelamin", options=['Laki-laki', 'Perempuan'])

    # Pilih model untuk prediksi
    model_type = st.radio("Pilih model untuk prediksi", options=["FNN", "Random Forest"])

    # Tombol untuk submit
    submit_button = st.form_submit_button(label="Prediksi Risiko Stunting")

# Menangani input dan menampilkan hasil prediksi
if submit_button:
    # Preprocessing data untuk stunting
    features = [
        umur,  # Fitur 1
        berat_badan,  # Fitur 2
        panjang_badan,  # Fitur 3
        1 if jenis_kelamin == 'Laki-laki' else 0,  # Fitur 4: Jenis Kelamin
        0,  # Placeholder fitur tambahan 1
        0,  # Placeholder fitur tambahan 2
        0   # Placeholder fitur tambahan 3
    ]

    # Prediksi risiko stunting
    result = predict_risk(features, model_type)

    if result is not None:
        # Prediksi status stunting berdasarkan model
        stunting_status = predict_stunting_status(result, model_type)  # Perbaikan di sini

        # Menampilkan hasil prediksi
        st.write(f"Prediksi Risiko Stunting: {stunting_status}")

        # # Menyediakan penjelasan hasil
        # if stunting_status in ["Risk of Overweight", "Severely Underweight"]:
        #     st.warning("Risiko tinggi stunting. Perlu perhatian lebih lanjut.")
        # else:
        #     st.success("Risiko stunting rendah. Namun tetap lakukan pemantauan rutin.")
