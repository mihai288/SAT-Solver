import time

start = time.time()

lista_clauze = []
pasi = 0

def intro():
    print("format exemplu: [1,2] [3,4] [-1,-4]")
    print("=== Sat Solver ===")


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
    clauze_actualizate = []

    for clauza in clauze:
        if literal in clauza:
            continue

        # eliminam negatia literalului
        clauza_noua = []
        for l in clauza:
            if l != -literal:
                clauza_noua.append(l)

        clauze_actualizate.append(clauza_noua)

    return clauze_actualizate



def dpll(clauze, asignari={}):
    global pasi
    pasi += 1

    # daca nu mai avem clauze -> sat
    if not clauze:
        return True, asignari

    # daca exista o clauza vida -> unsat
    if [] in clauze:
        return False, {}

    clauze_unitare = [clauza[0] for clauza in clauze if len(clauza) == 1]
    if clauze_unitare:
        for literal_unitar in clauze_unitare:
            clauze = simplifica(clauze, literal_unitar)
            asignari[abs(literal_unitar)] = literal_unitar > 0
        return dpll(clauze, asignari)

    # tratare literali puri
    toti_literalii = [literal for clauza in clauze for literal in clauza]
    literali_puri = []
    for literal in set(toti_literalii):
        if -literal not in toti_literalii:
            literali_puri.append(literal)

    if literali_puri:
        for literal_pur in literali_puri:
            clauze = simplifica(clauze, literal_pur)
            asignari[abs(literal_pur)] = literal_pur > 0
        # Apel recursiv după eliminarea literalilor puri
        return dpll(clauze, asignari)

    # alegeri si backtracking
    literal_de_incercat = clauze[0][0]

    # asignare true
    clauze_daca_true = simplifica(clauze, literal_de_incercat)
    asignari_true = {**asignari, abs(literal_de_incercat): literal_de_incercat > 0}
    satisfiabil_true, asignari_gasite_true = dpll(clauze_daca_true, asignari_true)

    if satisfiabil_true:
        return True, asignari_gasite_true

    # daca nu a mers asignarea cu true, incercam cu false
    clauze_daca_false = simplifica(clauze, -literal_de_incercat)
    asignari_false = {**asignari, abs(literal_de_incercat): literal_de_incercat < 0}
    satisfiabil_false, asignari_gasite_false = dpll(clauze_daca_false, asignari_false)

    return satisfiabil_false, asignari_gasite_false



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