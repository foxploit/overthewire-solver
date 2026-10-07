import re
from src.natas.base_level import NatasLevel

class Level_03(NatasLevel):

  num = 3
  explanation = "After executing Ctrl + U, we see a hint that leads to /robots.txt.\n     If we access it, we can find another hint /s3cr3t is available but\n     disallowed with a users.txt in it with the next password."

  def exploit(self) -> str:

    resp  = self.session.get(self.base_url + "/s3cr3t/users.txt")
    match = re.search(r"^natas4:(.+)$", resp.text, re.MULTILINE)

    return match.group(1)
