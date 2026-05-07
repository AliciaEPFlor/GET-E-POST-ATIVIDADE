from flask import Flask

app = Flask (__name__)

@app.route('/')
def Home():
    return "Site de Sinopse de Anime"

@app.route('/OnePiece') #CamelCase 
# filme_do_dia = SnakeCase 
def serIe():
    return "One Piece, o tesouro supremo escondido por Gol D. Roger, para se tornar o Rei dos Piratas. A série foca em aventura, amizade e a luta por liberdade. Protagonista: Luffy, um jovem elástico após comer uma Akuma no Mi.A Jornada: A tripulação explora o mar Grand Line, enfrentando outros piratas e o Governo Mundial. Conflitos Principais: A luta contra a opressão de governantes e imperadores do mar, como Kaido e Big Mom, buscando a libertação de nações. Contexto Atual: A história avança para o arco final, envolvendo o cientista Vegapunk e a investigação sobre o Século Perdido. O Tesouro: Localizado na última ilha, Laugh Tale, o One Piece é o objetivo que motiva a busca. Atualmente, a série se encontra na saga final, com a tripulação explorando novos segredos do mundo de One Piece"

@app.route('/Gachakuta')
def serie():
    return "Gachiakuta acompanha Rudo, um jovem da periferia de uma cidade flutuante, falsamente acusado de assassinato e exilado no 'Abismo', um lixão infernal. Para sobreviver aos monstros de lixo e buscar vingança contra a elite, ele se junta aos Zeladores, usando o poder de 'Instrumentos Vitais' para lutar. Cenário: Uma sociedade desigual dividida entre uma cidade flutuante luxuosa e um imenso lixão abaixo (o Abismo/Poço). O protagonista: Rudo Surebrec, um órfão marginalizado que tem talento para restaurar objetos descartados. Conflito: Após ser acusado da morte de seu guardião, Rudo é atirado no abismo. Ação/Poderes: Rudo descobre a capacidade de dar vida a objetos (armas chamadas 'Instrumentos Vitais') e se une aos Zeladores, um grupo que combate feras criadas a partir do lixo. Temas: Segregação social, a valorização do 'lixo' e busca por redenção. A obra é um mangá escrito por Kei Urana e ganhou adaptação em anime pelo Studio Bones."

@app.route('/BokuNoHero') 
def Serie():
    return "My Hero Academia (Boku no Hero Academia) acompanha Izuku Midoriya, um jovem nascido sem superpoderes ('individualidades') em um mundo onde 80 porcento da população os possui. Após conhecer seu ídolo, All Might, ele herda uma habilidade especial e ingressa na prestigiada Academia U.A. para se tornar um herói profissional e combater a Liga dos Vilões. Pontos principais da trama: O Sonho de Deku: Izuku, apelidado de Deku, é obcecado por heróis e determinado a provar seu valor mesmo começando do zero. A 'Individualidade' Recebida: All Might passa para Midoriya o seu poder, o One For All, um dom transferível que aumenta a força física. A Academia U.A.: A série foca no treinamento de Midoriya e seus colegas da Turma 1-A, enfrentando rivais e aprendendo a controlar seus poderes. Conflitos: A história aborda a luta contra vilões que desafiam a sociedade heroica. O anime, conhecido por suas cenas de ação, está disponível para streaming na Netflix e Crunchyroll. "

@app.route('/YuYuHakusho') 
def sErie():
    return "Yu Yu Hakusho narra a história de Yusuke Urameshi, um adolescente delinquente que morre ao salvar uma criança de um atropelamento. Por seu ato altruísta surpreender o mundo espiritual, ele ganha uma segunda chance e retorna à vida como 'Detetive Espiritual', investigando atividades demoníacas e paranormais. Pontos principais da trama: A Missão: Sob o comando de Koenma, Yusuke investiga Yokais (demônios) e objetos perigosos no mundo humano. O Grupo: Ele forma uma equipe com seu rival humano Kuwabara e os youkais Kurama e Hiei. Evolução: A série, criada por Yoshihiro Togashi, transita de casos investigativos para torneios de artes marciais (como o Torneio das Trevas).O Retorno: Após provar seu valor, Yusuke assume o papel de detetive para proteger a humanidade. O anime é um clássico dos anos 90, conhecido por lutas intensas e pelo desenvolvimento dos personagens."

@app.route('/Frieren') 
def seRie():
    return "Frieren: Beyond Journey's End (Sousou no Frieren) acompanha uma elfa maga imortal que, após derrotar o Rei Demônio com seu grupo, lida com a passagem do tempo ao ver seus companheiros humanos envelhecerem e morrerem. Arrependida de não conhecê-los melhor, ela inicia uma nova jornada para entender a vida e as emoções humanas. Principais detalhes da trama: A Vida Pós-Aventura: A história começa quando a missão de 10 anos termina e o grupo de heróis se separa, destacando o 'depois do fim' da aventura. A Perspectiva da Imortalidade: Como elfa, Frieren vive séculos e inicialmente não entende a efemeridade da vida humana, tornando-se indiferente ao passar do tempo. Conexão e Arrependimento: Após a morte do herói Himmel, Frieren decide viajar para se conectar verdadeiramente com as pessoas e valorizar as conexões profundas, aprendendo com novas companhias. Temas: A obra aborda melancolia, saudade, a passagem do tempo e o legado deixado pelos amigos, tudo com uma narrativa de fantasia.  O mangá, escrito por Kanehito Yamada e ilustrado por Tsukasa Abe, foi lançado em 2020 e recebeu uma aclamada adaptação em anime."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)