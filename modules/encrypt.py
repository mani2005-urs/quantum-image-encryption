import cv2
from modules.arnold import arnold_transform

def encrypt_image(input_path, key):
    img = cv2.imread(input_path, 0)

    if img is None:
        print("❌ Image not found")
        return None

    img = cv2.resize(img, (256, 256))

    # Arnold Scramble
    scrambled = arnold_transform(img, iterations=5)

    # XOR Encryption
    encrypted = scrambled ^ key

    # Show image
    cv2.imshow("Encrypted Image", encrypted)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return encrypted