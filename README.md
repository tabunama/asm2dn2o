# asm2dn2o

Python package for ASM2d-N₂O dynamic process modelling.

## Installation

This package is currently distributed as a compiled wheel for:

- Windows x64
- CPython 3.12

Install from PyPI:

```bash
pip install asm2dn2o
```

## Import

Import the package in Python with:

```python
from asm2dn2o import asm2d_n2o, clarifiers, combiner, delay
```

## Current modules

The package currently provides:

- `asm2d_n2o` : main ASM2d-N₂O biochemical reactor kernel
- `clarifiers` : primary and secondary clarifier separation blocks
- `combiner` : flow-weighted two-stream mixer
- `delay` : hydraulic delay block


## License and attribution

See:

- `LICENSE`
- `THIRD_PARTY_NOTICES.md`