
BLACKJACK GAME
Rianco Marcellino Andreas

17 Desember 2023

1. Pendahuluan
Pada tugas ini, dibangun sebuah permainan blackjack yang memberikan pengalaman bermain dengan komputer secara real-time. Dalam Tugas Akhir mata kuliah Pengolahan Citra Video, penulis menggunakan teknologi pengolahan citra untuk mendeteksi dan menyimpan kartu. Aturan permainan blackjack digunakan untuk menghitung nilai kartu (As = 11, J, K, Q = 10, kartu numerik = nilai kartu). Pemenang ditentukan berdasarkan pemain atau komputer yang mendekati nilai 21 tanpa melebihinya. Deteksi kartu dilakukan dengan bantuan Pengolahan Citra Video untuk mengidentifikasi kartu-kartu yang diperoleh oleh komputer. Pemain dan komputer dapat memilih untuk "hit" (minta kartu tambahan) atau "stand" (tinggal dengan kartu yang ada).

2. Alur Permainan
Permainan dimulai dengan pemain membagikan dua kartu kepada player. Player kemudian dapat melakukan aksi "Hit" atau "Stand" untuk menyimpan nilai kartu dengan menekan tombol spasi. Setelah kedua pihak menampilkan kartu, perbandingan nilai kartu dilakukan. Jika pemain melakukan "hit" dan nilai kartunya lebih dari 21, COM Player langsung menang. Jika nilai kartu pemain kurang dari atau sama dengan 21, COM akan terus mengambil kartu sampai mencapai nilai tertentu.


![image](https://github.com/marcelaritonang/DetectionCard_OPENCV/assets/62584017/46de7b7c-36b5-458d-9768-529a13e3b50d)
![image](https://github.com/marcelaritonang/DetectionCard_OPENCV/assets/62584017/ccda650c-95c3-47a3-ac38-585eb7897b47)
![image](https://github.com/marcelaritonang/DetectionCard_OPENCV/assets/62584017/a86da1c9-cf9e-4bf8-8b58-078e6c5de582)
![image](https://github.com/marcelaritonang/DetectionCard_OPENCV/assets/62584017/6bb628b2-79a8-414c-8179-ccf6eb781170)
![image](https://github.com/marcelaritonang/DetectionCard_OPENCV/assets/62584017/51348ba2-2c96-462f-ba20-5a0d65c083d1)
![image](https://github.com/marcelaritonang/DetectionCard_OPENCV/assets/62584017/f971a835-bc39-44b5-94b4-24209fabd3dd)<a name="br1"></a> 

Deteksi Kartu
Pada permainan blackjack ini, deteksi kartu dilakukan menggunakan teknologi Pengolahan Citra Video. Berikut adalah penjelasan mengenai proses deteksi kartu dalam permainan:

Inisialisasi dan Pengaturan Awal:

Pada awalnya, program melakukan inisialisasi beberapa parameter, termasuk frame rate dan pengaturan kamera.
Membuka kamera video dan memastikan bahwa kamera telah berhasil diakses.
Muat Gambar Latihan Nilai dan Jenis Kartu:

Memuat gambar-gambar kartu sebagai data latihan untuk mengenali nilai dan jenis kartu.
Loop Utama (Main Loop):

Program berjalan dalam loop utama yang terus-menerus mengambil frame dari aliran video.
Pra-pemrosesan gambar dilakukan untuk mengubahnya ke skala abu-abu, mengaburkan, dan menerapkan ambang adaptif.
Temukan dan Urutkan Kontur Kartu:

Menggunakan metode tertentu, program menemukan dan mengurutkan kontur dari kartu yang ada di frame.
Kontur yang diidentifikasi diurutkan dan disaring untuk memastikan bahwa hanya kontur kartu yang diakui.
Identifikasi Area Kartu Pemain, Area Hit, dan Area Kartu Komputer:

Berdasarkan status permainan (state), program menandai area untuk kartu pemain, area hit, dan area kartu komputer pada frame.
Menampilkan kotak dan teks yang menunjukkan area tersebut.
Loop Deteksi Kartu:

Program memulai loop untuk setiap kontur yang terdeteksi.
Memeriksa apakah kontur tersebut adalah kartu berdasarkan kriteria tertentu.
Pemilihan Kartu Pemain atau Kartu Komputer:

Program menentukan apakah kartu yang terdeteksi adalah kartu pemain atau kartu komputer berdasarkan posisi dan ukuran kartu.
Kartu pemain atau komputer yang terdeteksi akan ditambahkan ke daftar kartu.
Pencocokan Nilai dan Jenis Kartu:

Untuk setiap kartu yang terdeteksi, program mencocokkan nilai dan jenis terbaik dengan menggunakan gambar-gambar latihan.
Menyimpan hasil pencocokan dan perbedaan nilai atau jenis.
Menampilkan Hasil Pencocokan pada Frame:

Menambahkan titik tengah dan hasil pencocokan ke dalam frame untuk setiap kartu yang terdeteksi.
Menggambar kontur kartu pada frame.
Aksi Pemain dan Komputer:

Jika pemain memilih "hit," nilai kartu pemain akan diakumulasi.
Jika pemain memilih "stand," program akan menentukan aksi selanjutnya berdasarkan algoritma tertentu.
Proses ini diulang hingga pemain dan komputer melakukan "stand."
Perbandingan Kartu dan Penentuan Pemenang:

Setelah kedua pihak "stand," nilai kartu pemain dan komputer dibandingkan.
Pemenang ditentukan berdasarkan nilai kartu terdekat dengan 21 tanpa melebihi.
Menampilkan Hasil dan Aksi Selanjutnya:

Program menampilkan hasil permainan, apakah pemain menang, komputer menang, atau hasil seri.
Menampilkan instruksi atau pesan untuk aksi selanjutnya.
Interaksi Pengguna dan Pengakhiran Program:

Program memberikan instruksi kepada pengguna, seperti menekan spasi untuk menyimpan kartu atau tombol "q" untuk keluar dari permainan.
Saat pengguna menekan tombol keluar, program melepaskan aliran video dan menutup jendela.
Seluruh proses ini memastikan bahwa permainan blackjack berlangsung secara interaktif dengan deteksi kartu menggunakan Pengolahan Citra Video.

![image](https://github.com/marcelaritonang/DetectionCard_OPENCV/assets/62584017/59b605a6-5a0e-4fba-b09e-57a0b68db7b7)
![image](https://github.com/marcelaritonang/DetectionCard_OPENCV/assets/62584017/b920d964-4ffd-409e-bfcf-f1b6870b585b)





