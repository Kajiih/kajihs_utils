[![Build][github-ci-image]][github-ci-link]
[![Coverage Status][codecov-image]][codecov-link]
[![PyPI Version][pypi-image]][pypi-link]
[![PyPI - Python Version][python-image]][pypi-link]
![License][license-image]

# Kajihs Utils

Fully typed, plausibly practical, and remarkably random utilities for me—and maybe for you too.

## ⬇️ Installation

You can install **kajihs_utils** via pip:

```bash
pip install kajihs-utils
```

## 🏃 Getting Started

```python:dev/readme_snippets/formatted/features_demo.py
from kajihs_utils import get_first
from kajihs_utils.loguru import prompt, setup_logging
from kajihs_utils.numpy_utils import find_closest, Vec2d

# Useful protocols for structural subtyping
from kajihs_utils.protocols import SupportsLessThan

# Get first key existing in a dict
d = {"a": 1, "b": 2, "c": 3}
print(get_first(d, ["x", "a", "b"]))  # Output: 1


# === Loguru features ===
# Better logged and formatted prompts
prompt("Enter a number")  

# Simply setup well formatted logging in files and console
setup_logging(prefix="app", log_dir="logs")

# === Numpy features ===
import numpy as np

x = np.array([[0, 0], [10, 10], [20, 20]])
print(find_closest(x, [[-1, 2], [15, 12]]))  # Output: [0 1]

# Vec2d class
v = Vec2d(3.0, 4.0)
print("Original Vec2d:", v)  # Output: Original Vec2d: [3. 4.]
print("As a tuple", tuple(v))  # Output: As a tuple (np.float64(3.0), np.float64(4.0))
print("x coordinate:", v.x)  # Output: x coordinate: 3.0
print("y coordinate:", v.y)  # Output: y coordinate: 4.0
print("Magnitude:", v.magnitude())  # Output: Magnitude: 5.0
print("Normalized vector:", v.normalized())  # Output: Normalized vector: [0.6 0.8]
print("Angle (degrees):", v.angle())  # Output: Angle (degrees): 53.13010235415598
print("Rotated by 90 degrees:", v.rotate(90, center=(1, 1)))  # Output: Rotated by 90 degrees: [-2.  3.]
```

## 🧾 License

[MIT license](LICENSE)

<!-- Links -->
[github-ci-image]: https://github.com/Kajiih/kajihs_utils/actions/workflows/build.yml/badge.svg?branch=main
[github-ci-link]: https://github.com/Kajiih/kajihs_utils/actions?query=workflow%3Abuild+branch%3Amain

[codecov-image]: https://img.shields.io/codecov/c/github/Kajiih/kajihs_utils/main.svg?logo=codecov&logoColor=aaaaaa&labelColor=333333
[codecov-link]: https://codecov.io/github/Kajiih/kajihs_utils

[pypi-image]: https://img.shields.io/pypi/v/kajihs-utils.svg?logo=pypi&logoColor=aaaaaa&labelColor=333333
[pypi-link]: https://pypi.python.org/pypi/kajihs-utils

[python-image]: https://img.shields.io/pypi/pyversions/kajihs-utils?logo=python&logoColor=aaaaaa&labelColor=333333
[license-image]: https://img.shields.io/badge/license-MIT_license-blue.svg?labelColor=333333
