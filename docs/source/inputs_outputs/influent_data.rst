Influent and Measured Data
==========================

Purpose
-------

This page documents the expected input time-series formats used by the package
and by the reference BAS-style drivers.

Typical files
-------------

Common files used around the package are:

- ``infl56_<tag>.npz``
- ``time_<tag>.npz``
- ``pH_<tag>.npz``
- ``mes_ras_sludge_<tag>.npz`` or ``mes_ras_<tag>.npz``
- ``mes_ras_no3_<tag>.npz``
- ``mes_was_<tag>.npz``
- optional blower / aeration signal files such as ``C_<tag>.npz``

Accepted shapes
---------------

.. list-table::
   :header-rows: 1

   * - File type
     - Typical shape
     - Meaning
   * - Influent
     - ``(n,57)``
     - time + 56 states
   * - Influent
     - ``(n,56)``
     - already aligned 56-state series
   * - Time
     - ``(n,)``
     - explicit time vector
   * - pH
     - ``(n,)`` or ``(n,2)``
     - aligned series or time + value
   * - Measured scalar flow
     - ``(n,)`` or ``(n,2)``
     - aligned series or time + value
   * - Blower signals
     - ``(n,4)``
     - time + C11 + C13 + C15

Units
-----

The reference BAS workflow uses:

- time in **days**,
- flow ``Q`` in **m3/d** inside the 56-state vectors.

Measured recycle flows may arrive as scalar series in **m3/h** and then be
converted to **m3/d** before being imposed in the split logic.

Minimum preparation checklist
-----------------------------

Before running a new case, make sure that you have:

- a consistent time vector,
- one influent 56-state series,
- a pH series or a clear constant-pH assumption,
- any measured recycle flows required by your flowsheet,
- a documented rule for KLa (constant, signal-derived, or controller-generated).

Interpolation
-------------

The surrounding user driver, not the compiled wheel, is responsible for any
interpolation. Common choices are:

- linear interpolation,
- zero-order hold,
- pre-aligned arrays with no interpolation.

Notes
-----

Keep all input files on one consistent time grid whenever possible. That reduces
ambiguity and makes debugging much easier.
