from carregar_arquivo import load_file


def get_style(style, list_styles):
    if style in list_styles:
        load_file(style)
        return 1
    else:
        print("Estilo não encontrado.")
        return 0
