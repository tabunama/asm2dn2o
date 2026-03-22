Initial Conditions
==================

Purpose
-------

This page explains how to prepare the initial state vectors required by the
compiled unit models.

Required initial vectors
------------------------

The reference BAS configuration uses three 56-state vectors:

- ``XINIT_AR``: initial state of the aerobic / downstream reactor,
- ``XINIT_AX``: initial state of the anoxic / upstream reactor,
- ``XINIT_DELAY``: initial state for the hydraulic delay block.

Supported modes
---------------

The reference helper exposes three named modes:

- ``ss``
- ``dy``
- ``120d``

The helper function returns the three vectors as:

.. code-block:: python

   XINIT_AR, XINIT_AX, XINIT_DELAY = build_XINIT_sets(mode)

Combined matrix convention
--------------------------

The reference implementation stores each mode as a combined 56x3 matrix with columns:

- AR
- AX
- DELAY

The helper then slices those columns into three one-dimensional arrays.

Recommended practice
--------------------

When preparing a new case:

- keep all 56 states in the correct order,
- ensure ``Q_m3d`` and ``Temp`` are physically meaningful,
- ensure key biomass and nitrogen states are consistent with the intended operating point,
- decide whether ``X_TSS`` is used directly or treated mainly as a plotting/debugging proxy.

Example
-------

.. code-block:: python

   from bas_init_sets import build_XINIT_sets

   XINIT_AR, XINIT_AX, XINIT_DELAY = build_XINIT_sets("120d")

Notes
-----

Direct 56-element arrays are also acceptable if you do not want to keep the
combined matrix form. The important requirement is the exact state ordering.
