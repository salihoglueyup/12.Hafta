import socket


def main():
    # Server ayarları
    local_ip = "127.0.0.1"
    local_port = 20001
    buffer_size = 1024

    # Kullanıcı veritabanı (normalde gerçek veritabanı olurdu)
    user_database = {
        '17BIT0382': 'vivek',
        '17BEC0647': 'shikhar',
        '17BEC0150': 'tanveer',
        '17BCE2119': 'sahil',
        '17BIT0123': 'sidhant'
    }

    # UDP socket oluştur ve bind et
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((local_ip, local_port))

    print(f"UDP Server başlatıldı - {local_ip}:{local_port}")
    print("Bağlantılar dinleniyor...")

    try:
        while True:
            # Username al
            username_bytes, client_address = server_socket.recvfrom(buffer_size)
            username = username_bytes.decode('utf-8')

            # Password al
            password_bytes, client_address = server_socket.recvfrom(buffer_size)
            password = password_bytes.decode('utf-8')

            print(f"Giriş denemesi - Kullanıcı: {username}, Adres: {client_address}")

            # Authentication kontrolü
            response_message = authenticate_user(username, password, user_database)

            # Cevabı encode et ve gönder
            response_bytes = response_message.encode('utf-8')
            server_socket.sendto(response_bytes, client_address)

            print(f"Cevap gönderildi: {response_message}")
            print("-" * 50)

    except KeyboardInterrupt:
        print("\nServer kapatılıyor...")
    except Exception as e:
        print(f"Hata oluştu: {e}")
    finally:
        server_socket.close()
        print("Server kapatıldı.")


def authenticate_user(username, password, database):
    """Kullanıcı doğrulama fonksiyonu"""
    if username not in database:
        return "HATA: Kullanıcı adı bulunamadı"

    if database[username] == password:
        return "BAŞARILI: Giriş yapıldı"
    else:
        return "HATA: Şifre yanlış"


if __name__ == "__main__":
    main()