"""
Запуск socket сервера и прослушивание порта для подключения
"""
import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 8000         # Port to listen on (non-privileged ports are > 1023)

if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create TCP server
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    connection, client_address = server_socket.accept()
    print(f'Получен запрос на подключение от {client_address}')
