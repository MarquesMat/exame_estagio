# exame_estagio
Conjunto de códigos e respostas para o exame técnico da oportunidade de 'Estágio em Desenvolvimento'.

Q1) Executar código: python3 fibonacci.py
Q2) Executar cógigo; python3 count_a.py
Q3) SOMA = 77. Compilar e executar código: gcc sum_k.c -o sum_k; ./sum_k
Q4) a) 9 b) 128 c) 49 d) 100 e) 13 f) 20
Q5) Considerando que seja possível tocar nas lâmpadas, podemos resolver este problema baseando-se no fato de que lâmpadas acesas emitem uma certa quantidade de calor. Assim, eu ligaria apenas um interruptor e esperaria alguns minutos para a lâmpada aquecer. Em seguida, desligaria este interruptor, ligaria o próximo e, imediatamente, iria até a primeira sala. Aqui, temos dois cenários: 
  1. Se a sala estiver acesa, então sua lâmpada está conectada ao segundo interruptor, logo, basta visitar a próxima sala (que obrigatoriamente estará apagada) e verificar se sua lâmpada está quente (primeiro interruptor) ou fria (terceiro interruptor).
  2. Se a primeira sala estiver apagada, verifico se sua lâmpada está quente ou fria (seguindo a lógica do cenário anterior), então visito a próxima sala e observo se ela está acesa ou apagada.
Nota-se que no momento em que descobrimos os dois primeiros interruptores, podemos deduzir o terceiro.
