import cv2
import matplotlib.pyplot as plt

# get key
key = input("Enter quantum key (8-bit binary): ")

# check if key is valid
if len(key) != 8 or any(c not in "01" for c in key):
    print("❌ Wrong key format! Please enter a valid 8-bit binary key.")
    exit()

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

print("✅ Image decrypted successfully")

# show images
plt.subplot(1,2,1)
plt.title("Encrypted Image")
plt.imshow(encrypted, cmap="gray")

plt.subplot(1,2,2)
plt.title("Decrypted Image")
plt.imshow(decrypted, cmap="gray")

plt.show()