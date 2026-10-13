import questionary
import sys
from utils.clear import clear

def main_menu():
  module = questionary.select(
    "🎯 Select a wargame:",
    choices=[
      "👁️  Natas",
      "🐀 Bandit          [coming soon]",
      "🦎 Leviathan       [in development]",
      "🔐 Krypton         [in development]",
      "💣 Narnia          [in development]",
      "❌ Exit"
    ]
  ).unsafe_ask()

  clear()

  if module is None or "Exit" in module:
    return None

  if "coming soon" in module or "in development" in module:
    print("🚧 Not available yet.")
    return None

  level = questionary.text(
    f"📂 Level for {module}:"
  ).unsafe_ask()

  clear()

  if level is None:
    return None

  return int(level)
  # TODO Introduce multiple modules on selection.
