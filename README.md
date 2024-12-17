# **Technical Report: HandTweak - Pengendalian Image Processing dengan Gerakan Tangan**

---

## **1. Overview**

Proyek **HandTweak** adalah implementasi pemrosesan gambar yang dikendalikan oleh gerakan tangan, menggunakan jarak antara jari ibu dan jari telunjuk untuk mengatur berbagai efek gambar, seperti *blur*, *brightness*, dan *contrast*. Gerakan tangan ini dideteksi melalui kamera, dan efek gambar akan disesuaikan berdasarkan perubahan jarak antara kedua jari tersebut. Proyek ini tidak membutuhkan perangkat keras tambahan selain kamera untuk mendeteksi gerakan tangan dan mengubah pengaturan gambar secara dinamis.

---

## **2. Motivation**

Pengembangan antarmuka pengguna yang dapat dikendalikan tanpa perangkat input eksternal, seperti mouse atau keyboard, merupakan tantangan menarik dalam desain interaksi. **HandTweak** menawarkan solusi untuk mengendalikan efek gambar dengan cara yang lebih alami dan intuitif menggunakan deteksi posisi tangan. Dengan mengukur jarak antara jari telunjuk dan ibu jari, pengguna dapat mengatur intensitas efek seperti *blur*, *brightness*, dan *contrast*, memberikan kontrol yang lebih fleksibel dalam pengeditan gambar.

---

## **3. Success Metrics**

- **Akurasi Deteksi Jarak**: Keakuratan deteksi jarak antara jari telunjuk dan ibu jari dalam mengendalikan intensitas efek gambar.
- **Responsivitas Antarmuka**: Waktu respons dari sistem terhadap perubahan jarak tangan dalam melakukan perubahan pada gambar.

---

## **4. Requirements & Constraints**

### **4.1 Functional Requirements**

1. **Deteksi Jarak Tangan**: Menggunakan kamera untuk mendeteksi posisi jari telunjuk dan ibu jari.
2. **Pemrosesan Gambar**: Implementasi efek gambar seperti *blur*, *brightness*, dan *contrast* yang dikendalikan oleh jarak antara kedua jari.
3. **Antarmuka Pengguna**: Menampilkan efek yang dapat dipilih dengan mengubah jarak antara jari telunjuk dan ibu jari.
4. **Visualisasi Hasil**: Menampilkan gambar yang telah diproses sesuai dengan perubahan jarak tangan secara real-time.

### **4.2 Constraints**

- **Ketergantungan Kamera**: Menggunakan kamera untuk mendeteksi posisi tangan, yang dapat dipengaruhi oleh kondisi pencahayaan dan kualitas gambar.
- **Pengolahan Gambar Real-time**: Memastikan sistem dapat memproses gambar secara real-time tanpa latensi yang signifikan.
- **Ketepatan Penghitungan Jarak**: Keakuratan penghitungan jarak antara jari telunjuk dan ibu jari yang mempengaruhi efek gambar.

---

## **5. Methodology**

### **5.1 Problem Statement**

Proyek ini bertujuan untuk menyediakan kontrol berbasis gerakan tangan dengan mengukur jarak antara jari telunjuk dan ibu jari untuk mengendalikan efek pemrosesan gambar secara dinamis. Masalahnya adalah bagaimana mendeteksi jarak tersebut secara akurat dan menghubungkannya dengan intensitas efek gambar.

### **5.2 Data**

- **Sumber Data**: Gambar yang diambil langsung dari kamera untuk pemrosesan gambar secara real-time.
- **Jumlah Data**: Data berupa gambar yang diproses setiap kali pengguna melakukan gerakan tangan.
- **Preprocessing**:  
  - Pengolahan gambar dalam format RGB untuk pemrosesan.
  - Deteksi tangan dan posisi jari menggunakan pustaka MediaPipe.

### **5.3 Techniques**

1. **Hand Tracking**:  
   - Menggunakan MediaPipe untuk melacak posisi tangan dan jari.
   - Menghitung jarak antara jari telunjuk (ID 8) dan ibu jari (ID 4) untuk mengendalikan efek gambar.

2. **Image Processing**:  
   - **Blur**: Mengubah intensitas blur berdasarkan jarak antara jari telunjuk dan ibu jari.
   - **Brightness**: Mengubah kecerahan gambar berdasarkan jarak antara jari telunjuk dan ibu jari.
   - **Contrast**: Mengubah kontras gambar sesuai dengan jarak antara kedua jari.

3. **User Interface**:  
   - Menampilkan efek-efek gambar yang dapat diubah dengan menggerakkan tangan dan menghitung jarak antar jari.

---

## **6. Architecture**

Proyek ini menggunakan arsitektur berbasis deteksi tangan dengan MediaPipe dan pemrosesan gambar menggunakan OpenCV. Alur kerjanya adalah sebagai berikut:

1. Kamera menangkap gambar secara real-time.
2. MediaPipe digunakan untuk mendeteksi posisi tangan dan menghitung jarak antara jari telunjuk dan ibu jari.
3. Berdasarkan jarak tersebut, intensitas efek seperti *blur*, *brightness*, atau *contrast* diterapkan pada gambar.
4. Hasil pemrosesan gambar ditampilkan secara langsung di layar.

---

## **7. Results**

Proyek ini berhasil menyediakan kontrol pemrosesan gambar yang responsif dan interaktif hanya dengan menggunakan gerakan tangan. Jarak antara jari telunjuk dan ibu jari berfungsi sebagai pengukur intensitas efek seperti *blur*, *brightness*, dan *contrast*. Sistem ini memberikan pengalaman pengguna yang lebih intuitif tanpa perlu perangkat input tambahan.

---

## **8. Conclusion**

**HandTweak** adalah contoh implementasi inovatif dalam interaksi manusia-komputer, menggunakan gerakan tangan untuk mengontrol efek gambar. Dengan memanfaatkan deteksi jarak antara jari telunjuk dan ibu jari, proyek ini menawarkan kontrol berbasis gerakan tangan yang alami dan mudah diakses. Ini menunjukkan potensi besar untuk aplikasi pengolahan gambar berbasis interaksi tangan.

---

## **9. Future Work**

- **Peningkatan Akurasi Deteksi Jarak**: Mengoptimalkan sistem untuk mendeteksi jarak tangan dengan lebih tepat dalam berbagai kondisi pencahayaan.
- **Penambahan Efek Lain**: Menambahkan lebih banyak efek pemrosesan gambar yang dapat dikendalikan menggunakan gerakan tangan.
- **Pengujian Pengguna**: Melakukan pengujian lebih lanjut untuk mengevaluasi pengalaman pengguna dalam berbagai kondisi.

---

Semoga README ini sesuai dengan kebutuhan Anda untuk proyek **HandTweak**!
