import os
import sqlite3
import subprocess
import sys
import random
from DBcommand import DataBase
try:
    from barcode import EAN8
    from barcode.writer import ImageWriter
    from PIL import Image, ImageDraw, ImageFont
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "python-barcode", "pillow"])

def criar():
    #pegando do usuario o codigo do sistema
    barcod = systemCod = input("Digite o codigo do sistema ")
    name = input("digite o nome do produto ")
    #criando os numeros aleatorios para preencher os digitos restantes
    aux = 7-len(systemCod)
    for cont in range(aux):
        barcod += str(random.randint(0,9))
    #transformando o codigo criado em um EAN8(que adicione o 8° digito que é o digito verificador)
    barcod = EAN8(barcod)

    #inserindo no banco de dados
    dataBase.insert(name,systemCod,str(barcod))

    #imprimindo codigo criado
    print(barcod)
    
def gerar():
    barcod = input("Digite o codigo de Barras ")
    #criando codigo de barras
    codigo_barra = EAN8(barcod, writer=ImageWriter())
    #salvando codigo de barras
    codigo_barra.save(barcod)
    #abrindo a imagem do codigo de barras salva para editar
    img = Image.open(barcod + '.png')
    #criando cursor para editar imagem
    draw = ImageDraw.Draw(img)
    #pegando do usuario nome do produto
    descricao = input("Qual o nome do produto : ")
    #definindo o tamanho e a fonte da letra
    font = ImageFont.truetype('arial.ttf', 32)
    #adicionando descrição na imagem
    draw.text((0, 250), descricao, (0,0,0), font=font)
    #salvando a imagem de codigo de barras com descrição
    img.save(descricao + '.jpg')
    #apagando a imagem do codigo de barras sem edição
    os.remove(barcod +'.png')


 
if __name__=="__main__":
    #caminho do banco de dados
    databasePath = "DBbarcode.sqlite3" 
    #instanciando a classe DataBase que cria conexão com o banco de dados
    dataBase = DataBase(databasePath)
    #criando tabela caso não exista
    dataBase.create_table()

    print("1. Criar numero de codigo de barras para o sistema : ")
    print("2. Gerar imagem do codigo de barras :")
    opcao = int(input())
    if opcao ==1:
        criar()
    elif opcao == 2:
        gerar()
    else:
        print("opção invalida")
    

      
