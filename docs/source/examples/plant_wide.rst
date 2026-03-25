Plant wide WWTP
===================

Purpose
-------

Presents a Plant Wide WWTP workflow.

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

 
Recommended plots - diagnostics
-------------------------------

A full replay example should save or plot:

- ``DO``, ``NH4``, ``NO3``, ``N2O``,
- total overflow and underflow from the secondary clarifier,
- effluent, RAS sludge, RAS NO3, and WAS flow histories,
- any selected state-index traces needed for debugging.
