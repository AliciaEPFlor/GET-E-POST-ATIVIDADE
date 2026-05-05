from http.server import HTTPServer,BaseHTTPRequestHandler

class Servidor(BaseHTTPRequestHandler):
    
    def do_POST(self):
        tamanho = int(self.headers['content-length'])
    dado = self.file.read(tamanho)
    print("Dados recebidos:  ", dado.decode())

    self.send_response(200)
    self.end_headers()
    self.wfile.write(b"POST RECEBIDO")

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Servidor WEB funcionando! Bem vindo!")

#Esse código cria um servidor local para rodar HTTP, GET E POST