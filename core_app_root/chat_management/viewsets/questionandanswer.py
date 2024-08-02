import asyncio
from core_app_root.chat_management.models import GenieResponseToUser,UserQuestions



def chatRequest(message):
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
        {"role": "user", "content": f" {message} just make this straight to point  no much talk please and also try to be direct in your reply addressing main important things in the question, without explaining each ..just list key things "}
    ]
    )

    # await UserQuestions.objects.create(email=email,user_questions=message)
    return str(completion.choices[0].message.content)
# asyncio.run(chatRequest("what is java"))
