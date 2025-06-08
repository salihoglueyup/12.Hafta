import socket


def main():
    # Server bilgileri
    server_ip = "127.0.0.1"
    server_port = 8880

    # TCP socket oluştur
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Sunucuya bağlan
        client_socket.connect((server_ip, server_port))
        print(f"Sunucuya bağlanıldı: {server_ip}:{server_port}")

        # Mesaj gönder
        message = "Why don't you call me any more?"
        client_socket.send(message.encode('utf-8'))
        print(f"Gönderilen mesaj: {message}")

        # Cevap al
        response = client_socket.recv(1024)
        response_message = response.decode('utf-8')
        print(f"Sunucudan gelen cevap: {response_message}")

    except ConnectionRefusedError:
        print("Hata: Sunucuya bağlanılamadı. Sunucu çalışıyor mu?")
    except Exception as e:
        print(f"Hata oluştu: {e}")
    finally:
        client_socket.close()
        print("Bağlantı kapatıldı.")


if __name__ == "__main__":
    main()