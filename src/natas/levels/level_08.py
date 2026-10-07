import re
from src.natas.base_level import NatasLevel
import base64
from bs4 import BeautifulSoup

class Level_08(NatasLevel):

  num = 8
  explanation = "On this level the secret is encoded with bin2hex(strrev(base64_encode())).\n     We reverse these steps to decode it and get the password to the next level."

  def exploit(self) -> str:

    resp_secret = self.session.get(self.base_url + "/index-source.html")
    secret      = re.search(r'\$encodedSecret\s*=\s*"([^"]+)"', BeautifulSoup(resp_secret.text, "html.parser").get_text()).group(1).replace('\xa0', ' ')
    payload     = {
      "secret": base64.b64decode(bytes.fromhex(secret)[::-1]).decode(),
      "submit": "Enviar consulta"
    }
    resp        = self.session.post(self.base_url, data = payload)
    match       = re.search(r"natas9 is (\S+)", resp.text).group(1)

    return match
