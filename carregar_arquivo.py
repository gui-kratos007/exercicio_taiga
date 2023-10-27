def load_file(style):
    """
        Esta função lê o arquivo e retorna o seu conteúdo, mas caso não exista ele retorna uma mensagem de erro.
        :return: mensagem de erro
    """
    try:

        with open(f"{style}.txt", 'r', encoding="utf-8") as file:
            dados = file.read()
            if dados:
                #  print(dados)
                return dados
        return print("arquivo vazio")

    except FileNotFoundError:
        print("O arquivo não foi encontrado. Certifique-se de que o caminho está correto e que o arquivo existe.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
