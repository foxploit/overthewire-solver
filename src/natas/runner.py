import importlib
import logging

logging.basicConfig(level = logging.INFO, format = "%(message)s")
logger = logging.getLogger("natas")

def load_level(n: int, password: str):

  module   = importlib.import_module(f"src.natas.levels.level_{n:02d}")
  cls_name = f"Level_{n:02d}"
  cls = getattr(module, cls_name)

  return cls(password)

def solve_all(start_password: str = "natas0", up_to: int = 34):

  password = start_password
  results = {}

  for n in range(up_to):

    try:

      level = load_level(n, password)
      password = level.run()
      results[n] = {"password": password, "explanation": level.explanation}

    except Exception as e:

      logger.error("Failed at level %s: %s", n, e)

      break

  return results
