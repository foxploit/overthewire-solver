import re
from src.natas.base_level import NatasLevel

class Level_00(NatasLevel):

  num = 0
  explanation = "Password in a commented HTML, visible with Crtl + U command or Inspect Browser Function"

  def exploit(self) -> str:
    resp  = self.session.get(self.base_url)
    match = re.search(r"is (\S+) -->", resp.text)
    return match.group(1)
