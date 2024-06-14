# Tutorial de Uso e Explicação do Código

Este repositório contém uma implementação do algoritmo A* para encontrar o caminho mínimo entre dois pontos em um tabuleiro, considerando as restrições de movimento de um cavalo no xadrez.

## Estrutura dos Arquivos

movimentos.py: Define as possíveis jogadas de um cavalo no xadrez.
heuristica.py: Define a função de distância de Manhattan, usada como heurística no algoritmo A*.
entrada_saida.py: Define funções para ler entradas de um arquivo e escrever saídas em um arquivo.
busca_a_star.py: Implementa o algoritmo A* usando a heurística de distância de Manhattan e as possíveis jogadas do cavalo.
main.py: Script principal que lê a entrada, executa o algoritmo A* e escreve a saída.

## Arquivos de Entrada e Saída

### entrada-saida/entrada.txt: Arquivo de entrada contendo:

A dimensão do tabuleiro N
As coordenadas iniciais x0, y0
As coordenadas finais xf, yf

### entrada-saida/saida.txt: Arquivo de saída gerado pelo programa contendo:

A quantidade mínima de passos
A sequência de passos do cavalo do ponto inicial ao ponto final

## Estrutura do Arquivo de Entrada

O arquivo de entrada deve ter o seguinte formato:

```
N
x0 y0
xf yf
```

Onde:

N é a dimensão do tabuleiro (NxN)
x0,y0 são as coordenadas iniciais
xf,yf são as coordenadas finais

Exemplo:

```
8
0 0
7 7
```

## Estrutura do Arquivo de Saída

O arquivo de saída gerado terá o seguinte formato:

```
Quantidade minima de passos: X

Passo 0: (x0, y0)
Passo 1: (x1, y1)
...
Passo X: (xf, yf)
```

## Como Executar

Certifique-se de que todos os arquivos necessários estão na estrutura correta.
Crie um arquivo de entrada conforme o formato descrito acima e salve-o em entrada-saida/entrada.txt.
Execute o script principal:

```
python main.py
```

Verifique o arquivo de saída gerado em entrada-saida/saida.txt

## Explicação do Código

### movimentos.py

Define a função valid_moves(x, y, N) que retorna uma lista de movimentos válidos do cavalo a partir da posição (x, y) em um tabuleiro de dimensão N.

### heuristica.py

Define a função manhattan_distance(x1, y1, x2, y2) que calcula a distância de Manhattan entre dois pontos (x1, y1) e (x2, y2).

### entrada_saida.py

Define duas funções:

read_input(filename): Lê o arquivo de entrada e retorna os parâmetros N, x0, y0, xf, yf.
write_output(filename, path): Escreve o caminho encontrado no arquivo de saída.

### busca_a_star.py

Implementa o algoritmo A*:

a_star(x0, y0, xf, yf, N): Executa o algoritmo A* para encontrar o caminho mínimo do cavalo de (x0, y0) a (xf, yf) em um tabuleiro de dimensão N.
reconstruct_path(current, came_from): Reconstrói o caminho encontrado a partir do dicionário came_from.

### main.py

Script principal que:

Lê os parâmetros do arquivo de entrada usando read_input.
Executa o algoritmo A* usando a_star.
Escreve o caminho encontrado no arquivo de saída usando write_output.

## Exemplo de Execução

Suponha que o arquivo entrada-saida/entrada.txt contenha:

```
8
0 0
7 7
```

Execute o script principal:

```
python main.py
```

O arquivo entrada-saida/saida.txt será gerado com o caminho encontrado.

Pronto! Agora você pode usar este código para encontrar o caminho mínimo de um cavalo no tabuleiro de xadrez usando o algoritmo A*.
