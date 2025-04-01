'''
Autor: Rafael López Otero
'''

import smtplib
import pandas as pd
from email.message import EmailMessage
import openpyxl

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    
    user = "rlopezotero@hospitalsanmartin.gob.ar"
    msg['from'] = user
    password = "Lor247523"
    
    try:
        server = smtplib.SMTP("mail.hospitalsanmartin.gob.ar", 587)
        server.starttls()
        server.login(user, password)
        server.send_message(msg)
        server.quit()
        print(f"Correo enviado a {to}")
    except Exception as e:
        print(f"Error al enviar correo a {to}: {e}")

if __name__ == '__main__':
    # Cargar el archivo de Excel
    file_path = r"C:\Users\Rafael\Documents\emails.xlsx"  # Ajusta el nombre del archivo según corresponda
    df = pd.read_excel(file_path)
    
    # Iterar sobre cada fila del archivo y enviar el correo
    for index, row in df.iterrows():
        nombre = row["Nombre"]
        correo = row["mail"]
        asunto = "Hola " + nombre
        cuerpo = f"Estimado/a {nombre},\n\nEste es un TEST para automatizar envíos de correos electrónicos.\n\nSaludos."
        email_alert(asunto, cuerpo, correo)
