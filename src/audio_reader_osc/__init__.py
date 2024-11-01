"""Top-level package for Audio Reader OSC."""

from audio_reader_osc._version import __version__
from audio_reader_osc.main import pick_random_audio_file_with_text, read_audio_file

__author__ = """Amelien Deshams"""
__email__ = "a.deshams+git@slmail.me"
__all__ = [
    "__version__",
    "pick_random_audio_file_with_text",
    "read_audio_file",
]
