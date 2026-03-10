import cv2
import matplotlib.pyplot as plt

# get key
key = input("Enter quantum key: ")

key_int = int(key,2)

# load encrypted image
encrypted = cv2.imread("encrypted.jpeg",0)

if encrypted is None:
    print("Encrypted image not found")
    exit()

# decrypt
decrypted = encrypted ^ key_int

# save decrypted image
cv2.imwrite("decrypted.jpeg", decrypted)

print("Image decrypted successfully")

# show images
plt.subplot(1,2,1)
plt.title("Encrypted Image")
plt.imshow(encrypted, cmap="gray")

plt.subplot(1,2,2)
plt.title("Decrypted Image (Original)")
plt.imshow(decrypted, cmap="gray")

plt.show()