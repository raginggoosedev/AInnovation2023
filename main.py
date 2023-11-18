from openai import OpenAI

import ai
response = ai.get_response("Nicholas Woo", "I am feeling chest pains, as if my chest is tearing")
client = OpenAI()
print(response)