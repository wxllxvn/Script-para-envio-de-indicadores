#importando libs que irei usar
import pandas as pd 
import pyautogui as pg
from datetime import datetime
from datetime import date
import time
import requests

#imprtando API para datas
data = requests.get('http://worldtimeapi.org/api/timezone/America/Sao_Paulo')
data_json = data.json()

#pegando datas da API
day = int(data_json['datetime'][8:10])

#importando base de dados
tabela = pd.read_excel('PLANILHA DIÁRIA DE ABRIL + META POR PEÇAS  LJR.xls')

#Pegando informações da base de dados
meta_diaria = tabela.loc[day-1, 'cota $']
meta_por_vendedor = meta_diaria / 2
projecao = tabela.loc[day-1, 'projeção']
print(day)
print(f'{meta_diaria:.2f}')
print(f'{meta_por_vendedor:.2f}')
print(f'{projecao:.2f}')


#Avisando que o pyautogui vai começar e tempo de click
pg.alert("O codigo vai começar, não precione nenhuma tecla e não mova o mouse")
pg.PAUSE = 0.8

#abrindo o whatsapp
pg.press('winleft')
pg.write('chrome')
pg.press('enter')
pg.write('https://web.whatsapp.com/')
pg.press('enter')
time.sleep(5)

#entrando no destinatario da mensagem
pg.moveTo(229, 230)
pg.click()
pg.write('Isso ai')
pg.press('enter')

#escrevendo a mensagem
pg.write('=========================================')
pg.hotkey('ctrl', 'enter')
pg.write(f'DIA: {day}')
pg.hotkey('ctrl', 'enter')
pg.write(f'META DIÁRIA: R${meta_diaria:.2f}')
pg.hotkey('ctrl', 'enter')
pg.write(f'META POR VENDEDOR: R${meta_por_vendedor:.2f}')
pg.hotkey('ctrl', 'enter')
pg.write(f'PROJECAO: R${projecao:.2f}')
pg.hotkey('ctrl', 'enter')
pg.write('=========================================')

#enviando a mensagem e finalizando
pg.press('enter')
pg.alert('Tarefa finalizada')