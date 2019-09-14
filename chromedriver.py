# Python
    # https://www.python.org/

# Instalando o pip
    # Windows
        # Download: https://bootstrap.pypa.io/get-pip.py
        # > python get-pip.py
    # Linux: apt install python3-pip

# Chromedriver: https://chromedriver.chromium.org/downloads
# DOM: https://www.w3schools.com/whatis/whatis_htmldom.asp
# XPATH: https://www.w3schools.com/xml/xpath_intro.asp
# Selenium: https://www.seleniumhq.org/


import sys
import os
import utils
import pandas_utils 

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# Diretório padrão do executável do chromedriver
CHROMEDRIVER = os.getcwd() + '/driver/chromedriver'


def load(headless, download, dir_download):
    options = webdriver.ChromeOptions()

    # Se headless == True, então o driver é executado sem exibir o navegador
    if headless:
        options.add_argument('--headless')

    # Se download == True, então é configurado o diretório de download padrão
    if download:
        options.add_experimental_option('prefs', {'download.default_directory':   dir_download,
                                                  'download.prompt_for_download': False,
                                                  'download.directory_upgrade':   True})

    try:
        # Primeiro tenta carregar o driver automaticamente através do ChromeDriverManager
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        print('> Driver carregado via ChromeDriverManager')
    except:
        try:
            # Se não conseguir, tenta através de um executável local
            driver = webdriver.Chrome(CHROMEDRIVER, options=options)
            print('> Driver carregado via chromedriver')
        except Exception as erro:
            # Se as duas opções deram erro, então retorna uma exceção e encerra o aplicativo
            print(str(erro) + '\n> Baixe o chromedriver de acordo com a versao instalada do Google Chrome')
            sys.exit()
    
    # Permite fazer download em modo headless, logo headless em options precisa ser True
    if headless:
        try:
            driver.command_executor._commands['send_command'] = ('POST', '/session/$sessionId/chromium/send_command')
            driver.execute('send_command', {'cmd':    'Page.setDownloadBehavior',
                                            'params': {'behavior': 'allow', 'downloadPath': dir_download}})

            print('> Configuracoes de download em modo headless efetuadas com sucesso')
        except Exception as erro:
            print(str(erro) + '\n> Nao foi possivel efetuar as configuracoes de download em modo headless')

    return driver


def init():
    try:
        # Se for Linux, fecha todos os processos do chromedriver previamente abertos
        os.system('killall -9 chromedriver')
    except:
        pass

    driver = load(False, False, None)

    URL = 'https://www.unifacs.br'

    try:
        print('Site: ' + URL)
        driver.get(URL)  

        # TODO

        input()
    except Exception as erro:
        print(str(erro) + '\n> Nao foi possivel carregar o driver')

    driver.quit()


if __name__ == '__main__':
    init()

    # Dependências
        # pip install selenium
        # pip install webdriver-manager

    # Principais funções
        # Maximizar/minimizar janela
            # driver.maximize_window()
            # driver.minimize_window()

        # Capturar texto de um elemento
            # driver.find_element_by_xpath('').text
        
        # Captura vários elementos e exibe iterativamente
            # elements = driver.find_elements_by_xpath('')
            # for elem in elements:
            #     print(elem.text)

        # Inserir texto em formulários ou listas
            # driver.find_element_by_xpath('').send_keys('')
        
        # Apagar dados de formulários
            # driver.find_element_by_xpath('').clear()

        # Clicar em botões
            # driver.find_element_by_xpath('').click()

        # Capturar o conteúdo de um atributo, como um link
            # driver.find_element_by_xpath('').get_attribute('href')
        
        # Rolar/descer a página
            # driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')  

        # Aguardar X segundos até que determinado elemento da página seja carregado
            # WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '')))

        # Tira print da tela
            # driver.save_screenshot('')

        # Capturando, lendo e confirmando alertas
            # alert = driver.switch_to_alert()
            # alert_text = alert.text
            # alert.accept()