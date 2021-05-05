

def console(server):
    while server.running:
        com = input(">>")
        if com == "exit":
            server.exit()

