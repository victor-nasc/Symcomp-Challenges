import networkx as nx
import argparse
import pandas as pd
import random
    
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

    # Insert Vertex

    unique = df['personLabel'].unique()
    dictUnique = {}
    indexUnique = [0]
    index = 0

    for u in unique:
        if u and u not in dictUnique:
            index += 1
            dictUnique[u] = index
            indexUnique.append(u)
    
    seed = 15
    G = nx.fast_gnp_random_graph(index, 0.5, seed)

    with open("challenge_4.csv", "w+") as f:
        for (u, v, w) in G.edges(data=True):
            w['weight'] = random.randint(1, 100)
            f.write(f"{indexUnique[u + 1]},{indexUnique[v + 1]},{w['weight']},\n")