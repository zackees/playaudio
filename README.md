# playaudio

`pip install playaudio`

A cross platform solution for playing a sound in MacOS/Windows/Linux.

[![MacOS_Tests](../../actions/workflows/push_macos.yml/badge.svg)](../../actions/workflows/push_macos.yml)
[![Ubuntu_Tests](../../actions/workflows/push_ubuntu.yml/badge.svg)](../../actions/workflows/push_ubuntu.yml)
[![Win_Tests](../../actions/workflows/push_win.yml/badge.svg)](../../actions/workflows/push_win.yml)

[![Linting](../../actions/workflows/lint.yml/badge.svg)](../../actions/workflows/lint.yml)

## Install

Uses the built in system commands to play audio.

# Usage

### Python

```python
from playaudio import playaudio
playaudio("my.mp3")  # blocks until sound is played.
```

### Command line

```bash
> pip install playaudio
> playaudio "my.mp3"
> playaudio # plays an included bell.mp3 sound.
```

# Develop

PR's are welcome!

To develop software git clone the repo then run `. ./activate.sh`

# Windows

This environment requires you to use `git-bash`. This library expects a sound card to be installed. If you are running on a server then you will need to install a virtual sound card. See [windows setup here](.github/workflows/push_win.yml).

# Linting

Run `./lint.sh` to find linting errors using `pylint`, `flake8` and `mypy`.


# Releases:
  * 1.0.4: Windows: Supports playing mp3 files
  * 1.0.3: Adds ignore_errors=True for playaudio()
  * 1.0.2: BELL_FILE -> BELL_MP3
  * 1.0.1: Fix readme
  * 1.0.0: Initial release
