asm2dn2o
=========

Python package for ASM2d-N₂O dynamic process modelling.

Overview
--------

The ``asm2dn2o`` package publishes four compiled wastewater-process unit models under one namespace:

.. code-block:: python

   from asm2dn2o import asm2d_n2o, clarifiers, combiner, delay

The ``asm2dn2o`` package is built around an ASM2d-N₂O model that extends the IWA
ASM framework for biological carbon, nitrogen, and phosphorus removal with
explicit nitrous oxide pathway representation and gas-transfer calculations.
At the reactor level, the model resolves the simultaneous transformation and fate
of C, N, P, and S, while also tracking dissolved and off-gas N₂O dynamics.

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

- assemble dynamic ASM2d-N₂O reactor simulations in Python,
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
