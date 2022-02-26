import numpy as np
def DetFrom3Point(p1,p2,p3):
    mat = np.array([[1,1,1],
                    [p1[0],p2[0],p3[0]],
                    [p1[1],p2[1],p3[1]]])
    return np.linalg.det(mat)

p1 = np.array([1,2])
p2 = np.array([4,10])
p3 = np.array([1,4])

print

det = DetFrom3Point(p1,p2,p3)
print(det)
