import csv
import sqlite3
import patient_functions

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
        #Check in case of heading row
        if "weight" in row or len(row) == 0:
          continue
        patient = patient_functions.format_patient(row)
        try:
          if(len(patient) == 5): 
            params = (patient[0], patient[1], patient[2], patient[3], patient[4])
            cursor.execute(f"INSERT INTO {self.tableName} VALUES (?, ?, ?, ?, ?);", params)
          else:
            params = (patient[0], patient[1], patient[2], patient[3])
            cursor.execute(f"INSERT INTO {self.tableName} (Patientnumber, arrivaldate, ward, weight) VALUES (?, ?, ?, ?);", params)
        except sqlite3.IntegrityError:
          if(len(patient) == 5): 
            params = (patient[2], patient[3], patient[4], patient[0])
            cursor.execute(f"UPDATE {self.tableName} SET releasedate=?, ward=?, weight=? WHERE Patientnumber=?;", (params))
          else:
            params = (patient[2], patient[3], patient[0])
            cursor.execute(f"UPDATE {self.tableName} SET ward=?, weight=? WHERE Patientnumber=?;", (params))
        finally:
          self.db_conn.commit()

