import os
from openai import OpenAI

# os.environ["GITHUB_API_KEY"] = "API_KEY_GITHUB"

client_openai = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio"
)

# Modelo de requisição para o modelo de linguagem da OpenAI:
# resposta = client_openai.chat.completions.create(
#     model="Meta-Llama-3.1-8B-Instruct",
#     messages=[{"role": "user", "content": "Me explique o que é uma variável em Python em uma frase curta."}],
#     max_tokens=300
# )

def recebe_linha_e_retorna_json(linha):
  resposta_do_llm = client_openai.chat.completions.create(
    model="google/gemma-3-1b",
    messages=[{"role": "system", "content": f"""Você é um especialista em análise de dados e conversão de dados para JSON. Você entrega apenas a resposta em formato JSON, sem nenhum texto adicional."""},
                
              {"role": "user", "content": f"""Vou te passar muitas resenhas de análises diversas onde cada resenha é separada por "#####" e eu quero que você separe cada resenha em quatro chaves: 'usuario', 'resenha original', 'resenha_pt-br, 'avaliacao' (Positiva, Negativa, Neutra). 

              Depois quero que você me retorne APENAS um formato JSON, sendo obrigatoriamente uma LISTA DE DICIONÁRIOS, NÃO ACRESCENTE NENHUM OUTRO TEXTO À RESPOSTA ALÉM DA LISTA DE DICIONÁRIOS, com a seguinte estrutura:
              - 'usuario': irá conter onome do usuario que fez a resenha;
              - 'resenha original': irá conter a resenha original em algum idioma;
              - 'resenha_pt-br': irá conter a resenha traduzida para o português do Brasil;
              - 'avaliacao': irá conter a avaliação da resenha (Positiva, Negativa, Neutra).
                
              Exemplo de entrada:
                '53409593$Breno Santos$The app is fantastic! It has helped me organize my tasks and improve my productivity. Highly recommended!'
                
                Exemplo de saída:
              [
                  {{
                    "usuario": "Breno Santos",
                    "resenha original": "The app is fantastic! It has helped me organize my tasks and improve my productivity. Highly recommended!",
                    "resenha_pt-br": "O aplicativo é fantástico! Ele me ajudou a organizar minhas tarefas e melhorar minha produtividade. Altamente recomendado!",
                    "avaliacao": "Positiva"
                }}
              ]

              Exemplo de entrada:
                '62568452$Carlos da Silva$je n'aime pas cette application. Elle est lente et souvent boguée. Je ne la recommande pas du tout.'
                
                Exemplo de saída:
              [
                  {{
                    "usuario": "Carlos da Silva",
                    "resenha original": "je n'aime pas cette application. Elle est lente et souvent boguée. Je ne la recommande pas du tout.",
                    "resenha_pt-br": "Eu não gosto desta aplicação. Ela é lenta e frequentemente bugada. Eu não a recomendo de forma alguma.",
                    "avaliacao": "Negativa"
                }}
              ]
              
              Faça isso para todas as resenhas que eu te passar abaixo:
              {linha}"""}
      ],
      temperature=0.0
  )
  resposta = resposta_do_llm.choices[0].message.content.replace("```json", "").replace("```", "")
  print(resposta)
  return resposta

