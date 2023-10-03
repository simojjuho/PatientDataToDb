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

""" 
class Patient:
    def __init__(self, data):
        self.patient_number = data[0]
        self.arrival_date = data[1]
        self.release_date = data[2] if len(data) > 3 else None
        self.ward = data[3] if len(data) > 3 else data[2]
        self.weight = data[4] if len(data) > 4 else None

    def to_tuple(self):
        if self.release_date:
            return (self.patient_number, self.arrival_date, self.release_date, self.ward, self.weight)
        else:
            return (...) """