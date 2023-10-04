import os
import pytest

from src.repository import Repository

class Test_Repository:
  db_path = "./src/tests/test_database.db"
  db_table = "test_patients"
  db_rows = ["1151925,12.3.2006,17.3.2006,EP,76.3", "9442583,20.6.2006,30.6.2006,EP,53.8"]
  

  @pytest.fixture
  def repo(self):
    return Repository(self.db_path, self.db_table)
  
  @pytest.fixture(autouse=True)
  def delete_database(self):
    yield
    if os.path.exists(self.db_path):
      os.remove(self.db_path)
  
  def test_initialize_database(self, repo):
    repo.initialize_patient_database()
    assert repo.is_database_initialized() == True

  def test_save_to_database_successful(self, repo):
    repo.initialize_patient_database()
    assert repo.is_database_initialized() == True
    repo.save_to_database(self.db_rows)
    cursor = repo.check_database_connection()
    cursor.execute(f"""SELECT * FROM test_patients
                   """)
    entries = cursor.fetchall()
    assert len(entries) == 1