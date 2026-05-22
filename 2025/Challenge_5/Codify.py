import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='Codify',
        description='Codify a string'
    )
    parser.add_argument('word', type=str, help='word to be codify')

    args = parser.parse_args()
    word = args.word
    word = word.lower()

    n = len(word)
    codigo = [0]*n 
    codigo[0] = ord(word[0]) - 96 + n

    for i in range(1, n):
        if(word[i] == word[i - 1]):
            codigo[i] = codigo[i - 1] + n # ASCII - a
        else:
            codigo[i] = codigo[i - 1] * n + n
    
    print(codigo)