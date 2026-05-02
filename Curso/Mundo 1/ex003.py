from cores import status_sim as colorir

a = input('Digite algo para validar: ')

print(f"\n--- RELATÓRIO DE STATUS: {a} ---")
print(f"É alfanumérico?    -> {colorir(a.isalnum())}")
print(f"É apenas letra?    -> {colorir(a.isalpha())}")
print(f"É apenas número?   -> {colorir(a.isdigit())}")
print(f"Está em minúsculo? -> {colorir(a.islower())}")
print(f"Só tem espaços?    -> {colorir(a.isspace())}")
print("-" * 35)
