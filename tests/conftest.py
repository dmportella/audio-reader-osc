"""Pytest configuration file for Audio Reader OSC."""

from pathlib import Path

import pytest

CURRENT_DIR = Path(__file__).parent


def pytest_configure(config):
    # A "local" marker to ignore tests that will fail in the Gitlab pipelines
    # Add `@pytest.mark.local` above your tests functions you want to ignore online
    config.addinivalue_line("markers", "local : mark a local test")


@pytest.fixture
def test_folder_location():
    return CURRENT_DIR / "test_folder"


@pytest.fixture
def test_folder_with_no_audio_files_location():
    return CURRENT_DIR / "test_folder_with_no_audio_files"


@pytest.fixture
def test_folder_with_no_json_location():
    return CURRENT_DIR / "test_folder_with_no_json"


@pytest.fixture
def test_folder_with_missing_audio_files():
    return CURRENT_DIR / "test_folder_with_missing_audio_files"
