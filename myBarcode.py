import subprocess
import sys
import random
try:
    from barcode import EAN8
    from barcode.writer import ImageWriter
    from PIL import Image, ImageDraw, ImageFont, ImageFont
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "python-barcode", "pillow"])

def criar():
    #solicita ao usuário que insira um código do sistema
    systemCod = input("Digite o codigo do system ")
    
    #gera numeros aletorios para completar oito digitos para o padrão EAN8
    aux = 7-len(systemCod)
    for cont in range(aux):
        systemCod += str(random.randint(0,9))
        
    #cria um objeto EAN8 usando o código do sistema
    systemCod = EAN8(systemCod)
    
    #imprime o codigo EAN8 gerado
    print(systemCod)
    
def gerar():
    #solicita ao usuário que insira um código de barras
    barcod = input("Digite o codigo de Barras ")
    
    #cria um objeto EAN8 usando o código de barras fornecido pelo usuário 
    codigo_barra = EAN8(barcod, writer=ImageWriter()) #parâmetro writer=ImageWriter() indica que o código de barras será escrito como uma imagem.
    
    #salva a imagem do código de barras
    codigo_barra.save(barcod)

    # Abra a imagem do código de barras e Crie um objeto ImageDraw
    img = Image.open(barcod + '.png')
    d = ImageDraw.Draw(img)
    
    # Defina o texto e o tamanho da fonte (limite de 24 caracteres)
    texto = input("insira o nome do produto")
    tamanho_fonte = 30  # Defina o tamanho da fonte aqui
 
    # Defina a fonte (a fonte padrão é usada aqui, você pode especificar sua própria fonte se quiser)
    fonte = ImageFont.truetype("arial.ttf", tamanho_fonte)

    # Adicione o texto à imagem
    d.text((0,250), texto, fill="black", font=fonte)
    
    # Salve a imagem
    img.save(barcod + '.png')
    

if __name__=="__main__":    
    
    print("1. Criar numero de codigo de barras para o sistema : ")
    print("2. Gerar imagem do codigo de barras :")
    
    opcao = int(input())
    if opcao ==1:
        criar()
    elif opcao == 2:
        gerar()
    else:
        print("opção invalida")
    

      
