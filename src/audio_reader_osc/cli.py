"""Console script for Audio Reader OSC."""

import argparse
from sys import argv

from chatbox_osc import write_chatbox
from pythonosc.udp_client import SimpleUDPClient

from audio_reader_osc import pick_random_audio_file_with_text, read_audio_file


def main_cli() -> None:
    """Console script for Audio Reader OSC."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        dest="dir",
        type=str,
        help="",
    )
    parser.add_argument(
        "-d",
        "--delay",
        type=float,
        default=0,
        help="An optional delay before starting writing in the Chatbox (0 by default) "
        "which creates the '3 dots' typing animation.",
    )
    parser.add_argument(
        "-cl",
        "--chunk-length",
        type=int,
        default=25,
        help="The number of characters per segment for displaying the message "
        "as it is being typed-in. Set to 0 or None to disable this feature "
        "and show the full message at once.",
    )
    parser.add_argument(
        "-f",
        "--font",
        type=str,
        default="Normal",
        help="The name of a predefined text style from FONTS (default: 'Normal') "
        "to be used for the message.",
    )
    parser.add_argument(
        "-o",
        "--output-device-name",
        type=str,
        help="Name of the output device you want, else will be default device.",
    )
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=9000,
        help="Port number for VRChat OSC (default is 9000).",
    )
    args = parser.parse_args()

    audio_file, audio_text = pick_random_audio_file_with_text(args.dir)
    read_audio_file(audio_file, args.output_device_name)
    client = SimpleUDPClient("127.0.0.1", args.port)
    write_chatbox(client, audio_text, args.delay, args.chunk_length, args.font)


def create_text_associations_cli() -> None:
    """Console script for create_text_associations."""
    from audio_reader_osc.utils import create_text_associations

    mp3_files = [f for f in argv[1:] if f.endswith(".mp3")]
    create_text_associations(mp3_files)


def create_text_associations_for_musics_cli() -> None:
    """Console script for create_text_associations_for_musics."""
    from audio_reader_osc.utils import create_text_associations_for_musics

    mp3_files = [f for f in argv[1:] if f.endswith(".mp3")]
    create_text_associations_for_musics(mp3_files)
