import random
from frequencia import *
from frase import *

def check_tie(dict1, dict2, lista):
    """
    Encontra as palavras mais frequentes e ve se tem empate de aparições
    :param dict1: dict das palavras anteriores
    :param dict2: dict das palavras posteriores
    :param lista: lista de indices da palavra escolhida pelo usuário
    :return: mensagem de erro
    """
    # Encontra a(s) palavra(s) mais frequente(s)
    previous_word = max(dict1, key=lambda k: dict1[k])
    subsequent_word = max(dict2, key=lambda k: dict2[k])

    # Verifica se há empate de palavras mais frequentes
    previous_word_tie = [word for word in dict1 if dict1[word] == dict1[previous_word]]
    subsequent_word_tie = [word for word in dict2 if dict2[word] == dict2[subsequent_word]]
    if len(lista) > 0:
        return previous_word_tie, subsequent_word_tie
    return print("não tem inhumane palavra nas listas")


def desempate_anteriores(word, dict2, number, words):
    anteriores_em_comum = {}
    anteriores_total = {}
    metade = number // 2
    lista = []
    previous1 = {}
    subsequent1 = {}
    fill_itens(lista, word, words, previous1, subsequent1)
    anteriores_total.update(previous1)
    for i, n in enumerate(range(2, metade + 1)):
        anteriores_total.update(dict2[f"distancia {n}"].items())

    for i, n in enumerate(range(2, metade + 1)):
        for key, value in previous1.items():
            for key2, value2 in dict2[f"distancia {n}"].items():
                if key == key2:
                    anteriores_em_comum[key] = value + value2

    if len(anteriores_em_comum) == 0:
        result_dict = put_percentage_previous(anteriores_total)
        escolha = compare_frequencia_anteriores(result_dict, anteriores_total)
        return escolha
    elif len(anteriores_em_comum) == 1:
        for key, value in anteriores_em_comum.items():
            escolha = key
            return escolha
    else:
        result_dict = put_percentage_previous(anteriores_em_comum)
        escolha = compare_frequencia_anteriores(result_dict, anteriores_em_comum)
        return escolha


    """anteriores_em_comum = []

    for i, item in enumerate(lista1):
        for j, item2 in enumerate(lista2):
            if item2 == item:
                anteriores_em_comum.append(item)

    if len(anteriores_em_comum) == 0:
        anteriores = lista1 + lista2
        escolha = random.choice(anteriores)
        return escolha
    elif len(anteriores_em_comum) == 1:
        escolha = anteriores_em_comum[0]
        return escolha
    else:
        result_dict = put_percentage_previous(dict1, dict2)
        escolha = compare_frequencia_anteriores(result_dict, anteriores_em_comum)
        return escolha"""


def desempate_posteriores(word, dict4, number, words):
    posteriores_em_comum = {}
    posteriores_total = {}
    metade = number // 2
    lista = []
    previous1 = {}
    subsequent1 = {}
    fill_itens(lista, word, words, previous1, subsequent1)

    for i, n in enumerate(range(2, metade + 1)):
        for key, value in subsequent1.items():
            for key2, value2 in dict4[f"distancia {n}"].items():
                if key == key2:
                    posteriores_em_comum[key] = value + value2

    if len(posteriores_em_comum) == 0:
        posteriores_total.update(subsequent1)
        posteriores_total.update(dict4)
        result_dict = put_percentage_subsequent(subsequent1, dict4)
        escolha = compare_frequencia_posteriores(result_dict, posteriores_total)
        return escolha
    elif len(posteriores_em_comum) == 1:
        for key, value in posteriores_em_comum.items():
            escolha = key
            return escolha
    else:
        result_dict = put_percentage_subsequent(subsequent1, dict4)
        escolha = compare_frequencia_posteriores(result_dict, posteriores_em_comum)
        return escolha

def desempatar(lista):
    """
    escolhe um item aleatório da lista
    :param lista: lista de palavras a serem sorteadas
    :return: a escolha, ou seja, o item que foi sorteado
    """
    escolha = random.choice(lista)
    return escolha


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


def desempata_lista(lista):
    options = {
        True: (desempatar(lista)),
        False: (lista[0])
    }

    immediate_word = options[len(lista) > 1]
    return immediate_word
