import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE
from email import encoders
import os

class Teste:
    def __init__(self):
        self.email_lista = ['aaandersonpereira45265@gmail.com', 'aristocles.platao123@gmail.com', 'guh.roch4@gmail.com']
        self.desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        self.caminho = self.desktop_path + "\\projetonew\\HTML_Gerado.html"
        self.arquivo = self.caminho
        self.de = 'aandersonpereira45265@gmail.com'
        self.senha = 'wwfloewvotoxzpwa'
        self.assunto = 'Teste Email Anderson'

    def InicioEmail(self):
        para = COMMASPACE.join(self.email_lista)

    def ObjetoMime(self):
        # Crie o objeto MIMEMultipart para conter as partes do email
        msg = MIMEMultipart()
        msg['From'] = self.de
        msg['To'] = COMMASPACE.join(self.email_lista)
        msg['Subject'] = self.assunto

        # Adicione o texto do email como uma parte MIMEText
        corpo_email = """
        <p>Ola</>
        <p>Segue Email automatico </p>
        """
        msg.attach(MIMEText(corpo_email, 'html'))

        # Abra o arquivo que deseja anexar em modo binário
        arquivo = self.caminho
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
        servidor.login(self.de, self.senha)
        servidor.sendmail(self.de, self.email_lista, msg.as_string())
        servidor.quit()
        print("Email Enviado!")

teste = Teste()
teste.InicioEmail()
teste.ObjetoMime()


    

