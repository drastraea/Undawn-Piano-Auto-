# Undawn-Piano-Auto-
This Python script reads a MIDI file and simulates piano key presses on your computer using the `pyautogui` library.

## Features:
- **MIDI Playback Simulation**: Interprets MIDI note events and simulates key presses corresponding to those notes.
- **Pitch Modulation**: Allows you to apply pitch modulation to the notes being played.
- **Customizable**: You can specify the MIDI file path and pitch modulation directly from the command line.

## Requirements:
- `mido` for MIDI file parsing.
- `pyautogui` for simulating key presses.

## Usage:
1. Install the required packages:
   ```bash
   pip install mido pyautogui
   ```
2. Run the script with the desired MIDI file and pitch modulation:
   ```bash
   python midi_auto_keypress.py --file path/to/your/midi/file.mid --pitch 2
   ```

##Command-Line Arguments:
--file: Path to the MIDI file to play.
--pitch: Pitch modulation to apply to the MIDI notes.

Example:
```bash
python midi_auto_keypress.py --file example.mid --pitch 1
```
