Installation
============

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
   from asm2dghg import asm2d_ghg, clarifiers, combiner, delay
   from asm2dg import asm2d_g, clarifiers, combiner, delay

   print("ASM2d-GHG import OK")

