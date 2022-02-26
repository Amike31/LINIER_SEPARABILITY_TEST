import numpy as np

p1 = np.array([6,0])
p2 = np.array([0,0])
p3 = np.array([0,6])

def AngelFromLine(p1,p2,p3):
    ba = p1 - p2
    bc = p3 - p2
    cosine = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    return np.arccos(cosine)

def Cosine_AngelFromLine(p1,p2,p3):
    ba = p1 - p2
    bc = p3 - p2
    return np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))

def AngelFromCosine(cosine):
    return np.arccos(cosine)

print(AngelFromLine(p1,p2,p3))
print(Cosine_AngelFromLine(p1,p2,p3))
print(AngelFromCosine(Cosine_AngelFromLine(p1,p2,p3)))