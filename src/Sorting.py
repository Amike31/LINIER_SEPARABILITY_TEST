### Python program for implementation of Quicksort Sort

''' Proses : - Diambil titik terakhir sebagai pivot di setiap itetasi
             - Lalu letakkan pivot tersebut secara terurut di array hasil 
               dengan meletakkan nilai yang lebih kecil di sebelah kirinya
               dan nilai yang lebih besar di sebelah kananya '''

def partition(arr, low, high):
    ''' 1.1. Tentukan elemen pivot terlebih dahulu'''
    i = (low-1)		            # i adalah indeks dari elemen terkecil dalam array, "asumsi awal" : elemen terakhir
    pivotX = arr[high, 0]	    # penentuan pivot : elemen terakhir
    pivotY = arr[high, 1]

    ''' 1.2 Mencari semua elemen yang <= dari pivot + aturan
            Aturan : Jika nilai x sama, maka bandingkan berdasarkan nilai y'''
    for j in range(low, high):
        if (arr[j, 0] < pivotX) or (arr[j, 0] == pivotX and arr[j, 1] <= pivotY):
            ''' 1.3 Lakukan proses "SWAP" {mengganti elemen} '''
            i = i+1
            arr[i, 0], arr[j, 0] = arr[j, 0], arr[i, 0]
            arr[i, 1], arr[j, 1] = arr[j, 1], arr[i, 1]
    ''' 1.4 Swap elemen terakhir ditemukan nilai terkecil, dengan elemen terakhir '''
    arr[i+1, 0], arr[high, 0] = arr[high, 0], arr[i+1, 0]
    arr[i+1, 1], arr[high, 1] = arr[high, 1], arr[i+1, 1]
    
    return (i+1)

# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low --> Starting index,
# high --> Ending index

# Function to do Quick sort


def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:

		# pi is partitioning index, arr[p] is now
		# at right place
        pi = partition(arr, low, high)

		# Separately sort elements before
		# partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
