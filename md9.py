from mss import mss #screenshot
from PIL import Image
from selenium import webdriver  #pip install selenium
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager  #pip install webdriver-manager
import pyautogui
import time
import os
import base64  #subir github

def pngjpg(n):
    im = Image.open("monitor-1.png")
    im.mode
    im = im.convert('RGB')
    im.mode
    nombre='md9-'+str(n)+'.jpg'
    im.save(nombre, quality=95)

def captura():
    time.sleep(3)
    with mss() as sct:  #screenshot
        sct.shot()

def cerrvent():
    pyautogui.keyDown('alt') #cerrar ventana
    pyautogui.keyDown('f4')
    pyautogui.keyUp('f4')
    pyautogui.keyUp('alt')

def cambvent():
    pyautogui.keyDown('ctrl') #cerrar ventana
    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')
    pyautogui.keyUp('ctrl')

def zoom1():
    time.sleep(2)
    pyautogui.keyDown('ctrl') #cerrar ventana
    pyautogui.press('-')
    pyautogui.keyUp('ctrl')

def pagabajo():
    pyautogui.press('pagedown')
    time.sleep(2)

def coordenada():  #ver coordenadas
    time.sleep(5)
    x,y = pyautogui.position()
    print (x,y)

def pausa (seg):  #funcion pausa en segundos, rango de testeo de datos
    for i in range(seg,0,-1):
        print(f"{i}  ", end="\r")
        time.sleep(1)

def wifi(modo): 
    time.sleep(3)
    if modo=='on':
        os.system('netsh wlan connect md1')
        pausa(30)
    elif modo=='off':
        time.sleep(30)
        os.system('netsh wlan disconnect')

def pagina(web):
    options=Options()
    options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(web)
    time.sleep(3)
    pyautogui.press('f11')
    time.sleep(20)

while True:
    os.system('cls')
    wifi('on')

    #fead and greed, altcoin season, rsi
    num=1
    pagina('https://coinmarketcap.com/')
    #coordenada()
    captura()
    pngjpg(num)  #numero de archivo
    cerrvent()
    imagen = Image.open("md9-"+str(num)+".jpg")
    recorte = imagen.crop((460, 180, 1120, 300))  #izquierda, arriba, derecha, abajo
    recorte.save("md9-"+str(num)+".jpg")

    #fead and greed btc
    num=2
    pagina('https://alternative.me/crypto/fear-and-greed-index/')
    pagabajo()
    #coordenada()
    captura()
    pngjpg(num)  #numero de archivo
    cerrvent()
    imagen = Image.open("md9-"+str(num)+".jpg")
    recorte = imagen.crop((100, 55, 860, 385))  #izquierda, arriba, derecha, abajo
    recorte.save("md9-"+str(num)+".jpg")

    #fead and greed mercados
    num=3
    pagina('https://edition.cnn.com/markets/fear-and-greed')
    zoom1()
    zoom1()
    zoom1()
    zoom1()
    zoom1()
    #coordenada()
    captura()
    pngjpg(num)  #numero de archivo
    cerrvent()
    imagen = Image.open("md9-"+str(num)+".jpg")
    recorte = imagen.crop((325, 395, 660, 580))  #izquierda, arriba, derecha, abajo
    recorte.save("md9-"+str(num)+".jpg")

    #dolarhoy
    num=4
    pagina('https://dolarhoy.com/')
    pagabajo()
    #coordenada()
    captura()
    pngjpg(num)  #numero de archivo
    cerrvent()
    imagen = Image.open("md9-"+str(num)+".jpg")
    recorte = imagen.crop((50, 200, 400, 455))  #izquierda, arriba, derecha, abajo
    recorte.save("md9-"+str(num)+".jpg")

    #dominancia btc
    #num=5
    #pagina('https://coinmarketcap.com/es/charts/bitcoin-dominance/')
    #zoom1()
    #coordenada()
    #captura()
    #pngjpg(num)  #numero de archivo
    #cerrvent()
    #imagen = Image.open("md9-"+str(num)+".jpg")
    #recorte = imagen.crop((310, 270, 625, 425))  #izquierda, arriba, derecha, abajo
    #recorte.save("md9-"+str(num)+".jpg")

    #30 indicadores bull market
    #num=6
    #pagina("https://www.coinglass.com/bull-market-peak-signals")
    #coordenada()
    #captura()
    #pngjpg(num)  #numero de archivo
    #cerrvent()
    #imagen = Image.open("md9-"+str(num)+".jpg")
    #recorte = imagen.crop((940, 275, 1275, 380))  #izquierda, arriba, derecha, abajo
    #recorte.save("md9-"+str(num)+".jpg")

    #abre chromium
    #options=Options()
    #options.add_experimental_option("detach",True)
    #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    #driver.get('file:///C:/0python/index.html')
    #time.sleep(3)
    #pyautogui.press('f11')

    #subir archivos a github
    #https://www.youtube.com/watch?v=eQMcIGVc8N0 tutorial  git status
    os.system('git init')
    os.system('git reset origin/main')
    os.system('git config --global user.name mdchi')
    os.system('git config --global user.email marianochiodo@gmail.com')
    os.system('git add .')
    os.system('git commit -m "actualiza"')
    os.system('git branch -M main')                                       #subir a rama principal
    os.system('git remote add origin https://github.com/mdchi/md9.git')   #configura origin = repositorio
    os.system('git push --force -u origin main')    

    wifi('off')
    pausa(86400)  # 86400 seg = 1 dia
    cerrvent()

