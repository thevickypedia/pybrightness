![Generic badge](https://img.shields.io/badge/Platform-Linux|MacOS|Windows-1f425f.svg)
[![pypi-publish](https://github.com/thevickypedia/pybrightness/actions/workflows/python-publish.yml/badge.svg)](https://github.com/thevickypedia/pybrightness/actions/workflows/python-publish.yml)

# PyBrightness
Python module to modify display brightness on Linux, Windows and macOS

### Installation
```shell
python -m pip install pybrightness
```

### Usage
```python
import pybrightness

pybrightness.increase()  # Increase to 100%
pybrightness.decrease()  # Decrease to 0%
pybrightness.custom(percent=72)  # Set to a custom level
```

## [Release Notes](https://github.com/thevickypedia/pybrightness/blob/main/release_notes.rst)
**Requirement**
```shell
python -m pip install gitverse
```

**Usage**
```shell
gitverse-release reverse -f release_notes.rst -t 'Release Notes'
```

## Pypi Package
[![pypi-module](https://img.shields.io/badge/Software%20Repository-pypi-1f425f.svg)](https://packaging.python.org/tutorials/packaging-projects/)

[https://pypi.org/project/pybrightness/](https://pypi.org/project/pybrightness/)

## License & copyright

&copy; Vignesh Rao

Licensed under the [MIT License](https://github.com/thevickypedia/pybrightness/blob/main/LICENSE)
