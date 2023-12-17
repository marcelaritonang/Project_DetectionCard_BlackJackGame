import cv2
import numpy as np
import os

### Konstanta ###
# Tingkat ambang adaptif
BKG_THRESH = 60
CARD_THRESH = 30
# Lebar dan tinggi sudut kartu, di mana nilai dan jenis kartu ada
CORNER_WIDTH = 32
CORNER_HEIGHT = 84
# Dimensi gambar latihan nilai
RANK_WIDTH = 70
RANK_HEIGHT = 125
# Dimensi gambar latihan jenis
SUIT_WIDTH = 70
SUIT_HEIGHT = 100



class Train_ranks:
    """Struktur untuk menyimpan informasi tentang gambar latihan nilai."""

    def __init__(self):
        self.img = []  # Gambar nilai yang diatur ukurannya yang dimuat dari hard drive
        self.name = "Pemegang Tempat"

class Train_suits:
    """Struktur untuk menyimpan informasi tentang gambar latihan jenis."""

    def __init__(self):
        self.img = []  # Gambar jenis yang diatur ukurannya yang dimuat dari hard drive
        self.name = "Pemegang Tempat"

### Struktur untuk menyimpan informasi kartu kueri dan kartu latihan ###

class Query_card:
    """Struktur untuk menyimpan informasi tentang kartu kueri dalam gambar kamera."""

    def __init__(self):
        self.contour = []  # Kontur kartu
        self.width, self.height = 0, 0  # Lebar dan tinggi kartu
        self.corner_pts = []  # Titik sudut kartu
        self.center = []  # Titik tengah kartu
        self.warp = []  # Gambar yang dihancurkan, abu-abu, dan diburamkan berukuran 200x300
        self.rank_img = []  # Gambar kartu dengan nilai yang diatur ukurannya
        self.suit_img = []  # Gambar kartu dengan jenis yang diatur ukurannya
        self.best_rank_match = "Tidak Diketahui"  # Pencocokan nilai terbaik
        self.best_suit_match = "Tidak Diketahui"  # Pencocokan jenis terbaik
        self.rank_diff = 0  # Perbedaan antara gambar nilai dan gambar latihan nilai terbaik yang cocok
        self.suit_diff = 0  # Perbedaan antara gambar jenis dan gambar latihan jenis terbaik yang cocok


RANK_DIFF_MAX = 2000
SUIT_DIFF_MAX = 700
CARD_MAX_AREA = 120000
CARD_MIN_AREA = 25000

font = cv2.FONT_HERSHEY_TRIPLEX

class Train_ranks:
    """Struktur untuk menyimpan informasi tentang gambar latihan nilai."""

    def __init__(self):
        self.img = []  # Gambar nilai yang diatur ukurannya yang dimuat dari hard drive
        self.name = "Pemegang Tempat"

class Train_suits:
    """Struktur untuk menyimpan informasi tentang gambar latihan jenis."""

    def __init__(self):
        self.img = []  # Gambar jenis yang diatur ukurannya yang dimuat dari hard drive
        self.name = "Pemegang Tempat"

### Fungsi ###
def load_ranks(filepath):
    """Memuat gambar nilai dari direktori yang ditentukan oleh filepath. Menyimpan
    mereka dalam daftar objek Train_ranks."""

    train_ranks = []
    i = 0

    for Rank in ['Ace','Two','Three','Four','Five','Six','Seven',
                 'Eight','Nine','Ten','Jack','Queen','King']:
        train_ranks.append(Train_ranks())
        train_ranks[i].name = Rank
        filename = Rank + '.jpg'
        train_ranks[i].img = cv2.imread(filepath + filename, cv2.IMREAD_GRAYSCALE)
        i = i + 1

    return train_ranks

def load_suits(filepath):
    """Memuat gambar jenis dari direktori yang ditentukan oleh filepath. Menyimpan
    mereka dalam daftar objek Train_suits."""

    train_suits = []
    i = 0
    
    for Suit in ['Spades','Diamonds','Clubs','Hearts']:
        train_suits.append(Train_suits())
        train_suits[i].name = Suit
        filename = Suit + '.jpg'
        train_suits[i].img = cv2.imread(filepath+filename, cv2.IMREAD_GRAYSCALE)
        i = i + 1

    return train_suits

def preprocess_image(image):
    """Mengembalikan gambar kamera yang diubah menjadi abu-abu, diburamkan, dan ambang adaptif."""

    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)

    # Tingkat ambang batas terbaik bergantung pada kondisi pencahayaan sekitar.
     # Untuk pencahayaan yang terang, ambang batas yang tinggi harus digunakan untuk mengisolasi kartu
     # dari latar belakang. Untuk pencahayaan redup, ambang batas rendah harus digunakan.
     # Untuk membuat detektor kartu tidak bergantung pada kondisi pencahayaan,
     # metode ambang batas adaptif berikut digunakan.
     #
     # Piksel latar belakang di tengah atas gambar diambil sampelnya untuk ditentukan
     # intensitasnya. Ambang batas adaptif ditetapkan pada 50 (THRESH_ADDER) lebih tinggi
     # daripada itu. Hal ini memungkinkan ambang batas untuk beradaptasi dengan kondisi pencahayaan.
    img_w, img_h = np.shape(image)[:2]
    bkg_level = gray[int(img_h/100)][int(img_w/2)]
    thresh_level = bkg_level + BKG_THRESH

    retval, thresh = cv2.threshold(blur,thresh_level,255,cv2.THRESH_BINARY)
    
    return thresh

def find_cards(thresh_image):
    """Mencari semua kontur berukuran kartu dalam gambar kamera yang telah diubah menjadi ambang.
    Mengembalikan jumlah kartu, dan daftar kontur kartu yang diurutkan
    dari yang terbesar hingga yang terkecil."""

    # Find contours and sort their indices by contour size
    cnts, hier = cv2.findContours(thresh_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    index_sort = sorted(range(len(cnts)), key=lambda i : cv2.contourArea(cnts[i]),reverse=True)

    # If there are no contours, do nothing
    if len(cnts) == 0:
        return [], []
    
    # Otherwise, initialize empty sorted contour and hierarchy lists
    cnts_sort = []
    hier_sort = []
    cnt_is_card = np.zeros(len(cnts),dtype=int)

    # Fill empty lists with sorted contour and sorted hierarchy. Now,
    # the indices of the contour list still correspond with those of
    # the hierarchy list. The hierarchy array can be used to check if
    # the contours have parents or not.
    for i in index_sort:
        cnts_sort.append(cnts[i])
        hier_sort.append(hier[0][i])

    # Determine which of the contours are cards by applying the
    # following criteria: 1) Smaller area than the maximum card size,
    # 2), bigger area than the minimum card size, 3) have no parents,
    # and 4) have four corners

    for i in range(len(cnts_sort)):
        size = cv2.contourArea(cnts_sort[i])
        peri = cv2.arcLength(cnts_sort[i],True)
        approx = cv2.approxPolyDP(cnts_sort[i],0.01*peri,True)
        
        if ((size < CARD_MAX_AREA) and (size > CARD_MIN_AREA)
            and (hier_sort[i][3] == -1) and (len(approx) == 4)):
            cnt_is_card[i] = 1

    return cnts_sort, cnt_is_card

def preprocess_card(contour, image):
    """Menggunakan kontur untuk menemukan informasi tentang kartu kueri. Mengisolasi gambar nilai
    dan jenis dari kartu."""
    # Initialize new Query_card object
    qCard = Query_card()

    qCard.contour = contour

    # Find perimeter of card and use it to approximate corner points
    peri = cv2.arcLength(contour,True)
    approx = cv2.approxPolyDP(contour,0.01*peri,True)
    pts = np.float32(approx)
    qCard.corner_pts = pts

    # Find width and height of card's bounding rectangle
    x,y,w,h = cv2.boundingRect(contour)
    qCard.width, qCard.height = w, h

    # Find center point of card by taking x and y average of the four corners.
    average = np.sum(pts, axis=0)/len(pts)
    cent_x = int(average[0][0])
    cent_y = int(average[0][1])
    qCard.center = [cent_x, cent_y]

    # Warp card into 200x300 flattened image using perspective transform
    qCard.warp = flattener(image, pts, w, h)

    # Grab corner of warped card image and do a 4x zoom
    Qcorner = qCard.warp[0:CORNER_HEIGHT, 0:CORNER_WIDTH]
    Qcorner_zoom = cv2.resize(Qcorner, (0,0), fx=4, fy=4)

    # Sample known white pixel intensity to determine good threshold level
    white_level = Qcorner_zoom[15,int((CORNER_WIDTH*4)/2)]
    thresh_level = white_level - CARD_THRESH
    if (thresh_level <= 0):
        thresh_level = 1
    retval, query_thresh = cv2.threshold(Qcorner_zoom, thresh_level, 255, cv2. THRESH_BINARY_INV)
    
    # Split in to top and bottom half (top shows rank, bottom shows suit)
    Qrank = query_thresh[20:185, 0:128]
    Qsuit = query_thresh[186:336, 0:128]

    # Find rank contour and bounding rectangle, isolate and find largest contour
    Qrank_cnts, hier = cv2.findContours(Qrank, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    Qrank_cnts = sorted(Qrank_cnts, key=cv2.contourArea,reverse=True)

    # Find bounding rectangle for largest contour, use it to resize query rank
    # image to match dimensions of the train rank image
    if len(Qrank_cnts) != 0:
        x1,y1,w1,h1 = cv2.boundingRect(Qrank_cnts[0])
        Qrank_roi = Qrank[y1:y1+h1, x1:x1+w1]
        Qrank_sized = cv2.resize(Qrank_roi, (RANK_WIDTH,RANK_HEIGHT), 0, 0)
        qCard.rank_img = Qrank_sized

    # Find suit contour and bounding rectangle, isolate and find largest contour
    Qsuit_cnts, hier = cv2.findContours(Qsuit, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    Qsuit_cnts = sorted(Qsuit_cnts, key=cv2.contourArea,reverse=True)
    
    # Find bounding rectangle for largest contour, use it to resize query suit
    # image to match dimensions of the train suit image
    if len(Qsuit_cnts) != 0:
        x2,y2,w2,h2 = cv2.boundingRect(Qsuit_cnts[0])
        Qsuit_roi = Qsuit[y2:y2+h2, x2:x2+w2]
        Qsuit_sized = cv2.resize(Qsuit_roi, (SUIT_WIDTH, SUIT_HEIGHT), 0, 0)
        qCard.suit_img = Qsuit_sized

    return qCard

def match_card(qCard, train_ranks, train_suits):
    """Menemukan kecocokan pangkat dan setelan terbaik untuk kartu kueri. Perbedaan
      peringkat kartu kueri dan gambar setelan dengan peringkat kereta dan gambar setelan.
      Kecocokan terbaik adalah gambar pangkat atau setelan yang memiliki perbedaan paling kecil."""

    best_rank_match_diff = 10000
    best_suit_match_diff = 10000
    best_rank_match_name = "Unknown"
    best_suit_match_name = "Unknown"
    i = 0

    # If no contours were found in query card in preprocess_card function,
    # the img size is zero, so skip the differencing process
    # (card will be left as Unknown)
    if (len(qCard.rank_img) != 0) and (len(qCard.suit_img) != 0):
        
        # Difference the query card rank image from each of the train rank images,
        # and store the result with the least difference
        for Trank in train_ranks:

                diff_img = cv2.absdiff(qCard.rank_img, Trank.img)
                rank_diff = int(np.sum(diff_img)/255)
                
                if rank_diff < best_rank_match_diff:
                    best_rank_diff_img = diff_img
                    best_rank_match_diff = rank_diff
                    best_rank_name = Trank.name

        # Same process with suit images
        for Tsuit in train_suits:
                
                diff_img = cv2.absdiff(qCard.suit_img, Tsuit.img)
                suit_diff = int(np.sum(diff_img)/255)
                
                if suit_diff < best_suit_match_diff:
                    best_suit_diff_img = diff_img
                    best_suit_match_diff = suit_diff
                    best_suit_name = Tsuit.name

    # Combine best rank match and best suit match to get query card's identity.
    # If the best matches have too high of a difference value, card identity
    # is still Unknown
    if (best_rank_match_diff < RANK_DIFF_MAX):
        best_rank_match_name = best_rank_name

    if (best_suit_match_diff < SUIT_DIFF_MAX):
        best_suit_match_name = best_suit_name

    # Return the identiy of the card and the quality of the suit and rank match
    return best_rank_match_name, best_suit_match_name, best_rank_match_diff, best_suit_match_diff
    
    
def draw_results(image, qCard):
    """Gambarkan nama kartu, titik tengah, dan kontur pada gambar kamera."""
    x = qCard.center[0]
    y = qCard.center[1]
    # untuk warna dari titik tengah
    cv2.circle(image, (x, y), 5, (0, 0, 0), -1)

    # Ubah nama rank menjadi bahasa Indonesia
    rank_name = qCard.best_rank_match
    if rank_name == 'Ace':
        rank_name_display = 'As'
    elif rank_name == 'Two':
        rank_name_display = 'Dua'
    elif rank_name == 'Three':
        rank_name_display = 'Tiga'
    elif rank_name == 'Four':
        rank_name_display = 'Empat'
    elif rank_name == 'Five':
        rank_name_display = 'Lima'
    elif rank_name == 'Six':
        rank_name_display = 'Enam'
    elif rank_name == 'Seven':
        rank_name_display = 'Tujuh'
    elif rank_name == 'Eight':
        rank_name_display = 'Delapan'
    elif rank_name == 'Nine':
        rank_name_display = 'Sembilan'
    elif rank_name == 'Ten':
        rank_name_display = 'Sepuluh'
    elif rank_name == 'Jack':
        rank_name_display = 'Jack'
    elif rank_name == 'Queen':
        rank_name_display = 'Queen'
    elif rank_name == 'King':
        rank_name_display = 'King'
    else:
        rank_name_display = rank_name

    # Ubah jenis kartu menjadi bahasa Indonesia
    suit_name = qCard.best_suit_match
    if suit_name == 'Diamonds':
        suit_name_display = 'Berlian'
    elif suit_name == 'Clubs':
        suit_name_display = 'Keriting'
    elif suit_name == 'Spades':
        suit_name_display = 'Sekop'
    elif suit_name == 'Hearts':
        suit_name_display = 'Hati'
    else:
        suit_name_display = suit_name

    # Draw card name twice, so letters have black outline
    # Setelah dimodifikasi (mengganti warna huruf teks)
    cv2.putText(image, (rank_name_display + ''), (x-60, y-10), font, 1, (0, 0, 0), 7, cv2.LINE_AA)  # Warna huruf hitam
    cv2.putText(image, (rank_name_display + ''), (x-60, y-10), font, 1, (0, 200, 220), 2, cv2.LINE_AA)  # Warna huruf hijau

    cv2.putText(image, suit_name_display, (x-60, y+25), font, 1, (0, 0, 0), 7, cv2.LINE_AA)
    cv2.putText(image, suit_name_display, (x-60, y+25), font, 1, (0, 200, 220), 2, cv2.LINE_AA)

    return image


def flattener(image, pts, w, h):

    temp_rect = np.zeros((4,2), dtype = "float32")
    
    s = np.sum(pts, axis = 2)

    tl = pts[np.argmin(s)]
    br = pts[np.argmax(s)]

    diff = np.diff(pts, axis = -1)
    tr = pts[np.argmin(diff)]
    bl = pts[np.argmax(diff)]

    # Need to create an array listing points in order of
    # [top left, top right, bottom right, bottom left]
    # before doing the perspective transform

    if w <= 0.8*h: # If card is vertically oriented
        temp_rect[0] = tl
        temp_rect[1] = tr
        temp_rect[2] = br
        temp_rect[3] = bl

    if w >= 1.2*h: # If card is horizontally oriented
        temp_rect[0] = bl
        temp_rect[1] = tl
        temp_rect[2] = tr
        temp_rect[3] = br

    # If the card is 'diamond' oriented, a different algorithm
    # has to be used to identify which point is top left, top right
    # bottom left, and bottom right.
    
    if w > 0.8*h and w < 1.2*h: #If card is diamond oriented
        # If furthest left point is higher than furthest right point,
        # card is tilted to the left.
        if pts[1][0][1] <= pts[3][0][1]:
            # If card is titled to the left, approxPolyDP returns points
            # in this order: top right, top left, bottom left, bottom right
            temp_rect[0] = pts[1][0] # Top left
            temp_rect[1] = pts[0][0] # Top right
            temp_rect[2] = pts[3][0] # Bottom right
            temp_rect[3] = pts[2][0] # Bottom left

        # If furthest left point is lower than furthest right point,
        # card is tilted to the right
        if pts[1][0][1] > pts[3][0][1]:
            # If card is titled to the right, approxPolyDP returns points
            # in this order: top left, bottom left, bottom right, top right
            temp_rect[0] = pts[0][0] # Top left
            temp_rect[1] = pts[3][0] # Top right
            temp_rect[2] = pts[2][0] # Bottom right
            temp_rect[3] = pts[1][0] # Bottom left
            
        
    maxWidth = 200
    maxHeight = 300

    # Create destination array, calculate perspective transform matrix,
    # and warp card image
    dst = np.array([[0,0],[maxWidth-1,0],[maxWidth-1,maxHeight-1],[0, maxHeight-1]], np.float32)
    M = cv2.getPerspectiveTransform(temp_rect,dst)
    warp = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
    warp = cv2.cvtColor(warp,cv2.COLOR_BGR2GRAY)

        

    return warp



def main():
    # Inisialisasi frame rate yang dihitung karena dihitung SETELAH kali pertama ditampilkan
    frame_rate_calc = 1
    freq = cv2.getTickFrequency()

    # Pengaturan kamera
    LEBAR_FRAME = 1000
    TINGGI_FRAME = 700

    # Tentukan font yang akan digunakan
    font = cv2.FONT_HERSHEY_SIMPLEX

    # Buka kamera video
    videostream = cv2.VideoCapture(0)  # 0 sesuai dengan kamera default, bisa diubah jika Anda memiliki beberapa kamera

    # Periksa apakah kamera berhasil dibuka
    if not videostream.isOpened():
        print("Error: Tidak dapat membuka kamera.")
        exit() 

    # Muat gambar latihan nilai dan jenis
    path = os.path.dirname(os.path.abspath(__file__))
    train_ranks = load_ranks(path + '/Card_Imgs/')
    train_suits = load_suits(path + '/Card_Imgs/')

    # Loop utama berulang kali mengambil frame dari aliran video
    # dan memprosesnya untuk menemukan dan mengidentifikasi kartu remi.
    cam_quit = False  # Variabel kontrol loop

    # Mulai menangkap frame
    while not cam_quit:
        # Tangkap frame dari aliran video
        ret, frame = videostream.read()

        if not ret:
            break

        # Mulai timer (untuk menghitung frame rate)
        t1 = cv2.getTickCount()

        # Pra-pemrosesan gambar kamera (ubah ke abu-abu, buramkan, dan ambang adaptif)
        pre_proc = preprocess_image(frame)

        # Temukan dan urutkan kontur semua kartu dalam gambar (kartu kueri)
        cnts_sort, cnt_is_card = find_cards(pre_proc)

        # Jika tidak ada kontur, tidak lakukan apa-apa
        if len(cnts_sort) != 0:
            # Inisialisasi daftar "cards" baru untuk menetapkan objek kartu.
            # k mengindeks array kartu yang baru dibuat.
            cards = []
            k = 0

            # Untuk setiap kontur yang terdeteksi:
            for i in range(len(cnts_sort)):
                if cnt_is_card[i] == 1:
                    # Buat objek kartu dari kontur dan tambahkan ke daftar kartu.
                    cards.append(preprocess_card(cnts_sort[i], frame))

                    # Temukan pencocokan nilai dan jenis terbaik untuk kartu.
                    (
                        cards[k].best_rank_match,
                        cards[k].best_suit_match,
                        cards[k].rank_diff,
                        cards[k].suit_diff,
                    ) = match_card(cards[k], train_ranks, train_suits)

                    # Gambar titik tengah dan hasil pencocokan pada gambar.
                    frame = draw_results(frame, cards[k])
                    k += 1

            # Gambar kontur kartu pada gambar (harus melakukannya semua sekaligus atau
            # mereka tidak akan muncul dengan benar karena beberapa alasan)
            if len(cards) != 0:
                temp_cnts = [baru.contour for baru in cards]
                cv2.drawContours(frame, temp_cnts, -1, (0, 255,255), 4)

        # Gambar frame rate di sudut gambar. Frame rate dihitung pada akhir loop utama,
        # jadi kali pertama ini berjalan, frame rate akan ditampilkan sebagai 0.

        # Tampilkan gambar dengan kartu yang teridentifikasi
        cv2.imshow("Pendeteksi Kartu", frame)

        # Hitung frame rate
        t2 = cv2.getTickCount()
        time1 = (t2 - t1) / freq
        frame_rate_calc = 1 / time1

        # Periksa keyboard. Jika 'q' ditekan, keluar dari loop utama.
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            cam_quit = True

    # Bebaskan aliran video dan tutup semua jendela
    videostream.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()