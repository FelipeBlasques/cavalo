from entrada_saida import read_input, write_output
from busca_a_star import a_star
import movimentos

def main(input_file, output_file):
    N, x0, y0, xf, yf = read_input(input_file)
    path = a_star(x0, y0, xf, yf, N)
    if path:
        write_output(output_file, path)
        print("Caminho encontrado e salvo em", output_file)
    else:
        print("Não foi possivel encontrar um caminho.")

if __name__ == "__main__":
    main("entrada-saida/entrada.txt", "entrada-saida/saida.txt")
