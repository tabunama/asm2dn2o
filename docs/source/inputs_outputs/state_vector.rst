State Vector
============

Purpose
-------

The package is array-driven. Every stream exchanged between the public unit modules is
a fixed-order 56-state vector. Correct ordering is mandatory. The reactor wrapper then
extends that stream to a 62-entry runtime input and returns a 101-entry output, where
the first 56 entries are the outlet liquid state.

Core conventions
----------------

- 56-state stream = standard liquid stream exchanged between units.
- 62-entry reactor input ``u`` = stream + runtime control / auxiliary entries.
- 101-entry reactor output ``y`` = liquid outlet + extra calculated outputs.

Key indices
-----------

.. list-table::
   :header-rows: 1

   * - Simulink index
     - Python index
     - Meaning
   * - 1
     - 0
     - S_O2
   * - 5
     - 4
     - S_NH4
   * - 7
     - 6
     - S_N2O
   * - 10
     - 9
     - S_NO3
   * - 37
     - 36
     - X_TSS
   * - 38
     - 37
     - Q_m3d
   * - 39
     - 38
     - Temp

Full state catalogue
--------------------

.. list-table::
   :header-rows: 1

   * - Python index
     - State
     - Description
   * - 1
     - S_O2
     - dissolved oxygen
   * - 2
     - S_F
     - fermentable readily biodegradable substrate
   * - 3
     - S_A
     - acetate / VFA-like soluble carbon
   * - 4
     - S_I
     - soluble inert COD
   * - 5
     - S_NH4
     - ammonium + ammonia nitrogen
   * - 6
     - S_NH2OH
     - hydroxylamine intermediate
   * - 7
     - S_N2O
     - dissolved nitrous oxide
   * - 8
     - S_NO
     - nitric oxide
   * - 9
     - S_NO2
     - nitrite nitrogen
   * - 10
     - S_NO3
     - nitrate nitrogen
   * - 11
     - S_N2
     - dissolved nitrogen gas
   * - 12
     - S_PO4
     - orthophosphate phosphorus
   * - 13
     - S_IC
     - inorganic carbon
   * - 14
     - X_I
     - particulate inert COD
   * - 15
     - X_S
     - slowly biodegradable particulate substrate
   * - 16
     - X_H
     - ordinary heterotrophic organisms
   * - 17
     - X_PAO
     - phosphate accumulating organisms
   * - 18
     - X_PP
     - polyphosphate storage
   * - 19
     - X_PHA
     - PHA storage polymers
   * - 20
     - X_AOB
     - ammonia oxidizing biomass
   * - 21
     - X_NOB
     - nitrite oxidizing biomass
   * - 22
     - S_K
     - potassium
   * - 23
     - S_Mg
     - magnesium
   * - 24
     - S_SO4
     - sulfate sulfur
   * - 25
     - S_Fe2
     - ferrous iron
   * - 26
     - S_Fe3
     - ferric iron
   * - 27
     - S_IS
     - soluble sulfide / inorganic sulfur pool
   * - 28
     - X_S0
     - elemental sulfur solids
   * - 29
     - X_SRB
     - sulfate reducing biomass
   * - 30
     - X_HFO_L
     - low-reactivity hydrous ferric oxide
   * - 31
     - X_HFO_H
     - high-reactivity hydrous ferric oxide
   * - 32
     - X_HFO_LP
     - low-reactivity HFO with bound phosphate
   * - 33
     - X_HFO_HP
     - high-reactivity HFO with bound phosphate
   * - 34
     - X_HFO_HP_old
     - aged high-reactivity HFO-P fraction
   * - 35
     - X_HFO_LP_old
     - aged low-reactivity HFO-P fraction
   * - 36
     - X_HFO_old
     - aged HFO pool
   * - 37
     - X_TSS
     - total suspended solids proxy/state
   * - 38
     - Q_m3d
     - volumetric flow
   * - 39
     - Temp
     - liquid temperature
   * - 40
     - S_Na
     - sodium
   * - 41
     - S_Cl
     - chloride
   * - 42
     - S_Ca
     - calcium
   * - 43
     - AlOH3
     - aluminium hydroxide solids
   * - 44
     - X_ISS0
     - inorganic suspended solids pool
   * - 45
     - X_CaCO3
     - calcium carbonate solids
   * - 46
     - X_CaP
     - calcium phosphate solids
   * - 47
     - X_struv
     - struvite solids
   * - 48
     - X_Dummy1
     - reserved / unused placeholder
   * - 49
     - S_CH4
     - dissolved methane
   * - 50
     - X_Dummy2
     - reserved / unused placeholder
   * - 51
     - X_Dummy3
     - reserved / unused placeholder
   * - 52
     - X_Dummy4
     - reserved / unused placeholder
   * - 53
     - XSOB
     - sulfur oxidizing biomass
   * - 54
     - XAlPO4
     - aluminium phosphate solids
   * - 55
     - XCaO
     - calcium oxide / lime-related solids placeholder
   * - 56
     - XMgCO3
     - magnesium carbonate solids placeholder

Notes
-----

- ``Q_m3d`` and ``Temp`` are carried inside the same vector as biological and chemical
  states, so index mistakes can destabilize the whole flowsheet.
- Several late-vector states are placeholders or optional chemistry extensions. They
  still must remain in the correct position.
