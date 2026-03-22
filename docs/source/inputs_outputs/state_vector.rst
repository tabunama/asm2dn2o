State Vector
============

Purpose
-------

The package is array-driven. A process stream is represented by a fixed-order
56-state vector. Correct ordering is essential.

General convention
------------------

- 56-state stream: standard liquid stream exchanged between unit blocks.
- 62-entry reactor input ``u``: stream + control / auxiliary entries.
- 101-entry reactor output ``y``: first 56 entries are the liquid outlet stream.

Key index conventions
---------------------

The most frequently used indices are:

.. list-table::
   :header-rows: 1

   * - Simulink index (1-based)
     - Python index (0-based)
     - Meaning
   * - 1
     - 0
     - S_O2
   * - 5
     - 4
     - S_NH4
   * - 7
     - 6
     - S_N2O
   * - 9
     - 8
     - S_NO2
   * - 10
     - 9
     - S_NO3
   * - 37
     - 36
     - X_TSS proxy
   * - 38
     - 37
     - Q_m3d
   * - 39
     - 38
     - Temperature

Full 56-state order
-------------------

.. list-table::
   :header-rows: 1

   * - Python index
     - Simulink index
     - State
   * - 0
     - 1
     - S_O2
   * - 1
     - 2
     - S_F
   * - 2
     - 3
     - S_A
   * - 3
     - 4
     - S_I
   * - 4
     - 5
     - S_NH4
   * - 5
     - 6
     - S_NH2OH
   * - 6
     - 7
     - S_N2O
   * - 7
     - 8
     - S_NO
   * - 8
     - 9
     - S_NO2
   * - 9
     - 10
     - S_NO3
   * - 10
     - 11
     - S_N2
   * - 11
     - 12
     - S_PO4
   * - 12
     - 13
     - S_IC
   * - 13
     - 14
     - X_I
   * - 14
     - 15
     - X_S
   * - 15
     - 16
     - X_H
   * - 16
     - 17
     - X_PAO
   * - 17
     - 18
     - X_PP
   * - 18
     - 19
     - X_PHA
   * - 19
     - 20
     - X_AOB
   * - 20
     - 21
     - X_NOB
   * - 21
     - 22
     - S_K
   * - 22
     - 23
     - S_Mg
   * - 23
     - 24
     - S_SO4
   * - 24
     - 25
     - S_Fe2
   * - 25
     - 26
     - S_Fe3
   * - 26
     - 27
     - S_IS
   * - 27
     - 28
     - X_S0
   * - 28
     - 29
     - X_SRB
   * - 29
     - 30
     - X_HFO_L
   * - 30
     - 31
     - X_HFO_H
   * - 31
     - 32
     - X_HFO_LP
   * - 32
     - 33
     - X_HFO_HP
   * - 33
     - 34
     - X_HFO_HP_old
   * - 34
     - 35
     - X_HFO_LP_old
   * - 35
     - 36
     - X_HFO_old
   * - 36
     - 37
     - X_TSS
   * - 37
     - 38
     - Q_m3d
   * - 38
     - 39
     - Temp
   * - 39
     - 40
     - S_Na
   * - 40
     - 41
     - S_Cl
   * - 41
     - 42
     - S_Ca
   * - 42
     - 43
     - AlOH3
   * - 43
     - 44
     - X_ISS0
   * - 44
     - 45
     - X_CaCO3
   * - 45
     - 46
     - X_CaP
   * - 46
     - 47
     - X_struv
   * - 47
     - 48
     - X_Dummy1
   * - 48
     - 49
     - S_CH4
   * - 49
     - 50
     - X_Dummy2
   * - 50
     - 51
     - X_Dummy3
   * - 51
     - 52
     - X_Dummy4
   * - 52
     - 53
     - XSOB
   * - 53
     - 54
     - XAlPO4
   * - 54
     - 55
     - XCaO
   * - 55
     - 56
     - XMgCO3

Notes
-----

- ``X_TSS`` may be a direct state or a proxy depending on the surrounding workflow.
- The safest practice is to define all indices once and reuse them everywhere.
