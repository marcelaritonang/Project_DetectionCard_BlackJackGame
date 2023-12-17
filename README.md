<a name="br1"></a> 

LAPORAN DEMO AKHIR

BLACKJACK GAME

Rianco Marcellino Andreas

5024211061

17 Desemeber 2023

1 Pendahuluan

Pada tugas ini adalah permainan blackjack yang unik di mana pemain da-

pat bermain dengan komputer secara real-time. Pada Tugas Akhir mata ku-

liah Pengolahan Citra Video, penulis membuat program permainan kartu den-

gan menggunakan teknologi pengolahan citra untuk mendeteksi dan menyim-

pan kartu.dengan Aturan Permainan yaitu Penentuan Pemenang: Pemain dan

komputer masing-masing mendapatkan dua kartu awal. Nilai kartu dihitung

berdasarkan aturan blackjack (As = 11, J,K,Q = 10, kartu numerik = nilai

kartu). Pemain atau komputer yang mendekati nilai 21 tanpa melebihi akan

menjadi pemenang. Deteksi Kartu: Pada awal permainan, pemain dan kom-

puter mendapatkan dua kartu secara acak. Pengolahan Citra Video digunakan

untuk mendeteksi dan mengidentiﬁkasi kartu yang diperoleh oleh komputer.

ketika sudah menaruh dua kartu pada player bisa melakukan Pemain dapat

memilih untuk ”hit” (minta kartu tambahan) atau ”stand” (tinggal dengan

kartu yang ada). Komputer juga memutuskan apakah akan ”hit” atau ”stand”

berdasarkan algoritma tertentu. Perbandingan Kartu: Setelah kedua pihak

memutuskan untuk ”stand,” kartu pemain dan komputer dibandingkan. Peme-

nang ditentukan berdasarkan nilai kartu terdekat dengan 21 tanpa melebihi.

2 Alur Permainan

Game ini adalah sebuah permainan blackjack yang menggabungkan unsur de-

teksi kartu melalui pengolahan citra dengan game blackjack. Permainan dimu-

lai dengan pemain membagikan kartu dengan jumlah dua kartu kepada player.

Setelah itu, Player dapat melakukan Hit atau stand dan untuk menyimpan ni-

lai kartu dengan ’spasi’ maka ketika sudah stand maka yang dilakukan adalah

membandingkan.

Setelah kedua pihak menampilkan kartu, perbandingan nilai kartu dilakukan.

Jika Player melakukan hit sampai lebih dari ¿ 21 maka COM Player langsung

menang. Dan jika ¡ 21 maka COM terus melakukan pengambilan kartu sampai ¿

1



<a name="br2"></a> 

17 jika sudah maka berhenti dalam pengambilan kartu Jika sudah maka tinggal

tentukan apakah Player yang menang atau Com yang menang pada kartu.

3 Pembahasan Program Detection Card

3\.1 Liblary

import cv2

import numpy as np

import os

import time

3\.2 Class

Kelas ini digunakan untuk menyimpan informasi tentang gambar latihan dan

kartu yang ditemukan.

class Train\_ranks:

""" Struktur untuk menyimpan informasi tentang gambar latihan

nilai."""

def \_\_init\_\_(self):

[]

self.img

\=

\#

Gambar nilai yang diatur ukurannya yang

dimuat dari hard drive

self.name

\=

"Pemegang Tempat"

class Train\_suits:

""" Struktur untuk menyimpan informasi tentang gambar latihan

jenis."""

def \_\_init\_\_(self):

self.img

\=

[]

\#

Gambar jenis yang diatur ukurannya yang

dimuat dari hard drive

self.name

\=

"Pemegang Tempat"

\### Struktur untuk menyimpan informasi kartu kueri dan kartu

latihan ###

class Query\_card:

""" Struktur untuk menyimpan informasi tentang kartu kueri dalam

gambar kamera."""

def \_\_init\_\_(self):

self.contour

\=

[]

\#

Kontur kartu

0,

Titik sudut kartu

Titik tengah kartu

self.width , self.height

\=

0

\#

Lebar dan tinggi kartu

self.corner\_pts

\=

[]

\#

\#

self.center

self.warp

\=

[]

[]

\=

\=

\#

Gambar yang dihancurkan , abu -abu , dan

diburamkan berukuran

200x300

self.rank\_img

[]

\#

Gambar kartu dengan nilai yang diatur

ukurannya

2



<a name="br3"></a> 

self.suit\_img

\=

[]

\#

Gambar kartu dengan jenis yang diatur

ukurannya

self. best\_rank\_match

self. best\_suit\_match

\=

\=

"Tidak Diketahui"

\#

nilai terbaik

Pencocokan

"Tidak Diketahui" #

jenis terbaik

Pencocokan

self.rank\_diff

self.suit\_diff

\=

\=

0

0

\#

\#

Perbedaan antara gambar nilai dan

gambar latihan nilai

terbaik yang cocok

Perbedaan antara gambar jenis dan

gambar latihan jenis

terbaik yang cocok

3\.3 Inisialisasi Variabel

Konstanta dan variabel global yang digunakan untuk menentukan batas perbe-

daan nilai dan jenis kartu.

RANK\_DIFF\_MAX

SUIT\_DIFF\_MAX

CARD\_MAX\_AREA

CARD\_MIN\_AREA

\=

\=

\=

\=

2000

700

120000

25000

3\.4 Memuat Rank dan Suits

Figure 1: Enter Caption

Fungsi-fungsi ini digunakan untuk memuat gambar latihan nilai dan jenis

dari direktori yang ditentukan. Menyimpan Object Trains nilai dengan gambar

foto berikut ini

pada kode ini Fungsi loadranks(ﬁlepath) dalam program ini bertujuan un-

tuk memuat gambar-gambar yang mewakili nilai (rank) dari kartu remi. Fungsi

ini mengambil alamat direktori (ﬁlepath) di mana gambar-gambar ini disim-

pan. Kemudian, gambar-gambar tersebut dimuat dan disimpan dalam objek

Trainranks, yang kemudian akan digunakan dalam proses pengenalan kartu.

def load\_ranks(filepath):

3



<a name="br4"></a> 

""" Memuat gambar nilai dari direktori yang ditentukan oleh

filepath . Menyimpan

mereka dalam daftar objek Train\_ranks ."""

train\_ranks

i

\=

[]

\=

0

for Rank in [’Ace’,’Two’,’Three ’,’Four ’,’Five ’,’Six’,’Seven ’,

’Eight ’,’Nine ’,’Ten’,’Jack ’,’Queen ’,’King ’]:

train\_ranks.append(Train\_ranks ())

train\_ranks[i].name

filename Rank ’.jpg’

train\_ranks[i].img cv2.imread(filepath

IMREAD\_GRAYSCALE )

\=

Rank

\=

\+

\=

\+

filename , cv2.

i

\=

i

\+

1

return train\_ranks

def load\_suits(filepath):

""" Memuat gambar jenis dari direktori yang ditentukan oleh

filepath . Menyimpan

mereka dalam daftar objek Train\_suits ."""

train\_suits

i

\=

[]

\=

0

for Suit in [’Spades ’,’Diamonds ’,’Clubs ’,’Hearts ’]:

train\_suits.append(Train\_suits ())

train\_suits[i].name

filename Suit ’.jpg’

train\_suits[i].img cv2.imread(filepath+filename , cv2.

IMREAD\_GRAYSCALE )

\=

Suit

\=

\+

\=

i

\=

i

\+

1

3\.5 Preprocessing dan Card Detection

Fungsi-fungsi ini digunakan untuk memproses gambar kamera, mencari kontur

kartu, dan menentukan apakah suatu kontur adalah kartu.Menggunakan kontur

untuk menemukan informasi tentang kartu kueri. Mengisolasi gambar nilai dan

jenis dari kartu.

def preprocess\_image (image):

""" Mengembalikan gambar kamera yang diubah menjadi abu -abu ,

diburamkan , dan ambang

adaptif ."""

gray

blur

\=

\=

cv2.cvtColor(image ,cv2.COLOR\_BGR2GRAY)

cv2.GaussianBlur(gray ,(5,5),0)

\#

Tingkat ambang batas terbaik bergantung pada kondisi

pencahayaan sekitar .

\#

Untuk pencahayaan yang terang , ambang batas yang tinggi

harus digunakan untuk

mengisolasi kartu

4



<a name="br5"></a> 

\#

\#

dari latar belakang . Untuk pencahayaan redup , ambang batas

rendah harus digunakan .

Untuk membuat detektor kartu tidak bergantung pada kondisi

pencahayaan ,

metode ambang batas adaptif berikut digunakan .

\#

\#

\#

Piksel latar belakang di tengah atas gambar diambil

sampelnya untuk ditentukan

\#

\#

intensitasnya . Ambang batas adaptif ditetapkan pada 50

(

THRESH\_ADDER ) lebih tinggi

daripada itu. Hal ini memungkinkan ambang batas untuk

beradaptasi dengan kondisi

pencahayaan .

img\_w , img\_h

bkg\_level

thresh\_level

\=

np.shape(image)[:2]

gray[int(img\_h/100)][int(img\_w/2)]

bkg\_level BKG\_THRESH

\=

\=

\+

retval , thresh

return thresh

\=

cv2.threshold(blur ,thresh\_level ,255 ,cv2.

THRESH\_BINARY)

def find\_cards(thresh\_image):

""" Mencari semua kontur berukuran kartu dalam gambar kamera

yang telah diubah menjadi

ambang .

Mengembalikan jumlah kartu , dan daftar kontur kartu yang

diurutkan

dari yang terbesar hingga yang terkecil ."""

\#

cnts , hier

Find contours and sort their indices by contour size

\=

cv2.findContours(thresh\_image , cv2.RETR\_TREE , cv2.

CHAIN\_APPROX\_SIMPLE )

index\_sort

\=

sorted(range(len(cnts)), key=lambda

i

:

cv2.

contourArea(cnts[i]),reverse=

True)

\#

If there are no contours , do nothing

if len(cnts) == 0:

return [], []

\#

Otherwise , initialize empty sorted contour and hierarchy

lists

cnts\_sort

hier\_sort

\=

\=

[]

[]

\=

cnt\_is\_card

np.zeros(len(cnts),dtype=int)

\#

\#

\#

\#

Fill empty lists with sorted contour and sorted hierarchy .

Now ,

the indices of the contour list still correspond with those

of

the hierarchy list. The hierarchy array can be used to check

if

the contours have parents or not.

for

i in index\_sort:

cnts\_sort.append(cnts[i])

hier\_sort.append(hier[0][i])

5



<a name="br6"></a> 

\#

\#

Determine which of the contours are cards by applying the

following criteria : 1) Smaller area than the maximum card

size ,

2), bigger area than the minimum card size , 3) have no

parents ,

\#

\#

and 4) have four corners

for

i

in range(len(cnts\_sort)):

size

peri

\=

\=

cv2.contourArea(cnts\_sort[i])

cv2.arcLength(cnts\_sort[i],True)

approx

\=

cv2.approxPolyDP(cnts\_sort[i],0.01\*peri ,True)

if (( size

and (hier\_sort[i][3] == -1) and (len(approx) == 4)):

cnt\_is\_card[i]

<

CARD\_MAX\_AREA) and (size

\>

CARD\_MIN\_AREA)

\=

1

return cnts\_sort , cnt\_is\_card

1\. Fungsi preprocess image(image) Fungsi ini bertujuan untuk mengubah citra

dari kamera menjadi citra pra-pemrosesan yang lebih mudah untuk dianalisis.

Berikut adalah penjelasan mendetailnya:

cv2.cvtColor(image, cv2.COLORBGR2GRAY): Mengonversi citra ke skala

keabuan agar hanya terdapat satu saluran warna. Proses ini memudahkan untuk

melakukan operasi berikutnya.

cv2.GaussianBlur(gray, (5, 5), 0): Melakukan operasi blur menggunakan ﬁl-

ter Gaussian dengan kernel 5x5. Ini membantu mengurangi noise dan membuat

tepi objek lebih halus.

Ambang Adaptif:

imgw, imgh = np.shape(image)[:2]: Mendapatkan dimensi tinggi dan

lebar citra. bkglevel = gray[int(imgh/100)][int(imgw/2)]: Mengam-

bil sampel intensitas piksel latar belakang di tengah atas gambar.

threshlevel = bkglevel + BKGTHRESH: Menentukan ambang batas

adaptif berdasarkan intensitas latar belakang. cv2.threshold(blur, thresh-

level, 255, cv2.THRESHBINARY): Menggunakan ambang batas adaptif untuk

menghasilkan citra biner. Ambang batas ini disesuaikan dengan kondisi penca-

hayaan untuk mempertahankan deteksi kartu yang baik. Mengembalikan citra

hasil pra-pemrosesan dalam bentuk citra biner.

2\. Fungsi ﬁnd cards(thresh image) Fungsi ini bertujuan untuk menemukan

dan mengidentiﬁkasi kontur kartu pada citra yang telah diproses. Berikut

adalah penjelasan mendetailnya:

cv2.ﬁndContours(threshimage, cv2.RETRTREE, cv2.CHAINAPPROXSIMPLE):

Mencari semua kontur pada citra biner yang dihasilkan sebelumnya

dan mengurutkannya berdasarkan ukuran kontur.Pengurutan kontur

berdasarkan ukuran (area) dari yang terbesar ke yang terkecil. Membuat daf-

tar kontur dan daftar hierarki yang telah diurutkan. Menentukan kartu dengan

memeriksa kriteria berikut: Memiliki area lebih kecil dari ukuran maksimum

kartu (CARDMAXAREA). Memiliki area lebih besar dari ukuran minimum

kartu (CARDMINAREA). Tidak memiliki parent (hierarki [3] == -1). Memi-

6



<a name="br7"></a> 

liki empat sudut (kontur dengan panjang tepi sekitar 4). Mengembalikan daftar

kontur yang telah diurutkan dan daftar yang menunjukkan apakah kontur terse-

but adalah kartu atau bukan.

3\.6 Card Preprocessing and Matching

Figure 2: Enter Caption

1\.Menggunakan kontur untuk menemukan informasi tentang kartu kueri.

Mengisolasi gambar nilai dan jenis dari kartu. 2.Menemukan kecocokan pangkat

dan setelan terbaik untuk kartu kueri. Perbedaan peringkat kartu kueri dan

gambar setelan dengan peringkat kereta dan gambar setelan. Kecocokan terbaik

adalah gambar pangkat atau setelan yang memiliki perbedaan paling kecil.

def preprocess\_card (contour , image):

""" Menggunakan kontur untuk menemukan informasi tentang kartu

kueri. Mengisolasi gambar

nilai

dan jenis dari kartu."""

qCard

\=

Query\_card ()

qCard.contour

\=

contour

\#

Find perimeter of card and use it to approximate corner

points

peri

\=

cv2.arcLength(contour ,True)

cv2.approxPolyDP(contour ,0.01\*peri ,True)

np.float32(approx)

qCard.corner\_pts pts

approx

\=

pts

\=

\=

x,y,w,h

qCard.width , qCard.height

\=

cv2.boundingRect(contour)

w,

\=

h

average

\=

np.sum(pts , axis=0)/len(pts)

7



<a name="br8"></a> 

cent\_x

cent\_y

\=

\=

int(average[0][0])

int(average[0][1])

qCard.center

\=

[cent\_x , cent\_y]

qCard.warp

\=

flattener(image , pts , w, h)

Qcorner

Qcorner\_zoom

\=

qCard.warp[0:CORNER\_HEIGHT , 0:CORNER\_WIDTH]

\=

cv2.resize(Qcorner , (0,0), fx=4, fy=4)

\#

Sample known white pixel intensity to determine good

threshold level

white\_level

thresh\_level

\=

Qcorner\_zoom[15 ,int(( CORNER\_WIDTH\*4)/2)]

white\_level

\=

\-

CARD\_THRESH

if (thresh\_level <= 0):

thresh\_level

retval , query\_thresh

\=

1

\=

cv2.threshold(Qcorner\_zoom , thresh\_level

,

)

255 , cv2. THRESH\_BINARY\_INV

\#

Split in to top and bottom half (top shows rank , bottom shows

suit)

Qrank

Qsuit

\=

\=

query\_thresh[20:185 , 0:128]

query\_thresh[186:336 , 0:128]

\#

Find rank contour and bounding rectangle , isolate and find

largest contour

Qrank\_cnts , hier

\=

cv2.findContours(Qrank , cv2.RETR\_TREE , cv2.

CHAIN\_APPROX\_SIMPLE )

Qrank\_cnts

\=

sorted(Qrank\_cnts , key=cv2.contourArea ,reverse=

True)

\#

\#

Find bounding rectangle for largest contour , use it to resize

query rank

image to match dimensions of the train rank image

if len(Qrank\_cnts) != 0:

x1 ,y1 ,w1 ,h1 cv2.boundingRect(Qrank\_cnts[0])

Qrank\_roi Qrank[y1:y1+h1 , x1:x1+w1]

Qrank\_sized

\=

\=

\=

cv2.resize(Qrank\_roi , (RANK\_WIDTH ,RANK\_HEIGHT

), 0, 0)

qCard.rank\_img

\=

Qrank\_sized

\#

Find suit contour and bounding rectangle , isolate and find

largest contour

Qsuit\_cnts , hier

\=

cv2.findContours(Qsuit , cv2.RETR\_TREE ,cv2.

CHAIN\_APPROX\_SIMPLE )

Qsuit\_cnts

\=

sorted(Qsuit\_cnts , key=cv2.contourArea ,reverse=

True)

\#

\#

Find bounding rectangle for largest contour , use it to resize

query suit

image to match dimensions of the train suit image

if len(Qsuit\_cnts) != 0:

x2 ,y2 ,w2 ,h2 cv2.boundingRect(Qsuit\_cnts[0])

Qsuit\_roi

\=

\=

Qsuit[y2:y2+h2 , x2:x2+w2]

8



<a name="br9"></a> 

Qsuit\_sized

qCard.suit\_img

return qCard

\=

cv2.resize(Qsuit\_roi , (SUIT\_WIDTH ,

SUIT\_HEIGHT), 0, 0)

\=

Qsuit\_sized

def match\_card(qCard , train\_ranks , train\_suits):

""" Menemukan kecocokan pangkat dan setelan terbaik untuk kartu

kueri. Perbedaan

peringkat kartu kueri dan gambar setelan dengan peringkat

kereta dan gambar setelan .

Kecocokan terbaik adalah gambar pangkat atau setelan yang

memiliki perbedaan paling

kecil."""

best\_rank\_match\_diff

best\_suit\_match\_diff

best\_rank\_match\_name

best\_suit\_match\_name

\=

\=

\=

\=

10000

10000

""

""

i

\=

0

\#

If no contours were found in query card in preprocess\_card

function ,

\#

\#

the img size is zero , so skip the differencing process

(card will be left as Unknown )

if (len(qCard.rank\_img) != 0) and (len(qCard.suit\_img) != 0):

\#

\#

Difference the query card rank image from each of the

train rank images ,

and store the result with the least difference

for Trank in train\_ranks:

diff\_img

rank\_diff

\=

cv2.absdiff(qCard.rank\_img , Trank.img)

int(np.sum(diff\_img)/255)

\=

if rank\_diff

best\_rank\_diff\_img

best\_rank\_match\_diff

best\_rank\_name Trank.name

<

best\_rank\_match\_diff :

diff\_img

rank\_diff

\=

\=

\=

\# Same process with suit images

for Tsuit in train\_suits:

diff\_img

suit\_diff

\=

cv2.absdiff(qCard.suit\_img , Tsuit.img)

int(np.sum(diff\_img)/255)

\=

if suit\_diff

best\_suit\_diff\_img

best\_suit\_match\_diff

best\_suit\_name Tsuit.name

<

best\_suit\_match\_diff :

diff\_img

suit\_diff

\=

\=

\=

if ( best\_rank\_match\_diff

best\_rank\_match\_name

<

\=

RANK\_DIFF\_MAX):

best\_rank\_name

if ( best\_suit\_match\_diff

best\_suit\_match\_name

<

\=

SUIT\_DIFF\_MAX):

best\_suit\_name

9



<a name="br10"></a> 

\#

Return the identiy of the card and the quality of the suit

and rank match

return best\_rank\_match\_name , best\_suit\_match\_name ,

best\_rank\_match\_diff ,

best\_suit\_match\_diff

3\.7 Flattener(Membuat Menjadi lurus) dan Draw Results

Fungsi ini bertujuan untuk menggambar hasil identiﬁkasi kartu pada gambar

kamera. Berikut adalah penjelasan mendetailnya:

• x = qCard.center[0] dan y = qCard.center[1]: Mendapatkan koor-

dinat titik tengah dari kartu yang diidentiﬁkasi.

• cv2.circle(image, (x, y), 5, (0, 0, 0), -1): Menggambar lingkaran

kecil pada titik tengah kartu sebagai penanda.

• Mengonversi nama rank dan jenis kartu ke dalam bahasa Indonesia dengan

menggunakan serangkaian kondisi if-elif-else.

• cv2.putText(image, (rank name display + ’’), (x-60, y-10), font,

1, (0, 0, 0), 7, cv2.LINE AA): Menggambar nama rank pada gambar

dengan huruf hitam dan tebal sebagai kontur.

• cv2.putText(image, (rank name display + ’’), (x-60, y-10), font,

1, (0, 200, 220), 2, cv2.LINE AA): Menggambar nama rank kembali

dengan huruf hijau dan lebih tipis sebagai pengisi.

• cv2.putText(image, suit name display, (x-60, y+25), font, 1, (0,

0, 0), 7, cv2.LINE AA): Menggambar jenis kartu pada gambar dengan

huruf hitam dan tebal sebagai kontur.

• cv2.putText(image, suit name display, (x-60, y+25), font, 1, (0,

200, 220), 2, cv2.LINE AA): Menggambar jenis kartu kembali dengan

huruf hijau dan lebih tipis sebagai pengisi.

• Mengembalikan gambar yang telah dimodiﬁkasi.

Fungsi flattener(image, pts, w, h)

Fungsi ini bertujuan untuk melakukan transformasi perspektif pada citra kartu

yang diidentiﬁkasi. Berikut adalah penjelasan mendetailnya:

• Membuat array temp rect yang akan menyimpan empat titik sudut dari

kartu setelah diurutkan.

• Menghitung jumlah nilai koordinat x dan y dari keempat titik sudut kartu.

10



<a name="br11"></a> 

• Menentukan titik sudut tl, br, tr, dan bl berdasarkan hasil penjumlahan

dan pengurangan dari keempat titik sudut.

• Menentukan urutan titik sudut sesuai orientasi kartu (vertikal atau hori-

zontal).

• Menentukan orientasi kartu berdasarkan perbandingan lebar (w) dan tinggi

(h).

• Jika kartu lebih vertikal, maka temp rect diatur sesuai urutan titik sudut

yang sesuai.

• Jika kartu lebih horizontal, urutan titik sudut diatur untuk orientasi yang

sesuai.

• Jika kartu memiliki orientasi ”diamond,” penentuan urutan titik sudut

memperhatikan kecondongan kartu.

• Menentukan ukuran maksimum (maxWidth dan maxHeight) untuk citra

hasil transformasi.

• Membuat array destinasi (dst) yang berisi empat titik yang membentuk

kartu dengan ukuran yang diinginkan.

• Menghitung matriks transformasi perspektif (M) menggunakan fungsi cv2.getPerspectiveTransform.

• Melakukan transformasi perspektif pada citra kartu menggunakan fungsi

cv2.warpPerspective.

• Mengonversi citra hasil transformasi ke dalam skala keabuan.

• Mengembalikan citra hasil transformasi.

4 Penjelasan Program GAME BLACK JACK

def rank\_to\_int(rank\_name):

if rank\_name == ’Ace’:

return

elif rank\_name == ’Two’:

return

elif rank\_name == ’Three ’:

return

elif rank\_name == ’Four ’:

return

elif rank\_name == ’Five ’:

return

elif rank\_name == ’Six’:

return

elif rank\_name == ’Seven ’:

return

elif rank\_name == ’Eight ’:

return

1

2

3

4

5

6

7

8

11



<a name="br12"></a> 

elif rank\_name == ’Nine ’:

return

9

elif rank\_name == ’Ten’:

return 10

elif rank\_name == ’Jack ’:

return 10

elif rank\_name == ’Queen ’:

return 10

elif rank\_name == ’King ’:

return 10

else:

return

0

def add\_white\_frame (image , player1Count , player2Count):

Ambil dimensi frame

height , width image.shape[:2]

\#

\=

\#

white\_frame

Tambahkan outline

\=

0

\*

np.ones ((height , 300 , 3), dtype=np.uint8)

outline\_thickness

\=

5

white\_frame[ outline\_thickness :height-outline\_thickness ,

outline\_thickness :295 , :]

255 , 255 , 255]

\=

[

\#

Tambahkan teks informasi kartu ke dalam frame putih

cv2.putText(white\_frame , ’AREA KARTU PEMAIN:’, (10 , 30), font ,

0\.7, (0, 0, 0), 1, cv2.

LINE\_AA)

cv2.putText(white\_frame , ’AREA KARTU KOMPUTER:’, (10 , 200),

font , 0.7, (0, 0, 0), 1, cv2.

LINE\_AA)

cv2.putText(white\_frame , f"{player1Count}", (10 , 50), font , 0.7

,

(0, 0, 0), 1, cv2.LINE\_AA)

cv2.putText(white\_frame , f"{player2Count}", (10 , 220), font , 0.

7, (0, 0, 0), 1, cv2.LINE\_AA)

\# Gabungkan frame putih dengan frame utama

result np.hstack ((image , white\_frame))

\=

return result

Fungsi rank to int(rank name)

Fungsi ini bertujuan untuk mengonversi nama peringkat kartu menjadi nilai

numerik. Dalam konteks ini, setiap nama peringkat kartu diberikan nilai in-

teger sesuai dengan nama stringnya pada kode diatas agar nilainya bisa diam-

bil didalam game dan ditambahkan untuk score. Berikut adalah representasi

fungsinya:

12



<a name="br13"></a> 

Fungsi add white frame(image, player1Count, player2Count)

Fungsi ini bertujuan untuk menambahkan bingkai putih pada gambar dengan

informasi tambahan mengenai jumlah kartu pemain dan komputer. Berikut

adalah representasi fungsinya: “‘latex Input:

Langkah:

image, player1Count, player2Count

1\. Ambil dimensi frame: height, width = image.shape[:2]

2\. Tambahkan outline berwarna putih pada frame putih:

outline thickness = 5

white frame[outline thickness:height-outline thickness, outline thickness:295, :]

= [255, 255, 255]

3\. Tambahkan teks informasi kartu ke dalam frame putih:

cv2.putText(white frame, ’AREA KARTU PEMAIN:’, (10, 30), font, 0.7, (0, 0,

0), 1, cv2.LINE AA)

cv2.putText(white frame, ’AREA KARTU KOMPUTER:’, (10, 200), font, 0.7,

(0, 0, 0), 1, cv2.LINE AA)

cv2.putText(white frame, f”player1Count”, (10, 50), font, 0.7, (0, 0, 0), 1,

cv2.LINE AA)

cv2.putText(white frame, f”player2Count”, (10, 220), font, 0.7, (0, 0, 0), 1,

cv2.LINE AA)

4\. Gabungkan frame putih dengan frame utama:

result = np.hstack((image, white frame))

5\. Output: result

5 LOOPING UTAMA GAME BLACKJACK

5\.1 Inisialisasi Video dan pengaturan

\#

Inisialisasi frame rate yang dihitung karena dihitung SETELAH

kali pertama ditampilkan

frame\_rate\_calc

freq cv2. getTickFrequency ()

global detected\_cards\_history

Pengaturan kamera

\=

1

\=

\#

LEBAR\_FRAME

TINGGI\_FRAME

\=

1200

800

\=

\#

font

Tentukan font yang akan digunakan

\=

cv2. FONT\_HERSHEY\_SIMPLEX

\# Buka kamera video

videostream cv2.VideoCapture(0)

\=

\#

0

sesuai dengan kamera default

bisa diubah jika Anda memiliki

beberapa kamera

,

\# Periksa apakah kamera berhasil dibuka

if not videostream.isOpened ():

print("Error: Tidak dapat membuka kamera.")

exit ()

13



<a name="br14"></a> 

\# Muat gambar latihan nilai dan jenis

path os.path.dirname(os.path.abspath(\_\_file\_\_))

\=

train\_ranks

train\_suits

\=

\=

load\_ranks(path

load\_suits(path

\+

\+

’/Card\_Imgs/’)

’/Card\_Imgs/’)

• Inisialisasi variabel seperti frame rate calc, freq, dan detected cards history.

• Pengaturan ukuran frame video dengan LEBAR FRAME dan TINGGI FRAME.

• Penggunaan font cv2.FONT HERSHEY SIMPLEX.

• Buka kamera video dengan cv2.VideoCapture(0) dan muat gambar lati-

han untuk nilai dan jenis kartu.

5\.2 Loop Utama untuk Deteksi Kartu dan Permainan

• Loop utama untuk menangkap frame dari aliran video.

• Pra-pemrosesan gambar dengan mengubahnya menjadi abu-abu dan men-

erapkan teknik ambang adaptif.

• Temukan dan urutkan kontur kartu dalam gambar menggunakan fungsi

find cards.

• Inisialisasi variabel-variabel untuk kontrol permainan seperti player1Count,

player2Count, dan state.

• Tentukan area kartu berdasarkan status permainan (state) dan gambar

kotak di sekitarnya.

• Iterasi melalui setiap kontur yang terdeteksi dan tentukan apakah itu kartu

pemain 1, pemain 2, atau area lainnya.

• Buat objek kartu dari kontur, lakukan pencocokan nilai dan jenis, dan

gambar hasilnya di frame.

• Logika permainan terletak pada tombol spasi (” ”) dan state permainan

tertentu.

• Tampilkan hasil deteksi kartu dan status permainan di frame.

• Periksa tombol keyboard untuk mengontrol permainan dan keluar dari

loop jika tombol ”q” ditekan.

• Bebaskan aliran video dan tutup semua jendela saat permainan selesai

atau tombol ”q” ditekan.

14



<a name="br15"></a> 

6 KondisiGameBlackjack

6\.1 KONDISI AWA L

Kondisi awal terjadi ketika kartu dan contour terdeksi dibagian dalam contour

sesuai dengan nilai koordinat contour nya jika sudah maka akan melakukan

deteksi kartu sebanyak 2x dan jika sudah nilai disimpan di fungsi addwhiteframe

dan masuk kedalam kondisi ke 3 yaitu Hit atau Stand pada kode dibawah ada if

key == 32 dimana menjelaskan bahwa itu nilai dari spasi pada keyboard kode

meisnnya state ¡ 2 adalah kondisi yang mengharuskan player mendraw 2 kartu

pertama kali agar muncul hit atau stand yang sudah ada kondisinya dibawah

ini berikut gambar dan kodenya

Figure 3: KONDISI AWA L

if key == 32 and state

<

2

and rank\_to\_int(cards[0]. best\_rank\_match

!= 0:

player1Count += rank\_to\_int(cards[0].

best\_rank\_match

)

)

state +=

1

6\.2 KONDISI HIT

Kondisi HIT terjadi jika state 1 dan 2 sudah terjadi dan masuk kedalam state

3 atau state ke empat dimana pilihannya adalah HIT atau STAND pada player

jika player sudah memilih HIT dan sudah stand otomatis COM Contour muncul

dan deteksi kartu sampai nilainya lebih dari ¿17 berikut adalah kondisi hit dan

stand dimana stand langsung memuncul rectangle dari com player berikut kode

dan gambarnya

15



<a name="br16"></a> 

Figure 4: KONDISI HIT

if state == 3:

cv2.rectangle(frame , (370 ,160), (600 , 350), (0, 255 , 0)

\2) Ganti

,

\#

koordinat sesuai

kebutuhan

cv2.putText(frame , ’HIT AREA ’, (440 , 154), font , 0.7,

255 , 255 , 255), 1,

(

cv2.LINE\_AA)

elif state == 3:

cardDetected

\=

370

<

center\_x

<

600 and 160

<

center\_y

<

350

if key == 32 and state ==

3

and rank\_to\_int(cards[0].

best\_rank\_match ) != 0:

player1Count += rank\_to\_int(cards[0].

best\_rank\_match

)

if player1Count

\>

21:

state

else:

state

\=

5

\=

2

6\.3 KONDISI COM MENANG

kondisi com menang ketika nilai dari player lebih kecil ¡ daripada nilai dari com

karena com atau bila kondisi ini terjadi nilai dari player lebih dari 21 sehingga

otomatis kejadiannya adalah com menang

16



<a name="br17"></a> 

Figure 5: KONDISI COM MENANG

elif state == 4:

cardDetected 10

if key == 32 and state ==

\=

<

center\_x

<

240 and 260

and rank\_to\_int(cards[0].

best\_rank\_match ) != 0:

player2Count += rank\_to\_int(cards[0].

best\_rank\_match

<

center\_y

<

440

4

)

if player2Count >= 17:

state 5\

\=

elif state == 2:

cv2.putText(frame , "Tekan ’H’ untuk Hit , ’S’ untuk Stand",

(100 ,440), font , .7, (255

,255 ,255), 2)

if key == ord(’h’):

state

if key == ord(’s’):

state

\=

3

\=

4

6\.4 KONDISI PLAYER MENANG

Kondisi player menang adalah ketika draw dari kartu player == 21 atau jika

nilai com lebih dari 21 atau jika nilai Player lebih dari pada nilai com dalam

range ¡ 21 maka pada game ini kondisi player menang dengan penjelasan kode

dan gambar berikut ini :

17



<a name="br18"></a> 

Figure 6: KONDISI PLAYER MENANG

elif state == 5:

if player1Count

\>

cv2.putText(frame , "Player Menang", (240 ,220), font

player2Count and player1Count <= 21:

, 1, (255 ,255 ,255

), 3)

if key == 32 and state ==

3

and rank\_to\_int(cards[0].

best\_rank\_match ) != 0:

player1Count += rank\_to\_int(cards[0].

best\_rank\_match

)

if player1Count

\>

21:

state

else:

state

\=

5

\=

2

6\.5 KONDISI DRAW

Kondisi ini terjadi ketika nilai dari kartu memiliki nilai yang sama antar satu

sama lain berikut gambar dari kondisi draw

18



<a name="br19"></a> 

Figure 7: KONDISI DRAW

6\.6 PENJELASAN ALURNYA

• Periksa apakah terdapat kontur kartu (cnts sort) dalam frame.

• Jika ada, inisialisasi daftar cards untuk menyimpan objek kartu dan in-

deks k.

• Tentukan area deteksi kartu berdasarkan status permainan (state) dan

gambarkan kotak di sekitarnya.

• Iterasi melalui setiap kontur kartu yang terdeteksi.

• Tentukan apakah kartu tersebut adalah kartu pemain 1, pemain 2, atau

tidak termasuk area tertentu.

• Jika kartu terdeteksi sesuai dengan area dan status permainan, buat objek

kartu dari kontur tersebut.

• Hitung pencocokan nilai dan jenis kartu dengan fungsi match card.

• Gambar titik tengah dan hasil pencocokan pada frame video.

• Tambahkan nilai dan jenis kartu yang terdeteksi ke dalam daftar accumulated values.

• Gambar kontur kartu di frame video.

• Jika tombol spasi (” ”) ditekan dan kondisi tertentu terpenuhi, tambahkan

nilai kartu ke player1Count atau player2Count.

• Ubah status permainan (state) sesuai dengan kondisi tertentu.

• Tampilkan informasi dan status permainan di frame video.

19



<a name="br20"></a> 

• Tambahkan frame putih dengan informasi jumlah kartu pemain ke dalam

frame utama.

• Tampilkan pesan dan instruksi sesuai dengan status permainan.

if len(cnts\_sort) != 0:

\#

Inisialisasi daftar "cards" baru untuk menetapkan

objek kartu.

\#

cards

k

mengindeks array kartu yang baru dibuat .

\=

[]

k

\=

0

if state

<

2:

cv2.rectangle(frame , (10 , 40), (240 ,230), (0, 255 ,

0), 2) Ganti

\#

koordinat sesuai

kebutuhan

cv2.putText(frame , ’PLAYER CARD AREA ’, (27 , 35),

font , 0.7, (255 ,

255 , 255), 1, cv2

.LINE\_AA)

if state == 3:

cv2.rectangle(frame , (370 ,160), (600 , 350), (0, 255

0), 2) Ganti

,

\#

koordinat sesuai

kebutuhan

cv2.putText(frame , ’HIT AREA ’, (440 , 154), font , 0.

7, (255 , 255 , 255

), 1, cv2.LINE\_AA

)

if state == 4:

cv2.rectangle(frame , (10 ,270), (240 , 460), (0, 255 ,

0), 2) Ganti

\#

koordinat sesuai

kebutuhan

cv2.putText(frame , ’COM CARD AREA ’, (15 , 265), font

,

0\.7, (255 , 255 ,

255), 1, cv2.

LINE\_AA)

\#

Untuk setiap kontur yang terdeteksi :

for in range(len(cnts\_sort)):

if cnt\_is\_card[i] == 1:

i

\#

Tentukan apakah kartu pemain

1

atau pemain

berdasarkan

posisi dan

2

ukuran kartu

cv2.boundingRect(cnts\_sort[i])

x, y, w,

center\_x

center\_y

h

\=

\=

\=

x

y

\+

\+

w

h

//

//

2

2

\# Periksa untuk pemain

if state 2:

1

<

cardDetected

\=

10

<

center\_x

<

240 and 40

center\_y

<

20



<a name="br21"></a> 

<

230

elif state == 4:

cardDetected

\=

\=

\=

10

<

center\_x

center\_x

<

240 and 260

<

center\_y

<

440

elif state == 3:

cardDetected

370

<

<

600 and 160

<

center\_y

<

350

else:

cardDetected

False

if cardDetected:

\#

Buat objek kartu dari kontur dan tambahkan ke

daftar kartu

.

cards.append( preprocess\_card (cnts\_sort[i],

frame))

\#

Temukan pencocokan nilai dan jenis terbaik

untuk kartu.

(

cards[k].best\_rank\_match ,

cards[k].best\_suit\_match ,

cards[k].rank\_diff ,

cards[k].suit\_diff ,

match\_card(cards[k], train\_ranks ,

train\_suits

)

\=

)

\#

Gambar titik tengah dan hasil pencocokan pada

gambar .

frame

+=

accumulated\_values .append (( cards[k-1].

best\_rank\_match

cards[k

\=

draw\_results(frame , cards[k])

k

1

,

-1].

best\_suit\_match

))

\#

\#

Gambar kontur kartu pada gambar (harus melakukannya

semua sekaligus atau

mereka tidak akan muncul dengan benar karena beberapa

alasan )

if len(cards) != 0:

temp\_cnts [baru.contour for baru in cards]

cv2.drawContours(frame , temp\_cnts , -1, (0, 255 ,255)

\4)

\=

,

if key == 32 and state

<

2

and rank\_to\_int(cards[0]

. best\_rank\_match)

!= 0:

player1Count += rank\_to\_int(cards[0].

best\_rank\_match

)

state +=

1

21



<a name="br22"></a> 

if key == 32 and state ==

3

and rank\_to\_int(cards[0

]. best\_rank\_match

)

!= 0:

player1Count += rank\_to\_int(cards[0].

best\_rank\_match

)

if player1Count

\>

21:

state

else:

state

\=

5

\=

2

if key == 32 and state ==

4

and rank\_to\_int(cards[0

]. best\_rank\_match

)

!= 0:

player2Count += rank\_to\_int(cards[0].

best\_rank\_match

)

if player2Count >= 17:

state

\=

5

frame

\=

add\_white\_frame (frame , player1Count , player2Count)

if state

<

2

or state == 3 or state == 4:

cv2.putText(frame , "Tekan spasi untuk menyimpan kartu",

(100 ,440), font , .7,

(255 ,255 ,255), 2)

elif state == 2:

cv2.putText(frame , "Tekan ’H’ untuk Hit , ’S’ untuk

Stand", (100 ,440),

font , .7, (255 ,255 ,

255), 2)

if key == ord(’h’):

state

if key == ord(’s’):

state

elif state == 5:

if player1Count

cv2.putText(frame , "Player Menang", (240 ,220), font

1, (255 ,255 ,255

\=

3

\=

4

\>

player2Count and player1Count <= 21:

,

), 3)

player2Count or player1Count

elif player1Count

<

\>

cv2.putText(frame , "COM Menang", (260 ,220), font ,

21:

1

,

\3)

(255 ,255 ,255),

else:

cv2.putText(frame , "Draw", (280 ,220), font , 1, (255

,255 ,255), 3)

\#

\#

frame

\=

add\_stand\_and\_button (frame , stand\_pressed ,

hit\_pressed )

Tampilkan gambar dengan kartu yang teridentifikasi

cv2.imshow("Pendeteksi Kartu", frame)

\#

Periksa keyboard . Jika ’q’ ditekan , keluar dari loop

22



<a name="br23"></a> 

utama.

key

\=

cv2.waitKey(1)

if key == ord("q"):

cam\_quit True

\=

\#

\#

if key == ord ("s"):

stand\_pressed

\=

not stand\_pressed

\#

\#

\#

Cek jika tombol "h" (hit) ditekan

if key == ord ("h"):

hit\_pressed

\=

not hit\_pressed

\#

Bebaskan aliran video dan tutup semua jendela

videostream.release ()

cv2. destroyAllWindows ()

if \_\_name\_\_ == "\_\_main\_\_":

main ()

7 Kontrol Permainan dan Tampilan

• Jika permainan belum selesai (state < 2, 3, 4), tampilkan instruksi un-

tuk menyimpan kartu.

• Jika sedang memilih hit/stand (state == 2), tampilkan instruksi untuk

menekan ’H’ (Hit) atau ’S’ (Stand).

• Jika permainan selesai (state == 5), tampilkan hasil permainan berdasarkan

nilai kartu.

• Periksa tombol keyboard dan ubah status permainan atau kontrol per-

mainan sesuai dengan input keyboard.

• Tampilkan frame video dengan deteksi kartu dan status permainan di

jendela ”Pendeteksi Kartu”.

• Jika tombol ’q’ ditekan, keluar dari loop utama.

8 Penutup

• Setelah loop utama selesai, bebaskan aliran video dan tutup semua jendela.

23

