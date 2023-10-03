import datetime
from patient import Patient


class Test_Patient:
  patient_row_release = "1151925,12.3.2006,17.3.2006,EP,76.3"
  patient_row_no_release = "9442583,20.6.2006,,EP,53.8"
  patient = Patient(patient_row_release)

  def test_format_patient_length_release(self):
    assert len(self.patient.format_patient(self.patient_row_release)) == 5
    
  def test_format_patient_length_no_release(self):
    assert len(self.patient.format_patient(self.patient_row_no_release)) == 5

  def test_get_date_return_correct(self):
    date_string = "12.3.2006"
    assert isinstance(self.patient.get_date(date_string), datetime.date)
