<div align="center">

# 🦊 OverTheWire Solver

**Resuelve los niveles de [OverTheWire](https://overthewire.org/wargames/) de forma automatizada.**

![License](https://img.shields.io/badge/License-MIT-green)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Status](https://img.shields.io/badge/Status-WIP-orange)

</div>

---

## ¿Qué es?

*OverTheWire Solver* es una herramienta que automatiza la resolución de los wargames de [OverTheWire](https://overthewire.org/wargames/) ([Bandit], [Leviathan], [Natas]...). Se conecta a cada nivel, ejecuta la lógica necesaria para obtener la contraseña y pasa al siguiente.

> ⚠️ **Aviso:** este proyecto es solo para aprendizaje. Intenta resolver los niveles a mano primero: es la mejor forma de aprender.

## Características

* Resolución automática nivel a nivel de [wargame].
* [Guarda las contraseñas obtenidas en un fichero local.]
* [Salida por consola clara, con el progreso de cada nivel.]
* [Estructura modular: un solver por nivel, fácil de ampliar.]

## Wargames soportados

| Wargame   | Niveles resueltos | Estado |
|-----------|-------------------|--------|
| Bandit    | [0 – X]           | 🚧 En progreso |
| Natas     | [–]               | ⏳ Pendiente |

## Instalación

```bash
git clone https://github.com/foxploit/overthewire-solver.git
cd overthewire-solver
pip install -r requirements.txt
```

## Uso

```bash
python3 [main.py] --wargame bandit --level 0
```

| Argumento    | Descripción                      |
|--------------|----------------------------------|
| `--wargame`  | Wargame a resolver               |
| `--level`    | Nivel a resolver                 |

## Estructura del proyecto

```
overthewire-solver/
├── [main.py]
├── [solvers/]
├── requirements.txt
├── LICENSE
└── README.md
```

## Hoja de ruta

- [ ] Completar [Bandit]
- [ ] Añadir [Natas / Leviathan]
- [ ] [Tests por nivel]

## Contribuciones

Las contribuciones son bienvenidas: abre un [Issue](https://github.com/foxploit/overthewire-solver/issues) o un [Pull Request](https://github.com/foxploit/overthewire-solver/pulls).

## Autor

**x0n3** — [github.com/foxploit](https://github.com/foxploit)

## Licencia

Distribuido bajo licencia MIT. Consulta [`LICENSE`](LICENSE) para más información.
