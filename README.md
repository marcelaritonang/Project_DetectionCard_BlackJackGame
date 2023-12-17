
BLACKJACK GAME
Rianco Marcellino Andreas

17 Desember 2023

Pendahuluan
Tugas ini menghadirkan permainan blackjack interaktif yang memungkinkan pemain bermain secara real-time dengan komputer. Dalam konteks Tugas Akhir mata kuliah Pengolahan Citra Video, penulis mengembangkan program permainan kartu yang menggunakan teknologi pengolahan citra untuk mendeteksi dan menyimpan kartu. Aturan permainan didasarkan pada nilai kartu blackjack, dan deteksi kartu dilakukan secara otomatis melalui pengolahan citra.

Alur Permainan
1. Inisialisasi dan Pengaturan Awal
Program melakukan inisialisasi parameter, seperti frame rate dan pengaturan kamera.
Kamera video diakses dan disiapkan untuk pengambilan gambar.
2. Muat Gambar Latihan Nilai dan Jenis Kartu
Mengambil gambar-gambar kartu sebagai data latihan untuk proses pengenalan nilai dan jenis kartu.
3. Loop Utama (Main Loop)
Program berjalan dalam loop utama untuk terus-menerus mengambil frame dari aliran video.
4. Temukan dan Urutkan Kontur Kartu
Menggunakan metode tertentu, program menemukan dan mengurutkan kontur kartu pada setiap frame.
Kontur yang diidentifikasi diurutkan dan difilter agar hanya kontur kartu yang diakui.
5. Identifikasi Area Kartu Pemain, Area Hit, dan Area Kartu Komputer
Berdasarkan status permainan (state), program menandai area untuk kartu pemain, area hit, dan area kartu komputer pada frame.
Kotak dan teks ditampilkan untuk memvisualisasikan area tersebut.
6. Loop Deteksi Kartu
Program memulai loop untuk setiap kontur yang terdeteksi.
Memeriksa apakah kontur tersebut sesuai dengan kriteria kartu.
7. Pemilihan Kartu Pemain atau Kartu Komputer
Program menentukan apakah kartu yang terdeteksi adalah kartu pemain atau kartu komputer berdasarkan posisi dan ukuran kartu.
Kartu pemain atau komputer yang terdeteksi akan ditambahkan ke daftar kartu.
8. Pencocokan Nilai dan Jenis Kartu
Untuk setiap kartu yang terdeteksi, program mencocokkan nilai dan jenis dengan menggunakan gambar-gambar latihan.
Hasil pencocokan dan perbedaan nilai atau jenis disimpan.
9. Menampilkan Hasil Pencocokan pada Frame
Titik tengah dan hasil pencocokan ditambahkan ke dalam frame untuk setiap kartu yang terdeteksi.
Kontur kartu digambar pada frame.
10. Aksi Pemain dan Komputer
Jika pemain memilih "hit," nilai kartu pemain diakumulasi.
Jika pemain memilih "stand," program menentukan aksi selanjutnya berdasarkan algoritma tertentu.
Proses ini diulang hingga pemain dan komputer melakukan "stand."
11. Perbandingan Kartu dan Penentuan Pemenang
Setelah kedua pihak "stand," nilai kartu pemain dan komputer dibandingkan.
Pemenang ditentukan berdasarkan nilai kartu terdekat dengan 21 tanpa melebihi.
12. Menampilkan Hasil dan Aksi Selanjutnya
Program menampilkan hasil permainan, apakah pemain menang, komputer menang, atau hasil seri.
Instruksi atau pesan untuk aksi selanjutnya ditampilkan.
13. Interaksi Pengguna dan Pengakhiran Program
Program memberikan instruksi kepada pengguna, seperti menekan spasi untuk menyimpan kartu atau tombol "q" untuk keluar dari permainan.
Saat pengguna menekan tombol keluar, program melepaskan aliran video dan menutup jendela.
Seluruh proses ini dirancang untuk menciptakan pengalaman bermain blackjack yang interaktif dengan deteksi kartu menggunakan Pengolahan Citra Video.

![image](https://github.com/marcelaritonang/DetectionCard_OPENCV/assets/62584017/46de7b7c-36b5-458d-9768-529a13e3b50d)
![image](https://github.com/marcelaritonang/DetectionCard_OPENCV/assets/62584017/ccda650c-95c3-47a3-ac38-585eb7897b47)
![image](https://github.com/marcelaritonang/DetectionCard_OPENCV/assets/62584017/a86da1c9-cf9e-4bf8-8b58-078e6c5de582)
![image](https://github.com/marcelaritonang/DetectionCard_OPENCV/assets/62584017/6bb628b2-79a8-414c-8179-ccf6eb781170)
![image](https://github.com/marcelaritonang/DetectionCard_OPENCV/assets/62584017/51348ba2-2c96-462f-ba20-5a0d65c083d1)
![image](https://github.com/marcelaritonang/DetectionCard_OPENCV/assets/62584017/f971a835-bc39-44b5-94b4-24209fabd3dd)<a name="br1"></a> 



![image](https://github.com/marcelaritonang/DetectionCard_OPENCV/assets/62584017/59b605a6-5a0e-4fba-b09e-57a0b68db7b7)
![image](https://github.com/marcelaritonang/DetectionCard_OPENCV/assets/62584017/b920d964-4ffd-409e-bfcf-f1b6870b585b)





