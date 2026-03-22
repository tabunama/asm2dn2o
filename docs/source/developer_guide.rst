Developer Guide
===============

Purpose
-------

This page summarises the practical maintenance pattern for the public package and
its documentation.

Repository roles
----------------

The current public release is best understood as two layers:

- the package repository and published wheel,
- user- or project-level reference scripts built around the wheel.

The wheel should stay compact and stable. Larger site-specific drivers, calibration
notebooks, or plant data pipelines can remain outside the core package.

Documentation maintenance
-------------------------

The documentation is organised as a Sphinx project with a Read the Docs-style theme.
Recommended maintenance rules:

- keep pages short and specific,
- always state array sizes explicitly,
- always state whether indexing is 1-based Simulink or 0-based Python,
- document units for every page that uses time or flow,
- link to the state-vector page instead of duplicating long tables everywhere.

Recommended page template
-------------------------

A good package page usually contains:

- a short purpose statement,
- required inputs,
- array dimensions,
- a compact code example,
- notes on units and indexing,
- common failure modes.

Adding a new example
--------------------

When adding a new example page:

1. state the use case clearly,
2. show the required input files,
3. show the import statement,
4. include one short code block,
5. document the expected outputs,
6. list limitations or assumptions.

Rebuilding wheels
-----------------

When preparing a new package release:

- update package metadata,
- rebuild the wheel in a clean environment,
- validate the wheel with ``twine check``,
- upload to PyPI,
- update README and documentation to match the new public release.

Building docs locally
---------------------

Use the Sphinx Python-module call if the command-line launcher is not on PATH:

.. code-block:: bash

   python -m sphinx -M html docs/source docs/build

Then open:

.. code-block:: text

   docs/build/html/index.html

Publishing docs
---------------

The current recommended publication route is GitHub Pages with GitHub Actions:

- commit the ``docs/`` source tree,
- add ``.github/workflows/docs.yml``,
- enable Pages in the repository settings,
- deploy from GitHub Actions.

Notes
-----

- Keep generated HTML out of git unless you intentionally choose a branch-based Pages workflow.
- Keep private build inputs out of the public repository if the repo is meant to be wheel-first rather than source-build-first.
