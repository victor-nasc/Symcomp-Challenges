import networkx as nx
import argparse
import pandas as pd
    
def ThereNumber(value):
    for v in value:
        if ascii(v) >= 48 and ascii(v) <= 57:
            return True
    return False

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='Codify',
        description='Transform a graph'
    )
    parser.add_argument('csv', type=str, help='csv to take data')

    args = parser.parse_args()
    file = args.csv

    relGraph = nx.Graph()
    df = pd.read_csv(file, sep=',')

    print(df.head())

    # Insert Vertex

    unique = df['personLabel'].unique()
    dictUnique = {}
    index = 1

    for u in unique:
        if not ThereNumber(u) and u not in dictUnique:
            dictUnique[u] = index
            relGraph.add(index)
            index += 1
    
    unique = df['employerLabel'].unique()
    dictUnique = {}

    for u in unique:
        if u and u not in dictUnique:
            dictUnique[u] = index
            relGraph.add(index)
            index += 1