# Undawn Piano Auto

## Description

This Python script simulates keyboard inputs based on MIDI file data to your Undawn game.

## Support Me
If you enjoy my work and would like to support me, you can buy me a coffee on Ko-fi!

[![Support Me on Ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/drastraea)

## Features

- Plays MIDI files by simulating keyboard inputs.
- Allows pitch modulation of the MIDI notes.
- Provides a file dialog for easy MIDI file selection if not provided via command-line arguments.
- Uses colored terminal output for better readability.

## Dependencies

The following Python libraries are required:

- `mido` for handling MIDI files.
- `pyautogui` for simulating keyboard inputs.
- `colorama` for colored terminal output.
- `easygui` for file selection dialogs.

## Installation

1. Clone this repository or download the script.

   ```bash
   git clone https://github.com/drastraea/Undawn-Piano-Auto-.git
   ```
2. Navigate to the project directory.
   ```bash
   cd Undawn-Piano-Auto
   ```
3. Install the required dependencies.
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the script with the path to the MIDI file as a command-line argument:
```bash
python udpiano.py --file path/to/your/midi/file.mid --pitch 2
```
If the `--file` argument is not provided, a file dialog will appear to select the MIDI file.

## Arguments
+ `--file`: Path to the MIDI file to play.
+ `--pitch`: Integer value to add as pitch modulation. Default is `0`.

## Example
```bash
python udpiano.py --file example.mid --pitch 2
```
This command plays the `example.mid` file with a pitch modulation of `2`.
