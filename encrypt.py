import cv2
import matplotlib.pyplot as plt
from quantum_key import generate_key

# load image
img = cv2.imread("images/input.jpeg",0)

if img is None:
    print("Image not found")
    exit()

# generate quantum key
key = generate_key()
key_int = int(key,2)

# encrypt image
encrypted = img ^ key_int

# save encrypted image
cv2.imwrite("encrypted.jpeg", encrypted)

print("Quantum Key:", key)

# show images
plt.subplot(1,2,1)
plt.title("Original Image")
plt.imshow(img, cmap="gray")

plt.subplot(1,2,2)
plt.title("Encrypted Image")
plt.imshow(encrypted, cmap="gray")

plt.show()