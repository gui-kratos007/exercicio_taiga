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


def get_previous_in_document(lista, words, number):
    anteriores_especificos = []
    for i in lista:
        print(lista)
        for j, item in enumerate(words):
            for item2, k in range(4, number):
                #  esse if ta errado
                if j + item2 == i:
                    anteriores_especificos.append(item)
                    print(item)
    print(anteriores_especificos)
    return anteriores_especificos


num = 4
for i, item in range(4, number):
    #  aqui embaixo é a função
    anteriores_especificos = []
    for j in lista:
        for k, item2 in enumerate(words):
            if k + item == j:
                anteriores_especificos.append(item)
    return anteriores_especificos


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
    return list_add

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


while resp == 0:
    for i in range(1, number -3):
        for j, item in enumerate(words):
            for k, item2 in enumerate(lista):



def get_previous_in_phrase(word, words, number):
    """
    Essa função atribui valores à lista e as dicts de anteriores e posteriores criadas nesta função para
    que não fossem utiizadas as dicts originais, ou seja, com valores referentes e relacionados à palavra
    digitada pelo usuário, já que a palavra que deveria ser o parametro dessa vez não é a digitada pelo
    usuário antes. Depois disso ela realiza a função get_previous para a palavra inicial da frase.
    :param word: palavra inicial da frase
    :param words: todas as palavras presentes no texto
    :param number: numero de termos escolhidos pelo usuário
    :return: a função get_previous, ou seja, palavra anterior mais frequente ou mensagem de erro
    """
    lista = []
    previous1 = {}
    subsequent1 = {}
    immediate_previous_list = []
    fill_itens(lista, word, words, previous1, subsequent1)
    anteriores_especificos = add_itens_in_previous_specifics(lista, words, number)
    anteriores_mais_frequentes = check_tie(anteriores_especificos, subsequent1, lista)
    lista1, lista2 = check_tie(previous1, subsequent1, lista)

    for i, item in enumerate(lista1):
        print(f"index: {i}, item: {item}")
        for j, item2 in enumerate(anteriores_especificos):
            if lista1[i] == anteriores_especificos[j]:
                previous = anteriores_especificos[j]
                immediate_previous_list.append(previous)
    if len(immediate_previous_list) > 1:
        immediate_previous = desempatar(immediate_previous_list)
        return immediate_previous
    elif len(immediate_previous_list) == 1:
        immediate_previous = immediate_previous_list[0]
        return immediate_previous
    elif len(immediate_previous_list) < 1:
        immediate_previous = desempata_lista(lista1)
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


def get_subsequent_in_phrase(word, words, number):
    """
    Essa função atribui valores à lista e as dicts de anteriores e posteriores criadas nesta função para
    que não fossem utiizadas as dicts originais, ou seja, com valores referentes e relacionados à palavra
    digitada pelo usuário, já que a palavra que deveria ser o parametro dessa vez não é a digitada pelo
    usuário antes. Depois disso ela realiza a função get_previous para a palavra inicial da frase.
    :param word: palavra inicial da frase
    :param words: todas as palavras presentes no texto
    :param number: numero de termos escolhidos pelo usuário
    :return: a função get_previous, ou seja, palavra anterior mais frequente ou mensagem de erro
    """
    lista = []
    previous1 = {}
    subsequent1 = {}
    immediate_subsequent_list = []
    fill_itens(lista, word, words, previous1, subsequent1)
    posteriores_especificos = get_subsequent_in_document(lista, words, number)
    check_tie(previous1, subsequent1, lista)
    lista1, lista2 = check_tie(previous1, subsequent1, lista)

    for i, item in enumerate(lista2):
        for j, item2 in enumerate(posteriores_especificos):
            if lista2[i] == posteriores_especificos[j]:
                subsequent = posteriores_especificos[j]
                immediate_subsequent_list.append(subsequent)
    if len(immediate_subsequent_list) > 1:
        immediate_subsequent = desempatar(immediate_subsequent_list)
        return immediate_subsequent
    elif len(immediate_subsequent_list) == 1:
        immediate_subsequent = immediate_subsequent_list[0]
        return immediate_subsequent
    elif len(immediate_subsequent_list) < 1:
        immediate_subsequent = desempata_lista(lista2)
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


def phrases(frase, words, number):
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
            anterior = get_previous_in_phrase(palavra_inicial, words, number)
            posterior = get_subsequent_in_phrase(palavra_final, words, number)
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
    subsequent = {}
    words = list_the_words(style)
    if word in words:
        fill_itens(lista_de_busca, word, words, previous, subsequent)
        """add_previous_n(number, lista_de_busca, words)"""
        """sequency_anteriores(lista_de_busca, words)
        sequency_posteriores(lista_de_busca, words)
        anteriores = sequency_anteriores(lista_de_busca, words)"""
        previous_specifics = add_itens_in_previous_specifics(lista_de_busca, words, number)
        subsequent_specifics = add_itens_in_subsequent_specifics(lista_de_busca, words, number)
        """anteriores1 = anteriores[0]
        print(anteriores1[1])"""
        lista1, lista2 = check_tie(previous, subsequent, lista_de_busca)
        lista3, lista4 = check_tie(previous_specifics, subsequent_specifics, lista_de_busca)
        print("ESSAS: ")
        print(lista1)
        print(lista2)
        print(lista3)
        print(lista4)
        frase = make_phrase(lista1, lista2, word, number)
        #  print("frase inicial: ", frase)
        if number > 3:
            nova_frase = phrases(frase, words, number)
            return print(nova_frase)
        return print(frase)
    return print("A palavra que você buscou não está no documento lido.")


generate_sentence("essa", "cientifico", 4)
