import re


def is_acceptable_password(password: str) -> bool:
  return True if len(password) > 6 and re.search(r'\d+', password) else False

print(is_acceptable_password('short'))
print(is_acceptable_password('muchlonger'))
print(is_acceptable_password('ashort'))
print(is_acceptable_password('muchlonger5'))
print(is_acceptable_password('sh5'))