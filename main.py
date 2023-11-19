from openai import OpenAI
import ai
from user_input import *

prompt = ""
print("---------------------------------------\n" "Please type your name and your problem:\n")
input(prompt)
print("---------------------------------------\n")

name = get_name(prompt)
symptoms = get_symptoms(prompt)
response = translate_symptoms(symptoms)
conditions = get_possible_conditions(symptoms, response)
client = OpenAI()

print("NAME:", name)
print("SYMPTOMS DESCRIBED:", symptoms)
print("MEDICAL TERMS:", response)
print("POSSIBLE CONDITIONS: ", conditions)
