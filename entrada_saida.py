def read_input(filename):
    with open(filename, 'r') as file:
        N = int(file.readline())
        x0, y0 = map(int, file.readline().split())
        xf, yf = map(int, file.readline().split())
    return N, x0, y0, xf, yf

def coordenada_xadrez(x, y):
    colunas = "abcdefgh"
    return f"{colunas[x]}{y + 1}"

def write_output(filename, path):
    with open(filename, 'w') as file:
        file.write("Quantidade minima de passos: {}\n\n".format(len(path) - 1))
        for step, (x, y) in enumerate(path):
            file.write(f'Passo {step}: ({x}, {y}) : {coordenada_xadrez(x, y)}\n')


