XINIT sets
================

Purpose
-------

``bas_init_sets.py`` stores the mode-specific initialization matrices used to build
``XINIT_AR``, ``XINIT_AX``, and ``XINIT_DELAY``. The helper currently supports
``ss``, ``dy``, and ``120d`` modes.

How the helper works
--------------------

Each mode is stored as a 56 x 3 matrix with columns (as an example layout):

- AR for aeraobic tank
- AX for anoxic tank
- DELAY for delay block

The builder then returns:

.. code-block:: python

   XINIT_AR, XINIT_AX, XINIT_DELAY = build_XINIT_sets(mode)

