from cryptography.fernet import Fernet
import hashlib

# Generar clave AES
key = Fernet.generate_key()

with open("aes_key.key", "wb") as f:
    f.write(key)

cipher = Fernet(key)

# Leer imagen
with open("prueba.jpeg", "rb") as f:
    data = f.read()

# Cifrar imagen
encrypted = cipher.encrypt(data)

with open("prueba_encriptada.bin", "wb") as f:
    f.write(encrypted)

# SHA256
sha256 = hashlib.sha256(data).hexdigest()

with open("hash.txt", "w") as f:
    f.write(sha256)

print("Imagen cifrada correctamente")
print("SHA256:", sha256)