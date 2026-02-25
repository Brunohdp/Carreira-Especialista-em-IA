import requests

url = "https://cdn3.gnarususercontent.com.br/4790-python/Resenhas_App_ChatGPT.txt"

# 1. Baixando o conteúdo bruto
resposta = requests.get(url)

# 2. AQUI ESTÁ O TRUQUE:
resposta_final = resposta.encoding = 'utf-8'  # Forçando a codificação correta

# 3. Exportando o conteúdo corrigido para um novo arquivo
with open("Resenhas_App_ChatGPT.txt", "w", encoding="utf-8") as f:
    list_of_lines = [line + "\n" for line in resposta.text.splitlines()]
    f.writelines(list_of_lines)

# 4. Imprimindo as primeiras 5 linhas para testar
print("--- Texto Corrigido (UTF-8) ---")
print(resposta.text[:500])
