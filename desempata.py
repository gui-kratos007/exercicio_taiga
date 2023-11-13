import random
from frequencia import *

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
    print(f"Palavra anterior com mais aparições: {previous_word}")
    subsequent_word = max(dict2, key=lambda k: dict2[k])

    # Verifica se há empate de palavras mais frequentes
    previous_word_tie = [word for word in dict1 if dict1[word] == dict1[previous_word]]
    subsequent_word_tie = [word for word in dict2 if dict2[word] == dict2[subsequent_word]]
    if len(lista) > 0:
        return previous_word_tie, subsequent_word_tie
    return print("não tem nenhuma palavra nas listas")

def desempate_anteriores(lista1, lista2):
    anteriores = []

    for i, item in enumerate(lista1):
        for j, item2 in enumerate(lista2):
            if item2 == item:
                anteriores.append(item)

    if len(anteriores) == 0:
        anteriores = lista1 + lista3
        escolha = random.choice(anteriores)
        return escolha
    elif len(anteriores) > 1:
        escolha = random.choice(anteriores)
        return escolha
    else:
        escolha = random.choice(anteriores)
        return escolha


def desempate_posteriores(lista1, lista2):
    posteriores = []

    for i, item in enumerate(lista1):
        for j, item2 in enumerate(lista2):
            if item2 == item:
                posteriores.append(item)
    if len(posteriores) == 0:
        posteriores = lista1 + lista2
        escolha = random.choice(posteriores)
        return escolha
    elif len(posteriores) > 1:
        escolha = random.choice(posteriores)
        return escolha
    else:
        escolha = random.choice(posteriores)
        return escolha