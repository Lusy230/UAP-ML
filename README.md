# 👶🏻Prediksi Risiko Stunting pada Balita👶🏻

## Deskripsi Proyek
Proyek ini dikembangkan untuk membantu memprediksi risiko stunting pada balita berdasarkan data masukan seperti umur (bulan), berat badan, panjang badan, dan jenis kelamin. Dengan menggunakan model deep learning Feedforward Neural Network (FNN) dan Random Forest, proyek ini bertujuan memberikan rekomendasi awal untuk pemantauan dan intervensi dini pada balita yang berisiko stunting.

**Dataset** diperoleh dari [Stunting Wasting Dataset](https://www.kaggle.com/datasets/jabirmuktabir/stunting-wasting-dataset). Dataset ini mencakup data antropometri dan demografi yang terperinci untuk anak-anak, dengan fokus pada indikator stunting dan wasting. Dataset ini menyediakan fitur-fitur seperti:
- **Jenis Kelamin**: Laki-laki atau perempuan.
- **Umur (bulan)**: Rentang usia balita dalam bulan.
- **Berat badan (kg)**: Berat badan balita pada saat pengukuran.
- **Panjang badan (cm)**: Panjang badan balita pada saat pengukuran.
- **Label yang menunjukkan status stunting atau wasting**: Indikator status gizi berdasarkan rasio berat badan terhadap tinggi badan.
Berikut adalah tabel korelasi antar variabel dataset:
![korelasi dataset](https://github.com/user-attachments/assets/28f9a5b3-991f-42dd-a803-aafcc90c3ba3)


## Langkah Instalasi
_**Buat Virtual Environment**_
```bash
python -m venv env
source env/bin/activate  # Untuk Linux/MacOS
.\env\Scripts\activate  # Untuk Windows
```
_**Install Dependencies**_
```bash
pip install -r requirements.txt
```
_**Tambahkan Model ke Direktori `models`**_
Letakkan file `fnn.h5` dan `rf.joblib` ke dalam folder `models` di direktori utama proyek.
_**Jalankan Aplikasi**_
```bash
pdm run start
```


## Deskripsi Model
Proyek ini menggunakan dua jenis model untuk prediksi risiko stunting:
1. **Feedforward Neural Network (FNN):**
  - Model ini dibangun dengan TensorFlow/Keras menggunakan arsitektur jaringan saraf sederhana.
  - Input: Umur, berat badan, panjang badan, jenis kelamin, dan fitur tambahan placeholder.
  - Output: Nilai kontinu yang merepresentasikan tingkat risiko stunting.
  - Arsitektur yang digunakan:
    1. Input layer: jumlah neuron sesuai dengan fitur dalam data input `(X_train_scaled)`.
    2. Hidden layer 1: 128 neuron, aktivasi ReLU, dropout 30%.
    3. Hidden layer 2: 64 neuron, aktivasi ReLU, dropout 30%.
    4. Output layer:
    * Untuk klasifikasi biner: 1 neuron dengan fungsi aktivasi sigmoid.
    * Untuk klasifikasi multi-kelas: sejumlah neuron sesuai jumlah kelas, dengan fungsi aktivasi softmax.

![fnn](https://github.com/user-attachments/assets/a251e831-783f-4fcf-8b37-c919e727afd8)

2. **Random Forest (RF):**
  - Model ini dilatih menggunakan sklearn dengan algoritma ensemble Random Forest.
  - Input: Seluruh fitur yang tersedia (7 fitur).
  - Output: Kelas diskrit (0-3) yang merepresentasikan kategori risiko stunting.

![rf](https://github.com/user-attachments/assets/ed2d4042-6621-4279-8aa2-5c22c8e7c3eb)


## Hasil dan Analisis
### Performa Model
- FNN: Akurasi pelatihan mencapai 98% dengan loss yang stabil setelah beberapa epoch.
- RF: Akurasi cross-validation mencapai 99% dengan kelebihan dalam interpretasi hasil model.

### Perbandingan Model
Hasil evaluasi model dibandingkan menggunakan dataset validasi:
**Feedforward Neural Network (FNN):**
![fnn cr](https://github.com/user-attachments/assets/8822f10e-ed42-4956-9893-9e2d91532500)

**Random Forest (RF):**
![rf cr](https://github.com/user-attachments/assets/be23fe58-98b6-4462-8783-289ca18294bb)


### Grafik Evaluasi 
Berikut adalah visualisasi hasil evaluasi:
**Feedforward Neural Network (FNN):**
![cm fnn](https://github.com/user-attachments/assets/1fcf65ee-0c4a-4650-80dc-6d544951f7c8)

**Random Forest (RF):**
![cm rf](https://github.com/user-attachments/assets/cb78cf15-1eac-4db8-a82f-489cf16713ce)


## Kesimpulan
- Model Random Forest lebih stabil dan memiliki interpretasi lebih baik dibandingkan FNN.
- FNN lebih fleksibel untuk data baru dengan nilai kontinu, tetapi perlu dioptimalkan lebih lanjut.


## Author
[Lusy Rohmadhoni](https://github.com/Lusy230) - 202110370311230

