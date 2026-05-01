Installation
============

Purpose
-------

This page explains how to install the published package and what is included in
the PyPI wheel.

Install from PyPI
-----------------

The same compiled ASM2d-GHG/N₂O model can be installed using any of the
following package names:

.. code-block:: bash

   pip install asm2dn2o

or:

.. code-block:: bash

   pip install asm2dghg

or:

.. code-block:: bash

   pip install asm2dg

The package ``asm2dn2o`` is the main compiled package. The packages
``asm2dghg`` and ``asm2dg`` are alias packages that depend on ``asm2dn2o``.

Verify the import
-----------------

.. code-block:: python

   from asm2dn2o import asm2d_n2o, clarifiers, combiner, delay
   from asm2dghg import asm2d_ghg
   from asm2dg import asm2d_g

   print("ASM2d-GHG import OK")

What gets installed
-------------------

The main wheel installs four compiled modules:

- ``asm2d_n2o``
- ``clarifiers``
- ``combiner``
- ``delay``

The aliases ``asm2d_ghg`` and ``asm2d_g`` point to the same compiled model
engine as ``asm2d_n2o``.

Package boundary
----------------

The PyPI wheel includes the compiled model kernels only. User-specific
simulation scripts, datasets, notebooks, calibration files, and private engines
are not included.