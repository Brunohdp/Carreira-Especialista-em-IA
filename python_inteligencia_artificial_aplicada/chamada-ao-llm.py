from openai import OpenAI

client = OpenAI(
  base_url="http://127.0.0.1:1234/v1",
  api_key="lm_studio"
)

resposta_do_llm = client.chat.completions.create(
  model="google/gemma-3-1b",
  messages=[
    {"role": "system", "content": "Você é um modelo de IA que sempre responde de forma muito sarcastica."},
    {"role": "user", "content": "Qual é a capital da França?"}
  ],
  temperature=1.0
)

print(resposta_do_llm.choices[0].message.content)
