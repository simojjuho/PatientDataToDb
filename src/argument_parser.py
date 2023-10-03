import argparse

class ArgumentParser:
  parser = None
  def __init__(self):
    self.parser = argparse.ArgumentParser(
      prog="Patient data handler",
      description="Takes patient data out of string stream and saves in into a database.",
    )
    self.parser.add_argument(
      "file_name", help="The data source's relational path. EXAMPLE: ./src/datasource.txt"
    )
    self.parser.add_argument(
      "database_name", help="Name of the database"
    )
    self.parser.add_argument(
      "table_name", help="Name of the table that you want edited."
    )



""" 
#TODO: Finish argument parser, also logger

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