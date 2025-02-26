import cv2
from matplotlib import pyplot as plt

# Charger l'image en niveaux de gris
gray = cv2.imread('im.webp', cv2.IMREAD_GRAYSCALE)

# Appliquer un seuil fixe (127)
ret1, thresh1 = cv2.threshold(gray, 40, 255, cv2.THRESH_BINARY)
w
# Appliquer le seuil Otsu
ret2, thresh2 = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Afficher les résultats
plt.subplot(1,3,1), plt.imshow(gray, cmap='gray'), plt.title('Original')
plt.subplot(1,3,2), plt.imshow(thresh1, cmap='gray'), plt.title('Seuil Fixe')
plt.subplot(1,3,3), plt.imshow(thresh2, cmap='gray'), plt.title('Otsu')
plt.show()