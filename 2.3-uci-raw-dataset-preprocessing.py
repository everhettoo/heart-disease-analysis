import io
import os

import pandas as pd

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

headers = [
    'id',
    'ccf',
    'age',
    'sex',
    'painloc',
    'painexer',
    'relrest',
    'pncaden',
    'cp',
    'trestbps',
    'htn',
    'chol',
    'smoke',
    'cigs',
    'years',
    'fbs',
    'dm',
    'famhist',
    'restecg',
    'ekgmo',
    'ekgday',
    'ekgyr',
    'dig',
    'prop',
    'nitr',
    'pro',
    'diuretic',
    'proto',
    'thaldur',
    'thaltime',
    'met',
    'thalach',
    'thalrest',
    'tpeakbps',
    'tpeakbpd',
    'dummy',
    'trestbpd',
    'exang',
    'xhypo',
    'oldpeak',
    'slope',
    'rldv5',
    'rldv5e',
    'ca',
    'restckm',
    'exerckm',
    'restef',
    'restwm',
    'exeref',
    'exerwm',
    'thal',
    'thalsev',
    'thalpul',
    'earlobe',
    'cmo',
    'cday',
    'cyr',
    'num',
    'lmt',
    'ladprox',
    'laddist',
    'diag',
    'cxmain',
    'ramus',
    'om1',
    'om2',
    'rcaprox',
    'rcadist',
    'lvx1',
    'lvx2',
    'lvx3',
    'lvx4',
    'lvf',
    'cathef',
    'junk',
    'name'
]

temp_file = 'tmp.data'

def recover_dataset(dataset_name, input_path, output_path):
    print(f'processing {dataset_name} dataset ...')
    with open(input_path, 'r') as file:
        file_content = file.read()

    lines = file_content.replace('\n', ' ').split('name')
    # Remove the last empty line
    lines.pop()

    new_lines = []
    for line in lines:
        if line[0] == ' ':
            line = line[1:]
        new_line = line.replace(' ', ',')
        new_lines.append(new_line)

    if os.path.exists(temp_file):
        os.remove(temp_file)

    # Write temporary data.
    with open(temp_file, 'w') as f:
        for line in new_lines:
            f.write(line + '\n')

    df = pd.read_csv(temp_file, names=headers)

    # Write the CSV file.
    df.to_csv(output_path, index=False)
    print(f'The recovered {dataset_name} has the following {df.shape} shape')

for dataset in datasets:
    # Process to recover each dataset.
    recover_dataset(dataset['name'],dataset['input'],dataset['output'])

