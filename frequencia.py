import json
import random
from desempata import *


def calculate_percentage(ocurrences, total):
    """
    Uma fórmula para calcular porcentagem
    :param ocurrences: total de ocorrencias de um certo valor no meio de outros
    :param total: total de valores possíveis
    :return: retorna o valor calculado da porcentagem
    """
    percentage_value = (ocurrences / total) * 100
    return percentage_value


def print_percentage_previous(dict1, dict2):
    """
    imprime as porcentagens de aparições das palavras de cada dict
    :param dict1: dicionário das palavras que aparecem antes da escolhida pelo usuário
    :param dict2: dicionário das palavras que aparecem depois da escolhida pelo usuário
    :return: 0, ou seja, indica ao SO que o programa foi bem sucedido
    """
    dict_porcentagem = {}
    dict_porcentagem["anteriores"] = {}
    dict_porcentagem["anteriores2"] = {}
    total_itens = sum(dict1.values())
    total_itens2 = sum(dict2.values())

    for item in dict1:
        ocurrences = dict1.get(item, 0)
        percentage_value = calculate_percentage(ocurrences, total_itens)
        #  print(item, "(", percentage_value, "%) \n")
        dict_porcentagem["anteriores"][item] = percentage_value
    for item in dict2:
        ocurrences = dict2.get(item, 0)
        percentage_value = calculate_percentage(ocurrences, total_itens2)
        #  print(item, "(", percentage_value, "%) \n")
        dict_porcentagem["anteriores2"][item] = percentage_value
    return dict_porcentagem


def print_percentage_subsequent(dict3, dict4):
    """
    imprime as porcentagens de aparições das palavras de cada dict
    :param dict3: dicionário das palavras que aparecem antes da escolhida pelo usuário
    :param dict4: dicionário das palavras que aparecem depois da escolhida pelo usuário
    :return: 0, ou seja, indica ao SO que o programa foi bem sucedido
    """
    dict_porcentagem = {}
    dict_porcentagem["posteriores"] = {}
    dict_porcentagem["posteriores2"] = {}
    total_itens = sum(dict3.values())
    total_itens2 = sum(dict4.values())

    for item in dict3:
        ocurrences = dict3.get(item, 0)
        percentage_value = calculate_percentage(ocurrences, total_itens)
        #  print(item, "(", percentage_value, "%) \n")
        dict_porcentagem["posteriores"][item] = percentage_value
    for item in dict4:
        ocurrences = dict4.get(item, 0)
        percentage_value = calculate_percentage(ocurrences, total_itens2)
        #  print(item, "(", percentage_value, "%) \n")
        dict_porcentagem["posteriores2"][item] = percentage_value
    return dict_porcentagem


def porcentagens_anteriores(result, lista):
    porcentagens1 = {}
    porcentagens2 = {}
    for key, value in result["anteriores"].items():
        for item in lista:
            if key == item:
                porcentagens1[key] = value

    for key, value in result["anteriores2"].items():
        for item in lista:
            if key == item:
                porcentagens2[key] = value

    return porcentagens1, porcentagens2


def porcentagens_posteriores(result, lista):
    porcentagens1 = {}
    porcentagens2 = {}
    for key, value in result["posteriores"].items():
        for item in lista:
            if key == item:
                porcentagens1[key] = value

    for key, value in result["posteriores2"].items():
        for item in lista:
            if key == item:
                porcentagens2[key] = value

    return porcentagens1, porcentagens2


def compare_frequencia_anteriores(result, lista):
    porcentagens1, porcentagens2 = porcentagens_anteriores(result, lista)
    valor1 = 0
    valor2 = 0
    resultado1 = ""
    resultado2 = ""
    for key, value in porcentagens1.items():
        if value > valor1:
            valor1 = value
            resultado1 = key

    for key, value in porcentagens2.items():
        if value > valor2:
            valor2 = value
            resultado2 = key

    if valor1 == valor2:
        resultado = desempatar2(resultado1, resultado2)
    elif valor1 > valor2:
        resultado = resultado1
    else:
        resultado = resultado2
    print(porcentagens1)
    print(porcentagens2)
    print(resultado)
    return resultado


def compare_frequencia_posteriores(result, lista):
    porcentagens1, porcentagens2 = porcentagens_posteriores(result, lista)
    valor1 = 0
    valor2 = 0
    resultado1 = ""
    resultado2 = ""
    for key, value in porcentagens1.items():
        if value > valor1:
            valor1 = value
            resultado1 = key

    for key, value in porcentagens2.items():
        if value > valor2:
            valor2 = value
            resultado2 = key

    if valor1 == valor2:
        resultado = desempatar2(resultado1, resultado2)
    elif valor1 > valor2:
        resultado = resultado1
    else:
        resultado = resultado2
    print(porcentagens1)
    print(porcentagens2)
    print(resultado)
    return resultado



def main():
    lista = ["a", "b", "c"]
    lista2 = ["e", "f", "g"]
    dict1 = {"a": 3, "b": 5, "c": 7, "d": 4}
    dict2 = {"a": 4, "b": 5, "c": 4}
    dict3 = {"e": 1, "f": 6, "g": 8, "h": 9}
    dict4 = {"e": 3, "f": 5, "g": 2, "h": 4}
    result_dict = print_percentage_previous(dict1, dict2)
    result_dict2 = print_percentage_subsequent(dict3, dict4)

    print(result_dict)
    compare_frequencia_anteriores(result_dict, lista)
    print("POSTERIORES:")
    compare_frequencia_posteriores(result_dict2, lista2)


if __name__ == "__main__":
    main()
