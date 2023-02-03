def korok():
    elet_kor = []
    i = 0
    while i < 5:
        a = input("Adj meg egy számot [0,120] között")
        elet_kor.append(f"{a}:")
        i += 1
    print(elet_kor)
    elso_idos(elet_kor)


def elso_idos(elet_kor):
    i = 0
    idos = 0
    while i < len(elet_kor):
        if elet_kor[idos] >= 70:
            return elet_kor[idos]



