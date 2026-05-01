Unit Modules
============

Purpose
-------

This section documents the four public compiled modules exposed by the package.

The modules are intentionally low-level. They operate on fixed-order NumPy arrays
rather than on named species dictionaries or high-level plant objects. The expected
usage is:

.. code-block:: python

   from asm2dn2o import asm2d_n2o, clarifiers, combiner, delay
   from asm2dghg import asm2d_ghg
   from asm2dg import asm2d_g

.. toctree::
   :maxdepth: 1

   asm2d_n2o
   clarifiers
   combiner
   delay
