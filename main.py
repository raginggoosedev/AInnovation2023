from openai import OpenAI
import ai
from user_input import *

prompt = "I am Mr. White. Both my knee joints feel stiff, I have been fatigued and have a high fever. First name is Walter"

name = get_name(prompt)
symptoms = get_symptoms(prompt)
response = translate_symptoms(symptoms)
client = OpenAI()

print("*********************")
print("\t", prompt)
print("*********************\n")

print("NAME:", name)
print("SYMPTOMS DESCRIBED:", symptoms)
print("MEDICAL TERMS:", response)