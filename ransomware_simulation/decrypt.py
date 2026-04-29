from cryptography.fernet import Fernet

# Caminho do arquivo de teste
file_path = "test_files/exemplo.txt"

# Ler chave salva
with open("thekey.key", "rb") as key_file:
    key = key_file.read()

# Inicializar Fernet
fernet = Fernet(key)

# Ler conteúdo criptografado
with open(file_path, "rb") as encrypted_file:
    encrypted_data = encrypted_file.read()

# Descriptografar conteúdo
decrypted_data = fernet.decrypt(encrypted_data)

# Restaurar conteúdo original
with open(file_path, "wb") as decrypted_file:
    decrypted_file.write(decrypted_data)

print("Arquivo descriptografado com sucesso.")