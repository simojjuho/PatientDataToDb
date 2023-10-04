import sqlite3
from src.patient import Patient

class Repository:
  database_name = ""
  table_name = ""
  db_conn = None
  def __init__(self, database_name, table_name):
    self.databaseName = database_name
    self.tableName = table_name
    self.db_conn = self.connect_to_database()

  def connect_to_database(self):
      db_conn = sqlite3.connect(self.databaseName)
      print(f"Connected: {self.databaseName}")
      return db_conn

  def close_database_connection(self):
    self.db_conn.close()
    print("Database connection closed.")

  def check_database_connection(self):
    try:
      cursor = self.db_conn.cursor()
    except Exception:
      self.db_conn = self.connect_to_database()
      cursor = self.db_conn.cursor()
    finally:
      return cursor
  
  def initialize_patient_database(self):
    cursor = self.check_database_connection()
    cursor.execute(f"""CREATE TABLE {self.tableName} (
              Patientnumber varchar(20) NOT NULL,
              arrivaldate date NOT NULL CHECK (arrivaldate >= '2006-06-07'),
              releasedate date,
              ward varchar(10),
              weight numeric,
              PRIMARY KEY(Patientnumber, arrivaldate)
    )""")
    print(f"Created table: {self.tableName}") 
    self.db_conn.commit()


  def is_database_initialized(self):
    cursor = self.check_database_connection()
    cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{self.tableName}'")
    result = cursor.fetchall()
    return len(result) == 1

  def save_to_database(self, databaseRows):
    cursor = self.check_database_connection()
    for row in databaseRows:
        #Check in case of heading row or empty rows
        if "weight" in row or len(row) == 0:
          continue
        patient = Patient(row)
        try:
          cursor.execute(f"INSERT INTO {self.tableName} VALUES (?, ?, ?, ?, ?);", patient.to_tuple())
        except sqlite3.IntegrityError:
          params = (patient.release_date, patient.ward, patient.weight, patient.patient_number)
          cursor.execute(f"UPDATE {self.tableName} SET releasedate=?, ward=?, weight=? WHERE Patientnumber=?;", (params))
        finally:
          self.db_conn.commit()

