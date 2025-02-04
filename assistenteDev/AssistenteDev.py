import os
import subprocess
import webbrowser
import time

# Caminho correto para o executável do Opera GX
OPERA_PATH = r"C:\Users\Guilherme\AppData\Local\Programs\OperaGX\opera.exe"
webbrowser.register('opera', None, webbrowser.BackgroundBrowser(OPERA_PATH))

# Caminho correto para o Visual Studio Code
VS_CODE_PATH = r"C:\Users\Guilherme\AppData\Local\Programs\Microsoft VS Code\Code.exe"

def abrir_navegador(busca):
    """Abre o Opera GX com a pesquisa específica."""
    url = f"https://www.google.com/search?q={busca}"  # Pesquisa no Google
    webbrowser.get('opera').open(url)
    time.sleep(2)

def criar_aba(busca):
    """Abre uma nova aba no Opera GX com a pesquisa."""
    url = f"https://www.google.com/search?q={busca}"  # Pesquisa no Google
    webbrowser.get('opera').open_new_tab(url)

def fechar_todas_janelas():
    """Fecha todas as janelas abertas no sistema (similar ao Alt+F4)."""
    if os.name == "nt":  # Windows
        os.system("taskkill /F /FI \"STATUS eq RUNNING\"")  # Fecha todas as janelas em execução
    elif os.name == "posix":  # Linux/Mac
        os.system("pkill -9")  # Mata todos os processos
    else:
        print("Sistema não suportado para fechamento de janelas.")

def abrir_youtube():
    """Abre o YouTube no Opera GX."""
    url = "https://www.youtube.com"
    webbrowser.get('opera').open(url)

def abrir_chatgpt():
    """Abre o ChatGPT no Opera GX."""
    url = "https://chat.openai.com"
    webbrowser.get('opera').open(url)

def abrir_github():
    """Abre o perfil do GitHub no Opera GX."""
    url = "https://github.com/LuizGuilhes123"
    webbrowser.get('opera').open(url)

def fechar_janelas():
    """Fecha janelas do Opera GX."""
    if os.name == "nt":  # Windows
        os.system("taskkill /IM opera.exe /F")
    elif os.name == "posix":  # Linux/Mac
        os.system("pkill opera")
    else:
        print("Sistema não suportado para fechamento de janelas.")

def abrir_vscode():
    """Abre o Visual Studio Code."""
    subprocess.run([VS_CODE_PATH])

def abrir_pycharm():
    """Abre o PyCharm como administrador."""
    caminho = r"C:\Program Files\JetBrains\PyCharm Community Edition 2024.3\bin\pycharm64.exe"
    subprocess.run(["powershell", "-Command", f"Start-Process '{caminho}' -Verb RunAs"])

def abrir_intellij():
    """Abre o IntelliJ IDEA como administrador."""
    caminho = r"C:\Program Files\JetBrains\IntelliJ IDEA Community Edition 2023.3.3\bin\idea64.exe"
    subprocess.run(["powershell", "-Command", f"Start-Process '{caminho}' -Verb RunAs"])

def menu():
    """Menu principal para o usuário selecionar a ação desejada."""
    while True:
        print("\nAssistente Dev - Escolha uma opção:")
        print("1. Pesquisar no Opera GX")
        print("2. Criar nova aba no Opera GX com pesquisa")
        print("3. Fechar todas as janelas abertas (Alt+F4)")
        print("4. Abrir YouTube")
        print("5. Abrir ChatGPT")
        print("6. Abrir GitHub (perfil LuizGuilhes123)")
        print("7. Fechar todas as janelas do Opera GX")
        print("8. Abrir VSCode")
        print("9. Abrir PyCharm (como admin)")
        print("10. Abrir IntelliJ (como admin)")
        print("0. Sair")

        escolha = input("Digite sua escolha: ")

        if escolha == "1":
            busca = input("Digite o que deseja pesquisar: ")
            abrir_navegador(busca)
        elif escolha == "2":
            busca = input("Digite o que deseja pesquisar para a nova aba: ")
            criar_aba(busca)
        elif escolha == "3":
            fechar_todas_janelas()
        elif escolha == "4":
            abrir_youtube()
        elif escolha == "5":
            abrir_chatgpt()
        elif escolha == "6":
            abrir_github()
        elif escolha == "7":
            fechar_janelas()
        elif escolha == "8":
            abrir_vscode()
        elif escolha == "9":
            abrir_pycharm()
        elif escolha == "10":
            abrir_intellij()
        elif escolha == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
