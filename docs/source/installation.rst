Installation
============

Purpose
-------

This page explains how to install the published package and how to understand the
boundary between the PyPI wheel and the surrounding user project.

Install from PyPI
-----------------

The public package is installed with:

.. code-block:: bash

   pip install asm2dn2o

Then verify the import:

.. code-block:: python

   from asm2dn2o import asm2d_n2o, clarifiers, combiner, delay

   print("asm2dn2o import OK")

What gets installed
-------------------

The wheel installs four compiled modules under the ``asm2dn2o`` namespace:

- ``asm2d_n2o``
- ``clarifiers``
- ``combiner``
- ``delay``

