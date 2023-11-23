from carregar_arquivo import load_file


def get_style(style, list_styles):
    """
    verifica ser o estilo é valido, e se for, carrega ele
    :param style: estilo escolhido pelo usuário
    :param list_styles: lista de estilos validos
    :return: retorna o arquivo carregado
    """
    if style in list_styles:
        load_file(style)
        return 1
    else:
        print("Estilo não encontrado.")
        return 0
