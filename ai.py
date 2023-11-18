import os
import openai

os.environ['OPENAI_API_KEY'] = ""

#def get_response(name, problem):
def get_response(prompt):
    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You are a medical algorithm designed to take the problem of a patient writen in layman terms, "
                        "and write out the symptoms using medical terms, and then listing the different diagnosis' and "
                        "then also giving some possible remedies the doctor can prescribe.  Keep in mind, "
                        "you are giving information so that"
                        "a doctor can quickly find out what the problem with the patient is."
                        "The way it should be formatted, is by having the name of the patient written, then the "
                        "symptoms, then the diagnosis' written from"
                        "most likely to least likely, then the list of remedies, making sure to point out which "
                        "diagnosis they would be for"},
            {"role": "user",
             "content": name + problem}
        ],
        max_tokens=256,
        temperature=0.5
    )
    return completion.choices[0].message

def get_patient_name(prompt):
    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "A patient is going to give their personal information and the symptoms they are experience. I need you to tell me what their name is. For instance, if they say I am Walter White, you need to respond by saying Walter White. Nothing more nothing less, just the first name and last name"},
            {"role": "user",
             "content": prompt}
        ],
        max_tokens=256,
        temperature=0.5
    )
    return completion.choices[0].message.content

def get_patient_symptoms(prompt):
    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "A patient is going to give their personal information and the symptoms they are experience. I need you to tell me what their symptoms are. Please put all the symptoms they mention as a simple list, separated by commas"},
            {"role": "user",
             "content": prompt}
        ],
        max_tokens=256,
        temperature=0.5
    )
    return completion.choices[0].message.content

def translate_medical_terms(prompt):
    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "I am going to give you a list of symptoms that a patient is feeling. Translate them to precise medical doctor terms, and please put them in a comma-separated list. Make them sound fancy"},
            {"role": "user",
             "content": prompt}
        ],
        max_tokens=256,
        temperature=0.5
    )
    return completion.choices[0].message.content