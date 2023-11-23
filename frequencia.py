"""As dicts de anteriores e anteriores2 já estão definidas aqui, só falta uma função que modifique
a anteriores, que é a dict de anteriores da palavra escolhida, para que ela va se alterando conforme
a necessidade, por exemplo:
o cara quer uma frase com 5 termos. Uma função que eu criei ja faz a primeira parte da frase, que conterá 3 termos.
A partir dai o programa preciasará pegar a anterior e posterior 2 casas de distancia da palavra no texto de onde ela
é tirada, então as anteriores à serem usadas para pegar porcentagem de aparição e comparar serão exclusivamente as
anteriores 2 casas de distancia da palavra no texto. Se ele quisesse uma frase do texto, o procedimento seria feito
pegando as palavras duas casas anteriores e fazendo o caminho necessário, e depois iria fazer o mesmo com palavras
anteriores 3 casas, e assim sucessivamente de acordo com a quantidade de termos que o cara escolher.
"""
from configs import *


def calculate_percentage(ocurrences, total):
    """
    Uma fórmula para calcular porcentagem
    :param ocurrences: total de ocorrencias de um certo valor no meio de outros
    :param total: total de valores possíveis
    :return: retorna o valor calculado da porcentagem
    """
    percentage_value = (ocurrences / total) * 100
    return percentage_value


def put_percentage_previous(dict1):
    """
    Aloca as porcentagens de aparições das palavras de cada dict
    :param dict1: dicionário das palavras que aparecem antes da escolhida pelo usuário
    :return: 0, ou seja, indica ao SO que o programa foi bem sucedido
    """
    dict_porcentagem = {}
    dict_porcentagem["anteriores"] = {}
    total_itens = sum(dict1.values())

    for item in dict1:
        ocurrences = dict1.get(item, 0)
        percentage_value = calculate_percentage(ocurrences, total_itens)
        #  print(item, "(", percentage_value, "%) \n")
        dict_porcentagem["anteriores"][item] = percentage_value
    return dict_porcentagem


def put_percentage_subsequent(dict3):
    """
    Aloca as porcentagens de aparições das palavras de cada dict
    :param dict3: dicionário das palavras que aparecem antes da escolhida pelo usuário
    :return: 0, ou seja, indica ao SO que o programa foi bem sucedido
    """
    dict_porcentagem = {}
    dict_porcentagem["posteriores"] = {}
    total_itens = sum(dict3.values())

    for item in dict3:
        ocurrences = dict3.get(item, 0)
        percentage_value = calculate_percentage(ocurrences, total_itens)
        #  print(item, "(", percentage_value, "%) \n")
        dict_porcentagem["posteriores"][item] = percentage_value
    return dict_porcentagem


def porcentagens_anteriores(result, lista):
    """
    ele vai pegar as palavras que são comuns nas duas dicts e que estão na lista
    e vai retornar outras duas dicts separadas contendo suas devidas porcentagens
    como valores.
    :param result: é a result_dict decorrente da junção em uma única dict das
    dicts "anteriores", que são as anteriores à palavra digitada pelo usuário,
    e "anteriores2", que são as anteriores à primeira palavra da frase.
    :param lista: lista de palavras que são comuns nas duas dicts
    :param lista: anteriores em comum, que estão presentes nas duas dicts de
    anteriores
    :return: porcentagens 1 e 2, que são respectivamente as dicts das porcentagens
    das palavras anteriores à palavra digitada pelo usuário, e a das porcentagens
    das palavras anteriores à primeira palavra da frase.
    """
    porcentagens = {}
    for key, value in result["anteriores"].items():
        for item in lista:
            if key == item:
                porcentagens[key] = value

    return porcentagens


def porcentagens_posteriores(result, lista):
    """
    ele vai pegar as palavras que são comuns nas duas dicts e que estão na lista
    e vai retornar outras duas dicts separadas contendo suas devidas porcentagens
    como valores.
    :param result: é a result_dict decorrente da junção em uma única dict das
    dicts "posteriores", que são as posteriores à palavra digitada pelo usuário,
    e "posteriores2", que são as posteriores à primeira palavra da frase.
    :param lista: lista de palavras que são comuns nas duas dicts
    :param lista: posteriores em comum, que estão presentes nas duas dicts de
    posteriores
    :return: porcentagens 1 e 2, que são respectivamente as dicts das porcentagens
    das palavras posteriores à palavra digitada pelo usuário, e a das porcentagens
    das palavras posteriores à última palavra da frase.
        """
    porcentagens = {}
    for key, value in result["posteriores"].items():
        for item in lista:
            if key == item:
                porcentagens[key] = value

    return porcentagens


def compare_frequencia_anteriores(result, lista):
    """
    Acha a palavra de maior frequencia das dicts de porcentagens 1 e 2, afim
    de comparar entre a palavra de maior frequencia da procentagens 1 e 2 e
    retornar qual delas é a mais frequente. Nesse caso as porcentagens 1 e 2
    são equivalentes às anteriores à palavra escolhida e às anteriores à
    primeira palavra do texto.
    :param result: é a result_dict decorrente da junção em uma única dict das
    dicts "anteriores", que são as anteriores à palavra digitada pelo usuário,
    e "anteriores2", que são as anteriores à primeira palavra da frase.
    :param lista: lista de palavras que são comuns nas duas dicts
    :return: retorna a palavra com maior frequencia entre todas
    """
    porcentagens = porcentagens_anteriores(result, lista)
    valor = 0
    resultado = ""
    for key, value in porcentagens.items():
        if value > valor:
            valor = value
            resultado = key
        elif value == valor:
            desempate = desempatar2(resultado, key)
            resultado = desempate
    print(porcentagens)
    print(resultado)
    return resultado


def compare_frequencia_posteriores(result, lista):
    """
    Acha a palavra de maior frequencia das dicts de porcentagens 1 e 2, afim
    de comparar entre a palavra de maior frequencia da porcentagens 1 e 2 e
    retornar qual delas é a mais frequente. Nesse caso as porcentagens 1 e 2
    são equivalentes às posteriores à palavra escolhida e às posteriores à
    última palavra do texto.
    :param result: é a result_dict decorrente da junção em uma única dict das
    dicts "posteriores", que são as posteriores à palavra digitada pelo usuário,
    e "posteriores2", que são as posteriores à primeira palavra da frase.
    :param lista: lista de palavras que são comuns nas duas dicts
    :return: retorna a palavra com maior frequencia entre todas
    """
    porcentagens = porcentagens_posteriores(result, lista)
    valor = 0
    resultado = ""
    for key, value in porcentagens.items():
        if value > valor:
            valor = value
            resultado = key
        elif value == valor:
            desempate = desempatar2(resultado, key)
            resultado = desempate
    return resultado



def main_teste():
    lista = ["a", "b", "c"]
    lista2 = ["e", "f", "g"]
    dict1 = {"a": 3, "b": 5, "c": 7, "d": 4}
    dict2 = {"a": 4, "b": 5, "c": 4}
    dict3 = {"e": 1, "f": 6, "g": 8, "h": 9}
    dict4 = {"e": 3, "f": 5, "g": 2, "h": 4}
    result_dict = put_percentage_previous(dict1)
    result_dict2 = put_percentage_subsequent(dict3)

    print(result_dict)
    compare_frequencia_anteriores(result_dict, lista)
    print("POSTERIORES:")
    compare_frequencia_posteriores(result_dict2, lista2)


if __name__ == "__main__":
    main_teste()
