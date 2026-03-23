asm2d_n2o
=========

Purpose
-------

``asm2d_n2o`` is the main biochemical reactor kernel. It is the most complex unit
in the package and is intended to represent one activated-sludge process reactor,
for example an AX or AR tank in a BAS-style flowsheet.

Public usage pattern
--------------------

The public workflow uses the reactor through a wrapper class such as
``asm2d_n2o.BasReactor``. In the reference Python drivers, one object is usually
constructed for AX and one for AR.

Typical constructor pattern
---------------------------

.. code-block:: python

   reactor = asm2d_n2o.BasReactor(
       XINIT_AR,
       PAR_AR,
       np.array([VOL_AR]),
       np.array([SOSAT1]),
       np.array([DECAY]),
       np.array([TEMPMODEL]),
       HFO_PAR1,
       np.array([S_MODEL]),
       np.array([Fe_MODEL]),
       np.array([SOB_MODEL]),
   )

The compiled C core itself is organized around three main functions:

- ``bas_reactor_init(...)``
- ``bas_reactor_rhs(...)``
- ``bas_reactor_outputs(...)``

What the initialization function does
-------------------------------------

The initialization function copies the 56 liquid ASM2d states from ``XINIT`` into
the beginning of the reactor state vector, then sets additional gas and process
states to zero, and finally initializes the remaining scaling or miscellaneous
states to one.

This means the full internal state vector is larger than the 56 liquid process
states seen in the public stream interface.

Internal state layout
---------------------

A practical way to understand the internal state structure is:

- ``x[0:56]``: main liquid ASM2d states,
- ``x[56:76]``: additional gas or process states,
- ``x[76:89]``: scaling, diagnostics, or auxiliary states.

The public package user normally does **not** build this full internal state vector
manually. The user supplies only the 56-state ``XINIT`` vector, and the compiled
core expands it internally.

Runtime input interface
-----------------------

The runtime input to the reactor is a 62-entry vector ``u62``. In the reference
workflow:

- ``u[:56]`` is the inlet liquid stream,
- ``u[56]`` is ``KLa``,
- ``u[61]`` is ``pH``.

The remaining entries are available for auxiliary or legacy interface values.

Minimal runtime pattern
-----------------------

.. code-block:: python

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

What the RHS function includes
------------------------------

The ODE right-hand side is much richer than a basic ASM2d reactor. The compiled
implementation includes:

- heterotrophic hydrolysis and growth,
- PAO-related storage and growth processes,
- AOB and NOB kinetics,
- heterotrophic and AOB-related N2O pathways,
- sulfur-related processes,
- iron and HFO-related chemistry,
- gas-liquid transfer terms for N2, N2O, NO, CO2, H2S, and O2,
- off-gas tank states and off-gas emission terms,
- optional temperature compensation,
- optional decay switching based on available electron acceptor.

Temperature handling
--------------------

The core supports two temperature modes:

- pass-through temperature using the inlet temperature,
- reactor temperature balance using the internal reactor state.

The selected behavior depends on ``TEMPMODEL``.

Gas and off-gas behavior
------------------------

This reactor is not only a liquid-phase biochemical kernel. The implementation also
tracks gas-related quantities internally. The C code computes:

- Henry-law-adjusted gas transfer coefficients,
- direct stripping terms from the liquid,
- off-gas storage states,
- off-gas venting terms to air.

This is one reason why the internal state vector is larger than 56 and why the
output vector is larger than the liquid-state outlet alone.

Output interface
----------------

The reactor output is a 101-entry vector ``y101``.

In most flowsheet code, only the first 56 entries are used as the liquid outlet
stream. However, the remaining outputs contain valuable diagnostics and gas-related
quantities.

A practical interpretation is:

- ``y[0:56]``: liquid-state outlet,
- ``y[36]``: reconstructed ``X_TSS``,
- ``y[37]``: outlet flow,
- ``y[38]``: temperature,
- ``y[62]`` and beyond: airflow, transfer coefficients, gas emissions, and
  selected process-rate diagnostics.

X_TSS handling
--------------

The compiled output function reconstructs ``X_TSS`` from a VSS + ISS calculation
rather than simply copying the raw state. It uses COD/VSS and ISS-related
parameters from the long reactor parameter vector to compute the reported TSS-like
output.

What must be configured before using this unit
----------------------------------------------

Before building the reactor object, the user should already have:

- a 56-state initial vector,
- a basin-specific parameter vector,
- scalar reactor constants such as volume and oxygen saturation,
- model switches such as ``DECAY``, ``TEMPMODEL``, ``S_MODEL``, ``Fe_MODEL``, and
  ``SOB_MODEL``,
- the HFO parameter block,
- a strategy for KLa and pH over time.

Typical use cases
-----------------

This module is the correct starting point for:

- a single aeration-tank benchmark,
- an AX -> AR process line,
- replay of measured influent and blower signals,
- scenario studies on DO, NH4, NO3, or N2O dynamics.

Important caveats
-----------------

- The interface is array-based and order-sensitive.
- The compiled kernel expects consistent units and state ordering.
- KLa and pH are not generated internally; they must be supplied by the user
  driver.
- The first 56 outputs are not the full story; additional output channels may be
  essential for gas and N2O analysis.
