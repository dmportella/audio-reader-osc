"""Tests for Audio Reader OSC."""

from pathlib import Path

from audio_reader_osc import pick_random_audio_file_with_text


def test_pick_random_audio_file_with_text(test_folder_location):
    filepath, text = pick_random_audio_file_with_text(test_folder_location)
    filepath = str(Path(filepath).absolute())
    expected_pairs = [
        (str(test_folder_location / "16194894.mp3"), "Trust me, I'm not an AI"),
        (str(test_folder_location / "23919904.mp3"), "Am I really an AI?"),
    ]
    assert (filepath, text) in expected_pairs


def test_pick_random_audio_file_with_text_no_audio(test_folder_with_no_audio_files_location):
    assert pick_random_audio_file_with_text(test_folder_with_no_audio_files_location) is None


def test_pick_random_audio_file_with_text_no_json(test_folder_with_no_json_location):
    assert pick_random_audio_file_with_text(test_folder_with_no_json_location) is None


def test_pick_random_audio_file_with_missing_audio(test_folder_with_missing_audio_files):
    assert pick_random_audio_file_with_text(test_folder_with_missing_audio_files)
