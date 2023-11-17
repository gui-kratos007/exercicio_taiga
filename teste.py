def get_previous_in_document(dict, words, number, word, list):
    anteriores_especificos = {}
    for key, value in dict.items():
        for i, item in enumerate(words):
            for j in list:
                for k in range(4, number):
                    if key == item and i + k == list[j]:
                        anteriores_especificos[key] = value
                        print(anteriores_especificos)


def main():
    dict = {"as": 25, "elas": 25, "balsa": 25}
    words = ["as", "elas", "as", "elas", "o", "o", "balsa", "balsa"]
    number = 5
    list = [1, 3]
    get_previous_in_document(dict, words, number, list)
