import time
import pyautogui

pyautogui.PAUSE = 0.5 #Pausando a automação em segundo pois estava sendo muito rápido e o Chrome não conseguia abrir a tempo

pyautogui.press('win') #Serve para clicar em uma tecla no caso a do windows
pyautogui.write('chrome') #Escreve Chrome na barra de pesquisa 
pyautogui.press('enter') #Serve para dar um enter

link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)
pyautogui.press('enter')

time.sleep(3) #Deixando o transição mais de boa

pyautogui.click(x=699, y=377) #Colocando a posição do mouse
pyautogui.write('emailteste@gmail.com')
pyautogui.press('tab') #Passando para a cédemailteste@gmail.com senhatesteula de baixo de senha
pyautogui.write('senhateste')

pyautogui.click(x=952, y=535)
time.sleep(3)

import pandas #Serve para importar base de dados (no caso a produto.csv)
tabela = pandas.read_csv('produtos.csv') #Serve para ler o arquivo, como é um csv coloca _csv mas posso colocar read_pdf ou outros

print(tabela)