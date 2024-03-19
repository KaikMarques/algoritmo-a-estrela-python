# Criando algoritmo A*

## Algoritmo Para otmização de caminho

Algoritmo A Estrela (A*) é um algoritmo de otmização, neste projeto será utilizado para otmização de caminho.

 A ideia é utilizar um labirinto, para que consiga encontrar a melhor rota de caminho até o final.


Bibliotecas:

# Pyamaze {

####   Scripts em Python para gerar labirintos aleatórios solucionáveis usando os algoritmos de busca em profundidade e retrocesso recursivo. O código também implementa um algoritmo de busca em retrocesso recursivo para resolver os labirintos gerados. 

## Agent

 Agent são objetos que irei colocar para percorrer o labirinto

    Documentação:  https://github.com/jostbr/pymaze
}


 ## Explicação sobre o funcionamento do algotmito A*


    * [Artigo Com explicação] (https://www.hashtagtreinamentos.com/algoritmo-a-estrela-no-python)


  O algoritmo A* é um algoritmo de busca informada que combina a busca em largura (BFS) com uma heurística para encontrar o caminho mais curto entre dois pontos em um grafo ou grade.


Ele avalia os nós a serem expandidos com base em duas informações: o custo do caminho percorrido até o nó atual (custo g) e uma estimativa do custo restante até o destino (custo h). Isso é conhecido como função de avaliação f(n) = g(n) + h(n). O objetivo é minimizar essa função de avaliação para encontrar o caminho mais curto.


O algoritmo A* mantém uma lista de nós a serem explorados, chamada de fronteira. Ele começa com o nó inicial na fronteira e, em cada iteração, seleciona o nó com o menor valor de f(n) para expandir.


Para cada nó expandido, o algoritmo verifica se é o destino. Se sim, o algoritmo termina e o caminho é reconstruído, seguindo os nós antecessores de volta ao nó inicial. Caso contrário, o algoritmo gera sucessores para o nó atual e calcula os custos g e h para cada um desses sucessores. Os sucessores são adicionados à fronteira para posterior expansão.


Durante a expansão dos nós, o algoritmo atualiza os custos g e h dos nós conforme necessário. Se um nó já está na fronteira, o algoritmo verifica se o novo caminho leva a um custo g menor. Nesse caso, o nó é atualizado com o novo custo g e o caminho é recalculado.


O algoritmo continua expandindo nós até atingir o destino ou até que a fronteira esteja vazia, o que indica que não existe um caminho para o destino.


A heurística escolhida para estimar o custo h pode variar, mas geralmente é uma estimativa admissível, ou seja, nunca superestima o custo real para atingir o destino. 
