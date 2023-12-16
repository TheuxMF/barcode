import subprocess
import sys
import random
try:
    from barcode import EAN8
    from barcode.writer import ImageWriter
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "python-barcode", "pillow"])

def criar():
    systemCod = input("Digite o codigo do system ")
    aux = 7-len(systemCod)
    for cont in range(aux):
        systemCod += str(random.randint(0,9))
    systemCod = EAN8(systemCod)
    print(systemCod)
    
def gerar():
    barcod = input("Digite o codigo de Barras ")
    codigo_barra = EAN8(barcod, writer=ImageWriter())
    print(codigo_barra)
    codigo_barra.save(barcod)

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
    

      
