"""
Autor: Neemias Silva Amaro

Explicação: Código desenvolvido para enviar mensagens a determinada(s) pessoa(s) em horários específicos.
Necessitando apenas de executá-lo uma vez, visto que estará rodando em 2º plano e, somente 
nos horários especificados ao final do documento que executará todas as "tarefas" pendentes.

Data: 19/01/2022

Libs usadas: Pywhatkit para envio das mensagens;
Time para função time.sleep();
Schedule para organizar o momento das tarefas e
Datetime para uso do horário atual sem erros de inserção.                                  
                                                           
"""

import pywhatkit
import time
import schedule
from datetime import datetime

def dia():

    print("Iniciando...")

    i = 1
    j = 0

    while i <= datetime.now().hour :
        while j <= datetime.now().minute:
            if datetime.now().hour == 14 and datetime.now().minute == 28:
                pywhatkit.sendwhatmsg("*Numero da pessoa*","*Mensagem a ser enviada*","hora de envio : int","minuto de envio : int")
                time.sleep(60)
            elif datetime.now().hour == 14 and datetime.now().minute == 58:
                pywhatkit.sendwhatmsg("*Numero da pessoa*","*Mensagem a ser enviada*","hora de envio : int","minuto de envio : int")
                time.sleep(60)
            elif datetime.now().hour == 15 and datetime.now().minute == 28:
                pywhatkit.sendwhatmsg("*Numero da pessoa*","*Mensagem a ser enviada*","hora de envio : int","minuto de envio : int")
                time.sleep(60)
            else:
                print(f"Rodando normal...")
                time.sleep(60)
            j += 1
    i += 1

def noite():
    
    print("Iniciando...")
    
    i = 1
    j = 0

    while i <= datetime.now().hour :
        while j <= datetime.now().minute:
            if datetime.now().hour == 21 and datetime.now().minute == 28:
                pywhatkit.sendwhatmsg("*Numero da pessoa*","*Mensagem a ser enviada*","hora de envio : int","minuto de envio : int")
                time.sleep(60)
            elif datetime.now().hour == 22 and datetime.now().minute == 58:
                pywhatkit.sendwhatmsg("*Numero da pessoa*","*Mensagem a ser enviada*","hora de envio : int","minuto de envio : int")
                time.sleep(60)
            elif datetime.now().hour == 21 and datetime.now().minute == 58:
                pywhatkit.sendwhatmsg("*Numero da pessoa*","*Mensagem a ser enviada*","hora de envio : int","minuto de envio : int")
                time.sleep(60)
            else:
                print(f"Rodando normal...")
                time.sleep(60)
            j += 1
    i += 1

schedule.every().day.at('14:00').do(dia)
schedule.every().day.at('21:00').do(noite)

while 1:
    schedule.run_pending()
    time.sleep(5)