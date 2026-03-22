Running asm2dn2o
================

Purpose
-------

This page explains how to assemble and run simulations with the package.

General execution pattern
-------------------------

The recommended workflow is:

1. load a prepared 56-state influent time series,
2. load or define initial conditions and parameter vectors,
3. instantiate the required unit blocks,
4. run a Python time loop,
5. save and plot the resulting arrays.

The package does not impose a monolithic solver application. Instead, it exposes
compiled kernels that are stepped by the user driver.

Core import
-----------

.. code-block:: python

   import numpy as np
   from asm2dn2o import asm2d_n2o, clarifiers, combiner, delay

Typical build order
-------------------

A minimal dynamic case usually follows this order:

.. code-block:: python

   # 1) load configuration and time-series arrays
   # 2) instantiate unit blocks
   # 3) allocate outputs
   # 4) run explicit time loop
   # 5) save and plot results

In more detail:

- prepare ``XINIT_AR``, ``XINIT_AX`` and optional ``XINIT_DELAY``,
- prepare ``PAR_AR`` and ``PAR_AX``,
- prepare scalar reactor settings such as volume, toggles, and HFO parameters,
- build the ``u62`` reactor input vector at each time step,
- optionally add clarifiers, mixing, recycle logic, and delay blocks.

Typical runtime sequence
------------------------

A compact process line looks like:

.. code-block:: text

   Influent
     -> primary clarifier (optional)
     -> combiner(s) for recycle closure
     -> hydraulic delay (optional)
     -> AX reactor
     -> AR reactor
     -> secondary clarifier
     -> overflow / underflow split
     -> recycle / WAS / effluent handling

Time stepping
-------------

The published package is commonly used with an explicit fixed-step loop that follows
the incoming plant data grid. In many measured-data replay workflows, the external
time step is one minute expressed in days:

.. code-block:: python

   dt = 1.0 / 1440.0

For more demanding workflows, users may add:

- reactor internal substeps,
- outer flowsheet substeps,
- delay substeps,
- control updates between steps.

Minimal pattern
---------------

.. code-block:: python

   for k, t in enumerate(times[:-1]):
       u62 = build_u62(inlet56, kla=current_kla, ph=current_ph)
       _, y101 = reactor.step(float(t), u62, float(dt))
       outlet56 = np.asarray(y101, dtype=float).ravel()[:56]

Output handling
---------------

The most practical pattern is to preallocate arrays and store signals by time step:

.. code-block:: python

   y_hist = np.zeros((n_steps, 56), dtype=float)

   for k, t in enumerate(times[:-1]):
       ...
       y_hist[k, :] = outlet56

Notes
-----

- Keep all key indices in one place.
- Keep time in days internally if you follow the BAS reference workflow.
- Save diagnostic arrays during the loop and plot afterward, not during construction.
