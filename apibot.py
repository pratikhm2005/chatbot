from openai import OpenAI

client= OpenAI(
    api_key="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",
    base_url="https://api.groq.com/openai/v1"

)



response = client.chat.completions.create(
    model= "llama3-70b-8192",
    messages = [
        {"role": "user" , "content": "hello,how are you?"}
    ]

)
print("bot:" , response.choice[0].message.content)