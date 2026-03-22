bas_par_sets.py
===============

Purpose
-------

``bas_par_sets.py`` stores the kinetic and stoichiometric parameter vectors used
by the reactor kernels.

Main role
---------

The reference pattern defines combined matrices for several operating modes, then
builds basin-specific vectors:

- ``PAR_AR``
- ``PAR_AX``

Typical source matrices include:

- ``PAR_COMB_SS``
- ``PAR_COMB_DY``
- ``PAR_COMB_120d``

Why this structure is useful
----------------------------

A combined matrix with columns ``[AR, AX]`` makes it much easier to:

- compare values against MATLAB / Simulink,
- keep AR and AX parameters aligned,
- tune only selected parameters without losing the overall order.

Recommended rule
----------------

Treat the full vector order as canonical. Even if you tune only a subset of entries,
keep the entire vector assembled in the expected order.

Parameter families
------------------

The combined vectors typically include:

- stoichiometric yields and inert fractions,
- elemental C/N/P content,
- TSS/COD ratios,
- heterotrophic kinetics,
- OHO half-saturation and inhibition terms,
- PAO kinetics,
- AOB / NOB / N2O kinetics,
- solids and gas-transfer constants,
- inhibition shape factors.

Minimal user guidance
---------------------

If you prepare new parameter sets:

1. keep the exact ordering,
2. keep AR and AX as separate final vectors,
3. document which values you changed and why,
4. keep a mapping to the original MATLAB / Simulink index numbering.

Notes
-----

This is one of the most sensitive input files in the whole workflow. If the
ordering is wrong, results may look plausible while still being physically wrong.
