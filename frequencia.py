import json


def calculate_percentage(ocurrences, total):
    """
    Uma fórmula para calcular porcentagem
    :param ocurrences: total de ocorrencias de um certo valor no meio de outros
    :param total: total de valores possíveis
    :return: retorna o valor calculado da porcentagem
    """
    percentage_value = (ocurrences / total) * 100
    return percentage_value


def print_percentage(dict1, dict2):
    """
    imprime as porcentagens de aparições das palavras de cada dict
    :param dict1: dicionário das palavras que aparecem antes da escolhida pelo usuário
    :param dict2: dicionário das palavras que aparecem depois da escolhida pelo usuário
    :return: 0, ou seja, indica ao SO que o programa foi bem sucedido
    """
    dict_porcentagem = {}
    dict_porcentagem["anteriores"] = {}
    dict_porcentagem["posteriores"] = {}
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
        dict_porcentagem["posteriores"][item] = percentage_value
    return dict_porcentagem


def main():
    dict1 = {"a": 3, "b": 5, "c": 7, "d": 4}
    dict2 = {"e": 1, "f": 6, "g": 8, "h": 9}
    print(json.dumps(print_percentage(dict1, dict2), indent=4))


if __name__ == "__main__":
    main()
