import random
from carregar_arquivo import *


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


def fill_itens(lista, word, words, dict1, dict2):
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


def desempatar2(um, dois):
    """
    escolhe um item aleatorio dentre as 2 opções que forem designadas ao chamar essa função
    :param um: primeira opção das possiveis para desempatar
    :param dois: segunda opção das possiveis para desempatar
    :return: uma das duas opções possiveis, que sofreu uma escolha aleatória
    """
    lista = [um, dois]
    escolha = random.choice(lista)
    return escolha
