import sys

import sourceReader
import db

def main():
  try:
    patientStream = sys.argv[1]
    databaseName = sys.argv[2]
    tableName = sys.argv[3]
    repository = db.Repository(databaseName, tableName)
    if not repository.is_database_initialized():
      repository.initialize_patient_database()
    contentArr = sourceReader.string_to_array(patientStream)
    repository.save_to_database(contentArr)
  except IndexError:
    print("Three arguments are needed: source of the string stream, database name and table name!")
  except FileNotFoundError:
    print("Check file name!")
  finally:
    repository.close_database_connection()


if __name__ == "__main__":
  main()