import socket

PORT = 5000
BUFFER = 4096

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("0.0.0.0", PORT))
print(f"🔁 Relay Server çalışıyor... Port: {PORT}")

clients = []

while True:
    try:
        data, addr = server.recvfrom(BUFFER)

        if addr not in clients:
            clients.append(addr)
            print(f"📥 Yeni kullanıcı: {addr}")

        for client in clients:
            if client != addr:
                server.sendto(data, client)

    except Exception as e:
        print(f"❌ Relay server hatası: {e}")
