# simulated_logger.py
# Simulação controlada de captura de entrada de teclado
# Projeto exclusivamente educacional

from datetime import datetime

log_file = "logs/keystrokes.txt"

print("=== Keylogger Simulado (Modo Seguro) ===")
print("Digite algumas informações para simulação.")
print("Para encerrar, digite: sair")
print("-" * 50)

with open(log_file, "a", encoding="utf-8") as file:
    while True:
        user_input = input("Digite algo: ")

        if user_input.lower() == "sair":
            file.write("\n[Encerrado pelo usuário]\n")
            print("Simulação finalizada.")
            break

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        file.write(f"[{timestamp}] {user_input}\n")
        file.flush()

        print("Entrada registrada com sucesso.")