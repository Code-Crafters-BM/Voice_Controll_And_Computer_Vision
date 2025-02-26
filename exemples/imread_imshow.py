import cv2

# Lire l'image
image = cv2.imread('image.png')

# Vérifier si l'image a été chargée correctement
if image is None:
    print("Erreur de chargement de l'image")
    exit()

# Afficher l'image
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()