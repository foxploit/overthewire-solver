from src.natas.runner import solve_all

if __name__ == "__main__":

  results = solve_all("natas0")

  for level, data in results.items():

    print(f"natas{level + 1}: {data['password']}")
    print(f"  💡 {data['explanation']}\n")
