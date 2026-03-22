Full-Dataset Replay
===================

Purpose
-------

This example corresponds to the measured-data replay style used in the BAS
reference workflow.

Objective
---------

Run a full dynamic case on a measured time grid while using:

- influent 56-state time series,
- pH time series,
- measured recycle flows,
- explicit clarifier overflow / underflow splitting,
- delay closure for recycle loops.

Typical structure
-----------------

.. code-block:: text

   Influent
     -> primary clarifier
     -> combine with recycle streams
     -> delay
     -> AX reactor
     -> AR reactor
     -> secondary clarifier
     -> overflow split: effluent + RAS_NO3
     -> underflow split: RAS_sludge + WAS

What this example should document
---------------------------------

- accepted NPZ layouts,
- how measured flows are aligned to the model time grid,
- how ``KLa`` is prescribed or derived,
- how the split logic reconciles measured demands with model-available base flows,
- how outputs are saved and plotted.

Recommended splitter modes
--------------------------

A practical public driver should explain the difference between:

- ``force_meas``
- ``match_base``
- ``cap_meas``

For a public example, ``cap_meas`` is usually the safest default because it avoids
increasing measured flows beyond the model-available base flow.

Recommended diagnostics
-----------------------

A full replay example should save or plot:

- ``DO``, ``NH4``, ``NO3``, ``N2O``,
- total overflow and underflow from the secondary clarifier,
- effluent, RAS sludge, RAS NO3, and WAS flow histories,
- any selected state-index traces needed for debugging.
