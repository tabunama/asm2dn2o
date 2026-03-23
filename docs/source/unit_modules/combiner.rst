combiner
========

Purpose
-------

``combiner`` provides a two-stream mixer for 56-state process streams.

This unit is deliberately simple. It does exactly one task: combine two 56-state
streams into one mixed 56-state stream using flow-weighted mixing.

Public function
---------------

The practical public wrapper is typically exposed as something like:

- ``mix_streams(a56, b56)``

Inputs
------

The compiled C core takes:

- ``u1[56]``
- ``u2[56]``

and returns:

- ``y[56]``

Flow handling
-------------

The combiner uses the flow stored at index 37 in each stream:

- ``Q1 = u1[37]``
- ``Q2 = u2[37]``

If at least one of the two flows is positive, the module computes a flow-weighted
mixture for all 56 states:

.. code-block:: text

   y[i] = (u1[i] * Q1 + u2[i] * Q2) / (Q1 + Q2)

Then it explicitly sets:

.. code-block:: text

   y[37] = Q1 + Q2

This means the output flow is the algebraic sum of the two incoming flows.

Temperature handling
--------------------

Temperature is carried in the same 56-state vector and therefore is already mixed by
the same flow-weighted rule. The C code does not apply a separate temperature
equation in the combiner.

Zero-flow fallback
------------------

If both input flows are non-positive, the combiner returns an all-zero output
stream. This is useful for robust flowsheet execution because it avoids division by
zero and provides a clear no-flow state.

Why the design is intentionally limited
---------------------------------------

The two-stream-only design is often the right engineering choice for a low-level
unit block:

- it is easy to understand,
- it is easy to test,
- it preserves explicit flow closure,
- higher-order mixing can be built by chaining several combiners.

Typical use cases
-----------------

Examples include:

- combining primary effluent with a recycle stream,
- combining RAS sludge and RAS NO3,
- combining two upstream branches before a delay or a reactor,
- building larger mixing nodes in series.

Example
-------

.. code-block:: python

   from asm2dn2o import combiner

   mixed56 = combiner.mix_streams(stream_a56, stream_b56)

Debugging advice
----------------

When validating a combiner call, always check:

- input lengths are both 56,
- both streams use the same state order,
- flows at index 37 are physically meaningful,
- the output flow equals the sum of input flows.
