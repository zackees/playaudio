# playaudio

`pip install playaudio`

No dependency, cross platform solution for playing a sound in MacOS/Windows/Linux. This repo was inspired by [playsound](https://github.com/TaylorSMarks/playsound), but less buggy, *way* less dependencies, better tested and simpler.

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
```

# Develop

PR's are welcome!

To develop software git clone the repo then run `. ./activate.sh`

# Windows

This environment requires you to use `git-bash`.

# Linting

Run `./lint.sh` to find linting errors using `pylint`, `flake8` and `mypy`.
