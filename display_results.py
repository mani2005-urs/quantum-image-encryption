import matplotlib.pyplot as plt
import cv2

original = cv2.imread("images/input.png",0)
encrypted = cv2.imread("encrypted.png",0)
decrypted = cv2.imread("decrypted.png",0)

plt.subplot(1,3,1)
plt.title("Original")
plt.imshow(original,cmap="gray")

plt.subplot(1,3,2)
plt.title("Encrypted")
plt.imshow(encrypted,cmap="gray")

plt.subplot(1,3,3)
plt.title("Decrypted")
plt.imshow(decrypted,cmap="gray")

plt.show()