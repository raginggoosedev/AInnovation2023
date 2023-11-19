import ai


def get_name(sentence):
    name = ai.get_patient_name(sentence)
    return name


def get_symptoms(sentence):
    str = ai.get_patient_symptoms(sentence)
    symptoms = str.split(",")

    for symptom in symptoms:
        symptom = symptom.rstrip()
    return symptoms


def translate_symptoms(symptoms):
    str = ""
    for symptom in symptoms:
        str += symptom
    str = ai.translate_medical_terms(str)

    medical_terms = str.split(",")

    for medical_term in medical_terms:
        medical_term = medical_term.rstrip()
    return medical_terms


def get_possible_conditions(layman_terms, medical_terms):
    str = "Layman Terms: "
    for layman in layman_terms:
        str += layman + ", "

    str += " Medical_Terms: "
    for medical in medical_terms:
        str += medical + ", "

    str = ai.get_possible_conditions(str)

    return str