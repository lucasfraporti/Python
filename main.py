from datetime import date
import zipfile
import os
# import pyautogui
# import pyperclip

# Opção 1 e 2
# Verificar se o diretório é válido
def validar_directory():
    x = False
    while True:
        directory = input("Digite o diretório para validação: ")
        if(os.path.exists(directory)):
            exists = print(f"O diretório {directory} existe.")
            x = True
        else:
            exists = print(f"O diretório {directory} não existe, digite novamente.")
        if(x):
            break
    return exists

# Opção 3
# Obter todos os arquivos que estão dentro da pasta que o usuário informou
def listar_archives(directory):
    if(os.path.exists(directory)):
        arq_nomes = os.listdir(directory)
        if(arq_nomes != []):
            for nome in arq_nomes:
                print(nome)
        else:
            print(f"O diretório {directory} está vazio.")
    else:
        print(f"O diretório {directory} não existe.")

# Opção 4
# Realizar a compactação de todos os arquivos que tem dentro da pasta que o usuário informou. 
# Se já tiver um arquivo compactado, ele será compactado para dentro desse novo .zip.
def compactar_tudo(directory, newdirectory):
    if(os.path.exists(directory) and os.path.exists(newdirectory)):
        data_atual = date.today()
        arq_nomes = os.listdir(directory)
        os.chdir(directory)
        if(arq_nomes != []):
            with zipfile.ZipFile(f"{newdirectory}\\"+"backup"+str(data_atual)+".zip", "w") as arq_compactado:
                for nome in arq_nomes:
                    arq_compactado.write(nome)
            print(f"Todos os arquivos dentro do diretório {directory} foram compactados para o diretório {newdirectory}")
        else:
            print(f"O diretório {directory} está vazio.")
    elif(os.path.exists(directory) and (newdirectory == "")):
        data_atual = date.today()
        arq_nomes = os.listdir(directory)
        os.chdir(directory)
        if(arq_nomes != []):
            with zipfile.ZipFile("backup"+str(data_atual)+".zip", "w") as arq_compactado:
                for nome in arq_nomes:
                    arq_compactado.write(nome)
            print(f"Todos os arquivos dentro do diretório {directory} foram compactados para o mesmo diretório.")
        else:
            print(f"O diretório {directory} está vazio.")
    else:
        print(f"Houve algum problema nos diretórios {directory} e/ou {newdirectory}")

# Opção 5
# Utilização do pyautogui e pyperclip para upload no Google Drive
def google_drive_automatization(directory):
    # if(os.path.exists(directory)):
    #     pyautogui.PAUSE = 3

    #     pyautogui.hotkey("Win", "r") 
    #     pyautogui.hotkey("ctrl", "a") 
    #     pyautogui.PAUSE = 1
    #     pyperclip.copy(directory)
    #     pyautogui.hotkey("ctrl", "v")
    #     pyautogui.PAUSE = 2

    #     pyautogui.press("enter")
    #     pyautogui.PAUSE = 3

    #     pyautogui.press("down")
    #     pyautogui.PAUSE = 3
    #     pyautogui.hotkey("ctrl", "c")
    #     pyautogui.hotkey("ctrl", "c")
    #     copiar = pyautogui.locateOnScreen('copiar.png')
    #     pyautogui.moveTo(copiar)
    #     pyautogui.leftClick(duration=0.1)

    #     pyautogui.hotkey("Win","r")
    #     pyautogui.write("opera", interval=0.1)
    #     pyautogui.press("enter")
    #     pyautogui.click(x=547, y=49, clicks = 1)
    #     pyautogui.hotkey("ctrl","a")
    #     pyautogui.write("drive.google.com ", interval=0.1)
    #     pyautogui.press("enter")
    #     # Novo botão
    #     # pyautogui.click(x=122, y=199, clicks = 1)
    #     novo = pyautogui.locateOnScreen('novo_botao.png')
    #     pyautogui.moveTo(novo)
    #     pyautogui.leftClick(duration=0.1)

    #     # Upload
    #     # pyautogui.click(x=122, y=255, clicks = 1)
    #     upload = pyautogui.locateOnScreen('upload_arquivos.png')
    #     pyautogui.moveTo(upload)
    #     pyautogui.leftClick(duration=0.1)

    #     # Seleção do arquivo
    #     pyautogui.click(x=165, y=377, clicks = 1)

    #     # Caso houver dois arquivos iguais
    #     manter = pyautogui.locateOnScreen('manter.png')
    #     pyautogui.moveTo(manter)
    #     pyautogui.leftClick(duration=0.1)

    #     # Manter os dois arquivos no Google Drive
    #     manter = pyautogui.locateOnScreen('fazer_upload.png')
    #     pyautogui.moveTo(manter)
    #     pyautogui.leftClick(duration=0.1)
    # else:
    #     print(f"O diretório {directory} não existe.")
    pass

def this_system_dir():
    atual_path = os.getcwd()
    print(f"Este sistema está sendo executado no diretório {atual_path}")

if __name__ == '__main__':
    while True:
        user = input("Opção 1: Verificação de diretório de entrada.\nOpção 2: Verificação de diretório de saída.\nOpção 3: Listagem dos arquivos que estão dentro da pasta.\nOpção 4: Compactação da pasta desejada.\nOpção 5: Upload do arquivo compactado para o Google Drive.\nOpção 6: Informar o diretório que este sistema está sendo executado.\nSelecione uma opção: ")
        if(user == "1" or user == "2"):
            validar_directory()

        elif(user == "3"):
            pasta = input("Digite o endereço da pasta que será compactada: ")
            listar_archives(pasta)

        elif(user == "4"):
            pasta = input("Digite o endereço de entrada (pasta que será compactada): ")
            newpasta = input("Digite o endereço de saída (diretório para salvar o .zip): ")
            compactar_tudo(pasta, newpasta)

        elif(user == "5"):
            pasta = input("Digite o endereço da pasta que possui o .zip: ")
            google_drive_automatization(pasta)

        elif(user == "6"):
            this_system_dir()

        else:
            print(f"Selecione uma opção válida.")