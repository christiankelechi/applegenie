import asyncio
async def chatRequest(message):
    from openai import OpenAI
    import os
    import openai

    openai.api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI()

    completion = client.chat.completions.create(
    model="gpt-4o",
    max_tokens=150,

    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"{message}"}
    ]
    )

    return str(completion.choices[0].message.content)
# asyncio.run(chatRequest("what is java"))
