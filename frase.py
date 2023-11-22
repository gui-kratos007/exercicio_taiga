import random
from carregar_arquivo import load_file
from desempata import *

def text_clean(text):
    """
    Limpa o texto e garante a similaridade das palavras.
    :return text: Texto limpo e corrigido.
    """
    return (text.replace(",", "")
            .replace(".", "")
            .lower()
            )


def list_the_words(style):
    """
    lê o texto e retorna a lista de palavras dele
    :param style: caminho do arquivo (sem o .txt)
    :return: lista de palavras do texro
    """
    text = load_file(style)
    list_words = text_clean(text).split()
    return list_words


def search_word(txt):
    """
    Pesquisa a palavra escolhida pelo usuário e retorna uma lista com os indices de todas
    as aparições dessa palavra no texto
    :param txt: texto do documento
    :return: mensagem de erro
    """
    word = input("digite a palavra que quer pesquisar: ")
    lista_de_busca = []
    for i, item in enumerate(text_clean(txt).split()):
        if item == word:
            lista_de_busca.append(i)
    if len(lista_de_busca) > 0:
        return lista_de_busca
    return "essa palavra não está no texto"


def add_in_list(lista, word, words):
    """
    adiciona itens em uma lista se esse item for igual a palavra escolhida pelo usuário.
    :param lista: lista em que os itens serão adicionados
    :param word: palavra escolhida pelo usuário
    :param words: lista de palavras do documento
    :return: tamanho da lista
    """
    for i, item in enumerate(words):
        if item == word:
            lista.append(i)
    return len(lista)


def add_itens_in_dicts(func, dict1, dict2, word, words):
    """
    se existir ao menos 1 item na lista, adiciona esse item na sua respectiva dict e atribui
     valor a esses itens, que aumenta a medida que ele reaparece na contagem da lista
    :param func: função que retorna o tamanho da lista
    :param dict1: dicionário de palavras anteriores, que no início está vazio
    :param dict2: dicionário de palavras posteriores, que no início está vazio
    :param word: palavra escolhida pelo usuário
    :param words: lista de palavras
    :return: dicionarios de anteriores e posteriores, com os seus respectivos itens e valores,
    que agora não estará mais vazio, como no início
    """
    if func > 0:
        # Conta a frequencia das palavras anteriores e posteriores
        for j, item in enumerate(words):
            if item == word:
                if words[j] == words[0]:
                    previous_word = words[-1]
                else:
                    previous_word = words[j - 1]
                if words[j] == words[-1]:
                    subsequent_word = words[0]
                else:
                    subsequent_word = words[j + 1]

                # Se a palavra já estiver no dict das anteriores, adiciona mais 1 ao seu valor
                if previous_word in dict1:
                    dict1[previous_word] += 1
                # Se a palavra não estiver no dict das anteriores, adiciona ela e coloque seu valor como 1.
                else:
                    dict1[previous_word] = 1

                # Se a palavra já estiver no dict das posteriores, adiciona mais 1 ao seu valor
                if subsequent_word in dict2:
                    dict2[subsequent_word] += 1
                # Se a palavra não estiver no dict das posteriores, adiciona ela e coloque seu valor como 1.
                else:
                    dict2[subsequent_word] = 1
    return dict1, dict2


def add_itens_in_dicts2(func, dict1, dict2, word, words, number):
    """
    se existir ao menos 1 item na lista, adiciona esse item na sua respectiva dict e atribui
     valor a esses itens, que aumenta a medida que ele reaparece na contagem da lista
    :param func: função que retorna o tamanho da lista
    :param dict1: dicionário de palavras anteriores, que no início está vazio
    :param dict2: dicionário de palavras posteriores, que no início está vazio
    :param word: palavra escolhida pelo usuário
    :param words: lista de palavras
    :return: dicionarios de anteriores e posteriores, com os seus respectivos itens e valores,
    que agora não estará mais vazio, como no início
    """
    if func > 0:
        dict1[f"distancia {number}"] = {}
        dict2[f"distancia {number}"] = {}
        # Conta a frequencia das palavras anteriores e posteriores
        for j, item in enumerate(words):
            if item == word:
                if words[j] == words[0]:
                    previous_word = words[-1]
                else:
                    previous_word = words[j - number]
                if words[j] == words[-1]:
                    subsequent_word = words[0]
                else:
                    subsequent_word = words[j + number]

                # Se a palavra já estiver no dict das anteriores, adiciona mais 1 ao seu valor
                if previous_word in dict1[f"distancia {number}"]:
                    dict1[f"distancia {number}"][previous_word] += 1
                # Se a palavra não estiver no dict das anteriores, adiciona ela e coloque seu valor como 1.
                else:
                    dict1[f"distancia {number}"][previous_word] = 1

                # Se a palavra já estiver no dict das posteriores, adiciona mais 1 ao seu valor
                if subsequent_word in dict2[f"distancia {number}"]:
                    dict2[f"distancia {number}"][subsequent_word] += 1
                # Se a palavra não estiver no dict das posteriores, adiciona ela e coloque seu valor como 1.
                else:
                    dict2[f"distancia {number}"][subsequent_word] = 1
    return dict1, dict2


def add_itens_in_previous_specifics(lista, words, number):
    previous_specifics = {}
    anteriores_especificos = get_previous_in_document(lista, words, number)

    for i, item in enumerate(anteriores_especificos):
        if item in previous_specifics:
            previous_specifics[item] += 1
        else:
            previous_specifics[item] = 1
    print(previous_specifics)
    return previous_specifics


def add_itens_in_subsequent_specifics(lista, words, number):
    subsequent_specifics = {}
    posteriores_especificos = get_subsequent_in_document(lista, words, number)

    for i, item in enumerate(posteriores_especificos):
        if item in subsequent_specifics:
            subsequent_specifics[item] += 1
        else:
            subsequent_specifics[item] = 1
    print(f"posteriores especificos: {subsequent_specifics}")
    return subsequent_specifics


def get_previous_in_document(dict, words, number, list):
    anteriores_especificos = {}
    for key, value in dict.items():
        for i, item in enumerate(words):
            for j in list:
                for k in range(4, number):
                    if key == item and i + k == list[j]:
                        anteriores_especificos[key] = value



    """for i in lista:
        print(lista)
        for j, item in enumerate(words):
            for item2, k in range(4, number):
                #  esse if ta errado
                if j + item2 == i:
                    anteriores_especificos.append(item)
                    print(item)
    print(anteriores_especificos)
    return anteriores_especificos"""


def get_subsequent_in_document(lista, words, number):
    posteriores_especificos = []
    for i in lista:
        print(lista)
        for j, item in enumerate(words):
            for k, item2 in range(4, number):
                if j - item2 == i:

                    posteriores_especificos.append(item)
                    print(item)
    print(posteriores_especificos)
    return posteriores_especificos


def fill_itens(lista, word, words, dict1, dict2, dict3, dict4, number):
    """
    Preenche automaticamente as listas e os dicts de acordo com a palavra em análise
    :param lista: lista de índices da palavra em análise
    :param word: palavra em análise
    :param words: todas as palavras do texto
    :param dict1: lista de palavras anteriores à palavra em análise
    :param dict2: lista de palavras posteriores à palavra em análise
    :return: ela preenche as listas e os dicts
    """
    list_add = add_in_list(lista, word, words)
    add_itens_in_dicts(list_add, dict1, dict2, word, words)
    #  add_itens_in_dicts2(list_add, dict3, dict4, word, words, number)
    return list_add


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


def phrases(frase, number, dict1, dict2, dict3, dict4):
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
            anterior = desempate_anteriores(dict1, dict2, number)
            posterior = desempate_posteriores(dict3, dict4, number)
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
        num_list = fill_itens(lista_de_busca, word, words, previous, subsequent, previous2, subsequent2, number)
        for n in range(2, metade + 1):
            add_itens_in_dicts2(num_list, previous2, subsequent2, word, words, n)
        print(previous2)
        print(subsequent2)
        print("TEste+")
        most_frequent_previous, most_frequent_subsequent = dict_most_frequents(previous2, subsequent2,
                                                                               number, lista_de_busca)
        lista1, lista2 = check_tie(previous, subsequent, lista_de_busca)
        print(previous)
        frase = make_phrase(lista1, lista2, word, number)
        #  print("frase inicial: ", frase)
        if number > 3:
            nova_frase = phrases(frase, number, previous, previous2, subsequent, subsequent2)
            return print(nova_frase)
        return print(frase)
    return print("A palavra que você buscou não está no documento lido.")


if __name__ == "__main__":
    generate_sentence("essa", "cientifico", 6)
