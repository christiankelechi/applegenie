# import asyncio
# from core_app_root.chat_management.models import GenieResponseToUser,UserQuestions
# from openai import OpenAI
# import os
# import openai
# from datasets import load_dataset
# import pandas as pd
# import json
# from dotenv import load_dotenv
# load_dotenv()
# def chatRequest(message):
    
    
#     openai.api_key = os.getenv("OPENAI_API_KEY")
#     # client = OpenAI(api_key=openai.api_key)

#     completion = openai.chat.completions.create(
#     model="gpt-4o",
#     max_tokens=200,
#     temperature=0.8,
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": f" {message} just make this straight to point  no much talk please and also try to be direct in your reply addressing main important things in the question, without explaining each ..just list key things and also attach web links for places or key definitions and references and also images  encryted to link and also render the output to be a full text not gpt text showing stars .just direct to point"}
#     ]
#     )

#     # await UserQuestions.objects.create(email=email,user_questions=message)
#     return str(completion.choices[0].message.content)
# # asyncio.run(chatRequest("what is java"))

import asyncio
from core_app_root.chat_management.models import GenieResponseToUser,UserQuestions
from openai import OpenAI
import os
import openai
from datasets import load_dataset
import pandas as pd
import json
import google.generativeai as genai
import os


from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
def chatRequest(message):
    genai.configure(api_key=os.environ["API_KEY"])
  
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(f" {message} just make this straight to point  no much talk please and also try to be direct in your reply addressing main important things in the question, without explaining each .and make it to reply like real human too such that all special symbols are removed entirely and make it extrem short as possible unless when what being studied need to be big ")
   

    
   

    # await UserQuestions.objects.create(email=email,user_questions=message)
    return str(response.text)
# asyncio.run(chatRequest("what is java"))
