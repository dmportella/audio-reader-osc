import json
import random
import re
from pathlib import Path

from whisper_dictate.dictate_file import dictate_file


def create_text_associations(mp3_files: list[str]) -> None:
    """Create a dictionary of subtitles associations for the given list of mp3 files.

    Using Whisper's transcription.

    Parameters
    ----------
    mp3_files : List[str]
        A list of paths to mp3 files.
    """
    associations = {path: dictate_file(Path(path)) for path in mp3_files}
    text_associations_location = Path(mp3_files[0]).parent / "text_associations.json"
    with text_associations_location.open("w", encoding="utf8") as f:
        json.dump(associations, f)


def create_text_associations_for_musics(mp3_files: list[str]) -> None:
    """Create a dictionary of text associations for the given list of mp3 files.

    By formatting them as music titles with emojis.

    Parameters
    ----------
    mp3_files : List[str]
        A list of paths to mp3 files.
    """
    emojis = ["🎵", "🎶"]
    associations = {path: Path(path).name for path in mp3_files}
    for i, (path, filename) in enumerate(associations.items(), start=1):
        clear_filename = re.sub(r"\[.*?\]", "", filename).replace(".mp3", "")
        associations[path] = f"🎼 Musicbox n°{i}: {clear_filename} {random.choice(emojis)}"
    text_associations_location = Path(mp3_files[0]).parent / "text_associations.json"
    with text_associations_location.open("w", encoding="utf8") as f:
        json.dump(associations, f)
