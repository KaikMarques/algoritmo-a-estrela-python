# Importa os módulos necessários para a criação do labirinto, o agente e a fila de prioridade.

from pyamaze import maze, agent
from queue import PriorityQueue

# Define a coordenada de destino para o agente.
destino = (1, 1)

# Define a função de heurística utilizada no algoritmo A*. Essa função calcula a distância de Manhattan entre a célula atual e a célula de destino.
def h_score(celula, destino):
    linhac = celula[0]
    colunac = celula[1]
    linhad = destino[0]
    colunad = destino[1]
    return abs(colunac - colunad) + abs(linhac - linhad)


# Define a função principal que implementa o algoritmo A*. Ela recebe um objeto labirinto como parâmetro. A função inicializa os dicionários f_score e g_score, onde f_score representa o custo total de chegada 
# a uma célula e g_score representa o custo do caminho percorrido até determinada célula. A célula inicial é definida como a posição do agente no labirinto. 
# O f_score dessa célula é inicializado como a soma do g_score e da heurística estimada.
def aestrela(labirinto):
    # criação do dicionário f_score com todas as células do labirinto com valor "infinito"
    f_score = {celula: float("inf") for celula in labirinto.grid}
    g_score = {}
    celula_inicial = (labirinto.rows, labirinto.cols)
    # cálculo do valor da célula inicial
    g_score[celula_inicial] = 0
    f_score[celula_inicial] = g_score[celula_inicial] + h_score(celula_inicial, destino)
    print(f_score)
    
    # Cria uma fila de prioridade e adiciona
    fila = PriorityQueue()
    item = (f_score[celula_inicial], h_score(celula_inicial, destino), celula_inicial)
    fila.put(item)

    caminho = {}
    while not fila.empty():
        celula = fila.get()[2]

        if celula == destino:
            break

        for direcao in "NSEW":  # verifica as direções vizinhas
            # Verifica se é possível se mover para a direção atualmente analisada. Se o valor da célula vizinha naquela direção for 1, significa que é possível se mover para lá
            if labirinto.maze_map[celula][direcao] == 1: 
                linha_celula = celula[0]
                coluna_celula = celula[1]
                if direcao == "N":
                    proxima_celula = (linha_celula - 1, coluna_celula)
                elif direcao == "S":
                    proxima_celula = (linha_celula + 1, coluna_celula)
                elif direcao == "W":
                    proxima_celula = (linha_celula, coluna_celula - 1)
                elif direcao == "E":
                    proxima_celula = (linha_celula, coluna_celula + 1)
                novo_g_score = g_score[celula] + 1
                novo_f_score = novo_g_score + h_score(proxima_celula, destino)
                # Caso o cálculo do novo f_score para a célula vizinha seja menor que o valor atual do f_score, atualiza o f_score, o g_score e adiciona a célula na fila de prioridade. 
                # Além disso, armazena a informação de que a célula vizinha é alcançável a partir da célula atual no dicionário caminho.
                if novo_f_score < f_score[proxima_celula]:
                    f_score[proxima_celula] = novo_f_score
                    g_score[proxima_celula] = novo_g_score
                    item = (novo_f_score, h_score(proxima_celula, destino), proxima_celula)
                    fila.put(item)
                    caminho[proxima_celula] = celula
    caminho_final = {}  # Dicionário que armazenará o caminho final percorrido
    celula_analisada = destino  # Inicia a célula analisada como a célula destino
    print("Celulas analisadas", len(caminho.keys()))  # Imprime o número de células analisadas durante o algoritmo
    while celula_analisada != celula_inicial:  # Enquanto não alcançar a célula inicial
        caminho_final[caminho[celula_analisada]] = celula_analisada  # Armazena a célula atual e a célula anterior no caminho final
        celula_analisada = caminho[celula_analisada]  # Atualiza a célula analisada para a célula anterior
    return caminho_final  # Retorna o caminho final percorrido

labirinto = maze(100, 100)  # Cria um labirinto com 100 linhas e 100 colunas
labirinto.CreateMaze()  # Cria um labirinto aleatório

agente = agent(labirinto, filled=True, footprints=True)  # Cria um agente para percorrer o labirinto, exibindo preenchimento de células visitadas e pegadas
caminho = aestrela(labirinto)  # Chama a função de busca A* para encontrar o caminho no labirinto
labirinto.tracePath({agente: caminho}, delay=10)  # Exibe o caminho encontrado no labirinto, com um atraso de 10ms entre os movimentos

print("Total de celulas", len(labirinto.maze_map.keys()))  # Imprime o total de células no labirinto

labirinto.run()