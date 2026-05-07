from http.server import HTTPServer,BaseHTTPRequestHandler

class Servidor(BaseHTTPRequestHandler):
    
    def do_POST(self):
     self.send_response(200)
     self.end_headers()
     self.wfile.write(b"POST RECEBIDO")

# Método POST (novo)
def do_POST(self):
   
   tamanho = int(self.headers['Content-Lenght'])

   dados = self.rfile.read(tamanho)

   print("Dados recebidos:", dados.decode())

   self.send_response(200)
   self.end_headers()
   self.wfile.write(b"Post recebido")
       
