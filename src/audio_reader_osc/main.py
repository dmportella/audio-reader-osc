"""Main module."""

import json
import os
import random
import threading
from pathlib import Path

import pygame
import pygame.mixer
from logger import Logger

logger = Logger(name="Audio Reader OSC")


def pick_random_audio_file_with_text(path: str) -> tuple[str, str] | None:
    """Pick a random audio file and its associated text from the given directory.

    Parameters
    ----------
    path : str
        The directory containing the audio files and their `text_associations.json`.

    Returns
    -------
    Optional[Tuple[str, str]]
        A tuple of two strings: the file name of a random audio file (with .mp3 extension)
        found in the given directory, and its associated text.
        If no valid audio files or associated text are found, returns None instead.
    """
    audio_files_and_text = {}
    text_associations_filepath = Path(path) / "text_associations.json"
    if text_associations_filepath.exists():
        with text_associations_filepath.open(encoding="utf8") as f:
            audio_files_and_text.update(json.load(f))
    else:
        logger.error("'text_associations.json' file not found in the directory: %s", path, notify=True)
        return None
    if not audio_files_and_text:
        return None
    if not (audio_files := [f for f in os.listdir(path) if f.endswith(".mp3")]):
        logger.error("No audio files (.mp3) found in the directory: %s", path, notify=True)
        return None
    if len(audio_files_and_text) != len(audio_files):
        logger.warning(
            "The number of text associations in the directory: %s does not match the number "
            "of audio files. Some text will be missing.",
            path,
            notify=True,
        )
    random_audio_file_choice = random.choice(list(audio_files_and_text.keys()))
    return random_audio_file_choice, audio_files_and_text[random_audio_file_choice]


def read_audio_file(filepath: str, output_device_name: str | None = None) -> None:
    """Read an audio file and plays it using a specified output device name.

    Parameters
    ----------
    filepath : str
        The path to the audio file.
    output_device_name : str | None, optional
        The name of the output device where the audio will be played.
        If not provided, default output device is used, by default None.
    """

    def stream_thread() -> None:
        pygame.mixer.music.load(filepath)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():  # Wait until the music finishes playing
            continue
        pygame.mixer.quit()

    if output_device_name:
        pygame.mixer.pre_init(devicename=output_device_name)
    else:
        pygame.mixer.pre_init()
    pygame.mixer.init()
    thread = threading.Thread(target=stream_thread)
    thread.start()
