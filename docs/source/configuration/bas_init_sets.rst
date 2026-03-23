bas_init_sets.py
================

Purpose
-------

``bas_init_sets.py`` stores the mode-specific initialization matrices used to build
``XINIT_AR``, ``XINIT_AX``, and ``XINIT_DELAY``. The helper currently supports
``ss``, ``dy``, and ``120d`` modes. fileciteturn17file2

How the helper works
--------------------

Each mode is stored as a 56 x 3 matrix with columns:

- AR
- AX
- DELAY

The builder then returns:

.. code-block:: python

   XINIT_AR, XINIT_AX, XINIT_DELAY = build_XINIT_sets(mode)

Why this file matters
---------------------

Initialization is not a minor detail. It defines the first physically consistent
reactor, recycle, and transport states seen by the time loop. Unrealistic early
transients are often caused by inconsistent initialization rather than by wrong
kinetic parameters.

What should be reviewed first for a new site
--------------------------------------------

When adapting the file, review these groups first:

- dissolved oxygen and nitrogen states,
- biomass inventories ``X_H``, ``X_PAO``, ``X_AOB``, ``X_NOB``,
- flow and temperature,
- precipitation / inorganic solids if the chemistry extensions are active.

Mode summary
------------

.. list-table::
   :header-rows: 1

   * - Mode
     - Typical use
     - Key observation
   * - ss
     - pseudo steady-state warm start
     - AR starts with higher oxygen and high heterotrophic / nitrifier biomass
   * - dy
     - dynamic case warm start
     - lower ``X_H`` and altered dissolved nitrogen pools relative to SS
   * - 120d
     - long measured-data replay
     - nitrifier states differ from SS and are tailored to the long replay case

For the full numeric values, see the ``Initial Conditions`` page.
