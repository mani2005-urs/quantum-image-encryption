import random

def generate_key():
    key = random.randint(0, 255)
    print(f"🔑 Key Generated: {key}")
    return key