import re
from src.natas.base_level import NatasLevel

class Level_01(NatasLevel):

  num = 1
  explanation = "Password in a commented HTML, visible with Crtl + U command only, Inspect Browser Function. is disabled"

  def exploit(self) -> str:

    resp  = self.session.get(self.base_url)
    match = re.search(r"is (\S+) -->", resp.text)

    return match.group(1)
