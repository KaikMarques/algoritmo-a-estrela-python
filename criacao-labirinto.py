from pyamaze import maze, agent, textLabel

# definindo meu labirinto
labirinto = maze(10, 10)

# toda vez que rodar o código ele cria um novo labirinto, abaixo deixo salvo o ultimo estado
# labirinto.CreateMaze(saveMaze=True)

# Quando rodei o código acima gerou um arquivo csv, agora irei carregar o mesmo
labirinto.CreateMaze(loadMaze="maze--2024-03-12--10-16-50.csv")
# Cria mais possibilidades de caminhos até o destino
# labirinto.CreateMaze(loopPercent=50)

# celulas = labirinto.grid
#print(celulas)

# mapa = labirinto.maze_map
# print(mapa)

# aqui onde vejo o caminho perfeito do labirinto
caminho = labirinto.path
# print(caminho)

# criando o agente e mostrando o caminho percorrido
agente = agent(labirinto, footprints=True)

# possibilidade de passar o caminho
# caminho = {(10, 10): (10, 9), (10, 9): (10, 8), (10, 8): (10, 6)}
# caminho = "NWNWNWN"
labirinto.tracePath({agente: caminho}, delay=200)
# agent.position = (10, 9)
# posicao = agent.position
# print(posicao)

# Criando texto no labirinto para contar os passos
texto = textLabel(labirinto, title="Nº passos", value=len(caminho))
labirinto.run()

Agora irei criar o algoritmo neste video:  https://www.youtube.com/watch?v=fTtYzHfGlyk
