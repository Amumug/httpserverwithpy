import socket

# Define server address and port 
HOST, PORT = "", 8000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)
print(f"Listening on port {PORT}")


while True: 
  client_connection, client_address = server_socket.accept()
  request_data = client_connection.recv(1024)
  print(request_data.decode("utf-8"))

  
  with open("server.html", "r", encoding="utf-8") as f:
    response_body = f.read()
  
  # Make sure Content-Length is correctly calculated
  content_length = len(response_body.encode("utf-8"))
  
  http_response = (
  "HTTP/1.1 200 OK"
  "Content-Type: text/html; charset=UTF-8"
  "Content-Length: (len(response_body))\r\n"
  "\r\n"
  f"{response_body}"
  )
  client_connection.sendall(http_response.encode("utf-8"))
  client_connection.close()
