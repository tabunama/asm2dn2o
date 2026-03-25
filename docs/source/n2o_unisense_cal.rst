Unisense A/S N₂O Dissolved Sensing-Based Emission Calculation
===================================================================

Purpose
-------

This page documents how dissolved N₂O measurements can be converted into
N₂O emission rates and emission factors using the same mass-transfer logic
applied in the digital twin. The aim is to ensure that **measurement-based**
and **simulation-based** N₂O emissions are quantified consistently.


Overview
--------

Dissolved N₂O was monitored in the biological reactors using liquid-phase
sensors installed at representative locations in aerated and non-aerated
zones. The sensor signal is interpreted as dissolved ``N₂O-N`` in the liquid
phase. This is useful because it captures:

- accumulation during low-stripping periods,
- rapid release during aeration transitions,
- peak-driven behavior that is often more relevant than daily averages alone.

A key principle of the workflow is that the **same gas-liquid transfer logic**
is used to:

1. convert measured dissolved N₂O into emitted N₂O, and
2. compute emissions from simulated dissolved N₂O.

This is important because full-scale N₂O emissions often reflect **stripping of
previously accumulated dissolved N₂O**, not only instantaneous biological
production. The formulation below follows the project note you provided for
Unisense-based sensing and emission quantification.

Dissolved N₂O sensing
---------------------

The Unisense Environment A/S liquid sensor reports dissolved N₂O as
``mg N₂O-N L⁻¹``. Numerically, this is equivalent to:

.. math::

   1 \; \mathrm{mg \; N_2O\text{-}N \; L^{-1}}
   =
   1 \; \mathrm{g \; N_2O\text{-}N \; m^{-3}}

The sensor head used in the project note is described as
**Standard Range (SR): 0--1.5 mg N₂O-N L⁻¹**. fileciteturn25file0

For documentation and implementation, it is therefore convenient to work
internally with:

.. math::

   S_{N_2O}
   \quad [\mathrm{g \; N_2O\text{-}N \; m^{-3}}]

Unit conventions
----------------

The following unit conventions are recommended throughout this section:

.. list-table::
   :header-rows: 1

   * - Quantity
     - Symbol
     - Recommended unit
   * - Dissolved N₂O concentration
     - :math:`S_{N_2O}`
     - :math:`\mathrm{g \; N \; m^{-3}}`
   * - Airflow from plant signals
     - :math:`Q_A`
     - :math:`\mathrm{m^3 \; h^{-1}}`
   * - Airflow in emission equations
     - :math:`Q_{A,d}`
     - :math:`\mathrm{m^3 \; d^{-1}}`
   * - Aeration field area
     - :math:`A_{aer}`
     - :math:`\mathrm{m^2}`
   * - Reactor volume
     - :math:`V_R`
     - :math:`\mathrm{m^3}`
   * - Diffuser submergence
     - :math:`D_R`
     - :math:`\mathrm{m}`
   * - Laboratory reference depth
     - :math:`D_L`
     - :math:`\mathrm{m}`
   * - Process temperature
     - :math:`T_{proc}`
     - :math:`^\circ\mathrm{C}`
   * - N₂O mass transfer coefficient
     - :math:`kLa_{N_2O}`
     - :math:`\mathrm{d^{-1}}`
   * - Dimensionless Henry constant
     - :math:`H_{N_2O}`
     - :math:`[-]`
   * - Emission rate per reactor volume
     - :math:`r_{N_2O}`
     - :math:`\mathrm{g \; N \; m^{-3} \; d^{-1}}`
   * - Daily emitted mass
     - :math:`E_{N_2O}`
     - :math:`\mathrm{kg \; N \; d^{-1}}`

When airflow is measured as :math:`\mathrm{m^3 \; h^{-1}}`, convert it to
daily flow before using the emission-rate equations:

.. math::

   Q_{A,d} = 24 \, Q_A

Rationale for the emission formulation
--------------------------------------

The dissolved-N₂O signal alone is **not** an emission rate. A physically
consistent emission estimate requires a gas-liquid transfer formulation.

For full-scale benchmarking and control evaluation, the same mass-transfer
logic should be applied to both:

- measured dissolved N₂O, and
- simulated dissolved N₂O.

This makes measurement and simulation directly comparable within the same
boundary and with the same stripping assumptions.

Mass transfer coefficient from aeration field size and airflow
--------------------------------------------------------------

Superficial gas velocity
~~~~~~~~~~~~~~~~~~~~~~~~

Let the total aeration field be the reactor surface area above active
diffusers where bubble release is observed:

.. math::

   A_{aer}
   \quad [\mathrm{m^2}]

The superficial gas velocity is then:

.. math::

   \nu_g = \frac{Q_A}{A_{aer}}
   \qquad [\mathrm{m^3 \; m^{-2} \; s^{-1}}]

where :math:`Q_A` here is expressed in :math:`\mathrm{m^3 \; s^{-1}}`.

N₂O mass transfer coefficient at 20 °C
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The N₂O mass transfer coefficient at :math:`20^\circ\mathrm{C}` is obtained
from an empirical relation using superficial gas velocity and depth scaling:

.. math::

   kLa_{N_2O,20}
   =
   34500
   \left( D_R \, D_L^{-0.49} \right)
   \nu_g^{0.86}
   \qquad [\mathrm{d^{-1}}]

where:

- :math:`D_R` is the water depth above the diffuser in the full-scale reactor,
- :math:`D_L` is the laboratory reference depth.

This form Unisense Environment A/S N₂O Calculation documents.

Temperature correction
----------------------

The mass transfer coefficient is corrected from :math:`20^\circ\mathrm{C}` to
the process temperature using an Arrhenius-type factor:

.. math::

   kLa_{N_2O,T}
   =
   kLa_{N_2O,20}
   \; 1.024^{(T_{proc}-20)}

This correction is needed because gas-transfer rates depend on temperature
under full-scale operation.

Henry's law constant
--------------------

Temperature-dependent Henry coefficient
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Henry coefficient is calculated from a reference value at
:math:`T_\theta = 25^\circ\mathrm{C}`:

.. math::

   kH(T)
   =
   kH_\theta
   \exp\left[
      \left(\frac{-\Delta solnH}{R}\right)
      \left(
         \frac{1}{T_K}
         -
         \frac{1}{T_{\theta,K}}
      \right)
   \right]

with:

.. math::

   T_K = T_{proc} + 273.15

.. math::

   T_{\theta,K} = T_\theta + 273.15

and the constants:

.. math::

   kH_\theta = 0.0247
   \quad
   [\mathrm{mol \; L^{-1} \; bar^{-1}}]

.. math::

   \frac{-\Delta solnH}{R} = 2675
   \quad [\mathrm{K}]

.. math::

   R = 8.314 \times 10^{-5}
   \quad
   [\mathrm{m^3 \; bar \; mol^{-1} \; K^{-1}}]

Dimensionless Henry constant
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The dimensionless Henry constant is then:

.. math::

   H_{N_2O,T}
   =
   \frac{R \, T_K \, 10^3}{kH(T)}

This is the gas-liquid equilibrium coefficient used in the emission-rate
equations. The factor :math:`10^3` converts from liters to cubic meters.

Aerated-zone emission rate
--------------------------

For an aerated reactor region of volume :math:`V_R`, the finite-gas-residence
stripping rate per reactor volume is:

.. math::

   r_{N_2O,aer}
   =
   H_{N_2O,T}
   \, S_{N_2O}
   \left[
      1 -
      \exp\left(
         - kLa_{N_2O,T}
         \, H_{N_2O,T}
         \, \frac{V_R}{Q_{A,d}}
      \right)
   \right]
   \frac{Q_{A,d}}{V_R}

where:

- :math:`S_{N_2O}` is dissolved N₂O concentration,
- :math:`Q_{A,d}` is airflow in :math:`\mathrm{m^3 \; d^{-1}}`,
- :math:`V_R` is the aerated reactor volume.

The corresponding daily emitted mass is:

.. math::

   E_{N_2O,aer}
   =
   \frac{r_{N_2O,aer} \, V_R}{1000}

with :math:`E_{N_2O,aer}` in :math:`\mathrm{kg \; N \; d^{-1}}`.


Non-aerated-zone emission rate
------------------------------

For a non-aerated zone, gas transfer is approximated as a low-kLa surface
exchange process:

.. math::

   r_{N_2O,non}
   =
   kLa_{N_2O,non}
   \left(
      S_{N_2O}
      -
      \frac{C_{N_2O,air}}{H_{N_2O,T}}
   \right)

where:

.. math::

   kLa_{N_2O,non} \approx 2.0
   \quad [\mathrm{d^{-1}}]

and:

.. math::

   C_{N_2O,air} = 3 \times 10^{-4}
   \quad [\mathrm{g \; N \; m^{-3}}]

The corresponding daily emitted mass from a non-aerated region of volume
:math:`V_R` is:

.. math::

   E_{N_2O,non}
   =
   \frac{r_{N_2O,non} \, V_R}{1000}


Total emission over multiple zones
----------------------------------

If the reactor or plant is split into multiple aerated and non-aerated
measurement zones, then total emitted mass over a day is:

.. math::

   E_{N_2O,tot}
   =
   \sum_j E_{N_2O,aer,j}
   +
   \sum_k E_{N_2O,non,k}

For a time series, this quantity is evaluated at each time step and then
integrated or summed over the reporting window.

Recommended implementation workflow
-----------------------------------

A clear workflow for using measured dissolved N₂O is:

1. measure :math:`S_{N_2O}` in aerated and non-aerated zones,
2. measure or reconstruct :math:`Q_A`, :math:`T_{proc}`, and :math:`A_{aer}`,
3. compute :math:`\nu_g`,
4. compute :math:`kLa_{N_2O,20}`,
5. temperature-correct to :math:`kLa_{N_2O,T}`,
6. compute :math:`H_{N_2O,T}`,
7. compute zone-wise emission rates,
8. convert to emitted daily mass,
9. sum across zones,
10. compute the EF over the chosen evaluation window.
