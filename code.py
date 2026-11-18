import sys
import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def image_to_matrix_pil(path: str) -> np.ndarray:
    """Բացում է նկարը PIL-ի միջոցով և վերադարձնում որպես NumPy թվային մատրից (RGB ձևաչափով):"""
    with Image.open(path) as img_pil:
        return np.array(img_pil)

def analyze_image(image_path: str, print_full_matrix: bool = False) -> None:
    """Կարդում է նկարը OpenCV-ով, կատարում է գունային փոխակերպումներ,
    հաշվում է հիշողության ծավալը, ստուգում գծային ինդեքսավորումը և տպում մատրիցը:"""
    img = cv2.imread(image_path)
    if img is None:
        print(f"Սխալ․ հնարավոր չեղավ բեռնել նկարը՝ '{image_path}'։ Ստուգեք ֆայլի ուղին։")
        return
    
    print("Տիպը:", type(img))
    print("Գունավոր պատկերի չափսերը (Բարձրություն, Լայնություն, Ալիքներ):", img.shape)
    
    plt.imshow(img)
    plt.title("Նախնական պատկեր (BGR ձևաչափ)")
    plt.axis("off")
    plt.show()

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img_rgb)
    plt.title("Փոխակերպված պատկեր (RGB ձևաչափ)")
    plt.axis("off")
    plt.show()

    gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
    print("Մոխրագույն պատկերի չափսերը (M, N):", gray.shape)
    plt.imshow(gray, cmap="gray")
    plt.title("Մոխրագույն պատկեր (Grayscale)")
    plt.axis("off")
    plt.show()

    M, N = gray.shape
    k = 8  # 8 բիթ մեկ պիքսելի համար (0-255)
    total_bits = M * N * k
    total_bytes = total_bits // 8
    print(f"Հիշողության ծավալը՝ {total_bits} բիթ ({total_bytes} բայթ)")

    x_coord = 20  # սյուն (column / width)
    y_coord = 50  # տող (row / height)
    if y_coord < M and x_coord < N:
        alpha = N * y_coord + x_coord
        print(f"\nԿոորդինատներ (x={x_coord}, y={y_coord}):")
        print(f"Գծային ինդեքսը (α) = {alpha}")
        print(f"Ինտենսիվության արժեքը = {gray[y_coord, x_coord]}")

        y_recovered = alpha // N
        x_recovered = alpha % N
        print(f"Վերականգնված կոորդինատներ՝ x = {x_recovered}, y = {y_recovered}")

    print("\nՄատրիցի փոքր հատված (վերին ձախ 5x5 պիքսել):")
    print(gray[:5, :5])

    # Եթե print_full_matrix-ը True լինի, կտպի ամբողջական մատրիցը
    if print_full_matrix:
        np.set_printoptions(threshold=sys.maxsize)
        print("\nԱմբողջական մատրից.")
        print(gray)

if __name__ == "__main__":
    IMAGE_PATH = "images/normal-retinal-oct-image.jpg"  # Այստեղ կարող ես փոխել նկարի անունը կամ ուղին
    analyze_image(IMAGE_PATH, print_full_matrix=False)