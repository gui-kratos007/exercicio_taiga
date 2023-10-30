from pegar_estilo import get_style
from gerar_frase import *


def interface():
    list_styles = ["cientifico", "filosofico", "literario"]
    print("Opções de estilo disponíveis:")
    print(list_styles[0], ",", list_styles[1], ",", list_styles[2], "\n")
    continuar = True
    while continuar:
        style = input("Qual o estilo de arquivo que você gostaria de carregar? (Escreva sem acentos): ").lower()
        dados = get_style(style, list_styles)
        if dados == 1:
            word = input("A partir de qual palavra você quer gerar a frase? ")
            number_of_words = int(input("Quantas palavras você quer que tenha nessa frase: "))
            generate_sentence(word, style, number_of_words)
        else:
            continuar = False


interface()
