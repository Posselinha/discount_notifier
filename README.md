# O que é
Esse projeto é um notificar de descontos para jogos da Steam e ele funciona mandando emails dê uma conta para outra avisando sobre a existência de uma promoção

# Usos
Mesmo tendo a opção de wishlist da Steam, você não consegue dar wishlist caso você já possua o jogo em questão. Por isso, foi criado este projeto com o intuito de ainda poder ser notificado quando um jogo que eu já possuo, mas quero dar de presente para um amigo, entrar em promoção

# Como configurar
Primeiro de tudo, seria interessante você conectar sua conta do gmail com o [Sheety](https://sheety.co) e criar uma cópia desta [planilha](https://docs.google.com/spreadsheets/d/1PbeSTuNi4PCbvJpHsEoD8bh0K5aLfUTQNbAvkeB5QjY/edit?usp=sharing).

## Definir uma planilha como um projeto do Sheety
1. Simplesmente cópie a url da tabela que você duplicou e insira ela no input. (Caso você não veja a tela da imagem abaixo, clique em "New Project".

![Criar um projeto no Sheety](https://imgur.com/o02C7vw.png)

## Para ativar a autenticação do Sheety:
1. Dentro da página do Sheety, aperte em "Authentication";
![Seta mostrando onde apertar](https://imgur.com/LkBFOAZ.png)

2. Selecione "Basic" e defina um nome e uma senha própria;
![Colocando autenticação básica](https://imgur.com/AHAym5V.png)

3. Aperte em "Save Changes" para salvar as alterações.

![Mostrando como salvar as alterações](https://imgur.com/6TrMBtI.png)

## Como copiar a planilha e alimentar com dados
1. Aperte em "Arquivo" e depois em "Fazer uma cópia";
![Botões para copiar a tabela](https://imgur.com/OvO7rte.png)

2. Na janela que abrir, dê um nome para a nova planilha, defina onde ela será salva e enfim aperte em "Fazer uma cópia";
![Janela de salvar](https://imgur.com/jaQq8Hu.png)

3. Agora para alimentar a tabela com dados, você precisa fornecer o id dos jogos que você quer que o código pegue as informações, para isso, você deve ir para a página do jogo que você quer e copiar o id que está na url;
![Conseguir id do jogo](https://imgur.com/ilCA0VG.png)

4. Após copiar, você deve colocar este id na próxima linha da primeira coluna da planilha, sendo feito assim a alimentação de dados para a planilha.

![Planilha alimentada](https://imgur.com/0pSL6cU.png)

## Configurar o arquivo .env:
Quando você baixar o projeto, verá que dentro dele existe um arquivo chamado "env.sample", você deverá criar uma cópia deste arquivo e renomear a cópia para ".env". Dentro dele, existe as váriaveis que precisam ser alimentadas com dados que você irá fornecer, note que isto é importante para o funcionamento do projeto.

![Foto do arquivo .env](https://imgur.com/H9uMAk8.png)

### USERNAME_AUTH e PASSWORD_AUTH
Estas variavéis se referem ao nome e senha que você definiu na autenticação do Sheety

### SHEETY_ENDPOINT
Este seria o link que o código irá utilizar para fazer as requests da API, você irá consegui-lo na página do Sheety referente ao projeto que você criou na parte reference ao "GET" da API

![Conseguir Endpoint](https://imgur.com/Ecuhjqy.png)

### YOUR_EMAIL, EMAIL_PASSWORD, EMAIL_SMTP e RECEIVER_EMAIL
Se referem ao:
1. Conta de email que irá enviar os emails;
2. Senha desta suposta conta;
3. Protocolo de transferência de Email do provedor desta conta;
4. Conta que irá receber o email enviado.

#### Conseguir SMTP:
Você pode conseguir o link de SMTP do seu provedor fazer uma simples pesquisa no google, como por exemplo, "Outlook SMTP".
Um exemplo de STMP seria o do Outlook, "smtp-mail.outlook.com".

# Após configurar:
Caso você tenha feito os passos acima, você irá ter um arquivo .env parecido com este abaixo:

![.env exemplo](https://imgur.com/9vbg2YA.png)

Com isso então, o código já está pronto para ser utilzado, você só precisa rodar o arquivo "main.py".



