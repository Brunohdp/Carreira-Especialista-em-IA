
import json
from contato_com_AI import recebe_linha_e_retorna_json


lista_reviews = []

with open("Resenhas_App_ChatGPT.txt", "r", encoding="utf-8") as resenhas_gpt:
    for line in resenhas_gpt:
        lista_reviews.append(line.strip())


lista_de_resenhas_json = []

for resenha in lista_reviews:
  resenha_json = recebe_linha_e_retorna_json(resenha)
  resenha_dict = json.loads(resenha_json)
  lista_de_resenhas_json.append(resenha_dict)


texto_resposta = json.dumps(lista_de_resenhas_json, ensure_ascii=False, indent=4)


with open("resenhas_tratadas.json", "w", encoding="utf-8") as arquivo_json:
    json.dump(lista_de_resenhas_json, arquivo_json, ensure_ascii=False, indent=4)

def processar_avaliacoes(lista_dicionarios):
    contador_positivas = 0
    contador_negativas = 0
    contador_neutras = 0
    lista_dicionarios_str = []
    
    for dicionario in lista_dicionarios:
        if dicionario['avaliacao'] == "Positiva":
            contador_positivas += 1
        elif dicionario['avaliacao'] == "Negativa":
            contador_negativas += 1
        else:
            contador_neutras += 1
        
        lista_dicionarios_str.append(str(dicionario))

    texto_final_unido = "#####".join(lista_dicionarios_str)
    
    return {"Positiva": contador_positivas, "Negativa": contador_negativas, "Neutra": contador_neutras}, texto_final_unido

contagem_avaliacoes, textos_unidos_lista = processar_avaliacoes(lista_de_resenhas_json)
  
print(f"Contagem das avaliações positivas: {contagem_avaliacoes['Positiva']}")
print(f"Contagem das avaliações negativas: {contagem_avaliacoes['Negativa']}")
print(f"Contagem das avaliações neutras: {contagem_avaliacoes['Neutra']}")
print(f"Textos unidos: {textos_unidos_lista}")

with open("textos_unidos.txt", "w", encoding="utf-8") as arquivo_texto:
    arquivo_texto.write(textos_unidos_lista)
