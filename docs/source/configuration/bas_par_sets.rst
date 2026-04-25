PAR sets
===============

Purpose
-------

``bas_par_sets.py`` stores the kinetic and stoichiometric parameter vectors for
the reactor kernels. The current helper returns separate AR and AX vectors from
combined matrices for aerobic and anoxic tank, respectively.

How the helper is used
----------------------

The combined matrices are ordered column-wise as ``[AR, AX]``. This structure is
helpful because it keeps both basins aligned against the same parameter index map.


Practical advice
----------------

- Keep this file under strict version control.
- Never reorder entries at ALL.
- When calibrating, track changes by parameter index and name.
