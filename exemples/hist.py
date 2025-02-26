import cv2
from matplotlib import pyplot as plt

# Charger l'image en niveaux de gris
image = cv2.imread('image.png', cv2.IMREAD_GRAYSCALE)

# Calculer l'histogramme
hist = cv2.calcHist([image], [0], None, [256], [0,256])

# Afficher l'histogramme
plt.plot(hist)
plt.title('Histogramme des Pixels')
plt.xlabel('Intensité')
plt.ylabel('Nombre de Pixels')
plt.show()