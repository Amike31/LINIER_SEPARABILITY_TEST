import numpy as np
import math
from Sorting import quickSort

def DetFrom3Point(p1,p2,p3):
    mat = np.array([[1,1,1],
                    [p1[0],p2[0],p3[0]],
                    [p1[1],p2[1],p3[1]]])
    return np.linalg.det(mat)

def AngleFrom3Point(p1,p2,p3):
    ''' Fungsi: Menerima 2 buah titik (p1 dan p2) yang membentuk segmen garis p1p2 dan mengembalikan sudut p3p1p2
        Prekondisi : p1,p2,p3 adalah np.array 2 dimensi '''
    ba = p3 - p1
    bc = p2 - p1
    cosine = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    return np.arccos(cosine)

def DistanceFromLine(p1,p2,p3):
    ''' Fungsi: Menerima 2 buah titik (p1 dan p2) yang membentuk segmen garis dan mengembalikan jarak dari p3 ke garis tsb
        Prekondisi : p1,p2,p3 adalah np.array 2 dimensi '''
    abs = np.abs
    cross = np.cross
    norm = np.linalg.norm
    return abs(norm(cross(p2-p1, p1-p3)))/norm(p2-p1)

def NextSimplices(bucket,line,arr):             # UNTUK TAHAP KE-2 dst..
    ''' Proses: - Menerima himpunan titik pada suatu daerah yang ditandai oleh elemen array "arr" sebagai "indeks" dari array "bucket"
                - Array "arr" tidak kosong
                - Array "bucket" memiliki elemen berupa titik secara universal
                - Array "line" memiliki elemen berupa "indeks" dari array "bucket" yang merupakan garis batas daerah sebelumnya
                - Fungsi akan mengembalikan simplex baru dari daerah tersebut
        Prekondisi : Daerah tersebut tidak kosong, minimal elemen array "arr" ada 1 '''
    
    # a. Titik awal pada garis
    p1 = bucket[line[0]]
    # b. Titik akhir pada garis
    p2 = bucket[line[1]]
    ''' 1. Cari titik terjauh (p3) sehingga membentuk 2 buah line baru
           lineL adalah p1p3 berupa garis/ simplex sebelah KIRI
           lineR adalah p3p2 berupa garis/ simplex sebelah KANAN '''
    d   = -1      # Jarak tidak mungkin negatif, inisiasi awal sebagai pembanding
    idx = -1      # Indeks ditemukannya titik dengan jarak terjauh
    for i in arr:
        p3 = bucket[i]
        dTemp = DistanceFromLine(p1,p2,p3)
        if   (dTemp > d):
            d   = dTemp
            idx = i
        elif (dTemp == d): # Jika jaraknya sama, makan bandingkan sudut
            pD = bucket[idx]
            if (AngleFrom3Point(p1,p2,p3) > AngleFrom3Point(p1,p2,pD)):
                d   = dTemp
                idx = i
                
    ''' 2. Setelah didapat titik terjauh, bentuk 2 buah line baru '''
    ### GARIS BAGIAN KIRI
    lineL = [line[0],idx]
    p1L   = bucket[line[0]]
    p2L   = bucket[idx]
    
    ### GARIS BAGIAN KANAN
    lineR = [idx,line[1]]
    p1R   = bucket[idx]
    p2R   = bucket[line[1]]
    
    ''' 3. Bagi kumpulan titik pada array "arr" menjadi 2 partisi, namun yg dipakai hanya partisi KIRI
        Apabila berada pada garis p1X-p2X, maka abaikan '''   
    newSimplices = []
    arrL = []
    arrR = []
    ''' 3.1. Check di garis atau tidak untuk kedua garis batas baru, di garis (det=0) '''
    for i in arr:
        p3 = bucket[i]
        
        ''' 3.1.a. Check untuk bagian kiri lineL,
            3.1.b. Check untuk bagian kiri lineR,
            apabila (det>0) maka masukkan ke array selanjutnya untuk diperiksa '''
        detL = DetFrom3Point(p1L,p2L,p3)
        detR = DetFrom3Point(p1R,p2R,p3)
        if   (detL > 0):
            arrL += [i]
        elif (detR > 0):
            arrR += [i]
    
    ''' 3.4 CONQUER & COMBINE masing-masing sisi (INI TAHAP TERSULIT)'''
    #  URUTAN CONQUER = KIRI -> KANAN
    if arrL==[] and arrR==[]:
        newSimplices += [lineL]
        newSimplices += [lineR]
    elif arrL==[] and arrR!=[]:
        newSimplices += [lineL]
        newSimplices += NextSimplices(bucket,lineR,arrR)
    elif arrR==[] and arrL!=[]:
        newSimplices += [lineR]
        newSimplices += NextSimplices(bucket,lineL,arrL)
    else: # {left!=[] and right!=[]}
        newSimplices += NextSimplices(bucket,lineL,arrL)
        newSimplices += NextSimplices(bucket,lineR,arrR)
               
    return newSimplices

def ConvexHull_v2(bucket):
    ''' 1. Diurutkan berdasarkan nilai x dan y '''
    quickSort(bucket,0,len(bucket)-1)

    ''' 2. Buat p1-pn sebagai line batas awal '''
    line = [0,len(bucket)-1]
    # a. Titik awal pada garis
    p1   = bucket[line[0]]
    # b. Titik akhir pada garis
    p2   = bucket[line[1]]

    ''' 3. Bagi kumpulan titik yang lain menjadi 2 partisi
        Apabila berada pada garis p1-pn, maka abaikan '''
    simplices = []
    left  = []
    right = []
    ''' 3.1. Check di garis atau tidak, di garis (det=0) '''
    for i in range(1,len(bucket)-1):
        p3 = bucket[i]
        det = DetFrom3Point(p1,p2,p3)
        ''' 3.2 Jika tidak digaris, bagi menjadi bagian KIRI (det>0) dan KANAN (det<0) '''
        if   (det > 0):
            left  += [i]
        elif (det < 0):
            right += [i]

    lineL = [line[0],line[1]]
    lineR = [line[1],line[0]]
    
    if left==[] and right==[]:
        simplices += [line]

    elif left==[] and right!=[]:
        simplices += [line]
        simplices += NextSimplices(bucket,lineR,right)

    elif right==[] and left!=[]:
        simplices += [line]
        simplices += NextSimplices(bucket,lineL,left)

    else: # {left!=[] and right!=[]}
        simplices += NextSimplices(bucket,lineL,left)
        simplices += NextSimplices(bucket,lineR,right)
        
    return simplices