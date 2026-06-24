Opa! Muito obrigado por estar lendo isso.

Esse script que programei basicamente cria um pacote SYN e envia ele pra o host que você escolher;

Após o script enviar esse pacote SYN para o alvo, ele recebe a resposta da porta que ele enviou o pacote;

Tendo em vista que o código já armazenou essa resposta do alvo numa variável, o script verifica o tipo da resposta, vendo se as portas TCP responderam com SYN ACK ou RST ACK;


Como usar?

Para uasr o script vc tem que ter o python instalado na sua máquina, além de tbm ter o Scapy instalado

Além do mais, é bem importante que vc execute ele como administrador, já que o próprio script cria pacotes de redes brutos
