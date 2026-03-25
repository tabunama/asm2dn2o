Parameters and Switches
=======================

Purpose
-------

This page summarizes the parameter families that must be configured **before**
layout construction and input-data preparation. In the current workflow, these values
come from ``bas_interface.py``, ``bas_clarifiers.py``, ``bas_par_sets.py``, and
``config_bas.py``. fileciteturn17file0turn17file1

Recommended preparation order
-----------------------------

1. global model switches and reactor constants,
2. HFO / interface parameters,
3. clarifier operating parameters,
4. solids-characterization vectors,
5. reactor kinetic / stoichiometric parameter vectors,
6. initial-condition vectors,
7. time-series input files.

Global model switches
---------------------

The current Python configuration keeps the following switches and defaults:

.. list-table::
   :header-rows: 1

   * - Name
     - Current value
     - Meaning
     - Mode options
   * - SOB_MODEL
     - 1
     - include sulfur-oxidizing bacteria processes
     - 0=off, 1=on
   * - DECAY
     - 1
     - electron-acceptor-dependent decay
     - 0=fixed decay, 1=EA-dependent
   * - TEMPMODEL
     - 0
     - temperature balance handling
     - 0=pass-through temperature, 1=reactor temperature balance
   * - Bio_P
     - 1
     - biological phosphorus mode retained from MATLAB notes
     - 0=interface-transformed, 1=kinetic description
   * - S_MODEL
     - 1
     - sulfate-related processes
     - 0=off, 1=on
   * - Bio_S
     - 0
     - extended sulfate reduction guilds retained from MATLAB notes
     - 0=heterotrophic SRB only, 1=expanded guilds
   * - CEPT
     - 0
     - chemically enhanced primary treatment option
     - 0=default primary clarifier, 1=CEPT-adjusted
   * - Fe_MODEL
     - 0
     - iron-related ASM processes
     - 0=off, 1=on

Important note on scope
-----------------------

Only a subset of these switches is currently passed into ``BasReactorConfig``:
``DECAY``, ``TEMPMODEL``, ``S_MODEL``, ``Fe_MODEL``, and ``SOB_MODEL``. The other
switches are retained from the MATLAB-side configuration notes for completeness and
future coupling use. The dataclass-based grouping is explicit in ``config_bas.py``. fileciteturn17file0

Reactor-wide constants and hydraulics
-------------------------------------

.. list-table::
   :header-rows: 1

   * - Name
     - Current value
     - Meaning
     - Unit
   * - Qin0
     - 2160
     - nominal influent flow
     - m3/d
   * - Qintr
     - 0
     - internal recycle / interfacing placeholder
     - m3/d
   * - Qw
     - 408
     - waste flow
     - m3/d
   * - VOL_AX
     - 1700
     - anoxic reactor volume
     - m3
   * - VOL_AR
     - 2400
     - aerobic reactor volume
     - m3
   * - VOL_blanket
     - 600
     - clarifier blanket volume retained for context
     - m3
   * - SOSAT1
     - 8
     - oxygen saturation constant used in reactor setup
     - gO2/m3
   * - T_DELAY
     - 0.0001
     - hydraulic delay constant
     - d

HFO / interface block
---------------------

The current HFO block contains 12 values and is passed during reactor construction
as ``HFO_PAR1``. The current values are:

.. list-table::
   :header-rows: 1

   * - Name
     - Value
     - Meaning
   * - qaging_H
     - 450.0
     - high-reactivity HFO aging rate
   * - qaging_L
     - 0.1
     - low-reactivity HFO aging rate
   * - qPcoprecip
     - 360.0
     - phosphorus coprecipitation rate
   * - qPbinding
     - 0.3
     - phosphate binding rate
   * - qdiss_H
     - 36.0
     - dissolution rate for HFO_H
   * - qdiss_L
     - 36.0
     - dissolution rate for HFO_L
   * - Kp_diss
     - 0.03
     - phosphate dissociation constant
   * - KP
     - 1.2
     - generic phosphorus constant
   * - ASFH
     - 1.2
     - specific surface factor for HFO_H
   * - ASFL
     - 0.31
     - specific surface factor for HFO_L
   * - AMP
     - 31.0
     - atomic / molar phosphorus factor
   * - AMFe
     - 55.845
     - atomic mass of iron

Clarifier operating parameters
------------------------------

Primary and secondary clarifier settings are configured independently:

.. list-table::
   :header-rows: 1

   * - Name
     - Value
     - Meaning
     - Unit
   * - PAR_SEC[1]
     - 0.13
     - secondary clarifier target TSS in flotation
     - [gTSS/L]
   * - PAR_SEC[2]
     - 98.0
     - secondary clarifier TSS removal
     - [%]
   * - PAR_SEC[3]
     - 0.4
     - secondary clarifier inorganic enrichment factor
     - [-]
   * - PAR_SEC[4]
     - 0.8
     - secondary clarifier P-solids enrichment factor
     - [-]
   * - PAR_PRIM[1]
     - 1.0
     - primary clarifier target solids concentration
     - [gTSS/L equivalent]
   * - PAR_PRIM[2]
     - 50.0
     - primary clarifier TSS removal
     - [%]
   * - PAR_PRIM[3]
     - 0.5
     - primary clarifier inorganic enrichment factor
     - [-]
   * - PAR_PRIM[4]
     - 0.5
     - primary clarifier P-solids enrichment factor
     - [-]
   * - T_DELAY
     - 0.0001
     - hydraulic delay constant used by delay block
     - [d]

Current clarifier solids vector actually used by the Python clarifier cores
-----------------------------------------------------------------------------------

The current clarifier wrappers use the first nine solids-characterization entries.
These are:

.. list-table::
   :header-rows: 1

   * - Name
     - Value
     - Meaning
   * - CODtoVSS_XI
     - 1.25488
     - COD-to-VSS factor for XI
   * - CODtoVSS_XS
     - 1.25488
     - COD-to-VSS factor for XS
   * - CODtoVSS_Xbiom
     - 1.25488
     - COD-to-VSS factor for biomass
   * - CODtoVSS_XPHA
     - 1.5686
     - COD-to-VSS factor for XPHA
   * - ISS_P
     - 3.23
     - ISS per phosphorus
   * - f_ISS_biom
     - 0.0
     - ISS per biomass VSS
   * - CODtoVSS_Xch
     - 1.25488
     - COD-to-VSS factor for carbohydrates
   * - CODtoVSS_Xpr
     - 1.25488
     - COD-to-VSS factor for proteins
   * - CODtoVSS_Xli
     - 1.25488
     - COD-to-VSS factor for lipids

Legacy extended solids parameter set
------------------------------------

The MATLAB-side notes also carry a longer 29-entry solids / fractionation block
containing additional N, P, and S composition factors. Those values are useful for
documentation and future fractionator coupling, but the current clarifier C cores only
consume the first nine entries. This truncation is explicit in ``bas_clarifiers.py``. fileciteturn17file1

Reactor kinetic / stoichiometric vectors
----------------------------------------

The main reactor vectors are long, order-sensitive arrays split into:

- ``PAR_AR``
- ``PAR_AX``

These are derived from combined matrices ``PAR_COMB_SS``, ``PAR_COMB_DY``, and
``PAR_COMB_120d``. The public helper returns them with:

.. code-block:: python

   PAR_AR, PAR_AX = build_PAR_sets(mode)

The current Python module stores 182 ordered entries per basin and mode. fileciteturn16file4

Typical-range note
------------------

For many entries, there is **no universal range** that can be documented safely,
because values are a mix of stoichiometric constants, transport constants, and
site-specific calibration knobs. Where range notes were available from your MATLAB
comments, they are documented on the dedicated ``bas_par_sets.py`` page.
