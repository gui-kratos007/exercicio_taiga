import random
from carregar_arquivo import load_file

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
    return print("não tem nenhuma palavra nas listas")


def desempatar(lista):
    """
    escolhe um item aleatório da lista
    :param lista: lista de palavras a serem sorteadas
    :return: a escolha, ou seja, o item que foi sorteado
    """
    escolha = random.choice(lista)
    return escolha

def desempatar2(um, dois):
    lista = [um, dois]
    escolha = random.choice(lista)
    return escolha


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


def get_previous_in_phrase(word, words):
    """
    Essa função atribui valores à lista e as dicts de anteriores e posteriores criadas nesta função para
    que não fossem utiizadas as dicts originais, ou seja, com valores referentes e relacionados à palavra
    digitada pelo usuário, já que a palavra que deveria ser o parametro dessa vez não é a digitada pelo
    usuário antes. Depois disso ela realiza a função get_previous para a palavra inicial da frase.
    :param word: palavra inicial da frase
    :param words: todas as palavras presentes no texto
    :return: a função get_previous, ou seja, palavra anterior mais frequente ou mensagem de erro
    """
    lista = []
    previous1 = {}
    subsequent1 = {}
    fill_itens(lista, word, words, previous1, subsequent1)
    check_tie(previous1, subsequent1, lista)
    lista1, lista2 = check_tie(previous1, subsequent1, lista)

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


def get_subsequent_in_phrase(word, words):
    """
    Essa função atribui valores à lista e as dicts de anteriores e posteriores criadas nesta função para
    que não fossem utiizadas as dicts originais, ou seja, com valores referentes e relacionados à palavra
    digitada pelo usuário, já que a palavra que deveria ser o parametro dessa vez não é a digitada pelo
    usuário antes. Depois disso ela realiza a função get_subsequent para a palavra final da frase.
    :param word: palavra final da frase
    :param words: todas as palavras presentes no texto
    :return: a função get_subsequent, ou seja, palavra posterior mais frequente ou mensagem de erro
    """
    lista = []
    previous2 = {}
    subsequent2 = {}
    fill_itens(lista, word, words, previous2, subsequent2)
    check_tie(previous2, subsequent2, lista)
    lista1, lista2 = check_tie(previous2, subsequent2, lista)

    if word:
        options = {
            True: (desempatar(lista2)),
            False: (lista2[0])
        }

        immediate_subsequent = options[len(lista2) > 1]
        return immediate_subsequent
    return print("Essa palavra não esta no documento")



def make_phrase(lista1, lista2, word, number):
    anterior = get_previous(lista1, word)
    posterior = get_subsequent(lista2, word)
    frase = ""
    if number == 0:
        frase = "Você escolher zero numeros de palavras na frase"
    elif number == 1:
        option = desempatar2(anterior, posterior)
        if option == anterior:
            frase = f"{anterior} {word}"
        elif option == posterior:
            frase = f"{word} {posterior}"
    elif number == 2:
        frase = f"{anterior} {word} {posterior}"
    return frase


def phrases(frase, words, number):
    """
      Essa função imprime as frases mais provaveis de acordo com a frequencia das palavras. O usuário pode continuar
      o programa e formar frases maiores de acordo com a sua vontade
      :param frase: frase que foi formada anteiormente, quando o usuário digitou a palavra que ele quis
      :param words: todas as palavras presentes no texto
      :return: Mensagem de programa encerrado
      """
    resp = 0
    for i in range( 1, (number % 2))
    while resp < 1:
        palavras = frase.split()
        palavra_inicial = palavras[0]
        palavra_final = palavras[-1]
        anterior = get_previous_in_phrase(palavra_inicial, words)
        posterior = get_subsequent_in_phrase(palavra_final, words)
        nova_frase = f"{anterior} {frase} {posterior}"

        frase = nova_frase

        try:
            if resp != 0:
                print(nova_frase)
                break
            else:
                print(nova_frase)
        except ValueError:
            print("Digite um valor inteiro positivo")
    return print("Programa encerrado.")


def generate_sentence(word, style, number):
    lista_de_busca = []
    previous = {}
    subsequent = {}
    words = list_the_words(style)
    if word in words:
        fill_itens(lista_de_busca, word, words, previous, subsequent)
        check_tie(previous, subsequent, lista_de_busca)
        lista1, lista2 = check_tie(previous, subsequent, lista_de_busca)
        frase = check_print_tie(lista1, lista2, word)

        return frase
    return print("A palavra que você buscou não está no documento lido.")
