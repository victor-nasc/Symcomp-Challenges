from dataclasses import dataclass, field
from typing import (
    IO,
    TextIO,
    BinaryIO
)
import argparse

@dataclass
class Encrypt:
    file: str
    encrypt: bytearray = field(default_factory=bytearray)
    decrypt: bytearray = field(default_factory=bytearray)

    def xor_encript(self, key: list):
        self.encrypt = bytearray()

        with open(self.file, "rb") as f:
            data = f.read()

            for i, byte in enumerate(data):
                self.encrypt.append(byte ^ key[i % len(key)])

    def xor_decript(self, key: list):
        self.decrypt = bytearray()

        for i, byte in enumerate(self.encrypt):
            self.decrypt.append(byte ^ key[i % len(key)])

    def print_hex(self):
        return ' '.join(f"{byte:02X}" for byte in self.encrypt)

def xor_decript(file : str, key : list): 
    decrypt = bytearray() 

    with open(file) as f: 
        text = f.read() 
        for i, char in enumerate(text.split(" ")): 
            decrypt.append(int(char, 16) ^ key[i % len(key)]) 
    
    return decrypt

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('textFile')
    parser.add_argument('hex')

    args = parser.parse_args()

    fileName = args.textFile
    hexString = args.hex

    key = [int(hexString[i:i+2], 16) for i in range(0, 6, 2)]

    
    #enc = Encrypt(fileName)
    #enc.xor_encript(key)
    #print(enc.print_hex())
    
    print(xor_decript(fileName, key))

if __name__ == "__main__":
    main()