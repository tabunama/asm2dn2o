config_bas.py
=============

Purpose
-------

``config_bas.py`` is the configuration layer used by the reference
workflow. It combines initialization, reactor parameter vectors, clarifier settings,
reactor constants, and time-series loading into one structured object. The file
defines dataclasses for initialization, parameter vectors, clarifiers, reactor
configuration, and the assembled case configuration.

Dataclass structure
-------------------

.. list-table::
   :header-rows: 1

   * - Dataclass
     - Main contents
   * - BasInitConfig
     - ``XINIT_AX``, ``XINIT_AR``, ``XINIT_DELAY``, ``T_DELAY``
   * - BasParConfig
     - ``PAR_AX``, ``PAR_AR``
   * - BasClarifierConfig
     - ``PAR_PRIM``, ``PAR_SEC``, ``PAR_Solids_PRIM``, ``PAR_Solids_SEC``
   * - BasReactorConfig
     - ``VOL_AX``, ``VOL_AR``, ``SOSAT1``, ``DECAY``, ``TEMPMODEL``, ``HFO_PAR1``, ``S_MODEL``, ``Fe_MODEL``, ``SOB_MODEL``
   * - BasConfig
     - grouped init, parameters, clarifiers, reactor config, times, influent series, mode

Current reactor configuration values
------------------------------------

.. list-table::
   :header-rows: 1

   * - Field
     - Current value
   * - VOL_AX
     - 1700
   * - VOL_AR
     - 2400
   * - SOSAT1
     - 8
   * - DECAY
     - 1
   * - TEMPMODEL
     - 0
   * - S_MODEL
     - 1
   * - Fe_MODEL
     - 0
   * - SOB_MODEL
     - 1
   * - HFO_PAR1 length
     - 12

