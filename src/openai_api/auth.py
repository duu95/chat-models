import os
import openai

#Load env
openai.aiosession = os.getenv("API_TOKEN")

#Response interaction
response = openai.Completion.create(model="text-davinci-003", 
                                    prompt="Say this is a test", 
                                    temperature=0, 
                                    max_tokens=7)