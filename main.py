from openai import OpenAI
import ai
from user_input import *

prompt = "I am Mr. White. I've been having severe abdominal pain, especially after eating fatty foods, and my stool is a light color. First name is Walter"


name = get_name(prompt)
symptoms = get_symptoms(prompt)
response = translate_symptoms(symptoms)
conditions = get_possible_conditions(symptoms, response)
client = OpenAI()

print("*********************")
print("\t", prompt)
print("*********************\n")

print("NAME:", name)
print("SYMPTOMS DESCRIBED:", symptoms)
print("MEDICAL TERMS:", response)
print("POSSIBLE CONDITIONS: ", conditions)