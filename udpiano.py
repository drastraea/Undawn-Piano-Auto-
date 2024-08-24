import mido
import pyautogui
import time
import argparse
import easygui
from colorama import Fore, Style, init

init()

parser = argparse.ArgumentParser()
parser.add_argument("--file", type=str, help="Path to MIDI file to play", dest='path')
parser.add_argument("--pitch", type=int, default=0, help="Pitch modulation to add", dest="pt_mod")
args = parser.parse_args()

def map_piano_note_to_key(note):
    piano_G = ['f1', 'f2', 'f3']
    piano_keymap = ['q', '1', 'w', '2', 'e', 'r', '3', 't', '4', 'y', '5',
                    'u', 'i', '6', 'o', '7', 'p', '[', '8', ']', '9', '\\', '0', '-', '=']
    
    if not (36 <= note <= 96):
        return '', ''
    
    if 36 <= note <= 59:
        change_G = piano_G[0]
        baseline = 36
    elif 60 <= note <= 83:
        change_G = piano_G[1]
        baseline = 60
    else:
        change_G = piano_G[2]
        baseline = 84
    return change_G, piano_keymap[note-baseline]

if args.path:
    midifile = args.path
else:
    midifile = easygui.fileopenbox(title='Select MIDI File', filetypes=["*.mid"])
    if midifile is None:
        print(f"{Fore.RED}No MIDI file selected. Exiting...{Style.RESET_ALL}")
        quit()

print(f"{Fore.GREEN}Playing: {midifile}{Style.RESET_ALL}")

midi = mido.MidiFile(midifile)
print(f"{Fore.YELLOW}MIDI File parsed.{Style.RESET_ALL}")
time.sleep(2)

curr_pitch = 'f2'
pyautogui.press(curr_pitch)
pyautogui.PAUSE = 0

for msg in midi.play():
    if msg.type == 'note_on' and msg.velocity != 0:
        pitch, key = map_piano_note_to_key(msg.note + args.pt_mod)
        if curr_pitch != pitch:
            pyautogui.press(pitch)
            curr_pitch = pitch
        pyautogui.press(key)

print(f"{Fore.GREEN}Playback completed.{Style.RESET_ALL}")
