Emission Factor (EF) Calculation
=================================================

Emission factor definition
--------------------------

The emission factor (EF) is reported as the fraction of influent total nitrogen
load emitted as :math:`\mathrm{N_2O\text{-}N}` over the evaluation period.

Continuous form
~~~~~~~~~~~~~~~

.. math::

   EF_{N_2O}
   =
   100
   \frac{
      \int_{t_0}^{t_f} E_{N_2O,tot}(t)\,dt
   }{
      \int_{t_0}^{t_f}
      \frac{Q_{in}(t)\,TN_{in}(t)}{1000}
      \, dt
   }

where:

- :math:`E_{N_2O,tot}(t)` is in :math:`\mathrm{kg \; N \; d^{-1}}`,
- :math:`Q_{in}(t)` is in :math:`\mathrm{m^3 \; d^{-1}}`,
- :math:`TN_{in}(t)` is in :math:`\mathrm{g \; N \; m^{-3}}`.

Discrete form
~~~~~~~~~~~~~

For a discrete time series with step size :math:`\Delta t` in days:

.. math::

   EF_{N_2O}
   =
   100
   \frac{
      \sum_n E_{N_2O,tot,n}\,\Delta t
   }{
      \sum_n
      \left(
         \frac{Q_{in,n}\,TN_{in,n}}{1000}
      \right)
      \Delta t
   }

This EF definition is widely used because it normalizes emitted
:math:`\mathrm{N_2O\text{-}N}` by the incoming total nitrogen load.
