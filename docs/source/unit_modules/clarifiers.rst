clarifiers
==========

Purpose
-------

``clarifiers`` provides primary and secondary clarifier separation blocks.
Both clarifier cores take one 56-state inlet stream and split it into two 56-state
streams:

- overflow,
- underflow.

In the compiled C core, these are returned together as a 112-entry output vector:

- ``y[0:56]`` = overflow,
- ``y[56:112]`` = underflow.

Public functions
----------------

The practical public API is:

- ``primclar(u56, PAR, Solids_PAR)``
- ``secondclar(u56, PAR, Solids_PAR)``

Inputs
------

Both clarifier cores take:

- one 56-state inlet stream ``u``,
- a 4-entry clarifier parameter vector ``PAR``,
- a 9-entry solids vector ``Solids_PAR``.

Clarifier parameter vector
--------------------------

The 4 operating parameters are interpreted as:

- target sludge or flotation concentration term,
- TSS removal percentage,
- inorganic enrichment factor,
- inorganic phosphorus-solids enrichment factor.

Solids vector
-------------

The 9-entry solids vector contains COD-to-VSS and ISS-related factors used by the
clarifier calculations, including:

- ``CODtoVSS_XI``
- ``CODtoVSS_XS``
- ``CODtoVSS_Xbiom``
- ``CODtoVSS_XPHA``
- ``ISS_P``
- ``f_ISS_biom``
- ``CODtoVSS_Xch``
- ``CODtoVSS_Xpr``
- ``CODtoVSS_Xli``

Primary versus secondary clarifier logic
----------------------------------------

The current primary and secondary C implementations are structurally almost the
same. Both:

1. compute particulate COD in the influent,
2. derive a concentration factor,
3. derive underflow fraction and clarification factor,
4. build an overflow stream by preserving soluble states and scaling particulate
   states,
5. compute the underflow by mass balance.

Particulate COD basis
---------------------

Both cores compute the particulate-COD basis from a selected set of particulate
states:

- ``X_I``
- ``X_S``
- ``X_H``
- ``X_PAO`` or corresponding particulate biomass position
- ``X_AOB``
- ``X_NOB``
- ``X_S0`` converted to COD equivalent
- ``X_SOB``

This particulate COD basis is then used to compute the internal thickening or
clarification factor.

Overflow behavior
-----------------

In both clarifier cores:

- soluble states in the low-index soluble block pass through unchanged,
- particulate COD states are multiplied by a clarification factor,
- selected inorganic and phosphorus-solid states receive additional enrichment
  factors,
- flow is reduced to the overflow flow ``Q_over = Q_in * (1 - Qu_factor)``.

Underflow behavior
------------------

The underflow is computed by explicit mass balance:

.. code-block:: text

   C_under = (Q_in * C_in - Q_over * C_over) / Q_under

where:

.. code-block:: text

   Q_under = Q_in * Qu_factor

This makes the output physically interpretable and easy to audit when debugging.

Fallback behavior
-----------------

Both clarifier cores include a fallback condition for the case where the influent
is already too concentrated to be thickened further. In that case:

- the whole influent is passed to the overflow,
- the underflow is set to zero.

This is an important edge case for robust replay of measured plant data.

Primary clarifier notes
-----------------------

The primary clarifier core reads the 9-entry solids vector for completeness, but the
current active logic mainly uses the operating vector and the particulate-COD basis.
This should be documented clearly so users do not assume all solids entries are
actively shaping the result in the same way.

Secondary clarifier notes
-------------------------

The secondary clarifier core applies the same main structure but is intended for
post-biological settling and return-sludge separation. In practice, the Python
flowsheet often applies additional split logic after the secondary clarifier to
divide total overflow and underflow into:

- effluent,
- RAS NO3,
- RAS sludge,
- WAS.

Recommended wrapper behavior
----------------------------

Public examples should normalize the clarifier return shape immediately. Depending
on the wrapper or build, users may see either:

- one flat 112-vector, or
- two explicit 56-state arrays.

The safest pattern is to always convert the result to:

.. code-block:: python

   y = np.asarray(y, dtype=float).ravel()
   overflow56 = y[:56]
   underflow56 = y[56:]

Typical use cases
-----------------

- front-end primary solids removal,
- post-reactor secondary settling,
- sludge recycle and waste-sludge base splitting,
- plant-wide replay with measured overflow or underflow demands.

Important caveats
-----------------

- The clarifier is not a full settler PDE model; it is a compact separation block.
- Additional project-level split logic may still be needed after the compiled
  clarifier.
- The solids vector must stay in the expected order even if not every entry is
  equally active in the current ported code.
