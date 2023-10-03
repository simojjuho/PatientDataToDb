import re

def string_to_array(fileName):
  with open(fileName, 'r') as file:
    content = file.read()
    contentArr = re.split(r"(?<=weight)\s+|(?<!\w{2})\s", content)
    return contentArr
