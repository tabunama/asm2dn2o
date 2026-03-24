asm2dn2o
=========

Python package for ASM2d-N₂O dynamic process modelling.

Overview
--------

The ``asm2dn2o`` package publishes four compiled wastewater-process unit models under one namespace:

.. code-block:: python

   from asm2dn2o import asm2d_n2o, clarifiers, combiner, delay

The ``asm2dn2o`` package is built around an ASM2d-N₂O reactor formulation that extends the IWA
ASM2d framework for biological carbon, nitrogen, and phosphorus removal with
explicit nitrous oxide pathway representation and gas-transfer calculations.
At the reactor level, the model resolves the simultaneous transformation and fate
of COD, N, P, and S, while also tracking dissolved and off-gas N₂O dynamics.

N2O pathways
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
- build plant-specific municipal anaerobic/anoxic/oxic (A2/O) or AX/AR tank layouts, as well as broader flowsheets,
- replay measured influent and recycle time series,
- analyse DO, NH₄, NO₃, and N₂O dynamics,
- connect biological production with gas stripping and off-gas behaviour.

The four modules are:

- ``asm2d_n2o``: main biochemical reactor kernel,
- ``clarifiers``: primary and secondary clarifier blocks,
- ``combiner``: flow-weighted two-stream mixer,
- ``delay``: hydraulic delay / lag block.

What the package does not contain by itself
-------------------------------------------

The modules provide the compiled kernels only. A full simulation project
still requires user-prepared companion files such as:

- influent / pH time-series files,
- initial-condition vectors XINIT,
- basin-specific parameter vectors PAR,
- clarifiers settings,
- measured recycle (RAS/WAS) or blowers/airflow signals (or KLa),
- a plant-specific main driver.

This separation is intentional: the wheel stays compact and reusable, while the
flowsheet, control logic, data handling, and calibration remain project-specific.

Acknowledgement
---------------

The ``asm2dn2o`` package was prepared by Dr. Taher Abunama, based on the original model by Prof. Krist V. Gernaey and his team (PROSYS, DTU).

The ``asm2dn2o`` package was prepared during the `eWatLink <https://cebedeau.be/fr/nos-chroniques/article/projet-ewatlink>`_ project at
`SPGE <https://www.spge.be/en/index.html?IDC=1>`_ and `CEBEDEAU <https://cebedeau.be/fr>`_,
through the `BEWARE Fellowships <https://recherche.wallonie.be/en/home/nos-aides-1/engager-du-personnel-de-recherche-human/beware-fellowships.html>`_
programme funded by the European Commission and SPW Research, within the broader
`Wallonia Research and Innovation framework <https://recherche.wallonie.be/en/home.html>`_
and the `Marie Skłodowska-Curie Actions <https://marie-sklodowska-curie-actions.ec.europa.eu/actions/postdoctoral-fellowships>`_.

The ``asm2dn2o`` package release was prepared and published with the `PROSYS <https://www.kt.dtu.dk/research/prosys>`_,
Process and Systems Engineering Center, Technical University of Denmark (DTU),
under the Head of PROSYS: Prof. Krist V. Gernaey,
Department of Chemical and Biochemical Engineering
(`kvg@kt.dtu.dk <mailto:kvg@kt.dtu.dk>`_), Dr. Xavier Flores-Alsina, and Tianyu Lei.


For license, attribution, and contact information, see
:doc:`license_citation_contact`.



.. toctree::
   :maxdepth: 2
   :caption: User Guide

   installation
   n2o_pathways
   running
   inputs_outputs/index
   unit_modules/index
   configuration/index
   examples/index
   license_citation_contact
