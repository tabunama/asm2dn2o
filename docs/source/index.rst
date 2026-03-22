asm2dn2o
=========

Python package release for ASM2d-N2O dynamic process modelling.

``asm2dn2o`` publishes four compiled unit-model modules under one namespace:

.. code-block:: python

   from asm2dn2o import asm2d_n2o, clarifiers, combiner, delay

The package is designed as a compact modelling kernel rather than a complete end-user
application. Plant-wide simulations are assembled around these compiled units by
preparing the required arrays, parameter vectors, initial conditions, and time-series
inputs in Python.

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
(`kvg@kt.dtu.dk <mailto:kvg@kt.dtu.dk>`_), Dr Xavier Flores-Alsina, and Tianyu Lei.


For license, attribution, and contact information, see
:doc:`license_citation_contact`.

What the package contains
-------------------------

The current wheel provides the reusable computational blocks needed to build dynamic
ASM2d-N2O simulations:

- ``asm2d_n2o``: the main biochemical reactor kernel.
- ``clarifiers``: primary and secondary clarifier wrappers.
- ``combiner``: two-stream mixing.
- ``delay``: hydraulic transport and recycle delay handling.



.. toctree::
   :maxdepth: 2
   :caption: User Guide

   installation
   running
   inputs_outputs/index
   unit_modules/index
   configuration/index
   examples/index
   license_citation_contact
