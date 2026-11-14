
# Sistema de agendamento de quadras de vôlei/futevôlei

# Lista para armazenar os agendamentos
agendamentos = []

# Identificador do próximo agendamento
proximo_id = 1

opcao = ""

while opcao != "5":

    print("\n===== AGENDAMENTO DE QUADRAS =====")
    print("1 - Cadastrar reserva")
    print("2 - Consultar reservas")
    print("3 - Atualizar reserva")
    print("4 - Cancelar reserva")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    # CADASTRAR RESERVA
    if opcao == "1":

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

            agendamento = {
                "id": proximo_id,
                "nome_cliente": nome_cliente,
                "modalidade": modalidade,
                "data_reserva": data_reserva,
                "horario_reserva": horario_reserva
            }

            agendamentos.append(agendamento)

            proximo_id += 1

            print("\nReserva cadastrada com sucesso!")

        else:
            print("Modalidade inválida. Cadastro não realizado.")

    # CONSULTAR RESERVAS
    elif opcao == "2":

        if len(agendamentos) > 0:

            print("\n===== AGENDAMENTOS CADASTRADOS =====")

            for agendamento in agendamentos:

                print("\nID:", agendamento["id"])
                print("Nome do cliente:", agendamento["nome_cliente"])
                print("Modalidade:", agendamento["modalidade"])
                print("Data da reserva:", agendamento["data_reserva"])
                print("Horário da reserva:", agendamento["horario_reserva"])

        else:
            print("Nenhuma reserva cadastrada.")

    # ATUALIZAR RESERVA
    elif opcao == "3":

        if len(agendamentos) > 0:

            print("\n===== AGENDAMENTOS CADASTRADOS =====")

            for agendamento in agendamentos:
                print("ID:", agendamento["id"], "- Cliente:", agendamento["nome_cliente"])

            id_busca = input("\nDigite o ID da reserva que deseja atualizar: ")

            reserva_encontrada = False

            for agendamento in agendamentos:

                if str(agendamento["id"]) == id_busca:

                    reserva_encontrada = True

                    print("\n===== ATUALIZAR RESERVA =====")
                    print("1 - Alterar nome do cliente")
                    print("2 - Alterar modalidade")
                    print("3 - Alterar data")
                    print("4 - Alterar horário")

                    campo = input("O que deseja atualizar? ")

                    if campo == "1":

                        agendamento["nome_cliente"] = input("Novo nome do cliente: ")
                        print("Nome atualizado com sucesso!")

                    elif campo == "2":

                        print("\nEscolha a nova modalidade:")
                        print("1 - Vôlei")
                        print("2 - Futevôlei")

                        modalidade_digitada = input("Opção: ")

                        if modalidade_digitada == "1":
                            agendamento["modalidade"] = "Vôlei"
                            print("Modalidade atualizada com sucesso!")

                        elif modalidade_digitada == "2":
                            agendamento["modalidade"] = "Futevôlei"
                            print("Modalidade atualizada com sucesso!")

                        else:
                            print("Modalidade inválida. Nenhuma alteração realizada.")

                    elif campo == "3":

                        agendamento["data_reserva"] = input("Nova data da reserva: ")
                        print("Data atualizada com sucesso!")

                    elif campo == "4":

                        agendamento["horario_reserva"] = input("Novo horário da reserva: ")
                        print("Horário atualizado com sucesso!")

                    else:
                        print("Opção de atualização inválida.")

                    break

            if reserva_encontrada == False:
                print("Reserva não encontrada.")

        else:
            print("Não existe reserva para atualizar.")

    # CANCELAR RESERVA
    elif opcao == "4":

        if len(agendamentos) > 0:

            print("\n===== AGENDAMENTOS CADASTRADOS =====")

            for agendamento in agendamentos:
                print("ID:", agendamento["id"], "- Cliente:", agendamento["nome_cliente"])

            id_busca = input("\nDigite o ID da reserva que deseja cancelar: ")

            reserva_encontrada = False

            for agendamento in agendamentos:

                if str(agendamento["id"]) == id_busca:

                    agendamentos.remove(agendamento)

                    reserva_encontrada = True

                    print("Reserva cancelada com sucesso!")

                    break

            if reserva_encontrada == False:
                print("Reserva não encontrada.")

        else:
            print("Não existe reserva para cancelar.")

    elif opcao == "5":
        print("Sistema encerrado.")

    else:
        print("Opção inválida. Escolha de 1 a 5.")
