config_bas.py
=============

Purpose
-------

``config_bas.py`` is the configuration glue layer used by the BAS reference
workflow. It combines initialization, reactor parameter vectors, clarifier settings,
reactor constants, and time-series loading into one structured object. The file
defines dataclasses for initialization, parameter vectors, clarifiers, reactor
configuration, and the assembled case configuration. fileciteturn17file0

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

Why this design is useful
-------------------------

This design separates concerns cleanly:

- initialization is independent of parameter tuning,
- clarifier settings are independent of reactor kinetics,
- input-file loading is independent of reactor construction,
- the main driver can be written against one assembled configuration object.

Input-file loading
------------------

The helper currently expects aligned ``.npz`` files in the same folder, including
mode-specific influent arrays such as ``infl56ss.npz``, ``infl56dy.npz``, or
``infl56_120d.npz``. The loader accepts the first array in the NPZ file, or the
array under the ``data`` key if present. fileciteturn17file0

Recommended build order in a user project
-----------------------------------------

1. select mode,
2. assemble ``BasConfig``,
3. instantiate clarifiers / delays / reactors,
4. allocate output arrays,
5. run the explicit time loop,
6. save and plot results.

That ordering should be mirrored in user scripts and tutorials.
