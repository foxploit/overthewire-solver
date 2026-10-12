from src.natas.runner import solve_all   as solve_all_natas_levels
from src.natas.runner import solve_level as solve_natas_level
import argparse

parser = argparse.ArgumentParser(description = "# TODO: Update Program info")
parser.add_argument("--level", type = int, help = "# TODO: Update help info for argument")
parser.add_argument("--password", type = str, help = "# TODO Update password argunment info")

if __name__ == "__main__":

  args = parser.parse_args()

  if args.level:
    result = solve_natas_level(args.level, args.password)
    print(f"natas{args.level + 1}: {result['password']}")
    print(f"  💡 {result['explanation']}\n")
  else:
    results = solve_all_natas_levels("natas0")
    for level, data in results.items():
      print(f"natas{level + 1}: {data['password']}")
      print(f"  💡 {data['explanation']}\n")
