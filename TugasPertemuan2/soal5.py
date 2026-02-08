import math

def jarak(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

hasil_jarak = jarak(1, 2, 4, 6)
print("Jarak =", hasil_jarak)