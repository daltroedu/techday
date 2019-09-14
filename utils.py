import glob
import os
import unicodedata
import smtplib
import getpass
import subprocess as msg
import datetime
# import pynotify
# import pdfkit

from urllib.request import urlopen
from PIL import Image
from datetime import datetime


# Verifica status de um site
def is_online(url):
    try:
        urlopen(url)
        return True
    except:
        return False


# Verifica se é um arquivo
def is_file(file):
    if os.path.isfile(file):
        return True
    else:
        return False


# Verifica se o arquivo/diretório existe
def is_file_dir_exists(file_dir):
    if os.path.exists(file_dir):
        return True
    else:
        return False


# Verifica se é Windows
def is_windows():
    if os.name == 'nt':
        return True
    else:
        return False


# Retorna o usuário da sessão
def get_user():
    return getpass.getuser()


# Input em formato de senha
def get_passwd(msg):
    passwd = getpass.getpass(prompt='') # ex: 'Senha: '
    return passwd


# Captura extensão do arquivo
def get_extension_file(file):
    return os.path.splitext(file)[1]


# Deleta todos os arquivos de determinado tipo de um diretório
def delete_all_files(dir_files, type_files):
    files_list = glob.glob(os.path.join(dir_files, type_files))
    for file in files_list:
        os.remove(file)


# Cria um diretório
def mkdir(dir_name):
    os.makedirs(dir_name)


# Diretório atual
def get_current_dir():
    return os.getcwd()


# Limpa tela do terminal
def clear_terminal_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Corta imagem
def cut_image(img, dimensions):
    img_1 = Image.open(img)
    img_2 = img_1.crop((int(dimensions[0]),
                        int(dimensions[1]),
                        int(dimensions[2]),
                        int(dimensions[3])))
    img_2.save(img)


# Remove acentos de uma string
def rm_acento(string):
    try:
        string = string.decode('utf-8')
    except:
        pass
    return unicodedata.normalize('NFD', string).encode('ascii', 'ignore')


# Alterar resolução do monitor, input ex.: '1600x900'
def change_resolution(resolution):
    os.system('xrandr -s ' + resolution)


# Envia notificação para o sistema
def notification_system(type_ntf, title, msg):
    try:
        msg.call(["notify-send", "-i", type_ntf, title, msg])
        # ex:
            # "error", "ERRO", "404"
            # "face-laugh", "OK","200"
            # "", "WAIT","300"
    except:
        print('Recurso indisponivel')


# Enviar e-mail simples
def send_email(server, port, login, passwd, dest, title, body):
    try:
        smtp = smtplib.SMTP(server, port) # ex: 'smtp.gmail.com', 587

        smtp.starttls()
        smtp.login(login, passwd)

        from_login = login
        to_send = [dest]
        msg = 'From: ' + from_login + '\nTo: ' + ', '.join(to_send) + '\nSubject: ' + title + '\n\n' + body
        
        smtp.sendmail(from_login, to_send, msg)
        smtp.quit()

        return True
    except Exception as erro:
        print(erro)
        return False


# Obtém a data atual
def get_date():
    return datetime.now().strftime("%d/%m/%y %H:%M:%S")


# Formata a data informada
def set_date(date):
    return datetime.strptime(date, "%d/%m/%Y %H:%M:%S").strftime("%d/%m/%y %H:%M:%S")


# Imprime PDF a partir de um link
# def get_pdf_url(link_pdf):
#     pdfkit.from_url(link_pdf)


if __name__ == '__main__':
    pass