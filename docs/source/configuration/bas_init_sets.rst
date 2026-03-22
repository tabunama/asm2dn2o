bas_init_sets.py
================

Purpose
-------

``bas_init_sets.py`` stores mode-specific initial conditions for the BAS reference
workflow.

Main role
---------

The helper exposes combined initialization matrices and returns three one-dimensional
vectors:

- ``XINIT_AR``
- ``XINIT_AX``
- ``XINIT_DELAY``

Supported modes
---------------

The current helper supports:

- ``ss``
- ``dy``
- ``120d``

Return convention
-----------------

The public helper pattern is:

.. code-block:: python

   XINIT_AR, XINIT_AX, XINIT_DELAY = build_XINIT_sets(mode)

Internal structure
------------------

Each combined matrix stores columns in the order:

- AR
- AX
- DELAY

That matrix organisation is useful because it keeps all state values visible while
still allowing the driver to extract the exact 56-element vectors required by the
compiled kernels.

Recommended user practice
-------------------------

When adapting the file for a new plant:

- preserve the 56-state order,
- preserve the column meaning,
- keep units consistent with the rest of the project,
- check that biomass and nitrogen states reflect the intended operating mode.

Notes
-----

It is perfectly acceptable to replace the combined-matrix style with direct
``XINIT_AR`` / ``XINIT_AX`` / ``XINIT_DELAY`` arrays, as long as the final
vectors are still 56-element arrays in the correct order.
