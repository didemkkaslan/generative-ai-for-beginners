import openai
import os
import dotenv

# import dotenv
dotenv.load_dotenv()

openai.api_key = os.getenv("API_KEY") 

# add your completion code
prompt = "Complete the following: Once upon a time there was a"

# engine
engine = "davinci-001"

completion = openai.Completion.create(engine=engine, prompt=prompt, max_tokens=600)

# print response
print(completion.choices[0].text)


#  very unhappy _____.

# Once upon a time there was a very unhappy mermaid.

