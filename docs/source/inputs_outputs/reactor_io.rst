Reactor Inputs and Outputs
==========================

Purpose
-------

This page documents the reactor runtime interface used by
``asm2dn2o.asm2d_n2o.BasReactor``.

Core dimensions
---------------

The reactor interface is:

- 56-state liquid stream,
- 62-entry runtime input vector ``u``,
- 101-entry output vector ``y``.

Meaning of ``u62``
------------------

The practical runtime convention is:

- ``u[:56]`` = liquid inlet stream,
- ``u[56]`` = ``KLa``,
- ``u[61]`` = ``pH``.

The remaining entries follow the compiled reactor interface and are normally
handled by the surrounding driver.

Meaning of ``y101``
-------------------

The first 56 entries of the returned 101-element vector are the liquid outlet
state used by the flowsheet. The remaining entries are additional calculated
outputs retained by the compiled kernel.

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

   u62 = build_u62(inlet56, kla=current_kla, ph=current_ph)
   _, y101 = reactor.step(float(t), u62, float(dt))
   outlet56 = np.asarray(y101, dtype=float).ravel()[:56]

Common pitfalls
---------------

- passing arrays with the wrong length,
- forgetting to flatten vectors before the compiled call,
- mixing 1-based and 0-based indexing,
- forgetting that time is usually in days in the BAS reference workflow,
- confusing ``X_TSS`` with a derived plant diagnostic that may not be identical to the raw state.

Diagnostics
-----------

The safest pattern is to validate stream length, finiteness, flow, and temperature
at each inter-unit connection in the Python driver before continuing to the next unit.
