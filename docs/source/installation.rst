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

These modules are the modelling kernels. They are intended to be imported into a
separate user project where you define:

- initial conditions,
- parameter vectors,
- clarifier settings,
- input time series,
- flowsheet logic,
- plotting and calibration routines.

Recommended project layout
--------------------------

A practical user project usually has this structure:

.. code-block:: text

   user_project/
   ├─ data/
   │  ├─ infl56_case.npz
   │  ├─ time_case.npz
   │  ├─ pH_case.npz
   │  └─ measured_flows.npz
   ├─ parameters/
   │  ├─ bas_init_sets.py
   │  ├─ bas_par_sets.py
   │  ├─ bas_clarifiers.py
   │  └─ bas_interface.py
   ├─ run_case.py
   └─ plots/

Smoke test
----------

A compact smoke test is:

.. code-block:: python

   from asm2dn2o import asm2d_n2o, clarifiers, combiner, delay

   print("Modules available:")
   print(asm2d_n2o, clarifiers, combiner, delay)

Notes
-----

- The package is array-driven. Inputs and outputs are fixed-order NumPy arrays.
- The package does not convert raw plant exports into the required vector format automatically.
- The wheel is best treated as the stable computational layer inside a larger Python project.
