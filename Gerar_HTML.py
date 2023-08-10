import os
import openpyxl
import pandas as pd
import warnings
import datapane as dp
import datapane.resources
import datapane.resources.view_resources
import datapane.resources.html_templates
import datapane.resources.app_templates
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import seaborn as sns
import matplotlib.pyplot as plt

warnings.filterwarnings('ignore')

from Enviar_Email import Teste

class Gerar(Teste):
    def __init__(self):
        self.desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        self.titulo = '# Report Diario'
        self.df = pd.read_excel(self.desktop_path+"\\projetonew\\airlines_delay.xlsx")

    def CriarGRafico(self):
        fig3 = px.scatter(self.df,x='Airline',y='Length',size='Length',color='DayOfWeek')
        return fig3
    
    def CriarGRafico2(self):
        plt.figure(figsize=(12,4))
        fig3 = sns.boxplot(x='Airline', y='Length', data=self.df)
        return fig3

    def CriarTabela(self):
        tabela = dp.DataTable(self.df)
        return tabela
    
    def CriarTitulo(self):
        texto = dp.Text(self.titulo)
        return texto

    def CriarApp(self):
        tex = self.CriarTitulo()
        graf = self.CriarGRafico()
        graf2 = self.CriarGRafico2()
        tab = self.CriarTabela()
        app = dp.App(tex,graf,graf2,tab)
        return app
    
    def Salvar(self):
        app = self.CriarApp()
        app.save(self.desktop_path+"\\projetonew\\HTML_Gerado.html")

gerar = Gerar()
gerar.Salvar()
gerar.ObjetoMime()