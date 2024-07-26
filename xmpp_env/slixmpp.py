import slixmpp
import logging

# Configura o logging para depuração
logging.basicConfig(level=logging.DEBUG)

class SendMsgBot(slixmpp.ClientXMPP):
    def __init__(self, jid, password, recipient, message):
        super().__init__(jid, password)
        self.recipient = recipient
        self.message = message

        self.add_event_handler("session_start", self.start)
        self.add_event_handler("failed_auth", self.failed_auth)

    async def start(self, event):
        print("Session started.")
        self.send_presence()
        await self.get_roster()
        self.send_message(mto=self.recipient, mbody=self.message, mtype='chat')
        self.disconnect()

    def failed_auth(self, event):
        print("Authentication failed")
        self.disconnect()

if __name__ == '__main__':
    jid = "admin@localhost"
    password = "admin"
    recipient = "amigoteste@localhost"
    message = "hello world"

    xmpp = SendMsgBot(jid, password, recipient, message)
    xmpp.connect()
    xmpp.process(forever=False)