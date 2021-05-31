def exit_serv(server):
    actif = False
    print("Fin de la console.")
    server.exit()


def aff_ennemis(server):
    pass


def console(server):
    server.nb_t_actifs += 1
    actif = True
    while server.running and actif:
        com = input(">>")
        if com == "exit":
            exit_serv(server)

    # Fin du thread
    server.nb_t_actifs -= 1
