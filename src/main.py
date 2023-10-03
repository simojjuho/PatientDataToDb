import sys

import source_reader as source_reader
import repository as repository
import argument_parser as ap

def main():
  a_parser = ap.ArgumentParser()
  args = a_parser.parser.parse_args()
  try:
    repo = repository.Repository(args.database_name, args.table_name)
    if not repo.is_database_initialized():
      repo.initialize_patient_database()
    contentArr = source_reader.string_to_array(args.file_name)
    repo.save_to_database(contentArr)
  except FileNotFoundError:
    print("Check source file name!")
  finally:
    repo.close_database_connection()


if __name__ == "__main__":
  main()