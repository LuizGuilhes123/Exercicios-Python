import os
import subprocess
import webbrowser
import time

# Configuração do navegador Opera
OPERA_PATH = r"C:\Program Files\Opera\launcher.exe"
webbrowser.register('opera', None, webbrowser.BackgroundBrowser(OPERA_PATH))


def abrir_navegador(url):
    """Abre o Opera com a URL especificada."""
    webbrowser.get('opera').open(url)
    time.sleep(2)


def criar_aba(url):
    """Abre uma nova aba no Opera."""
    webbrowser.get('opera').open_new_tab(url)


def fechar_janelas():
    """Fecha janelas do Opera."""
    if os.name == "nt":  # Windows
        os.system("taskkill /IM opera.exe /F")
    elif os.name == "posix":  # Linux/Mac
        os.system("pkill opera")
    else:
        print("Sistema não suportado para fechamento de janelas.")


def abrir_vscode():
    """Abre o Visual Studio Code como administrador."""
    caminho = r"C:\Users\Guilherme\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code"
    subprocess.run(["powershell", "-Command", f"Start-Process '{caminho}' -Verb RunAs"])


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
        print("1. Abrir navegador com URL específica (Opera)")
        print("2. Criar nova aba no navegador (Opera)")
        print("3. Fechar todas as janelas do Opera")
        print("4. Abrir VSCode (como admin)")
        print("5. Abrir PyCharm (como admin)")
        print("6. Abrir IntelliJ (como admin)")
        print("0. Sair")

        escolha = input("Digite sua escolha: ")

        if escolha == "1":
            url = input("Digite a URL que deseja abrir: ")
            abrir_navegador(url)
        elif escolha == "2":
            url = input("Digite a URL para a nova aba: ")
            criar_aba(url)
        elif escolha == "3":
            fechar_janelas()
        elif escolha == "4":
            abrir_vscode()
        elif escolha == "5":
            abrir_pycharm()
        elif escolha == "6":
            abrir_intellij()
        elif escolha == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()