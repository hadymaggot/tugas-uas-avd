# Laporan Proyek Dashboard Data Video YouTube

## BAB I PENDAHULUAN

### 1.1 Latar Belakang

Pertumbuhan platform YouTube yang pesat telah menjadikannya sumber data yang kaya untuk memahami tren video dan perilaku penonton.  Analisis data video YouTube dapat memberikan wawasan berharga bagi para pembuat konten, pemasar, dan peneliti.  Dashboard interaktif dapat memfasilitasi eksplorasi data ini secara lebih mudah dan efektif.

### 1.2 Tujuan Proyek

Tujuan dari proyek ini adalah untuk mengembangkan dashboard interaktif yang memvisualisasikan data dari 1000 video YouTube terpopuler. Dashboard ini akan memungkinkan pengguna untuk menganalisis metrik kunci seperti jumlah penayangan, suka, tidak suka, dan komentar berdasarkan kategori video.

### 1.3 Ruang Lingkup

Ruang lingkup proyek ini meliputi:

*   Pengumpulan data dari 1000 video YouTube terpopuler.
*   Pembersihan dan persiapan data.
*   Pengembangan dashboard interaktif menggunakan Dash.
*   Visualisasi data menggunakan grafik dan tabel.

## BAB II TINJAUAN PUSTAKA

### 2.1 Konsep Analisis dan Visualisasi Data

Analisis data adalah proses pemeriksaan, pembersihan, transformasi, dan pemodelan data dengan tujuan untuk menemukan informasi yang berguna, menginformasikan kesimpulan, dan mendukung pengambilan keputusan. Visualisasi data adalah representasi grafis dari informasi dan data.  Dengan menggunakan elemen visual seperti grafik, diagram, dan peta, visualisasi data menyediakan cara yang mudah diakses untuk melihat dan memahami tren, outlier, dan pola dalam data.

### 2.2 Metode Analisis Data

Metode analisis data yang digunakan dalam proyek ini adalah analisis deskriptif. Analisis deskriptif digunakan untuk meringkas dan menggambarkan karakteristik utama dari dataset.  Dalam proyek ini, analisis deskriptif digunakan untuk menghitung statistik seperti rata-rata, total, dan jumlah video untuk setiap kategori.

### 2.3 Alat dan Teknologi

Alat dan teknologi yang digunakan dalam proyek ini adalah:

*   **Python:** Bahasa pemrograman yang digunakan untuk analisis data dan pengembangan dashboard.
*   **Pandas:** Pustaka Python untuk manipulasi dan analisis data.
*   **Plotly:** Pustaka Python untuk membuat visualisasi data interaktif.
*   **Dash:** Framework Python untuk membangun aplikasi web analitik.

### 2.4 Studi Kasus Serupa

Terdapat banyak studi kasus serupa yang menggunakan analisis data dan visualisasi untuk mengeksplorasi data YouTube.  Studi-studi ini menunjukkan manfaat dari visualisasi data dalam memahami tren dan pola pada platform YouTube.

## BAB III METODOLOGI

### 3.1 Pemilihan Dataset

Dataset yang digunakan dalam proyek ini berisi informasi tentang 1000 video YouTube terpopuler. Dataset ini diperoleh dari [kaggle.com](https://www.kaggle.com/datasets/samithsachidanandan/most-popular-1000-youtube-videos).

### 3.2 Tahapan Analisa Data

Tahapan analisis data dalam proyek ini meliputi:

1.  **Pengumpulan Data:** Mengumpulkan data dari sumber yang telah ditentukan.
2.  **Pembersihan Data:** Membersihkan data dari nilai yang hilang dan inkonsistensi.
3.  **Transformasi Data:** Mengubah data ke dalam format yang sesuai untuk visualisasi.
4.  **Visualisasi Data:** Membuat visualisasi data menggunakan Plotly dan Dash.

### 3.3 Tools dan Teknologi yang Digunakan

Tools dan teknologi yang digunakan dalam proyek ini dijelaskan pada Bab II.

## BAB IV IMPLEMENTASI DAN HASIL

### 4.1 Eksplorasi Data dan Visualisasi

Dashboard yang dikembangkan dalam proyek ini menyediakan beberapa visualisasi data, antara lain:

*   **Tabel Video:** Menampilkan informasi detail tentang setiap video, termasuk judul, kategori, jumlah penayangan, suka, tidak suka, dan komentar.  Tabel ini interaktif dan memungkinkan pengguna untuk mengurutkan data berdasarkan kolom yang berbeda.

*   **Tabel Statistik Kategori:** Menampilkan statistik ringkasan untuk setiap kategori, termasuk rata-rata penayangan, total penayangan, jumlah video, rata-rata suka, total suka, rata-rata tidak suka, dan total tidak suka.

*   **Grafik Batang Rata-rata Penayangan:** Menampilkan rata-rata penayangan untuk setiap kategori dalam bentuk grafik batang.  Grafik ini memungkinkan pengguna untuk membandingkan popularitas video di berbagai kategori.  *Contoh: Grafik batang dengan kategori di sumbu x dan rata-rata penayangan di sumbu y.*

*   **Grafik Batang Total Penayangan:** Menampilkan total penayangan untuk setiap kategori dalam bentuk grafik batang.  *Contoh: Grafik batang dengan kategori di sumbu x dan total penayangan di sumbu y.*

*   **Grafik Batang Rata-rata Suka:** Menampilkan rata-rata suka untuk setiap kategori dalam bentuk grafik batang.  *Contoh: Grafik batang dengan kategori di sumbu x dan rata-rata suka di sumbu y.*

*   **Grafik Batang Total Suka:** Menampilkan total suka untuk setiap kategori dalam bentuk grafik batang.  *Contoh: Grafik batang dengan kategori di sumbu x dan total suka di sumbu y.*

*   **Grafik Batang Rata-rata Tidak Suka:** Menampilkan rata-rata tidak suka untuk setiap kategori dalam bentuk grafik batang.  *Contoh: Grafik batang dengan kategori di sumbu x dan rata-rata tidak suka di sumbu y.*

*   **Grafik Batang Total Tidak Suka:** Menampilkan total tidak suka untuk setiap kategori dalam bentuk grafik batang.  *Contoh: Grafik batang dengan kategori di sumbu x dan total tidak suka di sumbu y.*

*   **Grafik Pie Jumlah Video:** Menampilkan proporsi jumlah video untuk setiap kategori dalam bentuk grafik pie.  Grafik ini memberikan gambaran umum tentang distribusi video di berbagai kategori. *Contoh: Grafik pie dengan setiap potongan mewakili kategori dan ukuran potongan sesuai dengan jumlah video dalam kategori tersebut.*

### 4.2 Analisis Hasil

Hasil visualisasi data menunjukkan bahwa kategori tertentu memiliki jumlah penayangan, suka, dan tidak suka yang lebih tinggi dibandingkan kategori lainnya.  Analisis lebih lanjut dapat dilakukan untuk memahami faktor-faktor yang memengaruhi popularitas video di setiap kategori.

## BAB V KESIMPULAN DAN SARAN

### 5.1 Kesimpulan

Dashboard interaktif yang dikembangkan dalam proyek ini berhasil memvisualisasikan data dari 1000 video YouTube terpopuler.  Dashboard ini memberikan wawasan yang berguna tentang tren video dan perilaku penonton.

### 5.2 Saran

Untuk pengembangan selanjutnya, disarankan untuk menambahkan fitur-fitur berikut:

*   Integrasi dengan data real-time.
*   Analisis sentimen pada komentar video.
*   Prediksi tren video di masa mendatang.

## DAFTAR PUSTAKA

kaggle.com
[https://www.kaggle.com/datasets/samithsachidanandan/most-popular-1000-youtube-videos](https://www.kaggle.com/datasets/samithsachidanandan/most-popular-1000-youtube-videos)

## LAMPIRAN

### Screenshot

![image](https://github.com/user-attachments/assets/3dc5083a-303e-4bf7-81fd-a3db7284f96e)

![image](https://github.com/user-attachments/assets/190d4f8c-ca93-4e4a-836a-53137af51e0e)

![image](https://github.com/user-attachments/assets/7b44145c-4600-4da5-862d-873406f5789a)

![image](https://github.com/user-attachments/assets/256762a0-1f25-4437-bc83-98555531ec12)

![image](https://github.com/user-attachments/assets/5d2cd6a9-3110-4adb-ab3f-665b49178fcf)

![image](https://github.com/user-attachments/assets/1122b23e-680b-4d6e-ae67-670c10d0c8b0)

![image](https://github.com/user-attachments/assets/bc88d7a9-1a18-4683-a1fb-e4288d92cb86)

![image](https://github.com/user-attachments/assets/9d77d3da-d000-4a2f-abc0-1075b6b2d562)

![image](https://github.com/user-attachments/assets/76f520f6-ec4f-43da-b9a8-5d670759ffee)
