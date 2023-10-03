import re
from datetime import datetime

class Patient:
  def __init__(self, data):
    self.patient_row = self.format_patient(data)
    self.patient_number = self.patient_row[0]
    self.arrival_date = self.patient_row[1]
    self.release_date = self.patient_row[2]
    self.ward = self.patient_row[3]
    self.weight = self.patient_row[4]

  def to_tuple(self):
    return (self.patient_number, self.arrival_date, self.release_date, self.ward, self.weight)
    
  def get_date(self, date_string):
    input_format = '%d.%m.%Y'
    parsedDate = datetime.strptime(date_string, input_format).date()
    return parsedDate

  def format_patient(self, patient_string):
      patient = patient_string.split(',')
      for index, element in enumerate(patient):
          if element == "":
              patient[index] = None
          elif index == 1 or (index == 2 and re.match(r"\d{1,2}.\d{1,2}.\d{4}", patient[index])):
              patient[index] = self.get_date(element)
      return patient


