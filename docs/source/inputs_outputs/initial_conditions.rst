Initial Conditions
==================

Purpose
-------

Initial conditions must be configured **before** building the flowsheet layout and
before preparing the input data replay. In the current BAS-style workflow, the
initialization helper returns one 56-state vector for each major block:

- ``XINIT_AR`` for the aerobic / downstream reactor,
- ``XINIT_AX`` for the anoxic / upstream reactor,
- ``XINIT_DELAY`` for the recycle or transport delay block.

Current Python helper
---------------------

The current helper returns the three vectors as:

.. code-block:: python

   XINIT_AR, XINIT_AX, XINIT_DELAY = build_XINIT_sets(mode)

Supported modes are ``"ss"``, ``"dy"``, and ``"120d"``. The current implementation
stores each mode as a 56 x 3 matrix with columns ``[AR, AX, DELAY]`` and then slices
them into the three one-dimensional vectors. The helper is exposed directly in
``bas_init_sets.py``. fileciteturn17file2

Configuration sequence
----------------------

A practical build order is:

1. select a mode and load ``XINIT_AR``, ``XINIT_AX``, ``XINIT_DELAY``,
2. load reactor parameter vectors ``PAR_AR`` and ``PAR_AX``,
3. load clarifier and solids parameters,
4. load reactor-wide switches and constants,
5. define the layout and instantiate the unit blocks,
6. load aligned influent / pH / measured-flow time series.

Interpretation notes
--------------------

- ``AR`` and ``AX`` values should reflect the intended operating point before the time
  replay starts.
- ``XINIT_DELAY`` should be hydraulically consistent with the stream it represents.
- ``Q_m3d`` and ``Temp`` must already be meaningful in the initial vectors.

XINIT values for AR, AX, DELAY
--------------------------------------

.. csv-table:: SS initial values (columns are AR, AX, DELAY)
   :header: "Simulink index", "State", "Description", "AR", "AX", "DELAY"

   "1", "S_O2", "dissolved oxygen", "5.1", "0.4", "0.4"
   "2", "S_F", "fermentable readily biodegradable substrate", "0.5", "0.3", "0.02"
   "3", "S_A", "acetate / VFA-like soluble carbon", "0.8", "0.1", "0.1"
   "4", "S_I", "soluble inert COD", "30", "30", "20"
   "5", "S_NH4", "ammonium + ammonia nitrogen", "0.4", "0.4", "0.4"
   "6", "S_NH2OH", "hydroxylamine intermediate", "0.066", "0.0577536", "0.01"
   "7", "S_N2O", "dissolved nitrous oxide", "0.005", "0.00335", "0.005"
   "8", "S_NO", "nitric oxide", "0.13", "1.34239", "0.13"
   "9", "S_NO2", "nitrite nitrogen", "0.4", "0.0465717", "0.4"
   "10", "S_NO3", "nitrate nitrogen", "4", "4", "4"
   "11", "S_N2", "dissolved nitrogen gas", "0.3", "2.93247", "0.3"
   "12", "S_PO4", "orthophosphate phosphorus", "2", "0.42098", "2"
   "13", "S_IC", "inorganic carbon", "45", "20", "45"
   "14", "X_I", "particulate inert COD", "600", "550", "500"
   "15", "X_S", "slowly biodegradable particulate substrate", "80", "75", "65"
   "16", "X_H", "ordinary heterotrophic organisms", "1250", "1200", "1000"
   "17", "X_PAO", "phosphate accumulating organisms", "250", "290", "240"
   "18", "X_PP", "polyphosphate storage", "85", "75", "70"
   "19", "X_PHA", "PHA storage polymers", "40", "45", "35"
   "20", "X_AOB", "ammonia oxidizing biomass", "140", "85", "80"
   "21", "X_NOB", "nitrite oxidizing biomass", "90", "60", "60"
   "22", "S_K", "potassium", "10", "11", "10"
   "23", "S_Mg", "magnesium", "14", "12", "14"
   "24", "S_SO4", "sulfate sulfur", "45", "32", "45"
   "25", "S_Fe2", "ferrous iron", "0", "0", "0"
   "26", "S_Fe3", "ferric iron", "0", "0", "0"
   "27", "S_IS", "soluble sulfide / inorganic sulfur pool", "0", "0", "0"
   "28", "X_S0", "elemental sulfur solids", "0.277", "0", "0.277"
   "29", "X_SRB", "sulfate reducing biomass", "0", "0", "0"
   "30", "X_HFO_L", "low-reactivity hydrous ferric oxide", "0", "0", "0"
   "31", "X_HFO_H", "high-reactivity hydrous ferric oxide", "0", "0", "0"
   "32", "X_HFO_LP", "low-reactivity HFO with bound phosphate", "0", "0", "0"
   "33", "X_HFO_HP", "high-reactivity HFO with bound phosphate", "0", "0", "0"
   "34", "X_HFO_HP_old", "aged high-reactivity HFO-P fraction", "0", "0", "0"
   "35", "X_HFO_LP_old", "aged low-reactivity HFO-P fraction", "0", "0", "0"
   "36", "X_HFO_old", "aged HFO pool", "0", "0", "0"
   "37", "X_TSS", "total suspended solids proxy/state", "2200", "2200", "2200"
   "38", "Q_m3d", "volumetric flow", "2191.2", "2191.2", "2191.2"
   "39", "Temp", "liquid temperature", "13.3", "13.3", "13.3"
   "40", "S_Na", "sodium", "90", "70", "90"
   "41", "S_Cl", "chloride", "120", "80", "120"
   "42", "S_Ca", "calcium", "55", "40", "55"
   "43", "AlOH3", "aluminium hydroxide solids", "1.1", "0.5", "1.1"
   "44", "X_ISS0", "inorganic suspended solids pool", "3", "2.5", "3"
   "45", "X_CaCO3", "calcium carbonate solids", "2", "1.2", "2"
   "46", "X_CaP", "calcium phosphate solids", "1", "0.5", "1"
   "47", "X_struv", "struvite solids", "0", "0", "0"
   "48", "X_Dummy1", "reserved / unused placeholder", "0", "0", "0"
   "49", "S_CH4", "dissolved methane", "0", "0", "0"
   "50", "X_Dummy2", "reserved / unused placeholder", "0", "0", "0"
   "51", "X_Dummy3", "reserved / unused placeholder", "0", "0", "0"
   "52", "X_Dummy4", "reserved / unused placeholder", "0", "0", "0"
   "53", "XSOB", "sulfur oxidizing biomass", "0", "0", "0"
   "54", "XAlPO4", "aluminium phosphate solids", "0", "0", "0"
   "55", "XCaO", "calcium oxide / lime-related solids placeholder", "0", "0", "0"
   "56", "XMgCO3", "magnesium carbonate solids placeholder", "0", "0", "0"



Practical guidance
------------------

- Treat these values as plant- and case-specific starting points, not universal defaults.
- Revisit biomass states first when switching to a new site or a new operating regime.
- Revisit dissolved nitrogen species and oxygen next when the early transient is unrealistic.
- Keep the initialization file separate from the parameter file.