import re

def string_to_array(file_name):
  with open(file_name, 'r') as file:
    content = file.read()
    content_arr = re.split(r"(?<=weight)\s+|(?<!\w{2})\s", content)
    return content_arr
