config_bas.py
=============

Purpose
-------

``config_bas.py`` is the configuration glue module used by the BAS reference
workflow. It combines initial conditions, reactor parameters, clarifier settings,
reactor-level constants, and input time-series loading into one structured object.

Main dataclasses
----------------

The current configuration pattern uses the following dataclasses:

- ``BasInitConfig``
- ``BasParConfig``
- ``BasClarifierConfig``
- ``BasReactorConfig``
- ``BasConfig``

What they group
---------------

``BasInitConfig``

- ``XINIT_AX``
- ``XINIT_AR``
- ``XINIT_DELAY``
- ``T_DELAY``

``BasParConfig``

- ``PAR_AX``
- ``PAR_AR``

``BasClarifierConfig``

- ``PAR_PRIM``
- ``PAR_SEC``
- ``PAR_Solids_PRIM``
- ``PAR_Solids_SEC``

``BasReactorConfig``

- ``VOL_AX``
- ``VOL_AR``
- ``SOSAT1``
- ``DECAY``
- ``TEMPMODEL``
- ``HFO_PAR1``
- ``S_MODEL``
- ``Fe_MODEL``
- ``SOB_MODEL``

``BasConfig``

- ``init``
- ``par``
- ``clar``
- ``reactor``
- ``times``
- ``infl_ts``
- ``mode``

Why this matters
----------------

This structure is a very good public template because it matches the way users
actually build new cases:

- initialize states,
- load parameter vectors,
- load clarifier parameters,
- load reactor constants,
- load time-series inputs,
- pass the grouped configuration to a main driver.

Recommendation
--------------

New users do not have to keep the exact same dataclass structure, but they should
keep the same conceptual separation between:

- state initialization,
- reactor parameters,
- clarifier parameters,
- scalar reactor settings,
- input time series.
