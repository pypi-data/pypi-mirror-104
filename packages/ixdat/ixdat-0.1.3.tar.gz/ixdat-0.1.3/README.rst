=============================================
``ixdat``: The In-situ Experimental Data Tool
=============================================

``ixdat`` provides a powerful **object-oriented** interface to experimental data, especially in-situ experimental data for which it is of interest to combine data obtained simultaneously from multiple techniques.

Documentation is at https://ixdat.readthedocs.io

``ixdat`` has replaced the existing electrochemistry - mass spectrometry data tool, `EC_MS <https://github.com/ScottSoren/EC_MS>`_,
and will thus become a powerful stand-alone tool for analysis and visualization of data acquired by the equipment of `Spectro Inlets <https://spectroinlets.com>`_ and other EC-MS solutions.
It will also replace the existing electrochemistry - synchrotron GIXRD data tool, `EC_Xray <https://github.com/ScottSoren/EC_Xray>`_ when needed.
Over time, it will acquire functionality for more and more techniques. Please help get yours incorporated!

In addition to a **pluggable** parser interface for importing your data format, ``ixdat`` it also includes
pluggable exporters and plotters, as well as a database interface. A relational model of experimental data is
thought into every level.

``ixdat`` is shown in practice in a growing number of open repositories of data and analysis
for academic publications:

- Tracking oxygen atoms in electrochemical CO oxidation - Part II: Lattice oxygen reactivity in oxides of Pt and Ir

  - Article: https://doi.org/10.1016/j.electacta.2021.137844
  - Repository: https://github.com/ScottSoren/pyCOox_public

- Dynamic Interfacial Reaction Rates from Electrochemistry - Mass Spectrometry

  - Article:
  - Repository: https://github.com/kkrempl/Dynamic-Interfacial-Reaction-Rates

`ixdat`` is free and open source software and we welcome input and new collaborators. Please help us improve!
