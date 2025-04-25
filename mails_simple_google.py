import pandas as pd
import smtplib
from email.message import EmailMessage

# URL directa al contenido CSV de tu Google Sheet
url_csv = "https://docs.google.com/spreadsheets/d/1awXIrKsOUil7NGZzVlzCF83QNgDCFoy7qOGVkFyVvZI/export?format=csv"

# Leer datos desde Google Sheets
df = pd.read_csv(url_csv)

# Credenciales del remitente
usuario = "rlopezotero@hospitalsanmartin.gob.ar"
contraseña = "Lor247523"

# Conexión al servidor SMTP
server = smtplib.SMTP("mail.hospitalsanmartin.gob.ar", 587)
server.starttls()
server.login(usuario, contraseña)

# Enviar correo a cada fila
for _, fila in df.iterrows():
    nombre = fila["Nombre"]
    correo = fila["mail"]
    
    if pd.isna(correo):
        continue  # Saltar si no hay mail
    
    asunto = f"Hola {nombre}"
    cuerpo = f"""Estimado/a {nombre},

Este es un TEST para automatizar envíos de correos electrónicos.

Saludos."""

    mensaje = EmailMessage()
    mensaje.set_content(cuerpo)
    mensaje['Subject'] = asunto
    mensaje['To'] = correo
    mensaje['From'] = usuario

    server.send_message(mensaje)
    print(f"Correo enviado a {correo}")

server.quit()
