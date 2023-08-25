# Automação de encaminhamento de mensagens no WhatsApp
# Usando a Funcionalidade nativa do WhatsApp de encaminhar mensagem
# Encaminhar de 5 em  5 mensagens

import time
import pyperclip
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)
browser.get('https://web.whatsapp.com')
time.sleep(360)

mensagem = ' Teste de automatização de mensagem pelo Whatsapp'
lista_de_contatos = ['Lucas Gomes', 'Mãe', 'Pai']

# Enviando as mensagens para meu número

browser.find_element('xpath', '//*[@id="side"]/div[1]/div/div/button/div[2]/span').click()
browser.find_element('xpath', '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p').send_keys('Lucas Gomes')
browser.find_element('xpath', '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p').send_keys(Keys.ENTER)

# Escrevendo mensagem para a lista de distribuição
pyperclip.copy(mensagem)
browser.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.CONTROL + 'v')
browser.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.ENTER)