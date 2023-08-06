setup-requirements
==================

.. image:: https://github.com/mbachry/setup-requirements/actions/workflows/ci.yaml/badge.svg?branch=master
    :alt: Build status
    :target: https://github.com/mbachry/setup-requirements/actions

A PEP 517 build backend that automatically adds ``requirements.txt``
contents to wheel dependencies.

Usage
-----

Use ``setup_requirements`` as your build backend in ``pyproject.toml``::

  [build-system]
  requires = ['setuptools>=42', 'wheel', 'setup-requirements']
  build-backend = 'setup_requirements'

Notes
-----

This backend should be used if you want to build an **application**
with pinned dependencies. For libraries use standard
``install_requires`` without pins.

The backend exists only because it's not possible to use ``file:`` in
``setup_requires`` (yet?). See this `github issue`_.

.. _github issue: https://github.com/pypa/setuptools/issues/1951

Limitations
-----------

It's not possible to use a different path than a top-level
``requirements.txt`` file.
