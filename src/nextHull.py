import numpy as np

def DetFrom3Point(p1,p2,p3):
    mat = np.array([[1,1,1],
                    [p1[0],p2[0],p3[0]],
                    [p1[1],p2[1],p3[1]]])
    return np.linalg.det(mat)

def DistanceFromLine(p1,p2,p3):
    ''' Fungsi: Menerima 2 buah titik (p1 dan p2) yang membentuk segmen garis dan mengembalikan jarak dari p3 ke garis tsb
        Prekondisi : p1,p2,p3 adalah np.array 2 dimensi '''
    return np.cross(p2-p1,p3-p1)/np.linalg.norm(p2-p1)

def AngelFromLine(p1,p2,p3):
    ''' Fungsi: Menerima 2 buah titik (p1 dan p2) yang membentuk segmen garis p1p2 dan mengembalikan sudut p3p1p2
        Prekondisi : p1,p2,p3 adalah np.array 2 dimensi '''
    ba = p3 - p1
    bc = p2 - p1
    cosine = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    return np.arccos(cosine)

def NextSimplex(bucket,line,arr):             # UNTUK TAHAP KE-2 dst..
    ''' Proses: - Menerima himpunan titik pada suatu daerah yang ditandai oleh elemen array "arr" sebagai "indeks" dari array "bucket"
                - Array "bucket" memiliki elemen berupa titik secara universal
                - Array "line" memiliki elemen berupa "indeks" dari array "bucket" yang merupakan garis batas daerah sebelumnya
                - Fungsi akan mengembalikan simplex baru dari daerah tersebut
        Prekondisi : Daerah tersebut tidak kosong, minimal elemen array "arr" ada 1 '''
    
    ''' 1. Cari titik terjauh (p3) sehingga membentuk 2 buah line baru
           lineL adalah p1p3 berupa garis/ simplex sebelah KIRI
           lineR adalah p3p2 berupa garis/ simplex sebelah KANAN '''
    # a. Titik awal pada garis
    p1 = bucket[line[0]]
    
    # b. Titik akhir pada garis
    p2 = bucket[line[1]]
    
    d   = -1      # Jarak tidak mungkin negatif, inisiasi awal sebagai pembanding
    idx = -1      # Indeks ditemukannya titik dengan jarak terjauh   
    for i in arr:
        X = bucket[i,0]
        Y = bucket[i,1]
        p3 = np.array([X,Y])
        dTemp = DistanceFromLine(p1,p2,p3)
        if   (dTemp > d) :
            d   = dTemp
            idx = i
        elif ( dTemp==d ) :     # Jika jaraknya sama, makan bandingkan sudut
            f = 0
            # dtheta    = AngelFromLine(p1,p2,p3)
            # Temptheta = AngelFromLine(p1,p2,p3)
            # if (Temptheta > dtheta) :
            #     d   = dTemp
            #     idx = i
        
    ''' 2. Setelah didapat titik terjauh, bentuk 2 buah line baru '''
    ### GARIS BAGIAN KIRI
    lineL = [line[0],idx]
    #   a. Titik awal pada garis
    p1L = bucket[lineL[0]]
    #   b. Titik akhir pada garis
    p2L = bucket[lineL[1]]
    
    ### GARIS BAGIAN KANAN
    lineR = [idx,line[1]]
    #   a. Titik awal pada garis
    p1R = bucket[lineR[0]]
    #   b. Titik akhir pada garis
    p2R = bucket[lineR[1]]
        
    ''' 3. Bagi kumpulan titik pada array "arr" menjadi 2 partisi, namun yg dipakai hanya partisi KIRI
        Apabila berada pada garis p1-p3, maka abaikan '''   
    arrL = []
    arrR = []
    ''' 3.1. Check di garis atau tidak untuk kedua garis batas baru, di garis (det=0) '''
    for i in arr:
        XX = bucket[i,0]
        YY = bucket[i,1]
        p3 = np.array([XX,YY])
        
        ''' 3.1.a. Check untuk bagian kiri lineL,
            3.1.b. Check untuk bagian kiri lineR,
            apabila (det>0) maka masukkan ke array selanjutnya untuk diperiksa '''
        detL = DetFrom3Point(p1L,p2L,p3)
        detR = DetFrom3Point(p1R,p2R,p3)
        if   (detL > 0) :
            arrL += [i]
        elif (detR > 0) :
            arrR += [i]        

    ''' 3.4 CONQUER & COMBINE masing-masing sisi (INI TAHAP TERSULIT)'''
    simplexL = []                            # {array simplex hanya menampung "pasangan" idx dari "adjecency" point}
    simplexR = []                            # {array simplex hanya menampung "pasangan" idx dari "adjecency" point}
    #  URUTAN CONQUER = KIRI -> KANAN
    # K-1 : Apabila kiri kosong
    if ( arrL==[] ) :
        simplexL += [lineL]
    else:
        simplexL += NextSimplex(bucket,lineL,arrL)
    if ( arrR==[] ) :
        simplexR += [lineR]
    else:
        simplexR += NextSimplex(bucket,lineR,arrR)
               
    return simplexL+simplexR