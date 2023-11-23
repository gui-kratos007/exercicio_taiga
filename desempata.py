from frequencia import *
from configs import *


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
    """
    agrega as anteriores em comum das duas dicts(anteriores da palavra escolhida e anteriores da primeira palavra da
    frase) em uma dict de comuns e junta seus values. Em seguida verifica a quantidade de mais comuns e se for 0
    ele junta as dicts que mencionei antes e seus valores e utiliza a função de comparar para dar o resultado, ou seja
    a palavra que irá para o início da frase. No caso de só existir uma palavra em comum, ela será o resultado. Por
    fim se houver mais de uma a função de comparar será usada e trará o resultado.
    :param word: palavra escolhida pelo usuário
    :param dict2: anteriores em relação a palavra escolhida, que terá um valor diferente a cada rotação da função
    phrases do arquivo frase.py.
    :param number: numero de termos escolhidos pelo usuário
    :param words: palavras do texto que foi escolhido pelo usuário
    :return: palavra que será acoplada ao inicio da frase.
    """
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


def desempate_posteriores(word, dict4, number, words):
    """
    agrega as posteriores em comum das duas dicts(posteriores da palavra escolhida e posteriores da ultima palavra da
    frase) em uma dict de comuns e junta seus values. Em seguida verifica a quantidade de mais comuns e se for 0
    ele junta as dicts que mencionei antes e seus valores e utiliza a função de comparar para dar o resultado, ou seja
    a palavra que irá para o fim da frase. No caso de só existir uma palavra em comum, ela será o resultado. Por
    fim se houver mais de uma a função de comparar será usada e trará o resultado.
    :param word: palavra escolhida pelo usuário
    :param dict4: posteriores em relação a palavra escolhida, que terá um valor diferente a cada rotação da função
    phrases do arquivo frase.py.
    :param number: numero de termos escolhidos pelo usuário
    :param words: palavras do texto que foi escolhido pelo usuário
    :return: palavra que será acoplada ao fim da frase.
    """
    posteriores_em_comum = {}
    posteriores_total = {}
    metade = number // 2
    lista = []
    previous1 = {}
    subsequent1 = {}
    fill_itens(lista, word, words, previous1, subsequent1)
    posteriores_total.update(subsequent1)
    for i, n in enumerate(range(2, metade + 1)):
        posteriores_total.update(dict4[f"distancia {n}"].items())

    for i, n in enumerate(range(2, metade + 1)):
        for key, value in subsequent1.items():
            for key2, value2 in dict4[f"distancia {n}"].items():
                if key == key2:
                    posteriores_em_comum[key] = value + value2

    if len(posteriores_em_comum) == 0:
        result_dict = put_percentage_previous(posteriores_total)
        escolha = compare_frequencia_anteriores(result_dict, posteriores_total)
        return escolha
    elif len(posteriores_em_comum) == 1:
        for key, value in posteriores_em_comum.items():
            escolha = key
            return escolha
    else:
        result_dict = put_percentage_subsequent(posteriores_em_comum)
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


def desempata_lista(lista):
    """
    não esta sendo usada, mas se a lista for maior que 1 ele usa a função desempatar para desempatar ela, e o grande
    diferencial é que se a lista for igual a 1 ela retorna o item inicial da lista, já que por ser unico, não tem com
    o que desempatar
    :param lista: uma lista que precisar ser desempatada
    :return: item da lista que foi sorteado, ou, no caso de ser uma lista de um unico item, retorna esse item.
    """
    options = {
        True: (desempatar(lista)),
        False: (lista[0])
    }

    immediate_word = options[len(lista) > 1]
    return immediate_word
