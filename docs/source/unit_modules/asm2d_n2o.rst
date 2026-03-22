asm2d_n2o
=========

Purpose
-------

``asm2d_n2o`` provides the main ASM2d-N2O biochemical reactor wrapper.

Primary object
--------------

The public workflow uses the reactor through ``BasReactor(...)`` and its ``step(...)``
method.

Expected constructor inputs
---------------------------

The reference driver constructs one reactor per basin using:

- a 56-state initial condition,
- a one-dimensional reactor parameter vector,
- scalar arrays for volume and model toggles,
- the HFO parameter block.

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

Runtime interface
-----------------

At runtime, the reactor is advanced with a 62-entry input vector ``u62``:

- first 56 entries: inlet liquid stream,
- entry 56: ``KLa``,
- entry 61: ``pH``.

The output is a 101-element vector whose first 56 entries are usually taken as
the liquid-state outlet.

Example
-------

.. code-block:: python

   u62 = build_u62(inlet56, kla=current_kla, ph=current_ph)
   _, y101 = reactor.step(float(t), u62, float(dt))
   outlet56 = np.asarray(y101, dtype=float).ravel()[:56]

Practical notes
---------------

- Use fixed-order NumPy arrays rather than named dictionaries.
- Flatten all arrays before passing them to the compiled core.
- Instantiate separate reactors for AX and AR if the two basins use different
  parameters or operating logic.

Common failure modes
--------------------

- wrong array length,
- non-finite values inside the stream,
- inconsistent index mapping for ``Q`` or ``Temp``,
- forgetting to supply pH in ``u[61]``.
