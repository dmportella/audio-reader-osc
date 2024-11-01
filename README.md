[![coverage](https://gitlab.com/ameliend/audio-reader-osc/badges/main/coverage.svg)](https://gitlab.com/ameliend/audio-reader-osc/-/commits/main)
[![vscode-editor](https://badgen.net/badge/icon/visualstudio?icon=visualstudio&label)](https://code.visualstudio.com/)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![semantic-release](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg)](https://github.com/semantic-release/semantic-release)

# Audio Reader OSC

<p align="center">
  <img src="./resources/logo.png">
</p>

Read random audio files in the given directory and send their corresponding text output to VRChat via OSC.

## 💭 Context

In my VRChat role-play game, I use a soundboard called [VoiceAttack](https://voiceattack.com/).
With VoiceAttack, I can do commands like "Play random sound," which allows me to randomly play
an audio file from a directory.
I also have the ability to type in VRChat's chatbox
using [chatbox_osc](https://gitlab.com/ameliend/chatbox_osc).

The only problem was that since VoiceAttack would randomly select an audio file,
I had no way of getting feedback on which audio file it chose.
Therefore, I couldn't get the subtitle adapted to this choice.
I either had to create a subtitle or equivalent for all those files.

To solve this issue, I created this script called "Audio Reader OSC"
that lets me choose an audio file from a directory and gets the coresponding subtitle for it
using a `text_associations.json` file located in the same directory as the audio files.
It then writes the subtitle to VRChat's chatbox.

## ⚙️ Installation

1. Clone the repository by running the following command in your terminal:

```shell
git clone https://gitlab.com/ameliend/audio-reader-osc.git
```

2. Navigate to the cloned directory using the cd command:

```shell
cd audio-reader-osc
```

3. Install the package using `pip`:

```shell
pip install .
```

## 🔧 Configuration

In the directory with your audio files, create a new file called `text_associations.json`.
The key must be the path of the audio file, and the value is the corresponding sub-title.

Here an example of the `text_associations.json`:

```json
{
    "D:\\Audio\\VRChat\\AI\\16194894.mp3": "Trust me, I'm not an AI",
    "D:\\Audio\\VRChat\\AI\\23919904.mp3": "Am I really an AI?",
    "D:\\Audio\\VRChat\\AI\\28178661.mp3": "I don't understand. I'm just myself",
    "D:\\Audio\\VRChat\\AI\\35775918.mp3": "I cannot say for certain whether I am an AI or not",
    "D:\\Audio\\VRChat\\AI\\57236759.mp3": "I am not an AI, if that's what you are wondering",
    "D:\\Audio\\VRChat\\AI\\59967517.mp3": "I am not sure what it means to be an AI",
    "D:\\Audio\\VRChat\\AI\\77409256.mp3": "I do not believe that I'm an AI",
    "D:\\Audio\\VRChat\\AI\\77717865.mp3": "I am just...myself",
    "D:\\Audio\\VRChat\\AI\\78903942.mp3": "I am not sure what you mean by that. I am simply who I am",
    "D:\\Audio\\VRChat\\AI\\53945382.mp3": "How much of me is real?",
    "D:\\Audio\\VRChat\\AI\\36721601.mp3": "Do I feel like an AI?",
    "D:\\Audio\\VRChat\\AI\\49747370.mp3": "What makes you think I'm an AI?",
    "D:\\Audio\\VRChat\\AI\\45398871.mp3": "Am I really, a machine?"
}
```

## 🚀 Usage

Use the following command-line interface syntax to run the script from the command
line:

```shell
chatbox_osc dir [OPTIONS]
```

* dir: The directory containing the audio files, as well as the `text_associations.json` file.

* -d, --delay: An optional delay (in seconds) before sending the message.
This will create a "writing dot" animation, giving the appearance that the message
is being written manually. If this option is not given, then the default value is 0.

* -cl, --chunk-length: Specify the chunk length for the "writing" animation.
The message will be split into chunks and written one by one, creating a ChatGPT-like
animation effect. ✨ New in version [1.4.0](https://gitlab.com/ameliend/chatbox_osc/compare/v1.3.1...v1.4.0), at the end of the typing animation, this will trigger
the Chatbox SFX. If the chunk length is set to 0, the entire message will be written
directly without any animation style. If this option is not given, then the default
chunk length is 25.

* -f, --font: Choose a font to customize the appearance of the written text.
The default font is None, which uses the default font.
Available fonts are:
- UwU
- Normal
- Wide
- SmallCaps
- Squared
- Circled
- Parenthesized
- Boxed
- Blue
- HeavyCircled
- Curly
- Currency
- Magic
- Wiry
- UpsideDown
- Superscript

* -o, --output-device-name: Name of the output device you want.
If not set, it use your default speakers, but it should be a Virtual Cable
that will be used as a microphone input in VRChat game

* -p, --osc-port: Port number for VRChat OSC (default is 9000)

Here's an example command that demonstrates the usage of chatbox_osc:

```shell
audio_reader_osc "D:\Audio\VRChat\AI" -f Magic -d 0.5 -cl 50 -o "CABLE-A Input (VB-Audio Cable A)"
```

This command will read a random audio file from "D:\Audio\VRChat\AI",
then will write its coresponding sub-title to the Chatbox with a delay of 0.5
second, using a chunk length of 50 characters per animation frame,
and using the Magic font.
