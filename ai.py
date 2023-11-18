import os
import openai

os.environ['OPENAI_API_KEY'] = ""

def get_response(name, problem):
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
