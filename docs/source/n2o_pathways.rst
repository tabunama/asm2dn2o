N₂O Pathways and Gas Transfer
=============================

Purpose
-------

This page documents how the current ``asm2d_n2o`` represents N₂O
formation, conversion, and stripping. It is intended as a scientific
reference page that connects the conceptual pathways to the actual
process-rate terms implemented in the compiled reactor code.

Scope 
---------------------------

The current ASM2d-N₂O reactor extends ASM2d with three biological N₂O
production pathways:

1. **NN pathway**: nitrifier nitrification,
2. **ND pathway**: nitrifier denitrification,
3. **DEN pathway**: heterotrophic denitrification.


Pathway map
----------------------

The implemented biological route can be read as follows:

**DEN pathway**

.. math::

   NO_3^- \rightarrow NO_2^- \rightarrow NO \rightarrow N_2O \rightarrow N_2

This route is carried by heterotrophic organisms and is split in the code
into separate rates for growth on fermentable substrate and on acetate.

**NN pathway**

.. math::

   NH_2OH \rightarrow NO_2^- \quad \text{coupled with} \quad NO \rightarrow N_2O

This is the nitrifier-nitrification route.

**ND pathway**

.. math::

   HNO_2 \rightarrow N_2O
   \quad \text{coupled with} \quad
   NH_2OH \rightarrow NO_2^-

This is the nitrifier-denitrification route.


DEN pathway equations
---------------------------------

The heterotrophic denitrification chain is implemented separately for:

- **SF-based growth**,
- **SA-based growth**.


SF-based branch
~~~~~~~~~~~~~~~

NO₂ to NO:

.. math::

   r_{H,SF}^{NO2 \rightarrow NO}
   =
   \mu_H \, hH_{NO2}
   \frac{KH3_{O2}}{KH3_{O2}+S_{O2}}
   \frac{S_F}{K_{F3}+S_F}
   \frac{S_F}{S_F+S_A}
   \frac{S_{NO2}}{KH_{NO2}+S_{NO2}}
   \, Monod_{NH4} \, X_H

NO to N₂O:

.. math::

   r_{H,SF}^{NO \rightarrow N2O}
   =
   \mu_H \, hH_{NO}
   \frac{KH4_{O2}}{KH4_{O2}+S_{O2}}
   \frac{S_F}{K_{F4}+S_F}
   \frac{S_F}{S_F+S_A}
   \frac{S_{NO}}{KH_{NO}+S_{NO}+S_{NO}^2/KI_{NO}}
   \, Monod_{NH4} \, X_H

N₂O to N2:

.. math::

   r_{H,SF}^{N2O \rightarrow N2}
   =
   \mu_H \, hH_{N2O}
   \frac{KH5_{O2}}{KH5_{O2}+S_{O2}}
   \frac{S_F}{K_{F5}+S_F}
   \frac{S_F}{S_F+S_A}
   \frac{S_{N2O}}{KH_{N2O}+S_{N2O}}
   \, Monod_{NH4} \, X_H

SA-based branch
~~~~~~~~~~~~~~~

NO₂ to NO:

.. math::

   r_{H,SA}^{NO2 \rightarrow NO}
   =
   \mu_H \, hH_{NO2}
   \frac{KH3_{O2}}{KH3_{O2}+S_{O2}}
   \frac{S_A}{KH_{A3}+S_A}
   \frac{S_A}{S_F+S_A}
   \frac{S_{NO2}}{KH_{NO2}+S_{NO2}}
   \, Monod_{NH4} \, X_H

NO to N₂O:

.. math::

   r_{H,SA}^{NO \rightarrow N2O}
   =
   \mu_H \, hH_{NO}
   \frac{KH4_{O2}}{KH4_{O2}+S_{O2}}
   \frac{S_A}{KH_{A4}+S_A}
   \frac{S_A}{S_F+S_A}
   \frac{S_{NO}}{KH_{NO}+S_{NO}+S_{NO}^2/KI_{NO}}
   \, Monod_{NH4} \, X_H

N₂O to N₂:

.. math::

   r_{H,SA}^{N2O \rightarrow N2}
   =
   \mu_H \, hH_{N2O}
   \frac{KH5_{O2}}{KH5_{O2}+S_{O2}}
   \frac{S_A}{KH_{A5}+S_A}
   \frac{S_A}{S_F+S_A}
   \frac{S_{N2O}}{KH_{N2O}+S_{N2O}}
   \, Monod_{NH4} \, X_H



NN pathway equation
-------------------------------

The nitrifier-nitrification N₂O production term is written as:

.. math::

   r_{NN,N2O}
   =
   q_{AOB,N2O,NN}
   \frac{S_{NH2OH}}{K_{AOB,NH2OH}+S_{NH2OH}}
   \frac{S_{NO}}{K_{AOB,NN,NO}+S_{NO}}
   X_{AOB}



ND pathway equation
-------------------------------

The nitrifier-denitrification term is written as:

.. math::

   r_{ND,N2O}
   =
   q_{AOB,N2O,ND}
   \frac{S_{NH2OH}}{K_{AOB,NH2OH}+S_{NH2OH}}
   \frac{S_{FNA}^{\,n_{KAOB,HNO2}}}
        {S_{FNA}^{\,n_{KAOB,HNO2}} + K_{AOB,HNO2}^{\,n_{KAOB,HNO2}}}
   f_{SO2}
   X_{AOB}

where the oxygen dependence is:

.. math::

   f_{SO2}
   =
   \frac{S_{O2}}
        {K_{AOB,ND,O2}
        + \left(1-2\sqrt{\frac{K_{AOB,ND,O2}}{K_{AOB,I,O2}}}\right)S_{O2}
        + \frac{S_{O2}^2}{K_{AOB,I,O2}}}


Gas transfer and stripping
--------------------------

The measured and simulated N₂O signal is shaped strongly by stripping.

General gas-liquid transfer logic
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Anoxic transfer**

.. math::

   \frac{dM_{i,gas}}{dt}
   =
   KLa_i
   \left(C_{i,liq} - K_{H,i} C_{i,gas}\right)
   V_{liq}

with a default anoxic transfer coefficient of about ``2 d^-1`` for the
non-aerated period.

**Aerated transfer**

.. math::

   \frac{dM_{i,gas}}{dt}
   =
   \frac{C_{i,liq}}{H_i}
   \left(
   1 -
   \exp\left(
   - \sqrt{\frac{D_i}{D_{O2}}}
   \, KLa_{O2} \, H_i \, \frac{V_{liq}}{Q_{gas}}
   \right)
   \right)
   Q_{gas}



References
----------

- Henze et al. (2000).
- Hiatt and Grady (2008).
- Pocquet et al. (2016).
- Massara et al. (2018).
- Lei et al. (2025).

