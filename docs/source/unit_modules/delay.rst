delay
=====

Purpose
-------

``delay`` provides a hydraulic delay block for 56-state streams.

Primary object
--------------

The delay kernel is commonly used through a wrapper such as:

- ``DelayBlock(XINIT_DELAY, T_DELAY)``
- then ``step(u56, dt)``

Inputs
------

A delay block needs:

- a 56-state initial condition,
- a travel time or delay constant,
- the incoming 56-state stream at each time step.

Typical output
--------------

- one delayed 56-state stream

Typical use
-----------

The delay block is useful for:

- hydraulic transport,
- recycle closure,
- explicit one-step causal execution of recycle loops.

Example
-------

.. code-block:: python

   dly = delay.DelayBlock(XINIT_DELAY, T_DELAY)
   y56 = dly.step(inlet56, dt)

Practical notes
---------------

In surrounding Python wrappers, it is often helpful to:

- convert concentration-like initial vectors to the mass-like internal state expected by the delay kernel,
- substep the delay internally when the external ``dt`` is large relative to ``T_DELAY``.

That kind of stabilization belongs in the user wrapper, not in the package documentation of the raw kernel alone.
