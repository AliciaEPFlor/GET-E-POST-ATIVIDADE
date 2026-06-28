<!DOCTYPE html>
<html lang="pt-BR">
<body>
    <div class="container">
        <hr>
        <div align="justify">
            <h1>DESCRIÇÃO DO PROJETO</h1>
            <p>Servidor Backend, onde é possível realizar dois tipos de requisições em HTTP:</p>
            <ul>
                <li><strong>Método GET</strong> - Retorna a mensagem: "Servidor funcionando com GET"</li>
                <li><strong>Método POST</strong> - Processa dados enviados pelo cliente</li>
            </ul>
        </div>
        <hr>
        <div align="justify">
            <h2>MÉTODO GET</h2>
            <figure>
                <figcaption>
                    <img width="884" height="344" alt="Exemplo do método GET no Postman" src="https://github.com/user-attachments/assets/1ccf081d-538e-4fe2-8b11-63e6d959d802" />
                    <br>
                    <i>Método GET via POSTMAN - Resposta: "Servidor funcionando com GET"</i>
                </figcaption>
            </figure>
            <p><strong>Como testar:</strong> Abra o Postman, faça uma requisição GET para <code>http://localhost:8000</code> e veja a resposta do servidor.</p>
        </div>
    </div>
  
<h1>📌 O que está sendo feito neste código</h1>
  
        Este é um servidor HTTP básico em Python, criado para responder a requisições do tipo <strong>GET</strong>.
        A seguir está a explicação de cada parte do código.
        
<h2>📦 Linha 1: Importação dos módulos</h2>

    from http.server import HTTPServer, BaseHTTPRequestHandler

    Importa duas classes essenciais do módulo <code>http.server.

        HTTPServer: Cria e gerencia o servidor web (escuta em uma porta e aceita conexões).
        BaseHTTPRequestHandler: Classe base responsável por definir como tratar requisições HTTP.
        
<h2>🏗️ Linha 3: Definição da classe Servidor</h2>

    class Servidor(BaseHTTPRequestHandler):
 
        Cria uma classe chamada *Servidor*, que herda da classe
        BaseHTTPRequestHandler. Dessa forma, ela pode sobrescrever ou
        estender o comportamento padrão do manipulador de requisições HTTP.

<h2>🔧 Linhas 4–8: Método GET</h2>

def do_GET(self):
    self.send_response(200)
    self.end_headers()
    self.wfile.write(b"Servidor funcionando com GET")

<h3>Explicação:</h3>
       
    do_GET(self): Método chamado automaticamente quando o
        servidor recebe uma requisição HTTP do tipo *GET*.
       
    self.send_response(200): Envia o código de status
        HTTP 200 OK, indicando que a requisição foi realizada com sucesso.
   
    self.end_headers(): Finaliza o envio dos cabeçalhos da resposta HTTP.
       
    self.wfile.write(b"Servidor funcionando com GET"):
        Envia o conteúdo da resposta ao cliente.
          
    O prefixo *B* indica que a mensagem é enviada em formato de bytes.
        O navegador exibirá a mensagem: "Servidor funcionando com GET".

<h2>🎯 Resumo do funcionamento</h2>

    Este código realiza as seguintes funções:

       Cria um servidor HTTP simples utilizando Python.
       Fica aguardando conexões em uma porta definida.
       Quando recebe uma requisição do tipo *GET*.
       
                Retorna o código 200 (OK);
                Finaliza os cabeçalhos HTTP;
                Envia ao navegador a mensagem <strong>"Servidor funcionando com GET".
                
<div align = "justify">
<h2>MÉTODO POST</h2>
<figure>
  <figcaption>
  <img <img width="979" height="688" alt="image" src="https://github.com/user-attachments/assets/684df0a9-669e-4f54-bdf9-17ffab3303cf" />
  <i>Metodo POST via POSTMAN</i>
  </figcaption>
</figure>
<h1>📌 O que está sendo feito neste código</h1>
  
    <p>Este é um servidor HTTP básico em Python, criado para responder a requisições do tipo <strong>POST</strong>.
    A seguir está a explicação de cada parte do código.</p>
        
<h2>📦 Linha 1: Importação dos módulos</h2>

    from http.server import HTTPServer, BaseHTTPRequestHandle

    Importa duas classes essenciais do módulo <code>http.server:
   
        HTTPServer</strong>: Cria e gerencia o servidor web (escuta em uma porta e aceita conexões).
        BaseHTTPRequestHandler</strong>: Classe base responsável por definir como tratar requisições HTTP.
        
<h2>🏗️ Linha 3: Definição da classe Servidor</h2>

    class Servidor(BaseHTTPRequestHandler):

    Cria uma classe chamada Servidor, que herda da classe
    BaseHTTPRequestHandler. Dessa forma, ela pode sobrescrever ou
    estender o comportamento padrão do manipulador de requisições HTTP.

    <h2>🔧 Linhas 4–8: Método POST</h2>

    def do_POST(self):
        tamanho = int(self.headers['Content-Length'])
        dados = self.rfile.read(tamanho)
        print("Dados recebidos:", dados.decode())
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"POST recebido")

  <h3>Explicação:</h3>
 
        do_POST(self):</strong> Método chamado automaticamente quando o
            servidor recebe uma requisição HTTP do tipo POST
            
        tamanho = int(self.headers['Content-Length']):
            Obtém o cabeçalho Content-Length que informa quantos bytes foram
            enviados no corpo da requisição e converte para inteiro.
    
        dados = self.rfile.read(tamanho):
            Lê exatamente a quantidade de bytes especificada, capturando os dados enviados pelo cliente.
  
        print("Dados recebidos:", dados.decode()):
            Decodifica os bytes recebidos para string (formato UTF-8) e exibe no terminal do servidor
            os dados que o cliente enviou.
      
        self.send_response(200):
            Envia o código de status HTTP 200 OK, indicando que a requisição foi realizada com sucesso.

        self.end_headers():
            Finaliza o envio dos cabeçalhos da resposta HTTP.
  
        self.wfile.write(b"POST recebido"):
            Envia o conteúdo da resposta ao cliente. O prefixo <em>b</em> indica que a mensagem é enviada
            em formato de bytes. O cliente receberá a mensagem: "POST recebido".
      
  <h2>🎯 Resumo do funcionamento</h2>

    Este código realiza as seguintes funções:
 
        Cria um servidor HTTP simples utilizando Python.
        Fica aguardando conexões em uma porta definida.
        Quando recebe uma requisição do tipo <em>POST</em>:
            Lê o tamanho dos dados enviados;
            Captura os dados enviados pelo cliente;
            Exibe os dados no terminal do servidor;
            Retorna o código 200 (OK);
            Finaliza os cabeçalhos HTTP;
            Envia ao cliente a mensagem <strong>"POST recebido";
</body>
</html>
