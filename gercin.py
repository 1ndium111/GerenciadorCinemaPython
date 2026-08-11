fila0 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
fila1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
fila2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
fila3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
fila4 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
fila5 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
fila6 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
fila7 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
fila8 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
fila9 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

teatro = [fila0, fila1, fila2, fila3, fila4, fila5, fila6, fila7, fila8, fila9]
repetir = str('s')
def mostrar_teatro():
    print("")
    print("           --------- ASSENTOS ---------")
    for x in range(10):
        print(f"Fila - {x} - {teatro[x][0]}, {teatro[x][1]}, {teatro[x][2]}, {teatro[x][3]}, {teatro[x][4]}, {teatro[x][5]}, {teatro[x][6]}, {teatro[x][7]}, {teatro[x][8]}, {teatro[x][9]}")
    print("           ----------------------------")

def reservar():
    fila = int(input("Qual a fila desejada?: "))
    assento = int(input("Qual o assento desejado?: "))

    reserva = teatro[fila][assento]
            
    if reserva == 0:
        teatro[fila][assento] = 1
        print("Lugar reservado com sucesso!")
    else:
        print("Esse lugar já está ocupado!")

    mostrar_teatro()

def cancelar():
    fila = int(input("Qual a fila do assento que deseja cancelar?: "))
    assento = int(input("Qual o assento que deseja cancelar?: "))

    reserva = teatro[fila][assento]

    if reserva == 1:
        teatro[fila][assento] = 0
        mostrar_teatro()
        print("Lugar cancelado com sucesso!")
    else:
        print("Lugar já está cancelado/está vazio!")
            

while repetir == 's':

    print("=================================")
    print("----- GERENCIADOR DE CINEMA -----")
    print("=================================")
    print("")
    print("1- Mostrar Cinema")
    print("2- Reservar Lugares")
    print("3- Cancelar Reservas")
    print("4- Sair do programa")
    print("")
    opcao = int(input("Escolha uma opção: "))
    match (opcao):
        case 1:
            mostrar_teatro()
        case 2:
            mostrar_teatro()
            print("")
            reservar()
            repetir = input("Gostaria de ir de volta ao menu? (s/n): ")

            if repetir == 's':
                continue
            else:
                break
    
        case 3:
            mostrar_teatro()
            print("")
            cancelar()
            repetir = input("Gostaria de ir de volta ao menu? (s/n): ")
            if repetir == 's':
                continue
            else:
                break
        
        case 4:
            print("Terminando o programa...")
            break

        case _:
            print("Opção Inválida!")

