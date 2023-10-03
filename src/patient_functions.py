from datetime import datetime
import re

def get_date(date_string):
  input_format = '%d.%m.%Y'
  parsedDate = datetime.strptime(date_string, input_format).date()
  return parsedDate

def format_patient(patient_string):
    patient = patient_string.split(',')
    for index, element in enumerate(patient):
        if element == "":
            del patient[index]
        if index == 1 or (index == 2 and re.match(r"\d{1,2}.\d{1,2}.\d{4}", patient[index])):
            patient[index] = get_date(element)
    return patient

#TODO: Into class structure