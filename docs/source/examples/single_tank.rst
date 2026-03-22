Single Aeration Tank
====================

Purpose
-------

This is the recommended first scientific example after the import smoke test.

Objective
---------

Build one ASM2d-N2O reactor with:

- one 56-state inlet stream,
- a constant ``KLa``,
- a pH value or pH time series,
- one explicit time loop.

Minimal pattern
---------------

.. code-block:: python

   import numpy as np
   from asm2dn2o import asm2d_n2o

   BAS_NSTATE = 56
   BAS_NINPUT = 62
   U_IDX_KLA = 56
   U_IDX_PH = 61

   def build_u62(stream56, kla, ph):
       u = np.zeros(BAS_NINPUT, dtype=float)
       u[:BAS_NSTATE] = stream56
       u[U_IDX_KLA] = kla
       u[U_IDX_PH] = ph
       return u

   reactor = asm2d_n2o.BasReactor(
       XINIT_AR, PAR_AR, np.array([VOL_AR]), np.array([SOSAT1]),
       np.array([DECAY]), np.array([TEMPMODEL]), HFO_PAR1,
       np.array([S_MODEL]), np.array([Fe_MODEL]), np.array([SOB_MODEL]),
   )

   for k, t in enumerate(times[:-1]):
       u62 = build_u62(infl56[k], kla=120.0, ph=7.0)
       _, y101 = reactor.step(float(t), u62, float(dt))
       out56 = np.asarray(y101, dtype=float).ravel()[:56]

What this example teaches
-------------------------

- how to instantiate the reactor,
- how to build ``u62``,
- how to interpret the first 56 entries of ``y101``,
- how to store results for plotting.

Recommended outputs
-------------------

Plot at least:

- ``S_O2``
- ``S_NH4``
- ``S_NO3``
- ``S_N2O``

That confirms both the index mapping and the basic runtime pattern.
