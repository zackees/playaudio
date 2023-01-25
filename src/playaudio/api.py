"""Sound utilities."""

import os
import sys
from subprocess import call
import warnings


def playaudio(file: str) -> None:
    assert os.path.exists(file), f"Sound file {file} does not exist."
    if sys.platform != "win32":
        if "linux" in sys.platform:
            call(["xdg-open", file])
        elif sys.platform == "darwin":
            call(["afplay", file])
        else:
            assert False, f"Unsupported platform: {sys.platform}."
        return
    try:
        import winsound  # type: ignore  # pylint: disable=all

        winsound.PlaySound(file, winsound.SND_FILENAME)
    except Exception as exc:
        warnings.warn(f"Cannot play audio because of {exc}.")
