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