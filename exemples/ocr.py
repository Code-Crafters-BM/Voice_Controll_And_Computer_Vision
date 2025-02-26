import cv2
import pytesseract
import numpy as np
from pdf2image import convert_from_path
import matplotlib.pyplot as plt

# Configurer le chemin vers Tesseract si nécessaire
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Chemin du fichier PDF et du fichier texte
pdf_path = 'Demande_reservation formation Vision.pdf'
output_text_path = 'extracted_text.txt'

# Ouvrir un fichier texte pour sauvegarder les résultats OCR
with open(output_text_path, 'w', encoding='utf-8') as output_file:
    try:
        # Étape 1 : Convertir le PDF en images
        images = convert_from_path(pdf_path, dpi=300)  # Résolution 300 dpi pour meilleure précision

        for i, page in enumerate(images):
            # Convertir la page en numpy array pour OpenCV
            page_array = cv2.cvtColor(np.array(page), cv2.COLOR_RGB2BGR)

            # Prétraitement : conversion en niveaux de gris
            gray = cv2.cvtColor(page_array, cv2.COLOR_BGR2GRAY)

            # Binarisation
            _, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

            # Appliquer l'OCR pour extraire le texte
            text = pytesseract.image_to_string(binary, lang='eng')  # Change 'eng' to 'fra' for French text

            # Sauvegarder le texte extrait dans le fichier
            output_file.write(f"--- Texte extrait de la page {i+1} ---\n")
            output_file.write(text + "\n")
            output_file.write("-" * 80 + "\n")

            # Afficher les images à chaque étape
            plt.figure(figsize=(12, 8))

            # Image originale
            plt.subplot(1, 3, 1)
            plt.imshow(cv2.cvtColor(page_array, cv2.COLOR_BGR2RGB))  # Convertir pour l'affichage RGB
            plt.title(f"Page {i+1} : Originale")
            plt.axis('off')

            # Image en niveaux de gris
            plt.subplot(1, 3, 2)
            plt.imshow(gray, cmap='gray')
            plt.title(f"Page {i+1} : Niveaux de Gris")
            plt.axis('off')

            # Image binaire
            plt.subplot(1, 3, 3)
            plt.imshow(binary, cmap='gray')
            plt.title(f"Page {i+1} : Binaire")
            plt.axis('off')

            # Afficher les résultats visuels
            plt.tight_layout()
            plt.show()

            # Afficher le texte extrait dans la console
            print(f"Texte extrait de la page {i+1} :\n")
            print(text)
            print("-" * 80)  # Ligne de séparation pour plus de lisibilité

    except Exception as e:
        print(f"Erreur lors du traitement du fichier PDF : {e}")
