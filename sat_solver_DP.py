import time

start = time.time()

lista_clauze = []
pasi = 0

def intro():
    print("=== Sat Solver ===")
    print("format exemplu: [1,2] [3,4] [-1,-4]")
    print("==================")

with open('input.txt', 'r') as f:
    clauze_input = f.read()

def citeste_clauze():
    global clauze_input, lista_clauze
    clauze_input = clauze_input.strip().split(" ")
    lista_clauze = []

    for clauza in clauze_input:
        if clauza:
            clauza = clauza.replace("[", "").replace("]", "")
            valori = list(map(int, clauza.split(",")))
            lista_clauze.append(sorted(list(set(valori))))

def rezolutie(cl1, cl2):
    global pasi
    pasi += 1
    for l in cl1:
        if -l in cl2:
            noua = list(set([x for x in cl1 if x != l] + [x for x in cl2 if x != -l]))
            return sorted(noua)
    return None

def dp(clauze):
    clauze = [sorted(list(set(c))) for c in clauze]
    clauze_set = set(tuple(c) for c in clauze)

    while True:
        rezolutii_noi = []
        for i in range(len(clauze)):
            for j in range(i + 1, len(clauze)):
                noua = rezolutie(clauze[i], clauze[j])
                if noua is not None:
                    if noua == []:
                        return False
                    t = tuple(noua)
                    if t not in clauze_set:
                        rezolutii_noi.append(noua)
                        clauze_set.add(t)
        if not rezolutii_noi:
            break
        clauze.extend(rezolutii_noi)

    return True

def main():
    intro()
    citeste_clauze()
    satisfiabil = dp(lista_clauze)

    if satisfiabil:
        print("rezultat: sat")
    else:
        print("rezultat: unsat")

    end = time.time()
    print("============================================")
    print(f"Timp de executie: {end - start:.4f} s")
    print(f"Numar de pasi: {pasi}")
    print("============================================")

if __name__ == "__main__":
    main()
