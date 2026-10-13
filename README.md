<div align="center">

# 🦊 OverTheWire Solver

**Automated solver for [OverTheWire](https://overthewire.org/wargames/) wargame levels.**

![License](https://img.shields.io/badge/License-MIT-green)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Status](https://img.shields.io/badge/Status-WIP-orange)

</div>

---

## What is this?

*OverTheWire Solver* automates solving the [OverTheWire](https://overthewire.org/wargames/) wargames. Each level implements its own exploit (`exploit()`), which connects to the wargame server, retrieves the next level's password, and explains how it got it.

> ⚠️ **Disclaimer:** this project is for learning purposes only. Try to solve the levels by hand first — that's the best way to actually learn.

## Features

* Interactive menu (`questionary` + `halo`) to pick a wargame, level, and current password.
* Direct CLI mode: solve a specific level by passing `--level` and `--password`.
* Every level includes an `explanation` of the technique used to solve it.
* Modular structure: each level is an independent `NatasLevel` class, easy to extend to other wargames.

## Supported wargames

| Wargame    | Levels solved     | Status          |
|------------|-------------------|-----------------|
| Natas      | 34/34 (0–33)      | ✅ Complete     |
| Bandit     | 0                 | 🚧 Not started  |
| Leviathan  | —                 | ⏳ In progress  |
| Krypton    | —                 | ⏳ In progress  |
| Narnia     | —                 | ⏳ In progress  |

## Installation

```bash
git clone https://github.com/foxploit/overthewire-solver.git
cd overthewire-solver
pip install -r requirements.txt
```

## Usage

### Interactive menu

```bash
python3 main.py
```

Pick the wargame, your current level, and the password you already have; then choose either a hint (💡) or the next level's password (🔓).

### Direct mode (Natas only, for now)

```bash
python3 main.py --level 0 --password natas0
```

Example output:

```
natas1: scfWG6qNEIdzqVyfRwEGXyNUfFZkZeQ7
  💡 Password in a commented HTML, visible with Crtl + U command or
     Inspect Browser Function.
```

| Argument     | Description                              |
|--------------|-------------------------------------------|
| `--level`    | Natas level number to solve               |
| `--password` | Current password for that level           |

## Project structure

```
overthewire-solver/
├── main.py                   # Entry point: interactive menu or CLI mode
├── menu.py                   # Wargame/level selection menu
├── utils/
│   └── clear.py
├── src/
│   ├── natas/
│   │   ├── natas.py          # Natas menu flow
│   │   ├── runner.py         # Dynamic level loading and execution
│   │   ├── base_level.py     # NatasLevel base class (ABC)
│   │   └── levels/
│   │       └── level_00.py … level_33.py   # 34 exploits, one per level
│   └── bandit/                # Not implemented yet
├── requirements.txt
├── LICENSE
└── README.md
```

## Roadmap

- [x] Complete Natas (34/34 levels)
- [ ] Implement Bandit
- [ ] Implement Leviathan
- [ ] Implement Krypton
- [ ] Implement Narnia
- [ ] Automated tests per level

## Contributing

Contributions are welcome: open an [Issue](https://github.com/foxploit/overthewire-solver/issues) or a [Pull Request](https://github.com/foxploit/overthewire-solver/pulls).

## Author

**foxploit animal de colina** — [github.com/foxploit](https://github.com/foxploit)

## License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for more information.
