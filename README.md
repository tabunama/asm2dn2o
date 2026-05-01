# ASM2d-GHG/N₂O

Python package for ASM2d-GHG/N₂O dynamic process modelling.

## Installation

The same compiled model can be installed using one of three PyPI package names:

```bash
pip install asm2dn2o
```

or:

```bash
pip install asm2dghg
```

or:

```bash
pip install asm2dg
```

`asm2dn2o` is the main compiled package. `asm2dghg` and `asm2dg` are alias packages that depend on `asm2dn2o` and expose the same model engine.

The package is currently distributed as a compiled wheel for:

- Windows x64
- CPython 3.12

## Import

```python
from asm2dn2o import asm2d_n2o, asm2d_ghg, asm2d_g
from asm2dn2o import clarifiers, combiner, delay
```

Alternative alias imports:

```python
from asm2dghg import asm2d_ghg, clarifiers, combiner, delay
from asm2dg import asm2d_g, clarifiers, combiner, delay
```

## Current modules

The package currently provides:

- `asm2d_n2o` : main ASM2d-N₂O / ASM2d-GHG biochemical reactor kernel
- `asm2d_ghg` : alias of `asm2d_n2o`
- `asm2d_g` : alias of `asm2d_n2o`
- `clarifiers` : primary and secondary clarifier separation blocks
- `combiner` : flow-weighted two-stream mixer
- `delay` : hydraulic delay block

## Package boundary

The PyPI wheel includes the compiled model kernels only.

## License and attribution

See:

- `LICENSE`
- `THIRD_PARTY_NOTICES.md`
