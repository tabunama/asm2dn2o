combiner
========

Purpose
-------

``combiner`` provides a two-stream mixing block for 56-state vectors.

Public function
---------------

- ``mix_streams(a56, b56)``

Inputs and output
-----------------

Inputs:

- two 56-state streams

Output:

- one 56-state mixed stream

Typical use
-----------

The block is intentionally simple and is commonly chained to reproduce larger
Simulink combiner networks.

Example
-------

.. code-block:: python

   from asm2dn2o import combiner

   mixed = combiner.mix_streams(stream_a, stream_b)

Typical flowsheet usage
-----------------------

Examples include:

- mixing primary effluent with recycle streams,
- combining RAS sludge and RAS NO3 before sending them forward,
- assembling inlet streams before a delay or reactor block.

Notes
-----

The two-stream design is a strength rather than a limitation: it keeps the unit
explicit and easy to debug, and larger mixing nodes can be built in series.
