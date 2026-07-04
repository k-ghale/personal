
from ollama import chat

response = chat(
        model:"llama3.1",
        message: [{'role':'user', 'content':'hello !'}]
        )

print(response.message.content)
