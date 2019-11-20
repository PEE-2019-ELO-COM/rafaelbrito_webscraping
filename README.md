# rafaelbrito_webscraping
Web scraping de passagens aéreas de um site de compra de passagens (mais especificamente, o site da Decolar).

# Informações gerais:

A ideia é entrar com a data e a localidade que deseja ir, será feito uma comparação de preços e será enviado um aviso quando existir uma queda nos preços. Essa notificação a priori é feita no pelo e-mail que se insere! Aparece também as melhores opções de voo em um log na linha de comando, se quiser visualmente checar as iterações do programa. Atualizações como notificações pelo WhatsApp estão sendo implementadas já em um código que existe no repositório, bastando acertar um jeito de manter o WhatsApp aberto pelo WhatsApp Web de forma mais automatizada do que a conferência via QRcode sempre. Já existe também um código compatível com o Chrome/Chromium, cuja finalidade é conseguir fazer o programa rodar em um Rasp Berry indefinidamente (não precisando deixar a aplicação rodando no seu computador), mas existe algum problema de inicialização do navegador do Chromium que precisa ser resolvido ainda.

A motivação dessa aplicação é a dificuldade de um familiar em encontrar passagens aéreas para fazer suas viagens, que acaba sendo um transtorno em casa (no caso recai sobre mim).

A biblioteca gráfica escolhida foi a Tkinter em python. Foram utilizados tutoriais da internet e testados os exemplos do likegeek (https://likegeeks.com/python-gui-examples-tkinter-tutorial/) no jupyter para ter uma noção das possibilidades. O programa possui uma tela apenas, pequena e simples para que não haja confusões com o usuário!

# Conteúdo do Repositório:

O repositório contém de essencial para a aplicação:
 - Arquivo IATAcode.py, responsável por fazer a conversão do nome da cidade para o código IATA. (Santos Dummont - SDU por exemplo)
 - ScrappingGUI-v1Chrome.py, que é o programa rodando no navegador do Chrome.
 - chromedriver.exe, o driver para a aplicação do Chrome.
 - scrappingGUI-v1.py, que é o programa rodando no navegador do FireFox.
 - geckodriver.exe, o driver para aplicação do FireFox.
 
De resto temos algumas prints do que seria o programa rodando em printRodando.docx e printRodandoGUI.docx, os logs dos drivers e um arquivo do jupyter já com início da implementação da mensagem por WhatsApp.

# Ajustes e instalações adicionais:

Para que o programa rode perfeitamente, devemos seguir alguns passos:

1) Primeiramente é instalar a biblioteca do Selenium python (estamos utilizando a versão 3.7.0 e Windows 10) através do "pip install selenium" no terminal do computador. As bibliotecas de protocolo SMTP para enviar o e-mail de alerta já vem incluso, mas vale a pena também instalar para ter certeza. A bilioteca Tkinter também é padrão para essa versão, mas caso ocorra um erro, basta fazer o "pip install tkinter" no terminal.

2) Abra o arquivo "scrappingGUI-v1.py", nele temos a aplicação rodando para Firefox. Esse arquivo está comentado e caso queira usar o Chrome na aplicação, é só fazer o mesmo de forma análoga. Para rodar em FireFox precisamos ter na mesma pasta o geckodriver.exe ou em Chrome o chromedriver.exe. (https://chromedriver.chromium.org/downloads e https://github.com/mozilla/geckodriver/releases) para os downloads, tome cuidado com as versões do chrome/mozilla para baixar o driver correto. Com os drivers baixados, coloque o PATH correto na linha 42 do programa.

3) Para que se consiga coletar as infos é necessário que a página carregue completamente, então o tempo de sleep da linha 47 deve ser de acordo com isso. Imaginamos que 15 segundos como está lá seja suficiente, mas troque de acordo com a sua necessidade.

4) O email que enviará a mensagem também pode ser trocado, esse setup é feito na linha 94, mas já existe um padrão para isso.

# Rodando o programa:

De forma bem intuitiva, preencha a tela da aplicação. Coloque as cidades com letra maiúscula e preste atenção ao formato das datas que deve seguir o formato ANO-MÊS-DIA.

<img src = "https://github.com/PEE-2019-ELO-COM/rafaelbrito_webscraping/tree/master/imgs/git1.PNG">

Agora basta esperar que ele mostrará no terminal a melhor opção encontrada naquele loop e caso seja a primeira, ou uma melhor do que ele já havia computado, ele mandará um email e no terminal uma confirmação para qual e-mail foi enviado.

<img src = "https://github.com/PEE-2019-ELO-COM/rafaelbrito_webscraping/tree/master/imgs/git2.PNG">

O e-mail terá o seguinte formato:

<img src = "https://github.com/PEE-2019-ELO-COM/rafaelbrito_webscraping/tree/master/imgs/GIT3.PNG">

Caso queira mudar o conteúdo da mensagem, basta com que se altere esse setup e a mensagem na parte de ALERTAS do código.
