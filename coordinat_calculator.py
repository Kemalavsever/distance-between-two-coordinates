def euclideanDistance(p1, p2):
    """
    p1 ve p2, 2D uzayında (x, y) şeklinde demetlerdir.
    Öklid mesafesini hesaplayıp döndürür.
    """
    x1, y1 = p1
    x2, y2 = p2
    # Üs alarak karekök hesaplanır
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return distance

# Kullanıcıdan nokta sayısını al
n = int(input("Kaç nokta gireceksiniz? "))

# Noktaları tutacak liste
points = []

# Kullanıcıdan noktaları al
for i in range(n):
    # Örnek giriş formatı: "1.2 3.4" -> x=1.2, y=3.4
    x, y = map(float, input(f"{i+1}. noktanın (x y): ").split())
    points.append((x, y))

# Tüm nokta çiftleri arasındaki mesafeleri hesaplayacak liste
distances = []

# Nokta çiftleri arasındaki mesafeleri hesapla
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

# Mesafeler listesi boş değilse minimumu bul
if distances:
    min_distance = min(distances)
    print("Tüm nokta çiftleri arasındaki minimum mesafe:", min_distance)
else:
    print("Hesaplanacak mesafe yok (en az 2 nokta girilmelidir).")
