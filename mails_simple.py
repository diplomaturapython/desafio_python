import smtplib
import pandas as pd
from email.message import EmailMessage

# Datos de usuario
usuario = "rlopezotero@hospitalsanmartin.gob.ar"
contraseña = "Lor247523"

# Cargar archivo Excel
ruta_archivo = r"C:\Users\Rafael\Documents\emails.xlsx"
df = pd.read_excel(ruta_archivo)

# Conectarse al servidor SMTP
server = smtplib.SMTP("mail.hospitalsanmartin.gob.ar", 587)
server.starttls()
server.login(usuario, contraseña)

# Recorrer el Excel y enviar correos
for i, fila in df.iterrows():
    nombre = fila["Nombre"]
    correo = fila["mail"]
    
    asunto = "Hola " + nombre
    cuerpo = f"Estimado/a {nombre},\n\nEste es un TEST para automatizar envíos de correos electrónicos.\n\nSaludos."
    
    mensaje = EmailMessage()
    mensaje.set_content(cuerpo)
    mensaje['Subject'] = asunto
    mensaje['To'] = correo
    mensaje['From'] = usuario
    
    server.send_message(mensaje)
    print("Correo enviado a:", correo)

# Cerrar la conexión con el servidor
server.quit()