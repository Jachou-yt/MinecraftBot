from python_aternos import Client


def start(username, password, server_id):
    aternos = Client.from_credentials(username, password)
    servs = aternos.list_servers()
    target_serv = servs[server_id]
    target_serv.start()


def stop(username, password, server_id):
    aternos = Client.from_credentials(username, password)
    servs = aternos.list_servers()
    target_serv = servs[server_id]
    target_serv.stop()


def restart(username, password, server_id):
    aternos = Client.from_credentials(username, password)
    servs = aternos.list_servers()
    target_serv = servs[server_id]
    target_serv.restart()
