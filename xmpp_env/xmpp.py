import xmpp

jabberid = "admin@localhost"
password = "admin"
receiver = "amigoteste@localhost"
message  = "hello world"

def main():
    jid = xmpp.protocol.JID(jabberid)
    connection = xmpp.Client(server=jid.getDomain(), debug=True)
    connection.connect()
    connection.auth(user=jid.getNode(), password=password, resource=jid.getResource())
    connection.send(xmpp.protocol.Message(to=receiver, body=message))

if __name__ == "__main__":
    main()