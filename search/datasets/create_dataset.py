import sys
import json

def getNotes(note_file):
    with open(note_file) as f:
        lines = f.read().splitlines()

        notes = []
        i = 1
        for line in lines:
            notes.append({
                "uuid" : i,
                "text" : str(line)
            })
            i = i+1
        return notes


note_file = sys.argv[1]
dataset_file = sys.argv[2]
notes = getNotes(note_file)

with open(dataset_file, 'w') as outfile:
    json.dump(notes, outfile, indent=2)
