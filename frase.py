from desempata import *
from configs import *


def get_previous(lista1, word):
    """
    Essa função pega a palavra anterior mais frequente da palavra digitada pelo usuário
    :param lista1: lista de palavras anteriores mais frequentes
    :param word: palavra digitada pelo usuário
    :return: Mensagem de erro
    """
    if word:
        options = {
            True: (desempatar(lista1)),
            False: (lista1[0])
        }

        immediate_previous = options[len(lista1) > 1]
        return immediate_previous
    return print("Essa palavra não esta no documento")


def get_subsequent(lista2, word):
    """
    Essa função pega a palavra posterior mais frequente da palavra digitada pelo usuário
    :param lista2: lista de palavras posteriores mais frequentes
    :param word: palavra digitada pelo usuário
    :return: Mensagem de erro
    """
    if word:
        options = {
            True: (desempatar(lista2)),
            False: (lista2[0])
        }

        immediate_subsequent = options[len(lista2) > 1]
        return immediate_subsequent
    return print("Essa palavra não esta no documento")


def make_phrase(lista1, lista2, word, number):
    """
    forma uma frase aleatória dependendo da palavra e do numero de termos escolhidos pelo usuário
    :param lista1: lista de palavras (do documento lido) anteriores à escolhida pelo usuário
    :param lista2: lista de palavras (do documento lido) posteriores à escolhida pelo usuário
    :param word: palavra escolhida pelo usuário
    :param number: número de termos escolhido pelo usuário
    :return: frase aleatória gerada a partir da escolha de palavra e número de termos feita pelo usuário
    """
    anterior = get_previous(lista1, word)
    posterior = get_subsequent(lista2, word)
    if number == 0:
        frase = "Você escolheu zero numeros de palavras na frase"
        return frase
    elif number == 1:
        frase = word
        return frase
    elif number == 2:
        option = desempatar2(anterior, posterior)
        if option == anterior:
            frase = f"{anterior} {word}"
            return frase
        elif option == posterior:
            frase = f"{word} {posterior}"
            return frase
    elif number >= 3:
        frase = f"{anterior} {word} {posterior}"
        return frase


def phrases(frase, number, words, dict2, dict4):
    """
      Essa função imprime as frases mais provaveis de acordo com a frequencia das palavras. O usuário pode continuar
      o programa e formar frases maiores de acordo com a sua vontade
      :param frase: frase que foi formada anteiormente, quando o usuário digitou a palavra que ele quis
      :param words: todas as palavras presentes no texto
      :param number: numero de termos que o usuário quer que a frase tenha
      :return: Mensagem de programa encerrado
      """
    resp = 0
    metade = number // 2
    while resp < 1:
        for i in range(1, metade):
            palavras = frase.split()
            palavra_inicial = palavras[0]
            palavra_final = palavras[-1]
            anterior = desempate_anteriores(palavra_inicial, dict2, number, words)
            posterior = desempate_posteriores(palavra_final, dict4, number, words)
            if (number - len(palavras)) % 2 == 0:
                nova_frase = f"{anterior} {frase} {posterior}"
            else:
                desempate = desempatar2(anterior, posterior)
                if desempate == anterior:
                    nova_frase = f"{anterior} {frase}"
                else:
                    nova_frase = f"{frase} {posterior}"

            frase = nova_frase

            try:
                if resp != 0:
                    return nova_frase
            except ValueError:
                print("Digite um valor inteiro positivo")
        resp = 1
    return frase


def dict_most_frequents(dict1, dict2, number, lista):
    """

    :param dict1:
    :param dict2:
    :param number:
    :param lista:
    :return:
    """
    most_frequents_previous = {}
    most_frequents_subsequent = {}
    metade = number // 2
    for n in range(2, metade + 1):
        most_frequents_previous[f"distancia {n}"] = {}
        most_frequents_subsequent[f"distancia {n}"] = {}
        lista3, lista4 = check_tie(dict1[f"distancia {n}"], dict2[f"distancia {n}"], lista)
        """print("anteriores")
        print(lista3)
        print("posteriores")
        print(lista4)"""
        for j, item in enumerate(lista3):
            for key, value in dict1[f"distancia {n}"].items():
                if key == item:
                    most_frequents_previous[f"distancia {n}"][key] = value
        for j, item in enumerate(lista4):
            for key, value in dict2[f"distancia {n}"].items():
                if key == item:
                    most_frequents_subsequent[f"distancia {n}"][key] = value

    print(most_frequents_previous)
    print(most_frequents_subsequent)
    return most_frequents_previous, most_frequents_subsequent


def generate_sentence(word, style, number):
    """
    gera a frase aleatória a partir da palavra e número de termos escolhidos pelo usuário. Essa frase
    terá exatamente o mesmo número de termos (palavras) que o usuário digitou.
    :param word: palavra escolhida pelo usuário
    :param style: nome do estilo de documento que deve ser lido
    :param number: número de termos escolhido pelo usuário
    :return: frase aleatória gerada a partir das escolhas feitas pelo usuário. Essa frase
    terá o mesmo número de termos (palavras) que o usuário digitou.
    """
    lista_de_busca = []
    previous = {}
    previous2 = {}
    subsequent = {}
    subsequent2 = {}
    metade = number // 2
    words = list_the_words(style)
    if word in words:
        num_list = fill_itens(lista_de_busca, word, words, previous, subsequent)
        for n in range(2, metade + 1):
            add_itens_in_dicts2(num_list, previous2, subsequent2, word, words, n)
        lista1, lista2 = check_tie(previous, subsequent, lista_de_busca)
        frase = make_phrase(lista1, lista2, word, number)
        #  print("frase inicial: ", frase)
        if number > 3:
            nova_frase = phrases(frase, number, words, previous2, subsequent2)
            return print(nova_frase)
        return print(frase)
    return print("A palavra que você buscou não está no documento lido.")


if __name__ == "__main__":
    generate_sentence("essa", "cientifico", 6)
