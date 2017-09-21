# create_dataset
This tool allows us to create a `dataset.json` file that can be used in `search_bench` from just a list of notes.

# To use
Inside this folder run:
```
python create_dataset.py RAW_NOTE_FILE DATASET_FILE
```
`RAW_NOTE_FILE` is the path to the file containing a list of notes.
Each line is interpreted as a different note. Please put these notes in `/raw_notes` folder.

`DATASET_FILE` is the path to where you want the formatted .json file to be stored.
Generally we want to put them in the `/formatted_datasets` folder.

Example run:
```
python create_dataset.py raw_notes/manual_notes.txt formatted_datasets/our_dataset.json
```

# Other integrations
The output of this program, the `dataset.json` file, can be passed to the
`convert-notes` tool inside the real aurora repo at `scripts/convert-notes`.
This will essentially load the notes in the json file into your aurora app.
Check it out. It's pretty cool.
