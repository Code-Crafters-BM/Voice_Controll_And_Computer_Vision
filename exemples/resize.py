import cv2
import matplotlib.pyplot as plt

# Charger l'image
image = cv2.imread('image.png')

# Redimensionner l'image à 800x600
resized_image = cv2.resize(image, (800, 600), interpolation=cv2.INTER_LINEAR)

# Convertir l'image en niveaux de gris
gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

# Convertir les images de BGR à RGB pour l'affichage avec Matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
resized_image_rgb = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)

# Afficher les images avec Matplotlib
plt.figure(figsize=(12, 8))

# Image originale
plt.subplot(1, 3, 1)
plt.imshow(image_rgb)
plt.title('Original')
plt.axis('off')

# Image redimensionnée
plt.subplot(1, 3, 2)
plt.imshow(resized_image_rgb)
plt.title('Redimensionnée')
plt.axis('off')

# Image en niveaux de gris
plt.subplot(1, 3, 3)
plt.imshow(gray_image, cmap='gray')
plt.title('Niveaux de Gris')
plt.axis('off')

# Afficher toutes les images
plt.tight_layout()
plt.show()
