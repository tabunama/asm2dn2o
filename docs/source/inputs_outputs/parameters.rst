Parameters and Switches
=======================

Purpose
-------

This page summarises the major parameter groups that surround the compiled kernels.

Main parameter families
-----------------------

The current reference BAS organisation groups parameters into:

- kinetic and stoichiometric reactor vectors,
- clarifier parameter vectors,
- solids-characterisation vectors,
- reactor-level scalar settings and model toggles,
- HFO / interface parameter blocks.

Reactor parameter vectors
-------------------------

The reactor parameter vectors are usually split into:

- ``PAR_AR``
- ``PAR_AX``

These are one-dimensional arrays passed to the corresponding ``BasReactor`` objects.
The reference project derives them from combined matrices such as ``PAR_COMB_SS``,
``PAR_COMB_DY`` and ``PAR_COMB_120d``.

The full vectors are long and order-sensitive. Users should not reorder entries.

Clarifier parameters
--------------------

The reference clarifier configuration separates:

- operating parameter vectors:
  - ``PAR_PRIM``
  - ``PAR_SEC``
- solids vectors:
  - ``PAR_Solids_PRIM``
  - ``PAR_Solids_SEC``

The compiled clarifier cores use a short operating vector together with a solids
fractionation vector.

Reactor-level settings
----------------------

Common scalar and switch-like settings include:

- ``VOL_AX``
- ``VOL_AR``
- ``SOSAT1``
- ``DECAY``
- ``TEMPMODEL``
- ``S_MODEL``
- ``Fe_MODEL``
- ``SOB_MODEL``

These are passed during reactor construction, not rebuilt at every time step.

HFO parameter block
-------------------

The reference project also uses a 12-element HFO parameter block often named
``HFO_PAR1``. This block is passed during ``BasReactor`` construction.

Recommended documentation rule
------------------------------

For public examples and user projects, keep these blocks separate:

- initial conditions,
- reactor parameter vectors,
- clarifier parameters,
- global switches and interface values.

That separation makes debugging much easier and mirrors the reference BAS workflow.
