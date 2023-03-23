import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE
from email import encoders
import os
import openpyxl
import pandas as pd
import warnings


desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
email_lista = ['aaandersonpereira45265@gmail.com','aristocles.platao123@gmail.com','guh.roch4@gmail.com'] #guh.roch4@gmail.com

caminho = desktop_path+"\\Teste_Diario.html"

#Enviar o Email----------------------
de = 'aandersonpereira45265@gmail.com'
para = COMMASPACE.join(email_lista)
senha = 'wwfloewvotoxzpwa'

assunto = 'Teste Email Anderson'

# Crie o objeto MIMEMultipart para conter as partes do email
msg = MIMEMultipart()
msg['From'] = de
msg['To'] = COMMASPACE.join(email_lista)
msg['Subject'] = assunto

# Adicione o texto do email como uma parte MIMEText
corpo_email = """
<p>Ola</>
<p>Segue Email automatico </p>
"""
msg.attach(MIMEText(corpo_email, 'html'))

# Abra o arquivo que deseja anexar em modo binário
arquivo = caminho
with open(arquivo, 'rb') as anexo:
    # Crie um objeto MIMEBase com o tipo apropriado
    parte = MIMEBase('application', 'octet-stream')
    parte.set_payload(anexo.read())

    # Codifique o anexo em base64 e defina o cabeçalho apropriado
    encoders.encode_base64(parte)
    parte.add_header('Content-Disposition', f'attachment; filename="{arquivo}"')

    # Adicione o objeto MIMEBase ao objeto MIMEMultipart
    msg.attach(parte)

# Conecte-se ao servidor SMTP do seu provedor de email e envie o email
servidor = smtplib.SMTP('smtp.gmail.com', 587)
servidor.starttls()
servidor.login(de, senha)
servidor.sendmail(de, para, msg.as_string())
servidor.quit()
print("Email Enviado!")

enviar()