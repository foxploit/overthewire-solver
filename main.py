from src.natas.runner import solve_all   as solve_all_natas_levels
from src.natas.runner import solve_level as solve_natas_level
from src.natas.natas  import menu        as WargamesApp
import argparse
import sys
import questionary
from utils.clear import clear

parser = argparse.ArgumentParser(description="# TODO: Update Program info")
parser.add_argument("--level",    type=int, help="# TODO: Update help info for argument")
parser.add_argument("--password", type=str, help="# TODO Update password argunment info")

if __name__ == "__main__":

  args = parser.parse_args()

  try:
    if args.level is not None and args.password:
      result = solve_natas_level(args.level, args.password)
      print(f"natas{args.level + 1}: {result['password']}")
      print(f"  💡 {result['explanation']}\n")
    else:
      while True:
        WargamesApp()
        again = questionary.confirm("🔄 Continue?").ask()
        clear()
        if not again:
          print("\n👋 Bye!")
          break
  except KeyboardInterrupt:
    print("\n👋 Bye!")
    sys.exit(0)
