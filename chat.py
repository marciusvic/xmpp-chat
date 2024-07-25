import xmpp
import threading

def message_callback(conn, msg):
    print(f"Mensagem recebida de {msg.getFrom()}: {msg.getBody()}")

def send_message(conn, recipient, message):
    msg = xmpp.Message(recipient, message)
    msg.setAttr('type', 'chat')
    conn.send(msg)

def listen_for_messages(client):
    while True:
        client.Process(1)

def main():
    jid = xmpp.protocol.JID('admin@localhost')
    password = 'password'

    client = xmpp.Client(jid.getDomain(), debug=[])
    connection = client.connect()
    if not connection:
        print("Falha ao conectar ao servidor")
        return

    auth = client.auth(jid.getNode(), password, resource=jid.getResource())
    if not auth:
        print("Falha ao autenticar")
        return

    client.RegisterHandler('message', message_callback)
    client.sendInitPresence()

    print("Conectado e autenticado com sucesso. Pronto para receber mensagens.")

    # Inicia uma thread para ouvir mensagens
    threading.Thread(target=listen_for_messages, args=(client,), daemon=True).start()

    while True:
        user_input = input("Digite a mensagem (ou 'sair' para encerrar): ")
        if user_input.lower() == 'sair':
            break
        send_message(client, 'outro_usuario@localhost', user_input)

if __name__ == '__main__':
    main()
