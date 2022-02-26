import numpy as np
from nextHull import *

def NewConvexHull(bucket):
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ TAHAP KE-1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ''' 1. Urutkan semua titik berdasarkan X-axis and Y-axis '''
    bucket.sort(axis=1)
    bucket.sort(axis=0)

    ''' 2. Buat p1-pn sebagai line batas awal '''
    line = [0,len(bucket)-1]
    # a. Titik awal pada garis
    p1   = bucket[line[0]]
    # b. Titik akhir pada garis
    p2   = bucket[line[1]]

    ''' 3. Bagi kumpulan titik yang lain menjadi 2 partisi
        Apabila berada pada garis p1-pn, maka abaikan '''
    left  = []
    right = []
    ''' 3.1. Check di garis atau tidak, di garis (det=0) '''
    for i in range(len(bucket)):
        X = bucket[i,0]
        Y = bucket[i,1]
        p3 = np.array([X,Y])
        det = DetFrom3Point(p1,p2,p3)
        ''' 3.2 Jika tidak digaris, bagi menjadi bagian KIRI (det>0) dan KANAN (det<0) '''
        if   (det > 0) :
            left  += [i]
        elif (det < 0) :
            right += [i]

    ''' 3.4 DIVIDE & CONQUER & COMBINE masing-masing sisi (INI TAHAP TERSULIT) '''
    simplex = []                                        # {array simplex hanya menampung "pasangan" idx dari "adjecency" point}
    #  URUTAN CONQUER = KIRI -> KANAN
    # K-1 : Apabila kiri kosong
    if ( left==[] ) :
        # K-1.1 : Kanan kosong, maka simplex tetep
        if ( right==[] ) :
            simplex += [line]
        # K-1.2 : Kanan ada, maka simplex diubah menjadi bagian kanan
        else :
            simplex += [line]
            simplex += NextSimplex(bucket,line,right)
            
    # K-2 : Apabila kiri ada, maka disimpan simpex batas, dan diubah menjadi bagian sebelah kiri
    else :
        # K-2.1 : Kanan kosong, maka simplex diubah menjadi bagian kiri
        if ( right==[] ) :
            simplex += NextSimplex(bucket,line,left)
            simplex += [line]
        else :
            simplex += NextSimplex(bucket,line,left)
            simplex += NextSimplex(bucket,line,right)
    
    return simplex