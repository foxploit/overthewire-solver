import questionary
from menu import main_menu
from halo import Halo
from src.natas.runner import solve_level as solve_natas_level
import os
import sys
from utils.clear import clear

def menu():
  level = main_menu()
  if level is None:
    return

  password = questionary.password(
    f"🔑 Password for natas{level} (current):"
  ).unsafe_ask()

  clear()

  if password is None:
    return

  action = questionary.select(
    "What do you need?",
    choices=[
      "💡 Hint only",
      "🔓 Reveal next password",
    ]
  ).unsafe_ask()

  clear()

  if action is None:
    return

  with Halo(text=f"Loading level {level}...", spinner="dots"):
    with open(os.devnull, 'w') as devnull:
      sys.stdout = devnull
      result = solve_natas_level(level, password)
      sys.stdout = sys.__stdout__

  if not result:
    questionary.print("❌ Wrong password or request failed.", style="bold fg:ansired")
    return

  if "Hint" in action:
    questionary.print(f"\n💡 {result['explanation']}\n", style="italic fg:ansiyellow")
  else:
    questionary.print(f"\n✅ natas{level + 1}: {result['password']}", style="bold fg:ansigreen")
    questionary.print(f"💡 {result['explanation']}\n", style="italic fg:ansiyellow")
