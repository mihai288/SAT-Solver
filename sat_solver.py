lista_clauze = []
def intro():
    print("=== Sat Solver ===")
    print("format exemplu: [1,2] [3,4] [-1,-4]")
    print("==================")

with open('input.txt','r') as f:
    clauze_input = f.read()


lista_clauze = []

def citeste_clauze():
    global clauze_input, lista_clauze
    lista_clauze = clauze_input.split(" ")


def elimina_paranteze(clauza1, clauza2):
    clauza1[0] = str(clauza1[0]).replace('[', '')
    clauza1[len(clauza1) - 1] = str(clauza1[len(clauza1) - 1]).replace(']', '')

    clauza2[0] = str(clauza2[0]).replace('[', '')
    clauza2[len(clauza2) - 1] = str(clauza2[len(clauza2) - 1]).replace(']', '')

    return clauza1, clauza2


def rezolutie(a,b):


    # definim 2 clauze si luam elementele din lista principala
    clauza1_str = a.split(',')
    clauza2_str = b.split(',')

    # scoatem parantezele patrate din clauze pentru manipularea mai usoara
    elimina_paranteze(clauza1_str, clauza2_str)

    clauza1 = list(map(int, clauza1_str))
    clauza2 = list(map(int, clauza2_str))
    clauza_finala = []



    # verificam daca un literal din a este gasit negativ in b, si invers
    found = 0
    for l1 in clauza1:
        if l1* -1 not in clauza2:
            clauza_finala.append(l1)

        if l1* -1 in clauza2:
            found = 1

    for l2 in clauza2:
        if l2* -1 not in clauza1:
            clauza_finala.append(l2)

    if found == 1:
        return clauza_finala
    else :
        return 0


def DP(lista):
    while True:
        rezolutie_realizata = False
        for i in range(len(lista)):
            for j in range(i + 1, len(lista)):
                # stocam lista finala intr-o variabila rezultat
                rezultat = rezolutie(str(lista[i]), str(lista[j]))

                if rezultat != 0:  # Dacă rezolutia a găsit un literal comun
                    # Înlocuim clauza i cu rezolutia
                    lista[i] = rezultat
                    # Eliminăm clauza j (pentru că deja am aplicat rezolutia)
                    lista.pop(j)
                    rezolutie_realizata = True
                    break  # Ieșim din bucla internă
            if rezolutie_realizata:
                break  # Ieșim din bucla externă dacă am făcut rezolutie

        # Dacă nu s-a făcut nicio rezolutie în ultima iterație, înseamnă că am terminat
        if not rezolutie_realizata:
            break

    return lista



def main():
    intro()
    citeste_clauze()

    DP(lista_clauze)

    if all(not sublista for sublista in lista_clauze):
        print("unsat")
    else:
        print("sat")

    print(lista_clauze)

    # de implementat: aplica rezolutia pe toate clauzele din lista_clauze, o ia pe prima si face rezolutia cu toate pana cand una nu returneaza 0
    # trece la a doua si tot asa


if __name__ == "__main__":
    main()
