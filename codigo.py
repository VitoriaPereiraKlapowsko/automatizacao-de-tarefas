import time
import pyautogui

pyautogui.PAUSE = 0.5 #Pausando a automação em segundo pois estava sendo muito rápido e o Chrome não conseguia abrir a tempo

pyautogui.press('win') #Serve para clicar em uma tecla no cCAHA000275   Marca Teste Tipo Teste  Categoria Teste Codigo Teste    Preo Teste  Custo Teste aso a do windows
pyautogui.write('chrome') #Escreve Chrome na barra de pesquisa 
pyautogui.press('enter') #Serve para dar TELG000821 Marca Teste Tipo Teste  Categoria Teste Codigo Teste    Preo Teste  Custo Teste Observao Teste      CustoMOMU000111 Marca Teste Tipo Teste  Categoria TesteCAHA000252 Marca Teste Tipo Teste  Categoria Teste Codigo Test Observao Teste  

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
tabela = pandas.read_csv('produtos.csv') #Semailteste@gmail.com senhatesteerve para ler o arquivo, como é um csv coloca _csv mas posso colocar read_pdf ou outros
print(tabela)

for linha in tabela.index: #Index pois o Pandas chama de index cada indice/linha
    pyautogui.click(x=681, y=257)
    
    codigo = tabela.loc[linha, "codigo"] 
    pyautogui.write(codigo)
    pyautogui.press('tab')  
    
    pyautogui.write(tabela.loc[linha, "marca"]) #Localizando(loc) a informação da tabela
    pyautogui.press('tab')
    
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press('tab')
    
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press('tab')
    
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press('tab')
    
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press('tab')
    
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs): #Se no Pandas não tiver obs ou seja for null passa para o próximo sem dar problema
        pyautogui.write(obs)
    pyautogui.press('tab')

    pyautogui.press('enter')
    pyautogui.scroll(5000)