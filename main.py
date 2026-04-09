from key import generate_key
from modules.encrypt import encrypt_image
from modules.decrypt import decrypt_image

input_path = "image/input/image.png"

# Step 1: Generate key
key = generate_key()

# Step 2: Encrypt & show
encrypted_img = encrypt_image(input_path, key)

# Step 3: Ask user for key
user_key = int(input("Enter key to decrypt: "))

# Step 4: Decrypt & show
decrypt_image(encrypted_img, user_key)