import socket


def main():
    # Server bilgileri
    server_ip = "127.0.0.1"
    server_port = 20001
    buffer_size = 1024

    # Kullanıcı girişi
    username = input('Kullanıcı adınızı girin: ')
    password = input('Şifrenizi girin: ')

    # UDP socket oluştur
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # Username'i encode et ve gönder
        username_bytes = username.encode('utf-8')
        client_socket.sendto(username_bytes, (server_ip, server_port))

        # Password'u encode et ve gönder
        password_bytes = password.encode('utf-8')
        client_socket.sendto(password_bytes, (server_ip, server_port))

        # Sunucudan cevap al
        response, server_address = client_socket.recvfrom(buffer_size)
        response_message = response.decode('utf-8')

        print(f"Sunucudan gelen cevap: {response_message}")

    except Exception as e:
        print(f"Hata oluştu: {e}")

    finally:
        client_socket.close()
        print("Bağlantı kapatıldı.")


if __name__ == "__main__":
    main()