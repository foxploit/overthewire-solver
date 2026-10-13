<div align="center">

# 🦊 OverTheWire Solver

**Resuelve los niveles de [OverTheWire](https://overthewire.org/wargames/) de forma automatizada.**

![License](https://img.shields.io/badge/License-MIT-green)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Status](https://img.shields.io/badge/Status-WIP-orange)

</div>

---

## ¿Qué es?

*OverTheWire Solver* es una herramienta que automatiza la resolución de los wargames de [OverTheWire](https://overthewire.org/wargames/). Cada nivel implementa su propio exploit (`exploit()`), que se conecta al servidor del wargame, obtiene la contraseña del siguiente nivel y explica cómo lo ha conseguido.

> ⚠️ **Aviso:** este proyecto es solo para aprendizaje. Intenta resolver los niveles a mano primero: es la mejor forma de aprender.

## Características

* Menú interactivo (`questionary` + `halo`) para elegir wargame, nivel y contraseña actual.
* Modo CLI directo: resuelve un nivel concreto pasando `--level` y `--password`.
* Cada nivel incluye una explicación (`explanation`) de la técnica usada para resolverlo.
* Estructura modular: cada nivel es una clase (`NatasLevel`) independiente, fácil de ampliar a otros wargames.

## Wargames soportados

| Wargame    | Niveles resueltos | Estado          |
|------------|--------------------|-----------------|
| Natas      | 34/34 (0–33)       | ✅ Completo     |
| Bandit     | 0                  | 🚧 Por empezar  |
| Leviathan  | —                  | ⏳ En desarrollo|
| Krypton    | —                  | ⏳ En desarrollo|
| Narnia     | —                  | ⏳ En desarrollo|

## Instalación

```bash
git clone https://github.com/foxploit/overthewire-solver.git
cd overthewire-solver
pip install -r requirements.txt
```

## Uso

### Menú interactivo

```bash
python3 main.py
```

Elige el wargame, el nivel actual y la contraseña que ya tienes; después puedes pedir solo la pista (💡) o la contraseña del siguiente nivel (🔓).

### Modo directo (solo Natas por ahora)

```bash
python3 main.py --level 0 --password natas0
```

| Argumento    | Descripción                                   |
|--------------|------------------------------------------------|
| `--level`    | Número de nivel de Natas a resolver            |
| `--password` | Contraseña actual del nivel indicado           |

## Estructura del proyecto

```
overthewire-solver/
├── main.py                   # Entry point: menú interactivo o modo CLI
├── menu.py                   # Menú de selección de wargame/nivel
├── utils/
│   └── clear.py
├── src/
│   ├── natas/
│   │   ├── natas.py          # Flujo del menú para Natas
│   │   ├── runner.py         # Carga dinámica y ejecución de niveles
│   │   ├── base_level.py     # Clase base NatasLevel (ABC)
│   │   └── levels/
│   │       └── level_00.py … level_33.py   # 34 exploits, uno por nivel
│   └── bandit/                # Pendiente de implementar
├── requirements.txt
├── LICENSE
└── README.md
```

## Hoja de ruta

- [x] Completar Natas (34/34 niveles)
- [ ] Implementar Bandit
- [ ] Implementar Leviathan
- [ ] Implementar Krypton
- [ ] Implementar Narnia
- [ ] Tests automáticos por nivel

## Contribuciones

Las contribuciones son bienvenidas: abre un [Issue](https://github.com/foxploit/overthewire-solver/issues) o un [Pull Request](https://github.com/foxploit/overthewire-solver/pulls).

## Autor

**x0n3** — [github.com/foxploit](https://github.com/foxploit)

## Licencia

Distribuido bajo licencia MIT. Consulta [`LICENSE`](LICENSE) para más información.
