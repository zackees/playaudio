"""Sound utilities."""

import os
import sys
import time
from subprocess import check_call
import warnings


def playaudio(file: str, ignore_errors=True) -> None:
    assert os.path.exists(file), f"Sound file {file} does not exist."
    try:
        if sys.platform != "win32":
            if "linux" in sys.platform:
                check_call(["xdg-open", file])
            elif sys.platform == "darwin":
                check_call(["afplay", file])
            else:
                assert False, f"Unsupported platform: {sys.platform}."
            return

        os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
        from pygame import mixer  # type: ignore  # pylint: disable=all

        mixer.init()
        mixer.music.load(file)
        mixer.music.play()
        while mixer.music.get_busy():
            time.sleep(0.01)
        mixer.quit()
    except Exception as exc:
        if ignore_errors:
            warnings.warn(f"Cannot play {file} because of {exc}.")
        else:
            raise
