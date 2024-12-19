from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def main(image_path):
    # Carrega a imagem
    original_image = Image.open(image_path)

    # Converte para níveis de cinza
    grayscale_image = original_image.convert("L")

    # Binariza a imagem
    binary_image = grayscale_image.point(lambda x: 255 if x > 128 else 0)

    # Exibe as imagens
    plt.figure(figsize=(12, 4))
    
    plt.subplot(1, 3, 1)
    plt.title("Imagem Original")
    plt.imshow(original_image)
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.title("Imagem em Níveis de Cinza")
    plt.imshow(grayscale_image, cmap='gray')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.title("Imagem Binarizada")
    plt.imshow(binary_image, cmap='gray')
    plt.axis('off')

    plt.show()

# Substitua 'caminho/para/sua/imagem.jpg' pelo caminho da sua imagem
if __name__ == "__main__":
    main('Lenna.png')