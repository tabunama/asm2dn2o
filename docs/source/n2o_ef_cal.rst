Emission Factor (EF) Calculation
=================================================

Emission factor definition
--------------------------

The emission factor (EF) is expressed as the percentage of influent total
nitrogen emitted as :math:`\mathrm{N_2O\text{-}N}` over the evaluation period.

For a time series with time step :math:`\Delta t` in days, the EF is calculated as:

.. math::

   EF_{N_2O}
   =
   100
   \frac{
      \sum_{n}
      E_{N_2O,tot,n}\,\Delta t
   }{
      \sum_{n}
      \left(
         \frac{Q_{in,n}\,TN_{in,n}}{1000}
      \right)\Delta t
   }

where:

- :math:`E_{N_2O,tot,n}` is the total emitted N₂O mass rate at time step
  :math:`n`, in :math:`\mathrm{kg \; N \; d^{-1}}`,
- :math:`Q_{in,n}` is the influent flow rate at time step :math:`n`, in
  :math:`\mathrm{m^3 \; d^{-1}}`,
- :math:`TN_{in,n}` is the influent total nitrogen concentration at time step
  :math:`n`, in :math:`\mathrm{g \; N \; m^{-3}}`,
- :math:`\Delta t` is the time step in days.

