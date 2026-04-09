import cv2
from modules.arnold import inverse_arnold

def decrypt_image(encrypted_img, key):
    if encrypted_img is None:
        print("❌ No encrypted image")
        return

    # XOR Decryption
    decrypted = encrypted_img ^ key

    # Reverse Arnold
    original = inverse_arnold(decrypted, iterations=5)

    # Show image
    cv2.imshow("Decrypted Image", original)
    cv2.waitKey(0)
    cv2.destroyAllWindows()