import random



def generalt():
    random_szam = random.randint(1, 50)
    oszthato(random_szam)
    return random_szam

def oszthato(random_szam):
    if random_szam / 5 == 0:
        print("A szám öttel osztható")
    elif random_szam / 3 == 0:
        print("A szám hárommal osztható")
    elif random_szam / 5 == 0 and random_szam / 3 == 0:
        print("A szám öttel és hárommal is osztható")
    else:
        print("A szám se öttel se hárommal nem osztható")
    return random_szam





