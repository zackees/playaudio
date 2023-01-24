"""
Main entry point.
"""

import argparse
from playaudio import playaudio

from playaudio.assets.builtin import BELL_MP3


def main() -> int:
    """Main entry point for the playaudio package."""
    parser = argparse.ArgumentParser("playaudio")
    parser.add_argument("file", help="Sound file to play.", nargs="?")
    args = parser.parse_args()
    file = args.file if args.file else BELL_MP3
    playaudio(file)
    return 0
