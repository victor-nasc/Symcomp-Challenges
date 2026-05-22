import os
import random
import string

def generate_random_content(length=100):
    """Gera letras aleatórias"""
    return ''.join(random.choices(string.ascii_letters + ' \n', k=length))

def create_structure(base_path, depth=6, max_folders=20, max_files=50):
    """Cria estrutura recursiva de pastas e arquivos"""
    if depth == 0:
        return
    
    # Criar arquivos na pasta atual
    num_files = random.randint(2, max_files)
    for i in range(num_files):
        file_path = os.path.join(base_path, f'arquivo_{i+1}.txt')
        with open(file_path, 'w') as f:
            f.write(generate_random_content())
    
    # Criar subpastas
    num_folders = random.randint(1, max_folders)
    for i in range(num_folders):
        folder_name = f'pasta_{i}'
        folder_path = os.path.join(base_path, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        
        # Recursão para criar estrutura nas subpastas
        create_structure(folder_path, depth - 1, max_folders, max_files)

if __name__ == '__main__':
    random.seed(15)
    base_dir = '/home/yukimi/USP/Symcomp-Challenges/Challenge_6'
    create_structure(base_dir, depth=6, max_folders=15, max_files=10)
    print('Estrutura criada com sucesso!')
