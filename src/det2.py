import numpy as np
# def DetFrom3Point(p1,p2,p3):
#     mat = np.array([[1,1,1],
#                     [p1[0],p2[0],p3[0]],
#                     [p1[1],p2[1],p3[1]]])
#     return np.linalg.det(mat)

# p1 = np.array([1,2])
# p2 = np.array([4,10])
# p3 = np.array([1,4])

# print

# det = DetFrom3Point(p1,p2,p3)
# print(det)

# -------------------------------------------
# norm = np.linalg.norm

# p1 = np.array([2,0])
# p2 = np.array([-4, 0])

# p3 = np.array([5, 6])
# def DistanceFromLine(p1,p2,p3):
#     ''' Fungsi: Menerima 2 buah titik (p1 dan p2) yang membentuk segmen garis dan mengembalikan jarak dari p3 ke garis tsb
#         Prekondisi : p1,p2,p3 adalah np.array 2 dimensi '''
#     abs = np.abs
#     cross = np.cross
#     norm = np.linalg.norm
#     return abs(norm(cross(p2-p1, p1-p3)))/norm(p2-p1)
# d = DistanceFromLine(p1,p2,p3)
# print("Jarak p3, ke line",d)


import math

# def angle(A, B, C):
#     atan2 = math.atan2
#     pi = math.pi
#     Ax, Ay = A[0]-B[0], A[1]-B[1]
#     Cx, Cy = C[0]-B[0], C[1]-B[1]
#     a = atan2(Ay, Ax)
#     c = atan2(Cy, Cx)
#     if a < 0: a += pi*2
#     if c < 0: c += pi*2
#     return (pi*2 + c - a) if a > c else (c - a)

# def AngleFrom3Point(p1, p2, p3):
#     ''' Fungsi: Menerima 2 buah titik (p1 dan p2) yang membentuk segmen garis p1p2 dan mengembalikan sudut p3p1p2
#     Prekondisi : p1,p2,p3 adalah np.array 2 dimensi '''
#     x1x2s = math.pow((p1[0] - p3[0]),2)
#     x1x3s = math.pow((p1[0] - p2[0]),2)
#     x2x3s = math.pow((p3[0] - p2[0]),2)
    
#     y1y2s = math.pow((p1[1] - p3[1]),2)
#     y1y3s = math.pow((p1[1] - p2[1]),2)
#     y2y3s = math.pow((p3[1] - p2[1]),2)

#     cosine_angle = np.arccos((x1x2s + y1y2s + x2x3s + y2y3s - x1x3s - y1y3s)/(2*math.sqrt(x1x2s + y1y2s)*math.sqrt(x2x3s + y2y3s)))

#     return np.degrees(cosine_angle)

l = [[1,2],[2,3]]
print(l)
l += [[3,4]]
print(l)

p = [1,2,3,4]
p.reverse()
print(p)