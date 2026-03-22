clarifiers
==========

Purpose
-------

``clarifiers`` provides primary and secondary clarifier wrappers for splitting a
56-state inlet stream into overflow and underflow streams.

Public functions
----------------

- ``primclar(u56, PAR, Solids_PAR)``
- ``secondclar(u56, PAR, Solids_PAR)``

Inputs
------

Each clarifier call expects:

- one 56-state inlet stream,
- a short operating parameter vector,
- a solids-characterisation vector.

Typical output
--------------

Depending on the wrapper/build convention, a clarifier may return:

- a tuple of two 56-state arrays, or
- one flat 112-element vector equal to ``overflow || underflow``.

Recommended normalization
-------------------------

User drivers should normalize the return shape immediately so that the rest of
the code always sees two explicit 56-state arrays.

Example
-------

.. code-block:: python

   y = clarifiers.secondclar(u56, PAR_SEC, PAR_Solids_SEC)
   y = np.asarray(y, dtype=float).ravel()
   over = y[:56]
   under = y[56:]

Typical role in the flowsheet
-----------------------------

- primary clarifier: front-end solids separation,
- secondary clarifier: post-reactor separation and hydraulic split basis.

Notes
-----

The measured-flow splitters in the BAS reference workflow are implemented outside
the compiled clarifier kernel. The clarifier provides total overflow and underflow;
the Python driver then allocates those total flows to effluent, nitrate recycle,
RAS sludge, and WAS.
