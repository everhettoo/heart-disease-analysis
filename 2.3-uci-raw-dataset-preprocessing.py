import os
import pandas as pd
import models.uci_heart_disease_dataset as uci

# The input and output file names for the 3 datasets.
datasets = [
        {
            'name': 'Long Beach',
            'input': 'data/uci-heart-disease/long-beach-va.data',
            'output': 'data/uci-heart-disease/recovered-va.data'
        },
        {
            'name': 'Hungarian',
            'input': 'data/uci-heart-disease/hungarian.data',
            'output': 'data/uci-heart-disease/recovered-hungarian.data'
        },
        {
            'name': 'Switzerland',
            'input': 'data/uci-heart-disease/switzerland.data',
            'output': 'data/uci-heart-disease/recovered-switzerland.data'
        }
]

# Temp file for processing in the current directory.
temp_file = 'tmp.data'

"""
Summary: Function to read all lines from source file, chop them into chunks using the 'name' as 
the delimiter and write the transformed lines into a new file.

Parameters:
dataset_name: String value for display.
input_path: The source file path to read content.
output_path: The target file path to write transformed lines to.
"""
def recover_dataset(dataset_name, input_path, output_path):
    print(f'processing {dataset_name} dataset ...')
    with open(input_path, 'r') as file:
        file_content = file.read()

    # From observation, 'name' is the last variable that be used for chopping chunks.
    lines = file_content.replace('\n', ' ').split('name')
    # Remove the last empty line.
    lines.pop()

    new_lines = []
    for line in lines:
        if line[0] == ' ':
            line = line[1:]
        # Replacing empty space into ',' for creating CSV file.
        new_line = line.replace(' ', ',')
        new_lines.append(new_line)

    # Delete if file exist before writing a new one.
    if os.path.exists(temp_file):
        os.remove(temp_file)

    # Write temporary data.
    with open(temp_file, 'w') as f:
        # Write all transformed lines into the temp file first.
        for line in new_lines:
            f.write(line + '\n')

    # Read the CSV file with original headers (76 features) into data frame.
    df = pd.read_csv(temp_file, names=uci.get_original_features())

    # Write the CSV file.
    df.to_csv(output_path, index=False)
    print(f'The recovered {dataset_name} has the following {df.shape} shape')

for dataset in datasets:
    # Process to recover each dataset.
    recover_dataset(dataset['name'],dataset['input'],dataset['output'])

