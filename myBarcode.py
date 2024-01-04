import os #para excluir uma imagem temporaria 
import subprocess #usado para instalar todas as bibliotecas nescessarias para o codigo
import sys #usado para instalar todas as bibliotecas nescessarias para o codigo
import random #usado para gerar numeros aleatorios

from DBcommand import DataBase #classe com comados slq

#instalando bibliotecas necessarias para o codigo
try:
    from barcode import EAN8
    from barcode.writer import ImageWriter
    from PIL import Image, ImageDraw, ImageFont
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "python-barcode", "pillow"])

def criar(teste):
    #pegando do usuario o codigo do sistema
    barcod = systemCod = input("Digite o codigo do sistema ").lstrip('0')
    
    #verificando se o codigo digitado ja esta no banco de dados
    systemCodList = dataBase.selectSystemCodALL()   
    for cod in systemCodList:
        if cod[0]==systemCod:
            print("codigo ja cadastrado no sistema ")
            return None
        
    #pegando nome do produto
    name = input("digite o nome do produto ")
    
    #criando codigo com verificação para não haver codigos reptidos
    
    while True:
        #criando os numeros aleatorios para preencher os digitos restantes
        aux = 7-len(systemCod)
        for cont in range(aux):
            barcod += str(random.randint(0,9))
            
        #transformando o codigo criado em um EAN8(que adicione o 8° digito que é o digito verificador)
        barcod = EAN8(barcod)
        #verificando se tem um codbar igual no banco    
        if checkBarcode(str(barcod)):
            print("deu certo")
            break

    #inserindo no banco de dados
    dataBase.insert(name,systemCod,str(barcod))
    #imprimindo codigo criado
    print(f"codigo numero {teste} : {str(barcod)}")
    
def checkBarcode(barcod):
    #selecionando todos os barcod no banco
    barcodList = dataBase.selectBarcodALL()
    #verificando se tem algum igual
    for cod in barcodList:
        #print("barcode : " + cod[0])
        if cod[0]==barcod:
            return False
            #codição para repetir o loop
    return True    

def gerar():
    systemCod = input("Digite o codigo do sistema : ")
    try:
        retorno = dataBase.selectBarcod(systemCod)
        barcod= retorno[0][0]
    except:
        print("codigo não encontrado no banco de dados")
        return None
    #criando codigo de barras
    codigo_barra = EAN8(barcod, writer=ImageWriter())
    #salvando codigo de barras
    codigo_barra.save(barcod)
    #abrindo a imagem do codigo de barras salva para editar
    img = Image.open(barcod + '.png')
    #criando cursor para editar imagem
    draw = ImageDraw.Draw(img)
    #pegando do banco nome do produto
    retorno = dataBase.selectName(systemCod)
    nome = retorno[0][0]
    #definindo o tamanho e a fonte da letra
    font = ImageFont.truetype('arial.ttf', 32)
    #adicionando descrição na imagem
    draw.text((0, 250), nome, (0,0,0), font=font)
    #salvando a imagem de codigo de barras com descrição
    img.save(nome + '.jpg')
    #apagando a imagem do codigo de barras sem edição
    os.remove(barcod +'.png')
 
if __name__=="__main__":
    #caminho do banco de dados
    databasePath = "DBbarcode.sqlite3" 
    #instanciando a classe DataBase que cria conexão com o banco de dados
    dataBase = DataBase(databasePath)
    #criando tabela caso não exista
    dataBase.create_table()
    
    while True:
        print("1. Criar numero de codigo de barras para o sistema : ")
        print("2. Gerar imagem do codigo de barras :")
        print("0. exit")
        opcao = input()
        if opcao == '1':
            criar()
        elif opcao == '2':
            gerar()
        elif opcao == '0':
            print("Fim da execução")
            dataBase.close()
            break
        else:
            print("opção invalida")