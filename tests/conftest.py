"""Shared pytest fixtures.

The functional tests resolve their Méso-NH fixtures through ``os.getcwd()``
(``examples/fuel_map``), so every test runs from the repository root, which
pytest resolves as ``rootpath`` from the location of ``pyproject.toml``.
"""

import pytest


@pytest.fixture(autouse=True)
def _run_from_repo_root(monkeypatch, pytestconfig):
    """Run each test from the repository root, whatever the invocation directory."""
    monkeypatch.chdir(pytestconfig.rootpath)
