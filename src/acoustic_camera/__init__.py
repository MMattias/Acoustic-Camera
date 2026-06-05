"""Acoustic Camera — locate sound sources with a microphone array + camera.

This is the top-level package. Real functionality (DSP, beamforming, audio/video
IO, visualization) arrives in later phases as submodules. For now this only
exposes the package version and a placeholder entry point, so the toolchain has
something concrete to build, lint, type-check, and test.
"""

__version__ = "0.1.0"


def main() -> None:
    """Console entry point, registered under ``[project.scripts]`` in pyproject.

    Replaced by a real command-line interface in a later phase. For now it just
    confirms the project is installed and runnable.
    """
    print(f"acoustic-camera {__version__}: setup OK")
