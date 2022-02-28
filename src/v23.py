import pandas as pd 
from sklearn import datasets
import matplotlib.pyplot as plt
from ConvexHull_v2 import ConvexHull_v2

# USER INTERFACE
print("Selamat datang di Uji Coba Convex Hull v.2.0.1")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Terdapat beberapa pilihan visualisasi :")
print("    1. Sepal Width (y) vs Sepal Length (x)    :: IRIS-Datasets")
print("    2. Petal Width (y) vs Petal Length (x)    :: IRIS-Datasets")
print("    3. Color Intensity (y) vs Alcohol % (x)   :: WINE-Datasets")
print("    4. Flavanoids (y) vs Total Phenols (x)    :: WINE-Datasets")
pil = int(input("Masukkan pilihan : "))

while not(1<=pil<=4):
    print("Masukan anda tidak sesuai..!! Harap masukkan pilihan kembali..!!")
    print("    1. Sepal Width (y) vs Sepal Length (x)    :: IRIS-Datasets")
    print("    2. Petal Width (y) vs Petal Length (x)    :: IRIS-Datasets")
    print("    3. Color Intensity (y) vs Alcohol % (x)   :: WINE-Datasets")
    print("    4. Flavanoids (y) vs Total Phenols (x)    :: WINE-Datasets")
    pil = int(input("Masukkan pilihan : "))

print("Pilihan anda adalah :",pil)

if (pil==1 or pil==2):
    data = datasets.load_iris()
    if pil==1:
        title = 'Sepal Width vs Sepal Length'
        col1 = 0
        col2 = 1
    elif pil==2:
        title = 'Petal Width vs Petal Length' 
        col1 = 2
        col2 = 3
elif (pil==3 or pil==4):
    data = datasets.load_wine()
    if pil==3:
        title = 'Alcohol vs Color Intensity'
        col1 = 0
        col2 = 9
    elif pil==4:
        title = 'Total Phenols vs Flavanoids' 
        col1 = 5
        col2 = 6
        
#create a DataFrame 
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Target'] = pd.DataFrame(data.target)
print()
print("Berikut Contoh Data yang Diolah :")
print(df.head())

# Visualizing Datasets
colors = ['b','r','g']
plt.figure(figsize = (10, 6))
plt.title(title)
plt.xlabel(data.feature_names[col1])
plt.ylabel(data.feature_names[col2])


print("Berikut Visualisasi Data yang Diolah :")
for i in range(len(data.target_names)):
    each = df[df['Target'] == i]                # untuk mengambil data dengan target yang seragam
    bucket = each.iloc[:,[col1,col2]].values    # untuk mendapatkan aray berupa posisi x dan y, berukuran n x 2, n adalah banyak data
    simplices = ConvexHull_v2(bucket)           # bagian ini diganti dengan hasil implementasi ConvexHull Divide & Conquer
    plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
    for simplex in simplices:
        plt.plot(bucket[simplex, 0], bucket[simplex, 1], colors[i])
plt.legend()