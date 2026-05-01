ASM2d-GHG/N₂O
================

Python package for ASM2d-GHG/N₂O dynamic process modelling.

Overview
--------

The same compiled model can be used through three PyPI package names:

.. code-block:: bash

   pip install asm2dn2o
   pip install asm2dghg
   pip install asm2dg

The main package is ``asm2dn2o``. The packages ``asm2dghg`` and ``asm2dg`` are
aliases that depend on ``asm2dn2o`` and expose the same compiled model engine.

.. code-block:: python

   from asm2dn2o import asm2d_n2o, clarifiers, combiner, delay
   from asm2dghg import asm2d_ghg
   from asm2dg import asm2d_g

The model extends the IWA ASM framework for biological carbon, nitrogen, and
phosphorus removal with explicit nitrous oxide pathway representation and
gas-transfer calculations. At reactor level, it resolves C, N, P, and S
transformations while tracking dissolved and off-gas N₂O dynamics.

N₂O pathways
-------------------

The current ASM2d-N₂O implementation distinguishes three biological N₂O
production pathways:

1. **NN pathway**  
   Nitrifier nitrification by AOB, linked to hydroxylamine oxidation.

2. **ND pathway**  
   Nitrifier denitrification by AOB, driven by nitrite / free nitrous acid and
   strongly influenced by low-DO conditions.

3. **DEN pathway**  
   Heterotrophic denitrification, where N₂O appears as an intermediate in the
   reduction chain:

   .. math::

      NO_3^- \rightarrow NO_2^- \rightarrow NO \rightarrow N_2O \rightarrow N_2

This pathways separation is central to the model because it allows the user to
interpret whether N₂O are dominated by heterotrophic denitrification,
AOB-related nitrifier denitrification, or nitrifier nitrification
contributions.

A more detailed equation-level description is provided on the dedicated
:doc:`n2o_pathways` page.

Why this package is useful
--------------------------

The package is designed as a compact modelling kernel rather than a full
end-user application. It gives the user the compiled building blocks needed to:

- assemble dynamic ASM2d-GHG/N₂O reactor simulations in Python,
- build plant-specific municipal anaerobic/anoxic/oxic (A2/O) or other layouts; including primary and secondary clarifiers, hydraulic combiner and delay, etc.,
- test control logics on aeration, RAS, WAS, etc.
- analyse DO, NH₄, NO₂, NO₃, and N₂O dynamics,
- connect biological production with gas stripping and off-gas behaviour.


For authors acknowledgement, see:
:doc:`acknowledgement`.

For citation, license and contact information, see:
:doc:`citation_license_contact`.

.. toctree::
   :maxdepth: 2
   :caption: User Guide

   installation
   running
   inputs_outputs/index
   unit_modules/index
   configuration/index
   examples/index
   n2o_pathways
   n2o_ef_cal
   n2o_unisense_cal
   acknowledgement
   citation_license_contact
