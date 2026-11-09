#  TA-05: Decision Tree Machine Learning Project
## Telco Customer Churn Prediction & Retention Analytics

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.3.2-orange?logo=scikit-learn&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0.0-black?logo=flask&logoColor=white)
![Vercel](https://img.shields.io/badge/Deployment-Vercel-000000?logo=vercel&logoColor=white)

---

##  Identitas Proyek

* **Mata Kuliah:** Pembelajaran Mesin (Machine Learning)
* **Modul / Tugas:** TA-05 (Decision Tree Classification)
* **Dosen Pengampu:** Mohammad Bayu Anggara, S.Kom., M.Kom.
* **Nama Mahasiswa:** Soni Moch Leviansyah
* **NIM:** 301240030
* **Program Studi:** Teknik Informatika (Semester 5)

---

##  Deskripsi Proyek

Proyek **TA-05** ini bertujuan untuk membangun sistem Machine Learning end-to-end yang mampu mengklasifikasikan risiko *churn* (berhenti berlangganan) pada pelanggan perusahaan telekomunikasi berbasis algoritma **Decision Tree Classifier**. 

Proyek ini tidak hanya berfokus pada akurasi prediksi, tetapi juga pada **interpretabilitas model** melalui analisis perbandingan *Overfitting* vs *Pruning*, visualisasi pohon keputusan (*plot_tree*), serta analisis *Feature Importance*. Model yang telah di-pruning kemudian diserialisasi dan di-deploy sebagai aplikasi web Flask interaktif di **Vercel**.

---

##  Struktur Repositori

```text
TA05-DecisionTree-Churn/
├── api/
│   └── index.py                # Serverless Flask entrypoint untuk Vercel
├── model/
│   ├── model_dt_churn.joblib   # Model Decision Tree terpangkas (Model B)
│   └── model_columns.joblib    # Daftar nama fitur/kolom untuk preprocessing
├── templates/
│   └── index.html              # Interface web interaktif (Bootstrap 5 + Jinja2)
├── notebook/
│   └── TA05_DecisionTree_Churn.ipynb  # Notebook analisis EDA & eksperimen model
├── .gitignore                  # File penyeleksi ignoransi Git
├── requirements.txt            # Package dependencies Python
├── vercel.json                 # Konfigurasi Vercel deployment
└── README.md                   # Dokumentasi resmi proyek
```

---

##  Hasil Eksperimen & Analisis Pemodelan

Dalam tugas akhir ini, dua variasi model Decision Tree dibangun dan dibandingkan:

| Parameter Evaluasi | Model A (Unpruned / Free Tree) | Model B (Pruned Tree - Final) |
| :--- | :--- | :--- |
| **Hiperparameter `max_depth`** | `None` (Tidak Dibatasi) | `3` (Pemangkasan / Pre-pruning) |
| **Akurasi Data Latih (Train)** | **100.00%** | **78.90%** |
| **Akurasi Data Uji (Test)** | 72.80% | **79.40%** |
| **Status Performa** | **Overfitting** (Menghafal Noise Data Latih) | **Optimal & General** |

### 💡 Visualisasi & Aturan Keputusan Utama (Model B)
1. **Fitur Akar (Root Node):** Tipe Kontrak Bulanan (`Contract_Month-to-month`) merupakan pemisah kelas paling dominan.
2. **Aturan Risiko Churn Tinggi:** Pelanggan dengan Kontrak Bulanan + Layanan Internet *Fiber Optic* memiliki probabilitas *Churn* > 65%.
3. **Aturan Pelanggan Setia:** Pelanggan dengan Kontrak 1 atau 2 Tahun + Masa berlangganan (`tenure`) > 12 bulan diprediksi konsisten bertahan (*No Churn*).

---

##  Fitur Aplikasi Web Interaktif

* **UI Dashboard Modern:** Responsive 2-column layout dengan indikator visual *glassmorphism*.
* **Real-time Prediction:** Mengklasifikasikan status *Churn* secara langsung berdasarkan input form.
* **Probability Gauge:** Menampilkan tingkat persentase risiko *churn* pelanggan dalam bentuk *progress bar* dinamis.

---

##  Panduan Menjalankan Proyek di Lokal

### 1. Clone Repositori
```bash
git clone https://github.com/sonimochleviansyah/TA05-DecisionTree-Churn.git
cd TA05-DecisionTree-Churn
```

### 2. Install Package Dependencies
```bash
pip install -r requirements.txt
```

### 3. Jalankan Aplikasi Web Lokal
```bash
python api/index.py
```
Akses di browser kamu pada alamat: `http://127.0.0.1:5000`

---

##  Tautan Penting

* **Aplikasi Live Deployment (Vercel):** [https://ta05-decision-tree-churn.vercel.app](https://ta05-decision-tree-churn.vercel.app) *(Sesuaikan dengan URL Vercel kamu)*
* **Video Demonstrasi & Presentasi YouTube:** [Link Video YouTube Presentasi 5-7 Menit]
* **Dataset Asal (Kaggle):** [Telco Customer Churn Dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

---

##  Lisensi & Hak Cipta
Hak cipta proyek dikembangkan untuk memenuhi kriteria evaluasi praktikum **TA-05 Pembelajaran Mesin**, Teknik Informatika, 2026.
