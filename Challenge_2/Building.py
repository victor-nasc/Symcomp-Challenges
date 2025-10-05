from dataclasses import dataclass, field
import pandas as pd
from random import randint, seed
import argparse

class Dataset:
    def __init__(self, codenameFile):
        seed(2025)
        with open(codenameFile, 'r') as f:
            self.codename = [line.strip() for line in f if line.strip()]

        month = ['jan', 'fev', 'mar', 'abr',
                 'mai', 'jun', 'jul', 'ago',
                 'set', 'out', 'nov', 'dez'
                 ]
        year = ['2009', '2010', '2011', '2012',
                '2013', '2014', '2015', '2016',
                '2017', '2018', '2019', '2020',
                '2021', '2022', '2023', '2024',
                '2025'
                ]

        n = 15_000_000

        data = []
        while len(data) < n:
            m = randint(1, 12)
            y = randint(0, len(year) - 1)

            u = randint(0, len(self.codename) - 1)
            acc = randint(1, 20)

            key = pd.Period(f'{year[y]}-{m}', freq='M')
            
            data.append([key, self.codename[u], acc])

        self.df = pd.DataFrame(data, columns=['data-acesso', 'quem-acessou', 'quantidade-de-acessos'])

    def GetOutput(self):
        self.df.to_csv('enigma2.csv', sep=';', index=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('textFile')

    args = parser.parse_args()
    fileName = args.textFile

    ds = Dataset(fileName)
    ds.GetOutput()