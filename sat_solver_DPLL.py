import time

start = time.time()

lista_clauze = []
pasi = 0

def intro():
    print("=== Sat Solver ===")
    print("format exemplu: [1,2] [3,4] [-1,-4]")
    print("==================")

with open('input.txt','r') as f:
    clauze_input = f.read()

def citeste_clauze():
    global clauze_input, lista_clauze
    clauze_input = clauze_input.strip().split(" ")
    lista_clauze = []

    for clauza in clauze_input:
        if clauza:
            clauza = clauza.replace("[", "").replace("]", "")
            valori = list(map(int, clauza.split(",")))
            lista_clauze.append(valori)


def simplifica(clauze, literal):
    nou = []
    for clauza in clauze:
        if literal in clauza:
            continue
        noua_clauza = [l for l in clauza if l != -literal]
        nou.append(noua_clauza)
    return nou


def dpll(clauze, asignari={}):
    global pasi
    pasi += 1

    # 1. elimina clauzele goale
    if not clauze:
        return True, asignari

    # 2. daca exista o clauza goala, rezultatul este unsat
    if [] in clauze:
        return False, {}

    # 3. clauze unitare
    unitari = [c[0] for c in clauze if len(c) == 1]
    if unitari:
        for literal in unitari:
            clauze = simplifica(clauze, literal)
            asignari[abs(literal)] = literal > 0
        return dpll(clauze, asignari)

    # 4. literali puri
    toti_literalii = [literal for clauza in clauze for literal in clauza]
    puri = [l for l in set(toti_literalii) if -l not in toti_literalii]
    if puri:
        for literal in puri:
            clauze = simplifica(clauze, literal)
            asignari[abs(literal)] = literal > 0
        return dpll(clauze, asignari)

    # 5. alegeri si backtracking
    literal = clauze[0][0]
    new_clauze_true = simplifica(clauze, literal)
    sat_true, asignari_true = dpll(new_clauze_true, {**asignari, abs(literal): literal > 0})
    if sat_true:
        return True, asignari_true

    new_clauze_false = simplifica(clauze, -literal)
    sat_false, asignari_false = dpll(new_clauze_false, {**asignari, abs(literal): literal < 0})
    return sat_false, asignari_false


def main():
    intro()
    citeste_clauze()
    satisfiabil, asignari = dpll(lista_clauze)

    if satisfiabil:
        print("rezultat: sat")
        print("atribuiri:", asignari)
    else:
        print("rezultat: unsat")

    end = time.time()
    print("============================================")
    print(f"Timp de executie: {end - start:.4f} s")
    print(f"Numar de pasi: {pasi}")
    print("============================================")





if __name__ == "__main__":
    main()