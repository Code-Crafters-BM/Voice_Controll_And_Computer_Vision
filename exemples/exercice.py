import cv2
from matplotlib import pyplot as plt

# 1. Renversement (Flipping)
# Charger l'image
image = cv2.imread('image.png')


# Appliquer un flip horizontal
flipped_image = cv2.flip(image, 1)

# 2. Conversion en niveaux de gris
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 3. Seuil Fixe
ret1, thresh1 = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

# 4. Seuil Otsu
ret2, thresh2 = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# 5. Redimensionnement
resized_image = cv2.resize(image, (800, 600), interpolation=cv2.INTER_LINEAR)
plt.figure(figsize=(12, 8))
# Image originale
plt.subplot(2,3,1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original')
# Image renversée
plt.subplot(2,3,2)
plt.imshow(cv2.cvtColor(flipped_image, cv2.COLOR_BGR2RGB))
plt.title('Flipped Horizontally')
# Seuil Fixe
plt.subplot(2,3,3)
plt.imshow(thresh1, cmap='gray')
plt.title('Threshold Fixe')
# Seuil Otsu
plt.subplot(2,3,4)
plt.imshow(thresh2, cmap='gray')
plt.title('Threshold Otsu')
# Image redimensionnée
plt.subplot(2,3,5)
plt.imshow(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))
plt.title('Redimensionnée')
plt.tight_layout()
plt.show()
