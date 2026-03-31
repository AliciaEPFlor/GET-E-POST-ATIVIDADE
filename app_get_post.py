from http.server import HTTPServer,BaseHTTPRequestHandler

class Servidor(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Servidor WEB funcionando! Bem vindo!")
    
    def do_POST(self):
        tamanho = int(self.headers['Content-Length'])
        dados = self.rfile.read(tamanho)
        print("Dados recebidos!", dados.decode())

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"POST recebido!")
        self.wfile.write(b"User registrado")

HTTPServer (("0.0.0.0", 8000), Servidor).serve_forever() 

#Esse código cria um servidor local para rodar HTTP, GET E POST