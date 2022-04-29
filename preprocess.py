from itertools import islice
import pandas as pd
import numpy as np


def parse_eufa(file_path="data/data.txt"):
    data = list()
    with open(file_path, mode='r', encoding='utf-8') as f:
        skip_start_line = 3
        for line in islice(f, skip_start_line, None):
            fields = line.strip().split('\t')
            data.append(fields)

    return data


def parse_arc_data(result_file_path="data/archive/results.csv", shootout_file_path="data/archive/shootouts.csv"):
    data = list()

    with open(result_file_path, mode='r', encoding='utf-8') as f:
        skip_start_line = 39701
        for line in islice(f, skip_start_line, None):
            fields = line.strip().split(',')

            # Add winner
            if fields[3] > fields[4]:
                fields.append(fields[1])
            elif fields[3] < fields[4]:
                fields.append(fields[2])
            else:
                fields.append("None")

            data.append(fields)

    with open(shootout_file_path, mode='r', encoding='utf-8') as f:
        skip_start_line = 403
        for line in islice(f, skip_start_line, None):
            date, ctry1, ctry2, winner = line.strip().split(',')

            for i in range(0, len(data)):
                if data[i][-1] == "None" and date == data[i][0]:
                    if (ctry1 == data[i][1] and ctry2 == data[i][2]) or (ctry1 == data[i][2] and ctry2 == data[i][1]):
                            data[i].append(winner)
                    else:
                        continue

    return data




if __name__ == '__main__':
    print('Preprocessing starts...')
    eufa_record = parse_eufa()
    acr_record = parse_arc_data()


    print('Preprocessing ends')
