import requests

Animals = []

def getAnimals():
    n = 100
    while(len(Animals) < n):
        r = requests.get("https://random-animal-api.vercel.app/api/random-animal")
        a = r.json()
        if a["city"] not in Animals:
            Animals.append(a["city"])
    
    return Animals

def main():
    animals = getAnimals()
    
    with open("saida.txt", "w+") as f:
        f.write('\n'.join([a for a in animals]))

if __name__ == '__main__':
    main()