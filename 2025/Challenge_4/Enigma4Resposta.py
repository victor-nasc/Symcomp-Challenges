import networkx as nx
import argparse

if __name__ == '__main__':
    """
        Para esse desafio, precisamos do .csv base (challenge_4.csv)
        Do nó origem e do nó alvo
        (Dois nomes de computeiros importantes)
    """
    parser = argparse.ArgumentParser(
        prog='Enigma4Resposta',
        description='Reveal the solve for challenge 4'
    )

    parser.add_argument('csv', type=str, help='csv to take data')
    parser.add_argument('src', type=str)
    parser.add_argument('tgt', type=str)

    args = parser.parse_args()
    file = args.csv
    src = args.src
    tgt = args.tgt

    relGraph = nx.Graph()
    dictUnique = {}
    index = 0

    """
        Cada linha do arquivo contém src, tgt, weight
        Colocamos no networkx
    """
    with open(file) as f:
        for line in f:
            line = line.strip().split(sep=',')
            a = str(line[0])
            b = str(line[1])
            c = int(line[2])
            relGraph.add_edge(a, b, weight=c)
    
    """
        Aplicamos dijkstra
    """
    cost = nx.dijkstra_path_length(relGraph, src, tgt, weight='weight')
    print(cost)