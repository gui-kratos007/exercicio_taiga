def get_style(style):
    """
        Esta função lê o arquivo e retorna o seu conteúdo, mas caso não exista ele retorna uma mensagem de erro.
        :return: mensagem de erro
    """
    if style in ["literario", "filosofico", "cientifico"]:
        with open(f"{style}.txt", 'r', encoding="utf-8") as file:
            dados = file.read()
            if dados:
                return dados
        return "arquivo vazio"
    else:
        print("Estilo não encontrado.")
