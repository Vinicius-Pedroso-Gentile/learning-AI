import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

historico = [
    {
        "role": "system",
        "content": "Responda em português"
    }
]


while True:
    pergunta = input("Você: ")

    if pergunta.lower() == 'sair':
        break

    historico.append({
        "role": "user",
        "content": pergunta
    })

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=historico,
    )

    resposta = response.choices[0].message.content

    historico.append({
        "role": "assistant",
        "content": resposta
    })

    print(f'Assistente: {resposta}') 
