"""Smoke tests: prove the package imports and the toolchain is wired up.

These intentionally assert almost nothing about behaviour. Their job is to fail
loudly if the project cannot even be imported — which would mean our setup is
broken. Real, meaningful tests arrive alongside real code in Phase 1 (the
ground-truth harness for beamforming).
"""

import acoustic_camera


def test_package_exposes_version() -> None:
    assert isinstance(acoustic_camera.__version__, str)
    assert acoustic_camera.__version__  # non-empty


def test_main_is_callable() -> None:
    assert callable(acoustic_camera.main)
