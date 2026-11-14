
# Sistema de agendamento de quadras de vôlei/futevôlei

nome_cliente = ""
modalidade = ""
data_reserva = ""
horario_reserva = ""

reserva_cadastrada = False
opcao = ""

while opcao != "5":

    print("\n===== AGENDAMENTO DE QUADRAS =====")
    print("1 - Cadastrar reserva")
    print("2 - Consultar reserva")
    print("3 - Atualizar reserva")
    print("4 - Cancelar reserva")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        if reserva_cadastrada == False:

            print("\nEscolha a modalidade:")
            print("1 - Vôlei")
            print("2 - Futevôlei")

            modalidade_digitada = input("Opção: ")

            if modalidade_digitada == "1":
                modalidade = "Vôlei"

            elif modalidade_digitada == "2":
                modalidade = "Futevôlei"

            else:
                modalidade = ""

            if modalidade != "":

                nome_cliente = input("Nome do cliente: ")
                data_reserva = input("Data da reserva: ")
                horario_reserva = input("Horário da reserva: ")

                reserva_cadastrada = True

                print("\nReserva cadastrada com sucesso!")

            else:
                print("Modalidade inválida. Cadastro não realizado.")

        else:
            print("Já existe uma reserva cadastrada.")

    elif opcao == "2":

        if reserva_cadastrada == True:

            print("\n===== DADOS DA RESERVA =====")
            print("Nome do cliente:", nome_cliente)
            print("Modalidade:", modalidade)
            print("Data da reserva:", data_reserva)
            print("Horário da reserva:", horario_reserva)

        else:
            print("Nenhuma reserva cadastrada.")

    elif opcao == "3":

        if reserva_cadastrada == True:

            print("\n===== ATUALIZAR RESERVA =====")
            print("1 - Alterar nome do cliente")
            print("2 - Alterar modalidade")
            print("3 - Alterar data")
            print("4 - Alterar horário")

            campo = input("O que deseja atualizar? ")

            if campo == "1":
                nome_cliente = input("Novo nome do cliente: ")
                print("Nome atualizado com sucesso!")

            elif campo == "2":

                print("\nEscolha a nova modalidade:")
                print("1 - Vôlei")
                print("2 - Futevôlei")

                modalidade_digitada = input("Opção: ")

                if modalidade_digitada == "1":
                    modalidade = "Vôlei"
                    print("Modalidade atualizada com sucesso!")

                elif modalidade_digitada == "2":
                    modalidade = "Futevôlei"
                    print("Modalidade atualizada com sucesso!")

                else:
                    print("Modalidade inválida. Nenhuma alteração realizada.")

            elif campo == "3":
                data_reserva = input("Nova data da reserva: ")
                print("Data atualizada com sucesso!")

            elif campo == "4":
                horario_reserva = input("Novo horário da reserva: ")
                print("Horário atualizado com sucesso!")

            else:
                print("Opção de atualização inválida.")

        else:
            print("Não existe reserva para atualizar.")

    elif opcao == "4":

        if reserva_cadastrada == True:

            nome_cliente = ""
            modalidade = ""
            data_reserva = ""
            horario_reserva = ""

            reserva_cadastrada = False

            print("Reserva cancelada com sucesso!")

        else:
            print("Não existe reserva para cancelar.")

    elif opcao == "5":
        print("Sistema encerrado.")

    else:
        print("Opção inválida. Escolha de 1 a 5.")
