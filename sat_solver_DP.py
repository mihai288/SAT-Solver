import time

start = time.time()

lista_clauze = []
pasi = 0

def intro():
    print("format exemplu: [1,2] [3,4] [-1,-4]")
    print("=== Sat Solver ===")

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

def rezolutie(clauza1, clauza2):
    global pasi
    pasi += 1

    for literal in clauza1:
        negatie = -literal
        if negatie in clauza2:

            noua_clauza = []

            for lit in clauza1:
                if lit != literal:
                    noua_clauza.append(lit)

            for lit in clauza2:
                if lit != negatie and lit not in noua_clauza:
                    noua_clauza.append(lit)

            noua_clauza.sort()
            return noua_clauza

    return None


def dp(clauze):
    # eliminam duplicatele din fiecare clauza
    clauze = [sorted(list(set(clauza))) for clauza in clauze]

    clauze_existente = set(tuple(clauza) for clauza in clauze)

    while True:
        rezolutii_generate = []

        # aplicam rezolutia pe fiecare pereche de clauze
        for i in range(len(clauze)):
            for j in range(i + 1, len(clauze)):
                clauza_rezolvata = rezolutie(clauze[i], clauze[j])

                if clauza_rezolvata is not None:
                    if clauza_rezolvata == []:
                        return False

                    # adaugam clauzele noi care nu sunt in set
                    clauza_tuplu = tuple(clauza_rezolvata)
                    if clauza_tuplu not in clauze_existente:
                        rezolutii_generate.append(clauza_rezolvata)
                        clauze_existente.add(clauza_tuplu)

        # daca nu s-au generat clauze noi, nu mai continuam
        if not rezolutii_generate:
            break

        # adaugam noile clauze in lista principala
        clauze.extend(rezolutii_generate)

    # daca nu s-a generat clauza vida -> sat
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
