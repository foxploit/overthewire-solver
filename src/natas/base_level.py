import base64
import logging
from abc import ABC, abstractmethod
import requests


logger = logging.getLogger("natas")

class NatasLevel(ABC):
  """ Base Class: each level imports and implements exploit(). """

  num: int # Its definded in each subclass

  def __init__(self, password: str):
    self.password     = password
    self.session      = requests.Session()
    self.session.auth = (f"natas{self.num}", password)

  @property
  def base_url(self) -> str:
    return f"http://natas{self.num}.natas.labs.overthewire.org"

  @abstractmethod
  def exploit(self) -> str:
    """ It must return te password for the next level.  """
    raise NotImplementedError

  @property
  def explanation(self) -> str:
    """ Optional Override: writeup text of each level.  """
    return ""

  def run(self) -> str:
    next_password = self.exploit()
    return next_password
