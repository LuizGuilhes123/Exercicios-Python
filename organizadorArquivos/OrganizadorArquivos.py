import os
import shutil

# Categorias de organização e suas extensões associadas
CATEGORIAS = {
    "Documentos": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Áudios": [".mp3", ".wav", ".ogg", ".flac"],
    "Vídeos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "Compactados": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Executáveis": [".exe", ".bat", ".sh"],
    "Outros": []
}

def organizar_pasta(pasta_alvo):
    """
    Organiza os arquivos na pasta especificada em subpastas baseadas em suas extensões.
    """
    if not os.path.exists(pasta_alvo):
        print(f"A pasta {pasta_alvo} não existe!.")
        return

    # Criar subpastas para categorias, se ainda não existirem
    for categoria in CATEGORIAS:
        caminho_categoria = os.path.join(pasta_alvo, categoria)
        os.makedirs(caminho_categoria, exist_ok=True)

    # Iterar pelos arquivos na pasta
    for arquivo in os.listdir(pasta_alvo):
        caminho_arquivo = os.path.join(pasta_alvo, arquivo)

        # Ignorar pastas
        if os.path.isdir(caminho_arquivo):
            continue

        # Encontrar a categoria com base na extensão
        _, extensao = os.path.splitext(arquivo)
        categoria_encontrada = "Outros"
        for categoria, extensoes in CATEGORIAS.items():
            if extensao.lower() in extensoes:
                categoria_encontrada = categoria
                break

        # Mover o arquivo para a subpasta apropriada
        destino = os.path.join(pasta_alvo, categoria_encontrada, arquivo)
        shutil.move(caminho_arquivo, destino)

    print(f"Arquivos organizados com sucesso na pasta: {pasta_alvo}")

# Caminho da pasta a ser organizada (modifique para sua necessidade)
pasta_para_organizar = input("Digite o caminho da pasta que deseja organizar: ")

# Executar a organização
organizar_pasta(pasta_para_organizar)
