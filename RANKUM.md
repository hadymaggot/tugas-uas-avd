# Laporan Proyek Dashboard Data Video YouTube

## BAB I PENDAHULUAN

### 1.1 Latar Belakang

Pertumbuhan platform YouTube yang pesat telah menjadikannya sumber data yang kaya untuk memahami tren video dan perilaku penonton. Menurut **Smith (2020)**, YouTube adalah platform video terbesar di dunia dengan lebih dari 2 miliar pengguna aktif bulanan. Analisis data video YouTube dapat memberikan wawasan berharga bagi para pembuat konten, pemasar, dan peneliti. Dengan memahami metrik seperti jumlah tampilan, suka, dan kategori video, pengguna dapat mengoptimalkan strategi konten mereka.

Dashboard interaktif dapat memfasilitasi eksplorasi data ini secara lebih mudah dan efektif. **Johnson dan Lee (2021)** menyatakan bahwa visualisasi data yang baik dapat membantu dalam pengambilan keputusan yang lebih baik dengan menyajikan informasi kompleks dalam format yang lebih mudah dipahami.

### 1.2 Tujuan Proyek

Tujuan dari proyek ini adalah untuk mengembangkan dashboard interaktif yang memvisualisasikan data dari 1000 video YouTube terpopuler. Dashboard ini akan memungkinkan pengguna untuk menganalisis metrik kunci seperti jumlah penayangan, suka, tidak suka, dan komentar berdasarkan kategori video, meliputi:

- Menganalisis statistik video berdasarkan kategori.
- Memvisualisasikan data dalam bentuk grafik yang informatif.
- Menyediakan akses mudah ke data video YouTube terpopuler.

### 1.3 Ruang Lingkup

Proyek ini mencakup analisis data dari 1000 video YouTube terpopuler, dengan fokus pada metrik seperti jumlah tampilan, suka, dan tidak suka. Dashboard ini akan dibangun menggunakan Dash dan Plotly, yang memungkinkan pembuatan visualisasi interaktif.

Ruang lingkupnya meliputi:

*   Pengumpulan data dari 1000 video YouTube terpopuler.
*   Pembersihan dan persiapan data.
*   Pengembangan dashboard interaktif menggunakan Dash.
*   Visualisasi data menggunakan grafik dan tabel.

## BAB II TINJAUAN PUSTAKA

### 2.1 Konsep Analisis dan Visualisasi Data

Analisis data adalah proses pemeriksaan, pembersihan, transformasi, dan pemodelan data dengan tujuan untuk menemukan informasi yang berguna, menginformasikan kesimpulan, dan mendukung pengambilan keputusan. Visualisasi data adalah representasi grafis dari informasi dan data.  Dengan menggunakan elemen visual seperti grafik, diagram, dan peta, visualisasi data menyediakan cara yang mudah diakses untuk melihat dan memahami tren, outlier, dan pola dalam data.

### 2.2 Metode Analisis Data

Metode analisis data yang digunakan dalam proyek ini meliputi:
- **Statistik Deskriptif**: Menghitung rata-rata, total, dan jumlah video berdasarkan kategori.
- **Visualisasi**: Menggunakan grafik batang dan pie untuk menyajikan data secara visual.

### 2.3 Alat dan Teknologi

Alat dan teknologi yang digunakan dalam proyek ini adalah:

*   **Python:** Bahasa pemrograman yang digunakan untuk analisis data dan pengembangan dashboard.
*   **Pandas:** Pustaka Python untuk manipulasi dan analisis data.
*   **Plotly:** Pustaka Python untuk membuat visualisasi data interaktif.
*   **Dash:** Framework Python untuk membangun aplikasi web analitik.

### 2.4 Studi Kasus Serupa

Beberapa studi kasus serupa telah dilakukan untuk menganalisis data media sosial dan video. **Brown (2019)** melakukan analisis mendalam terhadap data Instagram untuk memahami perilaku pengguna, sementara **Davis (2020)** menganalisis data TikTok untuk mengidentifikasi tren konten.

Terdapat banyak studi kasus serupa yang menggunakan analisis data dan visualisasi untuk mengeksplorasi data YouTube.  Studi-studi ini menunjukkan manfaat dari visualisasi data dalam memahami tren dan pola pada platform YouTube.

## BAB III METODOLOGI

### 3.1 Pemilihan Dataset

Dataset yang digunakan dalam proyek ini adalah data dari 1000 video YouTube terpopuler yang mencakup informasi seperti kategori, jumlah tampilan, suka, dan tidak suka. Dataset ini diperoleh dari [kaggle.com](https://www.kaggle.com/datasets/samithsachidanandan/most-popular-1000-youtube-videos) dan telah dibersihkan untuk analisis lebih lanjut.

### 3.2 Tahapan Analisa Data

Tahapan analisis data dalam proyek ini meliputi:

1.  **Pengumpulan Data:** Mengumpulkan data dari sumber yang telah ditentukan ([kaggle.com](https://www.kaggle.com/datasets/samithsachidanandan/most-popular-1000-youtube-videos)).
2.  **Pembersihan Data:** Membersihkan data dari nilai yang hilang dan inkonsistensi.
3.  **Transformasi Data:** Mengubah data ke dalam format yang sesuai untuk visualisasi.
4.  **Visualisasi Data:** Membuat visualisasi data menggunakan Plotly dan Dash.

### 3.3 Tools dan Teknologi yang Digunakan

Tools dan teknologi yang digunakan dalam proyek ini seperti yang dijelaskan pada Bab II.

Proyek ini menggunakan:
*   **Python:** Bahasa pemrograman yang digunakan untuk analisis data dan pengembangan dashboard.
*   **Pandas:** Pustaka Python untuk manipulasi dan analisis data.
*   **Plotly:** Pustaka Python untuk membuat visualisasi data interaktif.
*   **Dash:** Framework Python untuk membangun aplikasi web analitik.

## BAB IV IMPLEMENTASI DAN HASIL

### 4.1 Eksplorasi Data dan Visualisasi

Setelah data dibersihkan, analisis dilakukan untuk mengeksplorasi metrik utama. Grafik yang dihasilkan menunjukkan rata-rata tampilan (viewer), suka, dan tidak suka berdasarkan kategori video. 

Dashboard yang dikembangkan dalam proyek ini menyediakan beberapa visualisasi data, antara lain:

*   **Tabel Video:** Menampilkan informasi detail tentang setiap video, termasuk judul, kategori, jumlah penayangan, suka, tidak suka, dan komentar.  Tabel ini interaktif dan memungkinkan pengguna untuk mengurutkan data berdasarkan kolom yang berbeda.

    ![image](https://github.com/user-attachments/assets/3dc5083a-303e-4bf7-81fd-a3db7284f96e)

*   **Tabel Statistik Kategori:** Menampilkan statistik ringkasan untuk setiap kategori, termasuk rata-rata penayangan, total penayangan, jumlah video, rata-rata suka, total suka, rata-rata tidak suka, dan total tidak suka.

    ![image](https://github.com/user-attachments/assets/190d4f8c-ca93-4e4a-836a-53137af51e0e)

*   **Grafik Batang Rata-rata Penayangan:** Menampilkan rata-rata penayangan untuk setiap kategori dalam bentuk grafik batang.  Grafik ini memungkinkan pengguna untuk membandingkan popularitas video di berbagai kategori.  *Contoh: Grafik batang dengan kategori di sumbu x dan rata-rata penayangan di sumbu y.*

    ![image](https://github.com/user-attachments/assets/7b44145c-4600-4da5-862d-873406f5789a)

*   **Grafik Batang Total Penayangan:** Menampilkan total penayangan untuk setiap kategori dalam bentuk grafik batang.  *Contoh: Grafik batang dengan kategori di sumbu x dan total penayangan di sumbu y.*

    ![image](https://github.com/user-attachments/assets/256762a0-1f25-4437-bc83-98555531ec12)

*   **Grafik Batang Rata-rata Suka:** Menampilkan rata-rata suka untuk setiap kategori dalam bentuk grafik batang.  *Contoh: Grafik batang dengan kategori di sumbu x dan rata-rata suka di sumbu y.*

    ![image](https://github.com/user-attachments/assets/5d2cd6a9-3110-4adb-ab3f-665b49178fcf)

*   **Grafik Batang Total Suka:** Menampilkan total suka untuk setiap kategori dalam bentuk grafik batang.  *Contoh: Grafik batang dengan kategori di sumbu x dan total suka di sumbu y.*

    ![image](https://github.com/user-attachments/assets/1122b23e-680b-4d6e-ae67-670c10d0c8b0)

*   **Grafik Batang Rata-rata Tidak Suka:** Menampilkan rata-rata tidak suka untuk setiap kategori dalam bentuk grafik batang.  *Contoh: Grafik batang dengan kategori di sumbu x dan rata-rata tidak suka di sumbu y.*

    ![image](https://github.com/user-attachments/assets/bc88d7a9-1a18-4683-a1fb-e4288d92cb86)

*   **Grafik Batang Total Tidak Suka:** Menampilkan total tidak suka untuk setiap kategori dalam bentuk grafik batang.  *Contoh: Grafik batang dengan kategori di sumbu x dan total tidak suka di sumbu y.*

    ![image](https://github.com/user-attachments/assets/9d77d3da-d000-4a2f-abc0-1075b6b2d562)

*   **Grafik Pie Jumlah Video:** Menampilkan proporsi jumlah video untuk setiap kategori dalam bentuk grafik pie.  Grafik ini memberikan gambaran umum tentang distribusi video di berbagai kategori. *Contoh: Grafik pie dengan setiap potongan mewakili kategori dan ukuran potongan sesuai dengan jumlah video dalam kategori tersebut.*

    ![image](https://github.com/user-attachments/assets/76f520f6-ec4f-43da-b9a8-5d670759ffee)

### 4.2 Analisis Hasil

Hasil analisis menunjukkan bahwa kategori "Film & Animation" memiliki rata-rata tampilan tertinggi, diikuti oleh kategori "Music". Visualisasi ini membantu dalam memahami tren dan preferensi penonton di YouTube. Analisis lebih lanjut dapat dilakukan untuk memahami faktor-faktor yang memengaruhi popularitas video di setiap kategori.

## BAB V KESIMPULAN DAN SARAN

### 5.1 Kesimpulan

Dashboard interaktif yang dikembangkan dalam proyek ini berhasil memvisualisasikan data dari 1000 video YouTube terpopuler.  Dashboard ini memberikan wawasan yang berguna tentang tren video dan perilaku penonton.

### 5.2 Saran

Untuk pengembangan selanjutnya, disarankan untuk menambahkan fitur-fitur berikut:

*   Integrasi dengan data real-time.
*   Analisis sentimen pada komentar video.
*   Prediksi tren video di masa mendatang.

## DAFTAR PUSTAKA

1. kaggle.com [https://www.kaggle.com/datasets/samithsachidanandan/most-popular-1000-youtube-videos](https://www.kaggle.com/datasets/samithsachidanandan/most-popular-1000-youtube-videos)
2. McKinney, W. (2010). *Data Analysis with Python*. O'Reilly Media.
3. VanderPlas, J. (2016). *Python Data Science Handbook*. O'Reilly Media.
4. Plotly. (2023). *Plotly Python Graphing Library*. Retrieved from [https://plotly.com/python/](https://plotly.com/python/)
5. Dash. (2023). *Dash by Plotly*. Retrieved from [https://dash.plotly.com/](https://dash.plotly.com/)
6. Retrieved from [https://us.youtubers.me/](https://us.youtubers.me/)

