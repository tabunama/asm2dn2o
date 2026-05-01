asm2d_n2o
=========

Purpose
-------

``asm2d_n2o`` is the main biochemical reactor kernel for the ASM2d-N₂O /
ASM2d-GHG model.

It simulates biological carbon, nitrogen, and phosphorus transformations with
explicit N₂O pathway and gas-transfer calculations.

The same compiled reactor kernel can also be imported through the alias names:

.. code-block:: python

   from asm2dn2o import asm2d_n2o
   from asm2dn2o import asm2d_ghg
   from asm2dn2o import asm2d_g

   from asm2dghg import asm2d_ghg
   from asm2dg import asm2d_g